import time
import sys
import os
import argparse

try:
    from .netutil.SegmentNet import SegmentNet
except Exception:
    from netutil.SegmentNet import SegmentNet


def jcell_train(
    experiment="segmentation",
    output_path="",
    configuration_path="JCELL_RESOURCES",
    dataset_folder="",
    dataset="",
    dataset_param={},
    model="",
    model_param={},
    optimizer="Adam",
    optimizer_param={},
    loss="wce_j",
    loss_param={},
    is_3D=False,
    visdom=False,
    show_rate=4,
    print_rate=4,
    save_rate=100,
    save_image_rate=0,
    use_gpu=[-1],
    epochs=1000,
    batch_size=1,
    batch_accumulation=1,
    train_worker=1,
    dev_worker=1,
    resume=False,
):
    args_dict = locals().copy()
    args_dict["3D"] = args_dict["is_3D"]
    del args_dict["is_3D"]

    def args2list(args):
        cmd_args = []
        for key, value in args.items():
            if key == "args_dict":
                continue
            elif isinstance(value, str) and value == "":
                continue
            elif isinstance(value, bool):
                if value:
                    cmd_args += ["--{}".format(key)]
            elif isinstance(value, dict):
                cmd_args += [
                    "--{}={}".format(key, str(value).replace(" ", ""))
                ]
            elif isinstance(value, list):
                for val in value:
                    cmd_args += ["--{}={}".format(key, val)]
            else:
                cmd_args += ["--{}={}".format(key, value)]
        return cmd_args

    custom_folder = os.getcwd()
    args, _ = os.path.split(__file__)
    os.chdir(args)
    sys.path[0] = args
    args = os.path.join(args, "train.py")

    sys.argv = [args] + args2list(args_dict)
    parser = argparse.ArgumentParser(description="Parameters", add_help=False)
    parser.add_argument(
        "-h",
        "--help",
        action="store_true",
        help="Show this help message.",
    )
    net = main("defaults", parser, custom_folder)
    os.chdir(custom_folder)
    sys.path[0] = custom_folder
    return net


def main(default="defaults", parser=None, custom_folder=None):
    sortingDL = SegmentNet(default, parser=parser, custom_folder=custom_folder)
    start = time.time()
    sortingDL.do_train()
    print("Total Training Time {:.3f}".format(time.time() - start))
    return sortingDL.net


if __name__ == "__main__":
    main()
