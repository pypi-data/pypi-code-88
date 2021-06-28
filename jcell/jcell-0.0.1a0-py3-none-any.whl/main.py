import os
import sys
import warnings

import argparse


def main():
    parser = argparse.ArgumentParser(
        prog="jcell",
        usage="jcell [-h|--help] {train| segment}",
        formatter_class=lambda prog: argparse.HelpFormatter(
            prog, max_help_position=100, width=120
        ),
    )

    subparsers = parser.add_subparsers(dest="stage")

    train_parser = subparsers.add_parser(
        "train",
        usage="jcell train [-h| --help] [--experiment EXPERIMENT] [--output_path OUTPUT_PATH] [--configuration_path JSON_PATH] [--model MODEL] [--model_param MODEL_PARAM] [--dataset DATASET] [--dataset_param DATASET_PARAM] [--3D]  [--visdom]  [--show_rate SHOW_RATE] [--print_rate PRINT_RATE] [--save_rate SAVE_RATE] [--save_image_rate SAVEIM_RATE] [--use_gpu 1] [--epochs EPOCHS] [--batch_size BATCH_SIZE] [--batch_accumulation BATCH_ACC] [--train_worker TRAIN_WORKER] [--dev_worker DEV_WORKER] [--optimizer OPTIMIZER] [--optimizer_param OPTIMIZER_PARAM] [--loss LOSS] [--loss_param LOSS_PARAM] [--resume]  [--list_models]  [--list_loss]  [--list_datasets] [--version]",
        help="Use this positional argument to perform training",
        formatter_class=lambda prog: argparse.HelpFormatter(
            prog, max_help_position=100, width=120
        ),
        add_help=False,
    )

    test_parser = subparsers.add_parser(
        "segment",
        usage="jcell segment [-h| --help] {--input /path/to/images --model /path/to/models |--probability /path/to/probablities_maps} [--output /path/to/output/folder/] [--post MAP] [--post_param {'min_area':200}] [--use_gpu 1] [--output_type all [all ...]] [--confidence 0] [--3D]",
        help="Use this positional argument to perform segmentation",
        formatter_class=lambda prog: argparse.HelpFormatter(
            prog, max_help_position=100, width=120
        ),
        add_help=False,
    )

    help_parser = subparsers.add_parser(
        "help",
        usage="jcell {train| segment} [-h|--help] [--version]",
        help="jcell help",
        formatter_class=lambda prog: argparse.HelpFormatter(
            prog, max_help_position=100, width=120
        ),
        add_help=False,
    )
    help_parser.add_argument(
        "--version",
        action="store_true",
        help="If included shows current version",
    )
    help_parser.add_argument(
        "-h",
        "--help",
        action="store_true",
        help="Show this help message.",
    )

    try:
        if sys.argv[1] != "segment" and sys.argv[1] != "train":
            sys.argv.insert(1, "help")
        superargs, _ = parser.parse_known_args()

    except Exception:
        superargs = argparse.Namespace(stage=sys.argv[1])
    except SystemExit:
        superargs = argparse.Namespace(stage="help")

    args, _ = os.path.split(sys.argv[0])
    if superargs.stage == "help":
        if superargs.version:
            print("JCell Instance Segmentation")
            print("California Institute of Technology")
            print("Universidade Federal de Pernambuco")
            print("Version 0.0.1a0")
            sys.exit()

        else:
            help_parser.print_help()
            sys.exit()

    elif superargs.stage == "train":
        try:
            from .train import train
        except Exception:
            from train import train

        args = os.path.join(args, "train", "src")
        os.chdir(args)
        sys.path[0] = args
        args = os.path.join(args, "train.py")

        custom_folder = sys.argv[-1]
        sys.argv = [args] + sys.argv[2:-1]
        train_parser.add_argument(
            "-h",
            "--help",
            action="store_true",
            help="Show this help message.",
        )
        train("defaults", train_parser, custom_folder)

    elif superargs.stage == "segment":
        try:
            from .evaluation import eval
        except Exception:
            from evaluation import eval

        current_folder = sys.argv[-1]
        sys.argv = [args] + sys.argv[2:-1]
        test_parser.add_argument(
            "-h",
            "--help",
            action="store_true",
            help="Show this help message.",
        )
        eval(test_parser, current_folder)

    elif superargs.stage == "help":
        pass
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
