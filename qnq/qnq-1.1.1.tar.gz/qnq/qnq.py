# This script contain functions help quantization
# Author:
#     Albert Dongz
# History:
#     2020.7.16 First Release
# Dependencies:
#     PyTorch
# Attention:
#     1. Nothing

import sys
import yaml
import logging
from .operators import *
from .utils import *

from tensorboardX import SummaryWriter


class QNQ():
    def __init__(self,
                 model,
                 save_path="./checkpoints/test",
                 config_file=None,
                 metrics=None,
                 metrics_light=None,
                 steper=None):
        # init parameters
        self.model = model
        self.save_path = save_path
        self.config_file = config_file
        # metrics return a float value for search
        self.metrics = metrics
        # metrics_light return a float value for search, I suggest testset contain 1/10 of calibration datasets.
        self.metrics_light = metrics_light
        self.steper = steper

        # init abstract log path, logger, writer
        self.log_path = setup_logging(self.save_path)
        self.logger = logging.getLogger("qnq")
        self.writer = SummaryWriter(log_dir=self.log_path)

        # load custom config
        try:
            self.load_config()
        except IOError:
            if not os.path.exists(os.path.dirname(self.config_file)):
                os.makedirs(os.path.dirname(self.config_file))
            self.init_config()
            self.logger.error("Detected no config, creating...")
            self.logger.error("Please edit config and re-run the script.")
            sys.exit()

        # processing custom config
        # exec fuse
        if self.fuse_all:
            fuse_module(self.model)
        else:
            self.fuse(self.config_file)

        # initialize quantization
        self.quant_layer_list = []
        self.quant_names = []
        self.logger.info("Initializing...")
        for name, module in self.model.named_modules():
            quant_layer = qnq_switch.get(type(module), None)
            if quant_layer:
                # initialize quant_layer
                quant_layer = quant_layer(
                    name, module, self.qparams["qlayers"][name]['bit_width'],
                    self.writer)

                #! 1. layer config (load)
                #! load - save - default(quant_base)
                #? more robust here
                # do not load weight_fl, if origin is -1
                if quant_layer.weight_fl != -1:
                    quant_layer.weight_fl = self.qparams["qlayers"][name][
                        'weight_fl']
                # do not load activation_fl, if origin is -1
                if quant_layer.activation_fl != -1:
                    quant_layer.activation_fl = self.qparams["qlayers"][name][
                        'activation_fl']
                quant_layer.fuse_flag = self.qparams["qlayers"][name][
                    'fuse_flag']
                quant_layer.group_flag = self.qparams["qlayers"][name][
                    'group_flag']
                quant_layer.scale_flag = self.qparams["qlayers"][name][
                    'scale_flag']

                # append quant_layer and name
                self.quant_layer_list.append(quant_layer)
                self.quant_names.append(name)
                quant_layer.register_get_activation_hook()
        self.transfer_bn2scale()
        self.logger.debug("Quant_layer_list")
        self.logger.debug(str(self.quant_names))

    @exe_time
    def search(self):
        #todo when 2 or more fl have same metrics, how to do?
        def quantize_params():
            self.logger.info("Quantizing params...")
            for layer in self.quant_layer_list:
                layer.quantize_params()

        def quantize_activation():
            self.logger.info("Quantizing activation...")
            for layer in self.quant_layer_list:
                layer.quantize_activation()

        def search_params(layer, metrics_tmp):
            # info log
            self.logger.info("      Now searching " + layer.name +
                             "'s weight_fl...")

            metrics = []
            for test_fl in range(layer.bit_width):
                # save forward time
                if test_fl == layer.weight_fl:
                    metrics.append(metrics_tmp)
                else:
                    layer.trim_params(debug_bw=layer.bit_width,
                                      debug_fl=test_fl)
                    if self.metrics_light and self.metrics_light(
                    ) > self.metrics_light_threshold:
                        metrics_test = self.metrics()
                        metrics.append(metrics_test)
                        # info log
                        self.logger.info("      weight_fl: " + str(test_fl) +
                                         ", metrics: " + str(metrics_test))
                    else:
                        metrics_test = -1
                        metrics.append(metrics_test)
                        # info log
                        self.logger.info("      weight_fl: " + str(test_fl) +
                                         ", metrics: " + str(metrics_test) +
                                         ", metrics_light failed.")

            # if need end search
            if end_search(metrics):
                self.logger.error(
                    "Search Failed, metrics have been below or equals 0, please contact the developer."
                )
                sys.exit()

            # get maximum metrics' index
            layer.weight_fl = metrics.index(max(metrics))

            # info log
            self.logger.info("      " + layer.name + "'s weight_fl=" +
                             str(layer.weight_fl) + ", metrics=" +
                             str(max(metrics)))

            # maintain best weight_fl
            layer.trim_params(debug_bw=layer.bit_width,
                              debug_fl=layer.weight_fl)

            return max(metrics)

        def search_activation(layer, metrics_tmp):
            # info log
            self.logger.info("      Now searching " + layer.name +
                             "'s activation_fl...")

            metrics = []
            for test_fl in range(layer.bit_width):
                if test_fl == layer.activation_fl:
                    metrics.append(metrics_tmp)
                else:
                    layer.trim_activation(debug_bw=layer.bit_width,
                                          debug_fl=test_fl)
                    if self.metrics_light and self.metrics_light(
                    ) > self.metrics_light_threshold:
                        metrics_test = self.metrics()
                        metrics.append(metrics_test)
                        # info log
                        self.logger.info("      activation_fl: " + str(test_fl) +
                                         ", metrics: " + str(metrics_test))
                    else:
                        metrics_test = -1
                        metrics.append(metrics_test)
                        # info log
                        self.logger.info("      activation_fl: " + str(test_fl) +
                                         ", metrics: " + str(metrics_test) +
                                         ", below metrics_light_threshold ")

            # if need end search
            if end_search(metrics):
                self.logger.error(
                    "Search Failed, metrics have been below or equals 0, please contact the developer."
                )
                sys.exit()

            # get maximum metrics' index
            layer.activation_fl = metrics.index(max(metrics))

            # info log
            self.logger.info("      " + layer.name + "'s activation_fl=" +
                             str(layer.activation_fl) + ", metrics=" +
                             str(max(metrics)))

            # maintain best activation_fl
            layer.trim_activation(debug_bw=layer.bit_width,
                                  debug_fl=layer.activation_fl)

            return max(metrics)

        def search_group(layers):
            metrics = []
            # todo test all bit_width be same
            for test_fl in range(layers[0].bit_width):
                for layer in layers:
                    layer.trim_activation(debug_bw=layer.bit_width,
                                          debug_fl=test_fl)
                metrics_test = self.metrics()
                metrics.append(metrics_test)
                # info log
                self.logger.info("      activation_fl: " + str(test_fl) +
                                 ", metrics: " + str(metrics_test))
            # get maximum metrics' index
            for layer in layers:
                layer.activation_fl = metrics.index(max(metrics))

            # maintain best activation_fl
            for layer in layers:
                layer.trim_activation(debug_bw=layer.bit_width,
                                      debug_fl=layer.activation_fl)

            return max(metrics), metrics.index(max(metrics))

        def end_search(metrics_list):
            # todo, if metrics contain negative number??
            if max(metrics_list) <= 0:
                return True
            else:
                return False

        def do_quantize_params():
            # quantize params
            quantize_params()
            # test quantized metrics
            self.logger.info("  Testing quantized params metrics...")
            for layer in self.quant_layer_list:
                layer.trim_params()
            metrics_params = self.metrics()
            self.logger.info("    Quantized params metrics:" +
                             str(metrics_params))

            return metrics_params

        def do_search_params(metrics_mid, metrics_origin):
            self.logger.info("Searching params...")
            #? only search when metrics drop 2 * self.threshold
            if metrics_origin - metrics_mid >= 2 * self.search_params_threshold:
                self.logger.info("  Need to search params, starting...")
                #! recover un-trim before search
                for layer in self.quant_layer_list:
                    layer.recover_params()
                # search params
                for index, layer in enumerate(self.quant_layer_list):
                    #? only search when layer have params
                    if layer.weight_fl != -1:
                        self.logger.info("  " + str(index + 1) + "/" +
                                         str(len(self.quant_layer_list)) +
                                         " Checking " + layer.name +
                                         "'s weight_fl.")
                        layer.trim_params()
                        metrics_tmp = self.metrics()
                        #? only search when metrics drop >= self.threshold
                        if metrics_mid - metrics_tmp >= self.search_params_threshold:
                            self.logger.info("    Need to search, weight_fl=" +
                                             str(layer.weight_fl) +
                                             ", metrics=" + str(metrics_tmp))
                            metrics_mid = search_params(layer, metrics_tmp)
                        else:
                            metrics_mid = metrics_tmp
                            self.logger.info(
                                "    No need to search, weight_fl=" +
                                str(layer.weight_fl) + ", metrics=" +
                                str(metrics_mid))
            else:
                # metrics_mid = metrics_params
                self.logger.info("    No need to search params, metrics=" +
                                 str(metrics_params))
            return metrics_mid

        def do_quantize_activation():
            # process activation
            assert self.steper, "Quantize activation need a steper."
            self.logger.info("Quantizing activation...")
            self.logger.info("  Gathering activation...")
            self.steper()
            for layer in self.quant_layer_list:
                layer.steper_sign = True
            print(" ")

            # quantize activation
            quantize_activation()
            # test quantized metrics
            self.logger.info("  Testing quantized activation metrics...")
            for layer in self.quant_layer_list:
                layer.trim_activation()
            metrics_activation = self.metrics()
            self.logger.info("    Quantized activation metrics: " +
                             str(metrics_activation))
            return metrics_activation

        def do_search_activation(metrics_mid, metrics_origin):
            self.logger.info("Searching activation...")
            #? only search only search when metrics drop 2 * self.threshold
            if metrics_origin - metrics_mid >= 2 * self.search_activation_threshold:
                self.logger.info("  Need to search, starting...")
                #todo valide
                #? remove handler
                # recovery un-trim before search
                for layer in self.quant_layer_list:
                    if layer.hook_handler is not None:
                        layer.hook_handler.remove()
                # search activation
                for index, layer in enumerate(self.quant_layer_list):
                    #? only search when layer need trim activation
                    if layer.activation_fl != -1:
                        self.logger.info("  " + str(index + 1) + "/" +
                                         str(len(self.quant_layer_list)) +
                                         " Checking " + layer.name +
                                         "'s activation_fl.")
                        layer.trim_activation()
                        metrics_tmp = self.metrics()
                        #? only search when metrics drop >= self.threshold
                        if abs(metrics_tmp - metrics_mid
                               ) >= self.search_activation_threshold:
                            self.logger.info(
                                "    Need to search, activation_fl=" +
                                str(layer.activation_fl) + ", metrics=" +
                                str(metrics_tmp))
                            metrics_mid = search_activation(layer, metrics_tmp)
                        else:
                            metrics_mid = metrics_tmp
                            self.logger.info(
                                "    No Need to search, activation_fl=" +
                                str(layer.activation_fl) + ", metrics=" +
                                str(metrics_tmp))
            else:
                metrics_mid = metrics_activation
                self.logger.info("    No need to search activation, metrics=" +
                                 str(metrics_activation))
            return metrics_mid

        def do_search_group(metrics_mid):
            self.logger.info("Searching group...")
            if self.group_num == 0:
                self.logger.warning(
                    "   No need to do_search_group cause group_num = 0.")
                return metrics_mid
            else:
                self.logger.info("  Need to search, starting...")
                metrics_cat = 0
            self.logger.info("  There are " + str(self.group_num) +
                             " group(s) need to process.")
            # make every group's fl same
            for index in range(self.group_num):
                group_layer_list = []
                for layer in self.quant_layer_list:
                    if layer.group_flag == index:
                        group_layer_list.append(layer)
                group_layer_name = [x.name for x in group_layer_list]
                self.logger.info("  Now processing the " + str(index + 1) +
                                 "th group.")
                self.logger.info("  They are " + str(group_layer_name))
                # These layers' bit_width should be same.
                # todo test bitwidth
                metrics_cat, group_fl = search_group(group_layer_list)
                self.logger.info("  " + str(index + 1) +
                                 "th processing done, group_fl=" +
                                 str(group_fl) + ", metrics=" +
                                 str(metrics_cat))
            return metrics_cat

        assert self.metrics, "Search need a metrics."
        #! 1. qparams(show)
        #! show - save - load - default
        self.logger.info("Configuration:")
        self.logger.info("  Log_path: " + str(self.log_path))
        self.logger.info("  Fuse_all: " + str(self.fuse_all))
        self.logger.info("  Quantize_params: " + str(self.quantize_params))
        self.logger.info("  Search_params: " + str(self.search_params))
        self.logger.info("  Quantize_activation: " +
                         str(self.quantize_activation))
        self.logger.info("  Search_activation: " + str(self.search_activation))
        self.logger.info("  Search_group: " + str(self.search_group))
        self.logger.info("  Group_num: " + str(self.group_num))
        self.logger.info("  Search_params_threshold: " +
                         str(self.search_params_threshold))
        self.logger.info("  Search_activation_threshold: " +
                         str(self.search_activation_threshold))
        self.logger.info("  Metrics_light: " +
                         str(bool(self.metrics_light_threshold)))
        self.logger.info("  Metrics_light_threshold: " +
                         str(self.metrics_light_threshold))
        self.logger.info("  Testing origin metrics...")
        metrics_final = metrics_origin = metrics_mid = self.metrics()
        self.logger.info("    Initialization metrics: " + str(metrics_mid))

        if self.quantize_params:
            metrics_params = do_quantize_params()
            metrics_final = metrics_mid = metrics_params
        if self.search_params:
            assert self.quantize_params, "If you want to search params, you must set quantize_params=true in config file."
            metrics_search_params = do_search_params(metrics_mid,
                                                     metrics_origin)
            metrics_final = metrics_mid = metrics_search_params

        if self.quantize_activation:
            assert self.quantize_activation, "If you want to search activation, you must set quantize_activation=true in config file."
            metrics_activation = do_quantize_activation()
            metrics_final = metrics_mid = metrics_activation
        if self.search_activation:
            #? compare to origin not early metrics
            metrics_search_activation = do_search_activation(
                metrics_mid, metrics_origin)
            metrics_final = metrics_mid = metrics_search_activation

        if self.search_group:
            metrics_search_group = do_search_group(metrics_mid)
            metrics_final = metrics_search_group

        if not any([
                self.quantize_params, self.search_params,
                self.quantize_activation, self.search_activation,
                self.search_group
        ]):
            self.logger.error(
                "Oops! We have done nothing, pls check the program.")
            self.logger.error("You shouldn't set all stages to 'false'.")
        else:
            self.save_config()

            self.logger.info("Quantization finished, now summary:")
            self.logger.info("  Origin metrics: " + str(metrics_origin))

            if self.quantize_params:
                self.logger.info("  Quantized params metrics: " +
                                 str(metrics_params))
            if self.search_params:
                self.logger.info("  Search params metrics: " +
                                 str(metrics_search_params))
            if self.quantize_activation:
                self.logger.info("  Quantized activation metrics: " +
                                 str(metrics_activation))
            if self.search_activation:
                self.logger.info("  Search activation metrics: " +
                                 str(metrics_search_activation))
            if self.search_group:
                self.logger.info("  Search group metrics: " +
                                 str(metrics_search_group))

            self.logger.info("  Final metrics: " + str(metrics_final))

    def step(self):
        for layer in self.quant_layer_list:
            layer.init_histograms()
        #? simulate processing bar
        print(".", end=" ")

    def save_config(self, config_file=None):
        qparams = {}
        #! 2. qparams(save)
        qparams['qconfig'] = {}
        qparams['qconfig']['fuse_all'] = self.fuse_all
        qparams['qconfig']['group_num'] = self.group_num
        qparams['qconfig']['quantize_params'] = self.quantize_params
        qparams['qconfig']['search_params'] = self.search_params
        qparams['qconfig']['quantize_activation'] = self.quantize_activation
        qparams['qconfig']['search_activation'] = self.search_activation
        qparams['qconfig']['search_group'] = self.search_group
        qparams['qconfig'][
            'search_params_threshold'] = self.search_params_threshold
        qparams['qconfig'][
            'search_activation_threshold'] = self.search_activation_threshold
        qparams['qconfig'][
            'metrics_light_threshold'] = self.metrics_light_threshold
        qparams['qconfig']['notes'] = "Value '-1' means no operation."

        #! 2. layer config (save)
        qparams['qlayers'] = {}
        for layer in self.quant_layer_list:
            qparams['qlayers'][layer.name] = {}
            qparams['qlayers'][layer.name]['bit_width'] = int(layer.bit_width)
            qparams['qlayers'][layer.name]['weight_fl'] = int(layer.weight_fl)
            qparams['qlayers'][layer.name]['activation_fl'] = int(
                layer.activation_fl)
            qparams['qlayers'][layer.name]['fuse_flag'] = int(layer.fuse_flag)
            qparams['qlayers'][layer.name]['group_flag'] = int(
                layer.group_flag)
            qparams['qlayers'][layer.name]['scale_flag'] = layer.scale_flag
            qparams['qlayers'][layer.name]['layer_type'] = str(
                type(layer.module))[8:-2]

        if config_file:
            with open(config_file, 'w+') as file:
                yaml.dump(qparams, file, sort_keys=False, indent=4)
        else:
            with open(self.log_path + '/quant.yaml', 'w+') as file:
                yaml.dump(qparams, file, sort_keys=False, indent=4)

    def load_config(self):
        # open config
        with open(self.config_file, 'r') as f:
            self.qparams = yaml.load(f, Loader=yaml.SafeLoader)
        #! 3. qparams(load)
        self.fuse_all = self.qparams['qconfig']['fuse_all']
        self.group_num = self.qparams['qconfig']['group_num']
        self.quantize_params = self.qparams['qconfig']['quantize_params']
        self.search_params = self.qparams['qconfig']['search_params']
        self.quantize_activation = self.qparams['qconfig'][
            'quantize_activation']
        self.search_activation = self.qparams['qconfig']['search_activation']
        self.search_group = self.qparams['qconfig']['search_group']
        self.search_params_threshold = self.qparams['qconfig'][
            'search_params_threshold']
        self.search_activation_threshold = self.qparams['qconfig'][
            'search_activation_threshold']
        self.metrics_light_threshold = self.qparams['qconfig'][
            'metrics_light_threshold']

    def init_config(self):
        #! 4. qparams(default)
        self.fuse_all = True
        self.group_num = 0
        self.quantize_params = True
        self.search_params = True
        self.quantize_activation = True
        self.search_activation = True
        self.search_group = True
        self.search_params_threshold = 0.002  # 0.2%
        self.search_activation_threshold = 0.002  # 0.2%
        self.metrics_light_threshold = 0.5  # assume accuracy was metrics
        self.bit_width = 8

        #! 3. layer config (default) (check quant_base)
        # modify model arch because fuse_all default is True
        fuse_module(self.model)
        self.quant_layer_list = []
        for name, module in self.model.named_modules():
            quant_layer = qnq_switch.get(type(module), None)
            if quant_layer:
                quant_layer = quant_layer(name, module, self.bit_width,
                                          self.writer)
                self.quant_layer_list.append(quant_layer)
        # save init_config file
        self.save_config(self.config_file)

    def fuse(self):
        pass

    def trim_activation(self, index=None, debug_bw=None, debug_fl=None):
        self.logger.info("Turn on eval mode.")
        if index != None:
            self.quant_layer_list[index].trim_activation(debug_bw, debug_fl)
        else:
            for layer in self.quant_layer_list:
                layer.trim_activation()

    def transfer_bn2scale(self):
        for layer in self.quant_layer_list:
            if layer.scale_flag:
                bn2scale(layer.module)