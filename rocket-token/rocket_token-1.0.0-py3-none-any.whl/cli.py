"""Command line interface functions to access RocketToken class"""
import argparse
import logging
import os
import sys

from .rocket_token import RocketToken

logging.basicConfig(filename=".log")


def generate_keys() -> None:
    """Generate private and public key pair files using RSA algorithm.

    CLI: rt_keys - d < dir_path >

    Returns: None

    """
    # Create the parser
    my_parser = argparse.ArgumentParser(
        prog="rt_keys",
        usage="%(prog)s dir",
        description="Generate Public and Private key files.",
    )

    # Add the arguments
    my_parser.add_argument(
        "-d", metavar="dir", type=str, help="Location to save private/public key files"
    )

    # Execute the parse_args() method
    args = my_parser.parse_args()

    try:
        os.mkdir(args.d)
    except (OSError, FileNotFoundError, FileExistsError) as e:
        logging.exception(msg=e.strerror, exc_info=1)
        sys.exit(1)

    RocketToken.generate_key_pair(path=args.d)
    sys.exit(0)


def encrypt_dictionary_script() -> None:
    """Returns an encrypted dictionary:

    Required parameters:

        -f: Filepath to the public key file e.g. <path>/id_rsa.pub

    Optional arguments:

        -o: <argument>=<value> e.g. -o customer_id=3 refresh=refresh_token

    CLI usage:

    rt_encrypt -f <path>/id_rsa.pub -o customer_id=3 refresh=refresh_token

    :return: None

    """
    # Create the parser
    my_parser = argparse.ArgumentParser(
        prog="rt_encrypt",
        usage="%(prog)s -f <path>/id_rsa.pub -o parameter=value",
        description="Encrypt a dictionary.",
    )

    # Add the arguments
    my_parser.add_argument(
        "-f",
        metavar="--file",
        type=str,
        required=True,
        help="Filepath to the public key file.",
    )

    my_parser.add_argument(
        "-o",
        metavar="--optional",
        action="store",
        nargs=argparse.REMAINDER,
        help="Arbitrary number of keyword arguments <keyword>=<value>",
    )

    # options, args = my_parser.parse_args()
    args = my_parser.parse_args()

    # Generate payload dict from arguments
    payload = {}
    for arg in args.o:
        if "=" not in arg:
            print(f"Args must be split by a `=`, please fix: {arg}")
            sys.exit(1)
        key, value = arg.split("=")
        payload[key] = value

    rocket_token = RocketToken.load_from_path(public_path=args.f, private_path=None)
    token = rocket_token.encrypt_dictionary(dict_to_encrypt=payload)

    print(f"Token: {token}")
    sys.exit(0)


def generate_token_script() -> None:
    """Returns a token when supplied with:

    Required parameters:

        -f: Filepath to the public key file e.g. <path>/id_rsa.pub
        -p: Path to the requested resource e.g. /reports/campaign
        -e: Expiry time of request from now in minutes (integer).
        -m: Request method i.e. [GET, POST, DELETE, PUT]

    Optional arguments:

        -o: <argument>=<value> e.g. -o customer_id=3 refresh=refresh_token

    CLI usage:

    rt_token -f <path>/id_rsa.pub -p /reports -e 5 -m GET -o refresh=rtoken

    :return: None

    """
    # Create the parser
    my_parser = argparse.ArgumentParser(
        prog="rt_token",
        usage="%(prog)s -f -p -e -m -o parameter=value",
        description="Generate a new token.",
    )

    # Add the arguments
    my_parser.add_argument(
        "-f",
        metavar="--file",
        type=str,
        required=True,
        help="Filepath to the public key file.",
    )
    my_parser.add_argument(
        "-p",
        metavar="--path",
        type=str,
        required=True,
        help="Path to the requested resource e.g. /google-reporting/report/campaign",
    )
    my_parser.add_argument(
        "-e", metavar="--exp", type=int, required=True, help="Expiry time in minutes."
    )
    my_parser.add_argument(
        "-m",
        metavar="--method",
        type=str,
        required=True,
        help="Method used in the request must be in [GET, POST].",
    )
    my_parser.add_argument(
        "-o",
        metavar="--optional",
        action="store",
        nargs=argparse.REMAINDER,
        help="Arbitrary number of keyword arguments <keyword>=<value>",
    )

    # options, args = my_parser.parse_args()
    args = my_parser.parse_args()

    # Generate payload dict from arguments
    payload = {}
    for arg in args.o:
        if "=" not in arg:
            print(f"Args must be split by a `=`, please fix: {arg}")
            sys.exit(1)
        key, value = arg.split("=")
        payload[key] = value

    rocket_token = RocketToken.load_from_path(public_path=args.f, private_path=None)
    token = rocket_token.new_token(path=args.p, exp=args.e, method=args.m, **payload)

    print(f"Token: {token}")
    sys.exit(0)
