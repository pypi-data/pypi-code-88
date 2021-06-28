import os
import requests
import json
import wget
import zipfile
import argparse
import sys
import shutil

try:
    from train.src.netframework.utils.utils import create_folders, print_logger
except Exception:
    from .train.src.netframework.utils.utils import (
        create_folders,
        print_logger,
    )


def download(url, db, update_path=False):
    path_jcell, db_file = os.path.split(db)
    db_name = os.path.split(path_jcell)[1]
    create_folders(path_jcell)

    updated_models = requests.get(url).json()

    current_models_path = os.path.join(path_jcell, db_file)
    if not os.path.exists(current_models_path):
        current_models = {}
    else:
        current_models = json.load(open(current_models_path))

    for key, model in updated_models.items():
        if key == "version":
            continue

        cmodel = None
        if key in current_models:
            cmodel = current_models[key]

        if (
            (cmodel is None)
            or (
                (cmodel is not None) and (cmodel["version"] < model["version"])
            )
            or update_path
        ):
            filename = os.path.expanduser(
                os.path.join(
                    path_jcell,
                    model["urlpath"].split("/")[-1],
                )
            )

            if (cmodel is None) or cmodel["version"] < model["version"]:
                pbar = print_logger()

                def progress(current, total, width=80):
                    pbar.print(
                        current,
                        total,
                        "Downloading {}".format(
                            model["urlpath"].split("/")[-1]
                        ),
                        "",
                    )

                if os.path.exists(filename):
                    try:
                        os.remove(filename)
                    except Exception:
                        pass

                wget.download(model["urlpath"], filename, progress)

                folder, ext = os.path.splitext(filename)
                if ext == ".zip":
                    with zipfile.ZipFile(filename, "r") as zip_ref:
                        zip_ref.extractall(path_jcell)
                    os.remove(filename)
                    filename = filename[:-4]

            model["path"] = filename
            current_models[key] = model

        current_models["version"] = updated_models["version"]
        json.dump(current_models, open(current_models_path, "w"))
    print("{} are up-to-date".format(db_name))


def default_resource():
    resource_file = os.path.expanduser(os.path.join("~", ".jcell", "jcellrc"))
    if os.path.exists(resource_file):
        f = open(resource_file, "r")
        resource_line = f.read()
        f.close()
    else:
        resource_line = os.path.expanduser(os.path.join("~", ".jcell"))

    return resource_line


def main():
    parser = argparse.ArgumentParser(
        prog="jcell-update",
        usage="jcell-update [-h|--help] [--resources_folders]",
        formatter_class=lambda prog: argparse.HelpFormatter(
            prog, max_help_position=100, width=120
        ),
        add_help=False,
    )
    parser.add_argument(
        "--resource_folder",
        type=str,
        default=default_resource(),
        help="Path to resources folder containing pre-trained models and sample datasets.",
    )
    parser.add_argument(
        "-h",
        "--help",
        action="store_true",
        help="Show this help message.",
    )

    args = parser.parse_args()
    if args.help:
        parser.print_help()
        sys.exit()

    args.resource_folder = os.path.expanduser(args.resource_folder)

    resource_file = os.path.expanduser(os.path.join("~", ".jcell", "jcellrc"))
    update_path = False

    if os.path.exists(resource_file):
        f = open(resource_file, "r")
        resource_line = f.read()
        f.close()
    else:
        create_folders(os.path.split(resource_file)[0])
        resource_line = args.resource_folder
        f = open(resource_file, "w")
        f.write(resource_line)
        f.close()

    if args.resource_folder != resource_line:
        print(
            "It looks like you have previously storaged jcell resources at {}. Please, select one of the following options to proceed:".format(
                resource_line
            )
        )
        print(
            "[0] Move resources from {} to {}, and the update from the server into the new location.".format(
                resource_line, args.resource_folder
            )
        )
        print(
            "[1] Delete the content from {}, and the update from the server into the new location.".format(
                resource_line
            )
        )
        print(
            "[2] Update from the server into {} and ignore previous resources.".format(
                args.resource_folder
            )
        )
        print("[3] Cancel update.")
        try:
            option = int(input("Choose an option from 0-3: "))
            if option < 0 or option > 3:
                print("Invalid option. Choose a number from 0-3")
                sys.exit(0)
        except Exception:
            print("Invalid option. Choose a number from 0-3")
            sys.exit(0)

        if option == 3:
            sys.exit(0)
        elif option == 2:
            resource_line = args.resource_folder
            f = open(resource_file, "w")
            f.write(resource_line)
            f.close()
            update_path = True
        elif option == 1:
            try:
                shutil.rmtree(resource_line)
            except OSError as e:
                print("Error: %s : %s" % (resource_line, e.strerror))
            resource_line = args.resource_folder
            create_folders(os.path.split(resource_file)[0])
            f = open(resource_file, "w")
            f.write(resource_line)
            f.close()
            update_path = True
        elif option == 0:
            if os.path.exists(args.resource_folder):
                raise ValueError(
                    "It looks like the folder {} already exists. Please, indicate another folder.".format(
                        args.resource_folder
                    )
                )
            try:
                shutil.copytree(resource_line, args.resource_folder)
            except OSError as e:
                print("Error: %s : %s" % (resource_line, e.strerror))
            try:
                shutil.rmtree(resource_line)
            except OSError as e:
                print("Error: %s : %s" % (resource_line, e.strerror))
            resource_line = args.resource_folder
            create_folders(os.path.split(resource_file)[0])
            f = open(resource_file, "w")
            f.write(resource_line)
            f.close()
            update_path = True

    print("Checking server for updates")
    download(
        "http://jcell.org/models/models.json",
        os.path.expanduser(
            os.path.join(resource_line, "models", "models.json")
        ),
        update_path,
    )

    download(
        "http://jcell.org/datasets/datasets.json",
        os.path.expanduser(
            os.path.join(resource_line, "datasets", "datasets.json")
        ),
        update_path,
    )


if __name__ == "__main__":
    main()
