import copy
import math
import logging
import numpy as np

from decimal import Decimal
from scipy import stats
from ...utils.quant_utils import float2fixed


class QuantBase:
    def __init__(self, name, module, bit_width, writer):
        self.name = name
        self.module = module
        self.bit_width = bit_width
        self.logger = logging.getLogger("qnq")

        self.weight_fl = 0
        self.activation_fl = 0

        self.activation = None
        self.activation_positive = True
        self.bins_num = 2**(2 * self.bit_width - 1)
        self.activation_max = 2**(bit_width - 1) - 1
        self.activation_distribution = np.zeros(self.bins_num)
        self.activation_distribution_edge = None

        # if self.module have hook, self.hook_handler.remove() will remove it.
        self.hook_handler = None

        # 0, 1, 2...
        self.fuse_flag = -1
        # 0, 1, 2...
        self.group_flag = -1
        # True for bn2scale
        self.scale_flag = False

        self.writer = writer
        # tensorboard step variable
        self.step_count = 0

    def register_get_activation_hook(self):
        def hook(module, input, output):
            self.activation = output.cpu().detach().data.flatten().numpy()

        self.hook_handler = self.module.register_forward_hook(hook)

    def register_eval_hook(self, debug_bw=None, debug_fl=None):
        def hook(module, input, output):
            bit_width = self.bit_width if debug_bw is None else debug_bw
            fraction_length = self.activation_fl if debug_fl is None else debug_fl
            output = float2fixed(output, bit_width, fraction_length)
            return output

        if self.activation_fl is not -1:
            self.hook_handler = self.module.register_forward_hook(hook)

    def init_histograms(self):
        hist, hist_edge = np.histogram(self.activation,
                                       bins=self.bins_num,
                                       range=(-1 * self.activation_max,
                                              self.activation_max))
        self.activation_distribution += hist
        self.activation_distribution_edge = hist_edge

        self.step_count += 1
        self.writer.add_histogram(self.name + "_running_activation",
                                  self.activation, self.step_count)

    def reweight_kld(self):
        def adaptive_func(x):
            x /= 128 * 128
            return abs(x)

        adaptive_scale = [
            adaptive_func(x - self.bins_num // 2) for x in range(self.bins_num)
        ]
        self.activation_distribution *= adaptive_scale

    def adaptive_kld(self):
        # -1, 1
        adaptive_zone = copy.deepcopy(
            self.activation_distribution[self.bins_num // 2 -
                                         2**(self.bit_width -
                                             1):self.bins_num // 2 +
                                         2**(self.bit_width - 1)])
        activation_sum = sum(self.activation_distribution)
        adaptive_zero = 2**(self.bit_width - 1)
        # handcraft rule
        alpha = 0
        beta = 2**(2 - self.bit_width) / 8
        weight = 0
        for i in range(self.bit_width - 1, -1, -1):
            weight = sum(adaptive_zone[adaptive_zero - 2**
                                       (self.bit_width - 1 - i):adaptive_zero +
                                       2**(self.bit_width - 1 - i)]) - weight
            # handcraft rule
            if weight / activation_sum > 0.1:
                beta *= 2
            # handcraft rule
            alpha += (2**(i + 1)) * (weight / activation_sum)

        def adaptive_func(alpha, beta, x):
            # 防止计算指数时溢出
            x /= 128 * 8
            # 防止计算指数时溢出
            if x > 0:
                param = min(20, max(-20, -1 * alpha * (-1 * x + beta)))
                return 1 - 1 / (1 + (math.exp(param)))
            else:
                param = min(20, max(-20, -1 * alpha * (x + beta)))
                return 1 - 1 / (1 + (math.exp(param)))

        adaptive_scale = [
            adaptive_func(alpha, beta, x - self.bins_num // 2)
            for x in range(self.bins_num)
        ]

        self.activation_distribution *= adaptive_scale

    def quantize_params(self):
        # backup data, need overide
        self.backup_weight = copy.deepcopy(self.module.weight)
        self.writer.add_histogram(
            self.name + "_weight",
            self.backup_weight.clone().cpu().data.numpy(),
        )
        weight_data = self.module.weight.cpu().data.flatten().numpy()
        try:
            # many module may not have bias
            bias_data = self.module.bias.cpu().data.flatten().numpy()
            # backup bias
            self.backup_bias = copy.deepcopy(self.module.bias)
            self.writer.add_histogram(
                self.name + "_bias",
                self.backup_bias.clone().cpu().data.numpy(),
            )
        except:
            bias_data = None
            # no bias backup
            self.backup_bias = None
        if bias_data is None:
            data = weight_data
        else:
            data = np.concatenate((weight_data, bias_data))

        # init kld
        hist, _ = np.histogram(data,
                               bins=self.bins_num,
                               range=(-1 * self.activation_max,
                                      self.activation_max))
        self.weight_fl, kld = kld_based_dynamics_double(hist, self.bit_width)
        self.logger.debug(self.name + "'s weight_fl=" + str(self.weight_fl))
        self.logger.debug('KLDs=' + str(["%.3E" % Decimal(v) for v in kld]))

    def quantize_activation(self):
        self.writer.add_histogram(self.name + "_activation",
                                  self.activation_distribution)
        # pick fl which minimizes KL divergence
        if self.activation_positive:
            self.activation_fl, kld = kld_based_dynamics_single(
                self.activation_distribution, self.bit_width)
        else:
            # self.adaptive_kld()
            self.reweight_kld()
            self.activation_fl, kld = kld_based_dynamics_double(
                self.activation_distribution, self.bit_width)

        self.logger.debug(self.name + "'s activation_fl=" +
                          str(self.activation_fl))
        self.logger.debug('KLDs=' + str(["%.3E" % Decimal(v) for v in kld]))

    def trim_params(self, debug_bw=None, debug_fl=None):
        # for debug
        bit_width = self.bit_width if debug_bw is None else debug_bw
        fraction_length = self.weight_fl if debug_fl is None else debug_fl

        # trim backup data
        if self.weight_fl != -1:
            if self.backup_weight is not None:
                self.module.weight.data = float2fixed(self.backup_weight,
                                                      bit_width,
                                                      fraction_length)
            if self.backup_bias is not None:
                self.module.bias.data = float2fixed(self.backup_bias,
                                                    bit_width, fraction_length)

    def recover_params(self):
        # recover backup data
        if self.weight_fl != -1:
            self.module.weight.data = self.backup_weight
            if self.backup_bias is not None:
                self.module.bias.data = self.backup_bias

    def trim_activation(self, debug_bw=None, debug_fl=None):
        # remove origin get_activation hook or other fl's hook
        if self.hook_handler is not None:
            self.hook_handler.remove()

        # rigister new fl's hook for trim activation
        self.register_eval_hook(debug_bw, debug_fl)


def kld_based_dynamics_single(distribution, bit_width):
    kld = np.zeros(bit_width)
    # only calculate positive
    zero_bin = 2**(2 * bit_width - 2)
    distribution = distribution[zero_bin + 1:]

    for i in range(bit_width):
        range_bin = 2**(i + bit_width - 2)
        p = copy.deepcopy(distribution[:range_bin]).astype(np.float64)
        q = copy.deepcopy(distribution[:range_bin]).astype(np.float64)
        # p[0] += sum(distribution[:zero_bin - range_bin])
        p[-1] += sum(distribution[range_bin:])
        is_nonzeros = (p != 0).astype(np.int64)
        #extended q
        if i != 0:
            for j in range(0, 2**(i + bit_width - 1), 2**(i - 1)):
                step = 2**(i - 1)
                norm = sum(is_nonzeros[j:j + step])
                q[j:j + step] = sum(q[j:j + step]) / norm if norm != 0 else 0
        q[p == 0] = 0
        p[p == 0] = 0.000001
        q[q == 0] = 0.000001
        # calculate kl_divergence between q and p
        kld[i] = stats.entropy(p, q)

    kld = list(kld)
    kld.reverse()
    kld = np.array(kld)

    min_kld_fl = np.argmin(kld)

    return min_kld_fl, kld


def kld_based_dynamics_double(distribution, bit_width):
    kld = np.zeros(bit_width)
    zero_bin = 2**(2 * bit_width - 2)

    for i in range(bit_width):
        range_bin = 2**(i + bit_width - 1)
        p = copy.deepcopy(distribution[zero_bin - range_bin:zero_bin +
                                       range_bin]).astype(np.float64)
        q = copy.deepcopy(distribution[zero_bin - range_bin:zero_bin +
                                       range_bin]).astype(np.float64)
        p[0] += sum(distribution[:zero_bin - range_bin])
        p[-1] += sum(distribution[zero_bin + range_bin:])
        is_nonzeros = (p != 0).astype(np.int64)
        #extended q
        if i != 0:
            for j in range(0, 2**(i + bit_width), 2**i):
                if j == 0 or j == 2**(i + bit_width) - 2**i:
                    step = 2**(i - 1)
                else:
                    step = 2**i
                norm = sum(is_nonzeros[j:j + step])
                q[j:j + step] = sum(q[j:j + step]) / norm if norm != 0 else 0
        q[p == 0] = 0
        p[p == 0] = 0.000001
        q[q == 0] = 0.000001
        # calculate kl_divergence between q and p
        kld[i] = stats.entropy(p, q)

    kld = list(kld)
    kld.reverse()
    kld = np.array(kld)

    min_kld_fl = np.argmin(kld)

    return min_kld_fl, kld
