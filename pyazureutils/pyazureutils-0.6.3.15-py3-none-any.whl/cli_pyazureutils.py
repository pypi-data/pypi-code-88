"""
pyazure CLI
"""
import sys
import logging
import argparse
import os
import textwrap

from logging.config import dictConfig
from appdirs import user_log_dir
import yaml
from yaml.scanner import ScannerError

from .cli_iotcentral import iotcentral_cli_handler
from .status_codes import STATUS_SUCCESS, STATUS_FAILURE

try:
    #pylint: disable=no-name-in-module
    from .version import VERSION, BUILD_DATE, COMMIT_ID
except ImportError:
    print("Version info not found!")
    VERSION = "0.0.0"
    COMMIT_ID = "N/A"
    BUILD_DATE = "N/A"

def setup_logging(user_requested_level=logging.WARNING, default_path='logging.yaml',
                  env_key='MICROCHIP_PYTHONTOOLS_CONFIG'):
    """
    Setup logging configuration for this CLI
    """
    # Logging config YAML file can be specified via environment variable
    value = os.getenv(env_key, None)
    if value:
        path = value
    else:
        # Otherwise use the one shipped with this application
        path = os.path.join(os.path.dirname(__file__), default_path)
    # Load the YAML if possible
    if os.path.exists(path):
        try:
            with open(path, 'rt') as file:
                # Load logging configfile from yaml
                configfile = yaml.safe_load(file)
                # File logging goes to user log directory under Microchip/modulename
                logdir = user_log_dir(__name__, "Microchip")
                # Look through all handlers, and prepend log directory to redirect all file loggers
                num_file_handlers = 0
                for handler in configfile['handlers'].keys():
                    # A filename key
                    if 'filename' in configfile['handlers'][handler].keys():
                        configfile['handlers'][handler]['filename'] = os.path.join(
                            logdir, configfile['handlers'][handler]['filename'])
                        num_file_handlers += 1
                # If file logging is enabled, it needs a folder
                if num_file_handlers > 0:
                    # Create it if it does not exist
                    os.makedirs(logdir, exist_ok=True)
                # Console logging takes granularity argument from CLI user
                configfile['handlers']['console']['level'] = user_requested_level
                # Root logger must be the most verbose of the ALL YAML configurations and the CLI user argument
                most_verbose_logging = min(user_requested_level, getattr(logging, configfile['root']['level']))
                for handler in configfile['handlers'].keys():
                    # A filename key
                    if 'filename' in configfile['handlers'][handler].keys():
                        level = getattr(logging, configfile['handlers'][handler]['level'])
                        most_verbose_logging = min(most_verbose_logging, level)
                configfile['root']['level'] = most_verbose_logging
            dictConfig(configfile)
            return
        except ScannerError:
            # Error while parsing YAML
            print("Error parsing logging config file '{}'".format(path))
        except KeyError as keyerror:
            # Error looking for custom fields in YAML
            print("Key {} not found in logging config file".format(keyerror))
    else:
        # Config specified by environment variable not found
        print("Unable to open logging config file '{}'".format(path))

    # If all else fails, revert to basic logging at specified level for this application
    print("Reverting to basic logging.")
    logging.basicConfig(level=user_requested_level)


def main():
    """
    Entrypoint for installable CLI
    Configures the top-level CLI and parses the arguments
    """

    # Shared switches.  These are inherited by subcommands (and root) using parents=[]
    common_argument_parser = argparse.ArgumentParser(add_help=False)
    common_argument_parser.add_argument("-v", "--verbose",
                                        default="info",
                                        choices=['debug', 'info', 'warning', 'error', 'critical'],
                                        help="Logging verbosity/severity level")

    parser = argparse.ArgumentParser(
        parents=[common_argument_parser],
        formatter_class=argparse.RawTextHelpFormatter,
        description=textwrap.dedent('''\
    pyazureutils: a command line interface for Microchip pyazureutils utility

    Basic usage:
        - pyazureutils <command> <action> [-switches]
        '''),
        epilog=textwrap.dedent('''\
    Usage examples:
        Registration example
        - pyazureutils iotcentral register-device

        '''))

    # Global switches.  These are all "do X and exit"
    parser.add_argument("-V", "--version", action="store_true",
                        help="Print pyazureutils version number and exit")
    parser.add_argument("-R", "--release-info", action="store_true",
                        help="Print pyazureutils release details and exit")
    parser.add_argument("-s", "--serialnumber",
                        type=str,
                        help="USB serial number of the kit to use\n"
                        "This is optional if only one kit is connected\n"
                        "Substring matching on end of serial number is supported")


    # First 'argument' is the command, which is a sub-parser
    subparsers = parser.add_subparsers(title='commands',
                                       dest='command',
                                       description="use one and only one of these commands",
                                       help="for additional help use pyazureutils <command> --help")
    # Make the command required but not for -V or -R arguments
    subparsers.required = not any([arg in ["-V", "--version", "-R", "--release-info"] for arg in sys.argv])

    # iotcentral  command
    iotcentral_command = subparsers.add_parser(name='iotcentral',
                                                formatter_class=lambda prog: argparse.RawTextHelpFormatter(
                                                    prog, max_help_position=0, width=80),
                                                help='functions related to iotcentral',
                                                parents=[common_argument_parser])
    iotcentral_command.add_argument('action',
                                    choices=['register-device'],
                                    help=('''\
iotcentral  actions:
- register-device: reads out the ECC serial number from a kit
'''))

    iotcentral_command.add_argument("--cert", "--certificate-file", type=str,
                        help="Certificate file. Required if kit has not been provisioned",
                        dest="certificate_file")

    iotcentral_command.add_argument("--app", "--application-name", type=str,
                        help="Application name to register with",
                        dest="app_name")

    iotcentral_command.add_argument("--disp", "--display-name", type=str,
                        help="Device display-name to use for registration"
                        "Required if the provisioned kit is not connected; defaults to kit serial number",
                        dest="display_name")

    # Parse
    args = parser.parse_args()

    # Setup logging
    setup_logging(user_requested_level=getattr(logging, args.verbose.upper()))
    logger = logging.getLogger(__name__)

    # Dispatch
    if args.version or args.release_info:
        print("pyazureutils version {}".format(VERSION))
        if args.release_info:
            print("Build date:  {}".format(BUILD_DATE))
            print("Commit ID:   {}".format(COMMIT_ID))
            print("Installed in {}".format(os.path.abspath(os.path.dirname(__file__))))
        return STATUS_SUCCESS

    try:
        if args.command == "iotcentral":
            return iotcentral_cli_handler(args)
    except Exception as exc:
        logger.error("Operation failed with %s: %s", type(exc).__name__, exc)
        logger.debug(exc, exc_info=True)    # get traceback if debug loglevel

    return STATUS_FAILURE

if __name__ == "__main__":
    sys.exit(main())
