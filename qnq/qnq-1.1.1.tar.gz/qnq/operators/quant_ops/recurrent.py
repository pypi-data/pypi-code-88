# This script contain implentation of operators.
# Author:
#     Albert Dongz
# History:
#     2020.7.16 First Release
# Dependencies:
#     PyTorch
# Attention:
#     1. Nothing
import torch.nn as nn
from ..qnq_ops import *
from .quant_base import *


class QuantLSTM(QuantBase):
    def __init__(self, name, module, bit_width, writer):
        super().__init__(name, module, bit_width, writer)
        self.activation_fl = -1

    def quantize_params(self):
        # overide backup data
        self.backup_params = {
            k: v
            for k, v in zip(self.module.params, [
                copy.deepcopy(getattr(self.module, name))
                for name in self.module.params
            ])
        }

        for k, v in self.backup_params.items():
            self.writer.add_histogram(self.name + k,
                                      v.clone().cpu().data.numpy())

        #! TODO valide
        params = np.concatenate([
            getattr(self.module, attr).cpu().data.flatten().numpy()
            for attr in self.module.params
        ])
        # init kld
        hist, _ = np.histogram(params,
                               bins=self.bins_num,
                               range=(-1 * self.activation_max,
                                      self.activation_max))
        self.weight_fl, kld = kld_based_dynamics_double(hist, self.bit_width)
        self.logger.debug(self.name + "'s weight_fl=" + str(self.weight_fl))
        self.logger.debug('KLDs=' + str(["%.3E" % Decimal(v) for v in kld]))

    def trim_params(self, debug_bw=None, debug_fl=None):
        # for debug
        bit_width = self.bit_width if not debug_bw else debug_bw
        fraction_length = self.weight_fl if not debug_fl else debug_fl

        # trim from backed data
        for name in self.module.params:
            getattr(self.module,
                    name).data = float2fixed(self.backup_params[name].data,
                                             bit_width, fraction_length)

    def recover_params(self):
        # recover from backed data
        for name in self.module.params:
            getattr(self.module, name).data = self.backup_params[name].data

    def quantize_activation(self):
        pass

    def register_eval_hook(self, debug_bw=None, debug_fl=None):
        pass

    def register_get_activation_hook(self):
        pass

    def trim_activation(self, debug_bw=None, debug_fl=None):
        pass

    def init_histograms(self):
        pass


class QuantGRU(QuantBase):
    def __init__(self, name, module, bit_width, writer):
        super().__init__(name, module, bit_width, writer)
        self.activation_fl = -1

    def quantize_params(self):
        #! TODO valide
        params = np.concatenate([
            getattr(self.module, attr).cpu().data.flatten().numpy()
            for attr in self.module.params
        ])
        # init kld
        hist, _ = np.histogram(params,
                               bins=self.bins_num,
                               range=(-1 * self.activation_max,
                                      self.activation_max))
        min_kld_fl, kld = kld_based_dynamics_double(hist, self.bit_width)
        self.weight_fl = min_kld_fl
        for name in self.module.params:
            getattr(self.module, name).data = float2fixed(
                getattr(self.module, name).data, self.bit_width,
                self.weight_fl)
        self.logger.debug(self.name + 's\' weight fl:' + str(min_kld_fl) +
                          ', kld: ' + str(kld))

    def quantize_activation(self):
        pass

    def register_eval_hook(self, debug_bw=None, debug_fl=None):
        pass

    def register_get_activation_hook(self):
        pass

    def trim_activation(self, debug_bw=None, debug_fl=None):
        pass

    def init_histograms(self):
        pass


recurrent_switch = {
    QNQLSTM: QuantLSTM,
    QNQGRU: QuantGRU,
}