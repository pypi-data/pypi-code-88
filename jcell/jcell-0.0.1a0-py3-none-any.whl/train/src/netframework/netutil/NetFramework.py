import os
import json
import time
import signal
import argparse
from ..utils.utils import (
    parse_cuda,
    list_gpus,
    create_folders,
    AverageMeter,
    print_logger,
)

from ..utils.utils import Decoder
from importlib import import_module
from ..utils import graphics as gph
import torch.backends.cudnn as cudnn
from ..models.loadmodel import loadmodel
from ..loss.selectloss import selectloss
from ..loss.selectloss import get_metric_path
from ..dataloaders.loaddataset import loaddataset
from ..optimizers.selectopt import selectoptimizer

import warnings
import random
import sys
import numpy as np
import torch

warnings.filterwarnings("ignore")

from .. import (
    save_defaults,
    load_defaults,
    save_defaults_argparse,
    load_defaults_argparse,
)


class NetFramework:
    def __init__(self, defaults_path, custom_parser=None, custom_folder=None):
        self.defaults_path = defaults_path
        if custom_parser is None:
            parser = argparse.ArgumentParser(description="Parameters")
        else:
            parser = custom_parser
        parser.add_argument(
            "--experiment",
            type=str,
            default="segmentation",
            help="Experiment name. A folder with the same name will be created at --output_path (default: segmentation).",
        )
        parser.add_argument(
            "--output_path",
            type=str,
            default="",
            help="Output path for saving the experiments (default: ../out).",
        )
        parser.add_argument(
            "--configuration_path",
            type=str,
            default="",
            help="Configuration path (default: {}).".format(
                self.defaults_path
            ),
            dest="json_path",
        )
        parser.add_argument(
            "--dataset_folder",
            type=str,
            default="",
            help="Path to a dataset (default: '')",
        )
        parser.add_argument(
            "--dataset",
            type=str,
            default="",
            help="Select a value from "
            + str(self.list_data())
            + " which represent dataset key specified in dataconfig_*.json. (default: data2d)",
        )
        parser.add_argument(
            "--dataset_param",
            type=str,
            default="{}",
            nargs="+",
            help="Dataset parameters. Use this argument to specify the path to your images (dataset_folder/image_folder) and labels (dataset_folder/label_folder). Defining the number of classes (number_classes) and 3D processing (is_3D) is also possible. {'dataset_folder': '../../data/dataset1', 'image_folder': 'images', 'label_folder': 'labels3c', 'number_classes':'4', 'is_3D': 'False'}",
        )
        parser.add_argument(
            "--model",
            type=str,
            default="",
            help="Select a value from ["
            + self.list_model()
            + "] which represent the architecture to be used (default: unetpad2D).",
        )
        parser.add_argument(
            "--model_param",
            type=str,
            default="{}",
            nargs="+",
            help="Model parameters. Use this argument to specify if deconvolution is used in the decoder and to enable batch normalization. Model initialization is also possible using 'xavier_normal' or a path to a previously saved model {'is_deconv': False, 'is_batchnorm': False, 'init': ['xavier_normal'| /path/to/model]}",
        )

        parser.add_argument(
            "--loss",
            type=str,
            default="wce_j",
            help="Select a value from ["
            + self.list_loss()
            + "] corresponding with ["
            + self.list_loss_name()
            + "] loss functions respectively (default: wce_j).",
        )

        parser.add_argument(
            "--loss_param",
            type=str,
            default="{}",
            nargs="+",
            help="Loss function parameters. For a comprehensive list o arguments take a look at the documentation.",
        )

        parser.add_argument(
            "--optimizer",
            type=str,
            default="Adam",
            help="Select a value from ["
            + self.list_optimizer()
            + "] which represent the optimizer to be used. This list depend on your PyTorch version (default: Adam).",
        )

        parser.add_argument(
            "--optimizer_param",
            type=str,
            default="{}",
            nargs="+",
            help="Optimizer parameters. Accepted parameters correspond with allowed arguments for PyTorch optimizers (https://pytorch.org/docs/stable/optim.html#algorithms). Example {'lr': 0.0001}.",
        )

        parser.add_argument(
            "--3D",
            action="store_true",
            help="If --3D flag is used then 3D segmentation is performed. If --dataset and --model are not specified, then will be selected according to this flag.",
            dest="is_3D",
        )

        parser.add_argument(
            "--visdom",
            action="store_true",
            help="If included then shows visdom visualization.",
        )
        parser.add_argument(
            "--show_rate",
            type=int,
            default=4,
            help="Visdom refresh after --show_rate iterations (default: 4).",
        )
        parser.add_argument(
            "--print_rate",
            type=int,
            default=4,
            help="Print to standard output after --print_rate iterations (default: 4).",
        )
        parser.add_argument(
            "--save_rate",
            type=int,
            default=100,
            help="Save model after --save_rate epochs. If --save_rate=0 then no save is done during training (default: 100).",
        )
        parser.add_argument(
            "--save_image_rate",
            type=int,
            default=0,
            help="Save image after --save_image_rate epochs. If --save_image_rate=0 then no save is done during training (default: 10).",
            dest="saveim_rate",
        )

        parser.add_argument(
            "--use_gpu",
            action="append",
            type=int,
            help="Use --use_gpu=1 if want to train in the first GPU. If not included then training is executed using the CPU. If --use_gpu=0 the all GPUs are used. An specific list of GPUs can be used, i.e. --use_gpu 1 2 3 4.",
            metavar="[<integer> ...]",
        )

        parser.add_argument(
            "--epochs",
            type=int,
            default=1000,
            help="Number of epochs (default: 1000).",
        )

        parser.add_argument(
            "--batch_size",
            type=int,
            default=1,
            help="Minibatch size (default: 1).",
        )

        parser.add_argument(
            "--batch_accumulation",
            type=int,
            default=1,
            help="Minibatch accumulation (default: 1).",
            dest="batch_acc",
        )

        parser.add_argument(
            "--train_worker",
            type=int,
            default=1,
            help="Number of threads for loading training data (default: 1).",
        )

        parser.add_argument(
            "--dev_worker",
            type=int,
            default=1,
            help="Number of threads for loading validation data (default: 1).",
        )

        parser.add_argument(
            "--resume",
            action="store_true",
            help="Resume training from last saved model for --experiment.",
        )

        parser.add_argument(
            "--list_models",
            action="store_true",
            help="If included shows the list of models and waits for user's input.",
        )

        parser.add_argument(
            "--list_loss",
            action="store_true",
            help="If included shows the list of loss functions and waits for user's input.",
        )

        parser.add_argument(
            "--list_datasets",
            action="store_true",
            help="If included shows the list of datasets and waits for user's input.",
        )

        parser.add_argument(
            "--version",
            action="store_true",
            help="If included shows current version",
        )

        parser.add_argument(
            "--verbose",
            action="store_true",
            help=argparse.SUPPRESS,
        )

        parser.add_argument(
            "--continual_learning",
            type=str,
            default="{}",
            nargs="+",
            help=argparse.SUPPRESS,
        )

        save_defaults_argparse(parser)
        parser = load_defaults_argparse(parser)
        args, not_know_args = parser.parse_known_args()

        if len(not_know_args) > 1 or (
            len(not_know_args) == 1 and not os.path.exists(not_know_args[0])
        ):
            print("Parameters {} not recognized.".format(not_know_args[:-1]))

        if (
            args.help
            or len(not_know_args) > 1
            or (
                len(not_know_args) == 1
                and not os.path.exists(not_know_args[0])
            )
        ):
            parser.print_help()
            exit(0)

        if custom_folder is None and os.path.exists(not_know_args[0]):
            custom_folder = not_know_args[0]

        if not args.verbose:
            warnings.filterwarnings("ignore")
            sys.tracebacklimit = 0

        if args.version:
            print("JCell Instance Segmentation")
            print("California Institute of Technology")
            print("Universidade Federal de Pernambuco")
            print("Version 0.0.1a0")
            sys.exit()

        args.seed = -1
        if args.seed != -1:
            torch.manual_seed(args.seed)
            np.random.seed(args.seed)
            random.seed(args.seed)

        # create outputs folders
        if not os.path.isabs(args.output_path) and custom_folder is not None:
            args.output_path = os.path.join(custom_folder, "out", "")
        elif not os.path.isabs(args.output_path):
            args.output_path = os.path.join(os.getcwd(), "out", "")

        root = args.output_path
        experimentpath = os.path.join(root, args.experiment)
        print("Saving experiment at {}".format(experimentpath))
        folders = {
            "root_path": root,
            "experiment_path": experimentpath,
            "model_path": os.path.join(experimentpath, "model"),
            "images_path": os.path.join(experimentpath, "images"),
        }

        for _, path in folders.items():
            create_folders(path)

        json.dump(
            vars(args), open(os.path.join(experimentpath, "args.json"), "w")
        )
        args.folders = folders

        args.loss_param = " ".join(args.loss_param)
        args.lossparam = json.loads(
            args.loss_param.replace("'", '"'), cls=Decoder
        )
        args.dataset_param = " ".join(args.dataset_param)
        args.datasetparam = json.loads(
            args.dataset_param.replace("'", '"'), cls=Decoder
        )
        args.model_param = " ".join(args.model_param)
        args.modelparam = json.loads(
            args.model_param.replace("'", '"'), cls=Decoder
        )
        args.optimizer_param = " ".join(args.optimizer_param)
        args.optimizerparam = json.loads(
            args.optimizer_param.replace("'", '"'), cls=Decoder
        )
        args.continual_learning = " ".join(args.continual_learning)
        args.continual_learning = json.loads(
            args.continual_learning.replace("'", '"'), cls=Decoder
        )

        if args.json_path == "":
            args.json_path = "defaults"
        elif args.json_path == "JCELL_RESOURCES":
            resource_file = os.path.expanduser(
                os.path.join("~", ".jcell", "jcellrc")
            )
            if os.path.exists(resource_file):
                f = open(resource_file, "r")
                resource_line = f.read()
                f.close()
                args.json_path = os.path.join(
                    resource_line, "datasets", "configuration"
                )
            else:
                args.json_path = "JCELL_RESOURCES"
        elif not os.path.isabs(args.json_path) and custom_folder is not None:
            args.json_path = os.path.join(custom_folder, args.json_path)
        elif not os.path.isabs(args.json_path):
            args.json_path = os.path.join(os.getcwd(), args.json_path)
        defaults_path = args.json_path

        # Parse use cuda
        if args.use_gpu is None:
            args.use_gpu = [-1]

        min_gpu = -1 if len(args.use_gpu) == 1 else 1
        max_gpu = len(list_gpus())
        if any(np.array(args.use_gpu) < min_gpu) or any(
            np.array(args.use_gpu) > max_gpu
        ):
            raise ValueError(
                "Invalid value for --use_gpu. Please, use indexes between 1 and {}. Set --use_gpu=0 for using all GPUs or --use_gpu=-1 if CPU only is desired.".format(
                    max_gpu
                )
                if max_gpu > 0
                else "Nvidia GPU not found in this device. Please, set --use_gpu=0 for CPU only"
            )
        args.use_gpu = [gpu - 1 for gpu in args.use_gpu]
        if args.use_gpu[0] == -1:
            args.use_gpu = [gpu for gpu in range(len(list_gpus()))]
        elif args.use_gpu[0] == -2:
            args.use_gpu = [-1]

        self.device, self.use_parallel = parse_cuda(args.use_gpu)
        if self.device != torch.device("cpu"):
            torch.cuda.set_device(min(args.use_gpu))

        # Visdom visualization
        self.visdom = args.visdom
        if self.visdom:
            try:
                from visdom import Visdom

                self.vis = Visdom(
                    use_incoming_socket=False, raise_exceptions=True
                )
                self.vis.close(env=args.experiment)
                self.visplotter = gph.VisdomLinePlotter(
                    self.vis, env_name=args.experiment
                )
                self.visheatmap = gph.HeatMapVisdom(
                    self.vis, env_name=args.experiment
                )
                self.visimshow = gph.ImageVisdom(
                    self.vis, env_name=args.experiment
                )
                self.vistext = gph.TextVisdom(
                    self.vis, env_name=args.experiment
                )
            except Exception:
                print("Visdom server can't be reached")
                self.visdom = False

        # Showing results rate
        self.print_rate = args.print_rate
        self.show_rate = args.show_rate
        self.save_rate = args.save_rate
        self.saveim_rate = args.saveim_rate

        self.init_epoch = 0
        self.current_epoch = 0
        self.epochs = args.epochs
        self.folders = args.folders
        self.bestmetric = 0
        self.batch_size = args.batch_size
        self.batch_acc = args.batch_acc

        # Load datasets
        if args.list_datasets:
            data = json.load(
                open(os.path.join(defaults_path, "dataconfig_train.json")),
                cls=Decoder,
            )
            k = 0
            for elem in data.keys():
                print("[{}]: {}".format(k, elem))
                k += 1
            val = int(input("Select a dataset: "))
            args.dataset = list(data.keys())[val]

        if args.dataset_folder != "":
            args.datasetparam["dataset_folder"] = args.dataset_folder

        print("Loading dataset: ", end="")
        (
            self.traindataset,
            self.train_loader,
            self.dmodule,
            n_classes,
        ) = loaddataset(
            datasetname=args.dataset,
            experimentparam=args.datasetparam,
            batch_size=args.batch_size,
            worker=args.train_worker,
            is_3D=args.is_3D,
            config_file=os.path.join(defaults_path, "dataconfig_train.json"),
        )

        if isinstance(self.traindataset, list):
            self.traindataset, self.testdataset = self.traindataset
            self.train_loader, self.test_loader = self.train_loader
        else:
            self.testdataset, self.test_loader, _, _ = loaddataset(
                datasetname=args.dataset,
                experimentparam=args.datasetparam,
                batch_size=args.batch_size,
                worker=args.dev_worker,
                is_3D=args.is_3D,
                config_file=os.path.join(defaults_path, "dataconfig_dev.json"),
            )

        # Automatic detection of the number of channels and classes
        sample = self.traindataset[0]
        c = sample["image"].shape
        args.modelparam["in_channels"] = c[0]
        args.modelparam["n_classes"] = n_classes
        self.normalization_type = sample["normalization"]

        self.warp_var_mod = import_module(self.dmodule + ".dataset")

        # Setup model
        if args.list_models:
            data = json.load(
                open(os.path.join(self.defaults_path, "modelconfig.json")),
                cls=Decoder,
            )
            k = 0
            for elem in data.keys():
                print("[{}]: {}".format(k, elem))
                k += 1
            val = int(input("Select a model: "))
            args.model = list(data.keys())[val]

        print("Loading model: ", end="")
        self.net, self.arch, self.mmodule = loadmodel(
            modelname=args.model,
            experimentparams=args.modelparam,
            is_3D=args.is_3D,
            config_file=os.path.join(self.defaults_path, "modelconfig.json"),
        )

        self.net.to(self.device)
        if self.use_parallel:
            self.net = torch.nn.DataParallel(
                self.net, device_ids=self.use_parallel
            )
            cudnn.benchmark = False

        # Setup Optimizer
        print("Selecting optimizer: ", end="")
        self.optimizer = selectoptimizer(
            args.optimizer, self.net, args.optimizerparam
        )

        # Setup Loss criterion
        if args.list_loss:
            data = json.load(
                open(os.path.join(self.defaults_path, "loss_definition.json")),
                cls=Decoder,
            )
            k = 0
            for elem in data.keys():
                print("[{}]: {}".format(k, elem))
                k += 1
            val = int(input("Select a loss: "))
            args.loss = list(data.keys())[val]

        print("Selecting loss function: ", end="")
        self.criterion, self.losseval = selectloss(
            lossname=args.loss,
            parameter=args.lossparam,
            config_file=os.path.join(
                self.defaults_path, "loss_definition.json"
            ),
        )
        self.criterion.to(self.device)
        self.trlossavg = AverageMeter()
        self.vdlossavg = AverageMeter()

        # Others evaluation metrics
        print("Selecting metrics functions:")
        metrics_dict = get_metric_path(
            os.path.join(defaults_path, "metrics.json")
        )
        self.metrics = dict()
        self.metrics_eval = dict()
        self.trmetrics_avg = dict()
        self.vdmetrics_avg = dict()

        for key, value in metrics_dict.items():
            self.metrics[key], self.metrics_eval[key] = selectloss(
                lossname=value["metric"],
                parameter=value.pop("param", {}),
                config_file=os.path.join(
                    self.defaults_path, "metrics_definition.json"
                ),
            )
            self.metrics[key].to(self.device)
            self.trmetrics_avg[key] = AverageMeter()
            self.vdmetrics_avg[key] = AverageMeter()

        self.plogger = print_logger()

        if args.resume:
            self.resume()

        signal.signal(signal.SIGTERM, self.savemodel)
        self.args = args

        if bool(self.args.continual_learning):
            parameters = {
                "model": self.net,
                "dataset": self.traindataset,
                "loss": self.criterion,
                "device": self.device,
            }
            for key, val in self.args.continual_learning.items():
                parameters[key] = val
            self.EWC, _ = selectloss(
                "ewc",
                parameter=parameters,
                config_file=os.path.join(
                    self.defaults_path, "loss_definition.json"
                ),
            )

    def do_train(self):
        for current_epoch in range(self.init_epoch, self.epochs):
            # print("epoch ", current_epoch)
            self.current_epoch = current_epoch

            # Forward over validation set
            avgloss, avgmetric = self.validation(current_epoch)

            save_ = (
                True
                if self.save_rate != 0
                and (current_epoch % self.save_rate) == 0
                else False
            )
            # Save netowrk after self.save_rate epochs
            if save_:
                print("Saving checkpoint epoch {}\n".format(current_epoch))
                self.savemodel(
                    os.path.join(
                        self.folders["model_path"],
                        "epoch{}model.t7".format(current_epoch),
                    )
                )

            # Forward and backward over training set
            self.train(current_epoch)
            self.valid_visualization(current_epoch, 0)

        # Save last model network
        self.savemodel(
            os.path.join(self.folders["model_path"], "lastmodel.t7")
        )

    # Train function
    def train(self, current_epoch):
        data_time = AverageMeter()
        batch_time = AverageMeter()

        self.trlossavg.new_local()
        for key, value in self.trmetrics_avg.items():
            self.trmetrics_avg[key].new_local()

        self.net.train()

        end = time.time()
        total_train = len(self.train_loader)
        for i, sample in enumerate(self.train_loader):
            data_time.update(time.time() - end)

            iteration = float(i) / total_train + current_epoch
            sample = self.warp_var_mod.warp_Variable(sample, self.device)
            images = sample["image"]

            outputs = self.net(images)
            kwarg = eval(self.losseval)
            loss = self.criterion(**kwarg)
            if bool(self.args.continual_learning):
                loss = loss + self.EWC(self.net)
            loss.backward()
            if (i + 1) % self.batch_acc == 0 or (i + 1) == total_train:
                self.optimizer.step()

            self.trlossavg.update(loss.item(), images.size(0))
            for key, value in self.metrics_eval.items():
                kwarg = eval(self.metrics_eval[key])
                metric = self.metrics[key](**kwarg)
                self.trmetrics_avg[key].update(metric.item(), images.size(0))

            if (i + 1) % self.batch_acc == 0 or (i + 1) == total_train:
                self.optimizer.zero_grad()

            batch_time.update(time.time() - end)
            end = time.time()

            if (i % self.print_rate) == 0 or (i + 1 == total_train):
                prefix = "Train [{0}/{1}]".format(
                    current_epoch + 1, self.args.epochs
                )

                print_dict = dict()
                for key, value in self.trmetrics_avg.items():
                    print_dict[key] = "{:.3f} ({:.3f})".format(
                        value.val, value.avg
                    )

                print_dict["loss"] = "{:.3f} ({:.3f})".format(
                    self.trlossavg.val, self.trlossavg.avg
                )

                self.plogger.print(i + 1, total_train, prefix, print_dict)

            if self.visdom and (
                ((i + 1) % self.show_rate) == 0 or ((i + 1) % total_train) == 0
            ):
                info = {"loss": self.trlossavg}

                for key, value in self.trmetrics_avg.items():
                    info[key] = value

                for tag, value in info.items():
                    self.visplotter.show(tag, "train", iteration, value.avg)
                    self.visplotter.show(
                        tag, "train_mean", iteration, value.total_avg
                    )

    def validation(self, current_epoch):
        data_time = AverageMeter()
        batch_time = AverageMeter()

        self.vdlossavg.new_local()
        for key, value in self.vdmetrics_avg.items():
            self.vdmetrics_avg[key].new_local()

        end = time.time()
        total_valid = len(self.test_loader)
        self.net.eval()
        with torch.no_grad():
            for i, sample in enumerate(self.test_loader):
                data_time.update(time.time() - end)

                iteration = float(i) / total_valid + current_epoch - 1
                sample = self.warp_var_mod.warp_Variable(sample, self.device)
                images = sample["image"]

                outputs = self.net(images)
                kwarg = eval(self.losseval)
                loss = self.criterion(**kwarg)

                self.vdlossavg.update(loss.item(), images.size(0))
                for key, value in self.metrics_eval.items():
                    kwarg = eval(self.metrics_eval[key])
                    metric = self.metrics[key](**kwarg)
                    self.vdmetrics_avg[key].update(
                        metric.item(), images.size(0)
                    )

                batch_time.update(time.time() - end)
                end = time.time()

                if i % self.print_rate == 0 or (i + 1 == total_valid):
                    prefix = "Valid [{0}/{1}]".format(
                        current_epoch + 1, self.args.epochs
                    )

                    print_dict = dict()
                    for key, value in self.vdmetrics_avg.items():
                        print_dict[key] = "{:.3f} ({:.3f})".format(
                            value.val, value.avg
                        )

                    print_dict["loss"] = "{:.3f} ({:.3f})".format(
                        self.vdlossavg.val, self.vdlossavg.avg
                    )

                    self.plogger.print(i + 1, total_valid, prefix, print_dict)

                if (
                    self.visdom
                    and current_epoch != self.init_epoch
                    and (
                        ((i + 1) % self.show_rate) == 0
                        or ((i + 1) % total_valid) == 0
                    )
                ):
                    info = {"loss": self.vdlossavg}

                    for key, value in self.vdmetrics_avg.items():
                        info[key] = value

                    for tag, value in info.items():
                        self.visplotter.show(
                            tag, "valid", iteration, value.avg
                        )
                        self.visplotter.show(
                            tag, "valid_mean", iteration, value.total_avg
                        )

        if list(self.vdmetrics_avg.keys()):
            watch_metric = self.vdmetrics_avg[
                list(self.vdmetrics_avg.keys())[0]
            ]
        else:
            watch_metric = self.vdlossavg

        return self.vdlossavg.avg, watch_metric.avg

    def valid_visualization(self, current_epoch, index=0, save=False):
        with torch.no_grad():
            sample = self.testdataset[index]
            sample["image"].unsqueeze_(0)

            sample = self.warp_var_mod.warp_Variable(sample, self.device)
            images = sample["image"]
            img = images[0].cpu().numpy()
            if self.visdom:
                self.visimshow.show("Image", img)

        return 1

    def savemodel(self, modelpath="", killsignal=None):
        if modelpath == "" or killsignal is not None:
            print("Saving checkpoint epoch {}\n".format(self.current_epoch))
            modelpath = os.path.join(
                self.folders["model_path"],
                "epoch{}model.t7".format(self.current_epoch),
            )
        to_save = self.net.module if self.use_parallel else self.net
        state = {
            "epoch": self.current_epoch,
            "arch": self.arch,
            "net": to_save.state_dict(),
            "optimizer": self.optimizer.state_dict(),
            "bestmetric": self.bestmetric,
            "normalization": self.normalization_type,
        }
        torch.save(state, modelpath)

        metrics_dict = {
            "train_loss": self.trlossavg,
            "valid_loss": self.vdlossavg,
        }
        for key, value in self.trmetrics_avg.items():
            metrics_dict["train_" + key] = value
        for key, value in self.vdmetrics_avg.items():
            metrics_dict["valid_" + key] = value

        for tag, value in metrics_dict.items():
            np.savetxt(
                self.folders["experiment_path"] + "/" + tag + ".txt",
                np.array(value.array),
                delimiter=",",
                fmt="%3.6f",
            )

        if killsignal is not None:
            exit(-1)

    def loadmodel(self, modelpath):
        if os.path.isfile(modelpath):
            checkpoint = torch.load(modelpath, map_location="cpu")
            to_load = self.net.module if self.use_parallel else self.net
            to_load.load_state_dict(checkpoint["net"])
            self.optimizer.load_state_dict(checkpoint["optimizer"])
            self.current_epoch = checkpoint["epoch"]
            self.arch = checkpoint["arch"]
            self.bestmetric = checkpoint["bestmetric"]

            files = [
                f
                for f in sorted(os.listdir(self.folders["experiment_path"]))
                if (f.find("train_") != -1 and f.find(".txt") != -1)
            ]
            for f in files:
                narray = np.loadtxt(
                    os.path.join(self.folders["experiment_path"], f),
                    delimiter=",",
                )
                metric = f[6 : f.find(".txt")]
                if metric == "loss":
                    self.trlossavg.load(narray, 1)
                if metric in self.trmetrics_avg:
                    self.trmetrics_avg[metric].load(narray.tolist(), 1)

            files = [
                f
                for f in sorted(os.listdir(self.folders["experiment_path"]))
                if (f.find("valid_") != -1 and f.find(".txt") != -1)
            ]
            for f in files:
                narray = np.loadtxt(
                    os.path.join(self.folders["experiment_path"], f),
                    delimiter=",",
                )
                metric = f[6 : f.find(".txt")]
                if metric == "loss":
                    self.vdlossavg.load(narray, 1)
                if metric in self.vdmetrics_avg:
                    self.vdmetrics_avg[metric].load(narray.tolist(), 1)

        else:
            raise Exception("Model not found")

    def resume(self):
        if os.path.isdir(self.folders["model_path"]):
            files = [
                f
                for f in sorted(os.listdir(self.folders["model_path"]))
                if (f.find("epoch") != -1 and f.find("model.t7") != -1)
            ]
            if files:
                self.init_epoch = (
                    max([int(f[5 : f.find("model.t7")]) for f in files]) + 1
                )
                self.loadmodel(
                    os.path.join(
                        self.folders["model_path"],
                        "epoch" + str(self.init_epoch - 1) + "model.t7",
                    )
                )
                print("Resuming on epoch" + str(self.init_epoch - 1))

    def current_folder(self):
        folder = os.path.split(__file__)[0]
        folder = os.path.split(folder)[0]
        folder = os.path.split(folder)[0]
        return folder

    def list_data(self):
        data = json.load(
            open(
                os.path.join(
                    self.current_folder(),
                    self.defaults_path,
                    "dataconfig_train.json",
                )
            ),
            cls=Decoder,
        )
        dl = []
        for elem in data.keys():
            dl += [elem]
        return dl

    def list_model(self):
        data = json.load(
            open(
                os.path.join(
                    self.current_folder(),
                    self.defaults_path,
                    "modelconfig.json",
                )
            ),
            cls=Decoder,
        )
        dl = ""
        for elem in data.keys():
            dl += elem + ", "
        dl = dl[:-2]
        return str(dl)

    def list_loss(self):
        data = json.load(
            open(
                os.path.join(
                    self.current_folder(),
                    self.defaults_path,
                    "loss_definition.json",
                )
            ),
            cls=Decoder,
        )
        dl = ""
        for elem in data.keys():
            dl += elem + ", "
        dl = dl[:-2]
        return str(dl)

    def list_loss_name(self):
        data = json.load(
            open(
                os.path.join(
                    self.current_folder(),
                    self.defaults_path,
                    "loss_definition.json",
                )
            ),
            cls=Decoder,
        )
        dl = ""
        for elem in data.keys():
            dl += (
                data[elem].pop("name", "unknown loss function")
                + "("
                + elem
                + "),"
            )
        dl = dl[:-2]
        return str(dl)

    def list_optimizer(self):
        import inspect

        data = inspect.getmembers(sys.modules["torch.optim"], inspect.isclass)
        dl = ""
        for elem, _ in data:
            if elem != "Optimizer":
                dl += elem + ", "
        dl = dl[:-2]
        return str(dl)
