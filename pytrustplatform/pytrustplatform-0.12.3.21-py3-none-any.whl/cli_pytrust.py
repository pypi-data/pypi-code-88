"""
pytrustplatform CLI: "pytrust"
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

from .cli_certificate_main import certificate_cli_handler
from .cli_manifest_main import manifest_cli_handler
from .status_codes import STATUS_SUCCESS, STATUS_FAILURE
from .ca_create import DEFAULT_ORGANIZATION_NAME, DEFAULT_ROOT_COMMON_NAME, DEFAULT_SIGNER_COMMON_NAME

try:
    #pylint: disable=no-name-in-module
    from .version import VERSION, BUILD_DATE, COMMIT_ID
except ImportError:
    print("Version info not found!")
    VERSION = "0.0.0"
    COMMIT_ID = "N/A"
    BUILD_DATE = "N/A"

# Actions requiring signer CA certificate and signer CA key file arguments
ACTIONS_REQUIRING_SIGNER_CA = ['create-from-csr', 'create-verification']

# Actions requiring certificate argument (--cert)
ACTIONS_REQUIRING_CERT = ['fingerprint', 'get-skid', 'get-common-name']

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
                if num_file_handlers > 0:
                    # Create it if it does not exist
                    os.makedirs(logdir, exist_ok=True)

                if user_requested_level <= logging.DEBUG:
                    # Using a different handler for DEBUG level logging to be able to have a more detailed formatter
                    configfile['root']['handlers'].append('console_detailed')
                    # Remove the original console handlers
                    try:
                        configfile['root']['handlers'].remove('console_only_info')
                    except ValueError:
                        # The yaml file might have been customized and the console_only_info handler might
                        # already have been removed
                        pass
                    try:
                        configfile['root']['handlers'].remove('console_not_info')
                    except ValueError:
                        # The yaml file might have been customized and the console_only_info handler might
                        # already have been removed
                        pass
                else:
                    # Console logging takes granularity argument from CLI user
                    configfile['handlers']['console_only_info']['level'] = user_requested_level
                    configfile['handlers']['console_not_info']['level'] = user_requested_level

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
    pytrust: a command line interface for Microchip pytrustplatform

    basic usage:
        - pytrust <command> <action> [-switches]
            '''),
        epilog=textwrap.dedent('''usage examples:
        Read the Subject Key Identifier (SKID) from a certificate
        - pytrust certificate get-skid --cert mycertificate.crt

        Read the Common Name (CN) from a certificate
        - pytrust certificate get-common-name --cert mycertificate.crt

        Create a fingerprint from a certificate
        - pytrust certificate fingerprint --cert mycertificate.crt

        Create a device certificate from an ECC device on a kit
        - pytrust certificate create-from-ecc

        Create chain of trust certificates and save it in myfolder
        - pytrust certificate create-chain-of-trust -o myfolder

        Create a device certificate and Certificate Signing Request (CSR)
        - pytrust certificate create-from-csr --scac my_signer_ca.crt --scak my_signer_ca.key

        Create a verification certificate
        - pytrust certificate create-verification --scac my_signer_ca.crt --scak my_signer_ca.key --reg "0123456789"
        '''))

    # Global switches.  These are all "do X and exit"
    parser.add_argument("-V", "--version", action="store_true",
                        help="Print pytrust version number and exit")
    parser.add_argument("-R", "--release-info", action="store_true",
                        help="Print pytrust release details and exit")
    parser.add_argument("-s", "--serialnumber",
                        type=str,
                        help="USB serial number of the kit to use\n"
                        "This is optional if only one kit is connected\n"
                        "Substring matching on end of serial number is supported")

    # First 'argument' is the command, which is a sub-parser
    subparsers = parser.add_subparsers(title='commands',
                                       dest='command',
                                       description="use one and only one of these commands",
                                       help="for additional help use pytrust <command> --help")
    # Make the command required but not for -V or -R arguments
    subparsers.required = not any([arg in ["-V", "--version", "-R", "--release-info"] for arg in sys.argv])

    # Certificate command
    certificate_command = subparsers.add_parser(name='certificate',
                                                formatter_class=lambda prog: argparse.RawTextHelpFormatter(
                                                    prog, max_help_position=0, width=80),
                                                aliases=['cert'],
                                                help='functions related to individual certificates',
                                                parents=[common_argument_parser])
    certificate_command.add_argument('action',
                                     help=('''\
\ncertificate actions:
- read-ecc-serialnumber: reads out the ECC serial number from a kit
- create-from-ecc: creates a device certificate and signer certificate
  using compressed data read out from the ECC device on a kit
- create-from-csr: creates a device certificate using a Certificate Signing
  Request (CSR) created from data read out from the ECC device on a kit
- create-verification: creates a verification certificate from a signer
  CA certificate and key
- fingerprint:  generates a fingerprint from a certificate file passed in
- get-skid: prints Subject Key Identifier from a certificate file passed in
- get-common-name: prints Common Name from a certificate file passed in
- create-chain-of-trust: Create a chain of trust with root CA, signer CSR and signer certificates at current or specified folder
'''),
                                     choices=['read-ecc-serialnumber', 'create-from-ecc', 'create-from-csr',
                                              'create-verification', 'create-chain-of-trust', 'fingerprint',
                                              'get-skid', 'get-common-name'])

    certificate_command.add_argument("--skip", "--skip-target-programming",
                                     help="do not program the target with provisioning firmware",
                                     action="store_true",
                                     dest="skip_target_programming")

    certificate_command.add_argument("--dct", "--device-certificate-template", type=str,
                                     help="device certificate template",
                                     dest="device_certificate_template")

    certificate_command.add_argument("--sct", "--signer-certificate-template", type=str,
                                     help="signer certificate template",
                                     dest="signer_certificate_template")

    certificate_command.add_argument("--scak", "--signer-ca-key-file", type=str,
                                     help="signer certificate authority private key file",
                                     required=any(action in sys.argv for action in ACTIONS_REQUIRING_SIGNER_CA),
                                     dest="signer_ca_key_file")

    certificate_command.add_argument("--scac", "--signer-ca-certificate-file", type=str,
                                     help="signer certificate authority certificate file",
                                     required=any(action in sys.argv for action in ACTIONS_REQUIRING_SIGNER_CA),
                                     dest="signer_ca_certificate_file")

    certificate_command.add_argument("-o", "--output-path", type=str,
                                     help="path to store certificates")

    certificate_command.add_argument("--cert", "--certificate-file", type=str,
                                     help="certificate file",
                                     required=any(action in sys.argv for action in ACTIONS_REQUIRING_CERT),
                                     dest="certificate_file")

    certificate_command.add_argument("--reg", "--registration-code", type=str,
                                     help="registration code",
                                     required="create-verification" in sys.argv,
                                     dest="registration_code")

    certificate_command.add_argument("--org", "--organization-name", type=str,
                                     help="CA certificate issuer organization name",
                                     required=False, default=DEFAULT_ORGANIZATION_NAME,
                                     dest="organization_name")

    certificate_command.add_argument("--rcn", "--root-common-name", type=str,
                                     help="Root CA certificate issuer common name",
                                     required=False, default=DEFAULT_ROOT_COMMON_NAME,
                                     dest="root_common_name")

    certificate_command.add_argument("--scn", "--signer-common-name", type=str,
                                     help="Signer CA certificate issuer common name",
                                     required=False, default=DEFAULT_SIGNER_COMMON_NAME,
                                     dest="signer_common_name")

    certificate_command.add_argument("-f", "--force",
                                     help="Force re-generation and overwriting existing device CSR/certificate files",
                                     action="store_true")


    # Manifest command
    manifest_command = subparsers.add_parser(name='manifest',
                                             formatter_class=lambda prog: argparse.RawTextHelpFormatter(
                                                 prog, max_help_position=0, width=80),
                                             help='functions related to certificate manifests',
                                             parents=[common_argument_parser])
    manifest_command.add_argument('action',
                                  choices=['build', 'search', 'extract', 'validate', 'download'],
                                  help=('''
\nmanifest actions:
- build:  build manifest from a local certificate, a compressed certificate
  or ECC608 certificates
- search:  search a manifest for a specific entry
- extract:  extract all certificates
- validate: validate a manifest
- download: retrieve latest manifest verification certificates
'''))

    # Parse
    args = parser.parse_args()

    # Setup logging
    setup_logging(user_requested_level=getattr(logging, args.verbose.upper()))
    logger = logging.getLogger(__name__)

    # Dispatch
    if args.version or args.release_info:
        print("pytrust version {}".format(VERSION))
        if args.release_info:
            print("Build date:  {}".format(BUILD_DATE))
            print("Commit ID:   {}".format(COMMIT_ID))
            print("Installed in {}".format(os.path.abspath(os.path.dirname(__file__))))
        return STATUS_SUCCESS

    try:
        if args.command == "certificate" or args.command == "cert":
            return certificate_cli_handler(args)
        if args.command == "manifest":
            return manifest_cli_handler(args)
    except Exception as exc:
        logger.error("Operation failed with %s: %s", type(exc).__name__, exc)
        logger.debug(exc, exc_info=True)    # get traceback if debug loglevel

    return STATUS_FAILURE

if __name__ == "__main__":
    sys.exit(main())
