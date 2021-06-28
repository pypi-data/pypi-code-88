"""
Entry point for certificate command of pytrust CLI
"""
import os.path
from logging import getLogger

from pyedbglib.serialport.serialportcheck import check_access
from pykitcommander.kitprotocols import get_iot_provision_protocol
from pykitcommander.firmwareinterface import KitSerialConnection
from pykitcommander.kitmanager import KitConnectionError

from .ecc_cert_builder import build_certs_from_ecc

from .cert_get_data import cert_get_skid, create_cert_fingerprint, cert_get_common_name
from .device_cert_builder import build_device_cert
from .verification_cert_builder import build_verification_cert
from .status_codes import STATUS_SUCCESS, STATUS_FAILURE

from .ca_create import ca_create_root
from .ca_create import ca_create_signer_csr
from .ca_create import ca_create_signer

ROOT_CA_FILENAME_BASE = 'root-ca'
ROOT_CA_KEY_FILENAME = ROOT_CA_FILENAME_BASE + '.key'
ROOT_CA_CERT_FILENAME = ROOT_CA_FILENAME_BASE + '.crt'

SIGNER_CA_FILENAME_BASE = 'signer-ca'
SIGNER_CA_KEY_FILENAME = SIGNER_CA_FILENAME_BASE + '.key'
SIGNER_CA_CSR_FILENAME = SIGNER_CA_FILENAME_BASE + '.csr'
SIGNER_CA_CERT_FILENAME = SIGNER_CA_FILENAME_BASE + '.crt'
SIGNER_CA_VER_CERT_FILENAME = SIGNER_CA_FILENAME_BASE + '-verification.crt'

DEVICE_FILENAME_BASE = 'device'
DEVICE_CSR_FILENAME = DEVICE_FILENAME_BASE + '.csr'
DEVICE_CERT_FILENAME = DEVICE_FILENAME_BASE + '.crt'

def print_kit_status(error):
    """
    Print details from KitConnectionError exception due to none or too many kits
    matching serial number specification (if any)
    :args error: KitConnectionError exception object
    """
    # There must be exactly one tool connected, or user must disambiguate with (partial)
    # serial number
    logger = getLogger(__name__)
    if not error.value:
        logger.error("No suitable IoT kits found")
    elif len(error.value) > 1:
        logger.error("Multiple kits found.")
        logger.error("Please specify serial number ending digits for the one you want")
        for tool in error.value:
            logger.error("Tool: %s Serial: %s Device: %s",
                         tool["product"][:16],
                         tool["serial"][:20],
                         tool["device_name"])
    else:
        # If exactly one was found, something is wrong with it, expect reason in msg
        tool = error.value[0]
        logger.error("Tool: %s Serial: %s Device: %s: %s",
                     tool["product"][:16],
                     tool["serial"][:20],
                     tool["device_name"],
                     error.msg)

def certificate_cli_handler(args):
    """
    Entry point for certificate command of CLI
    """
    logger = getLogger(__name__)
    if args.action == "create-from-ecc":
        return _action_create_from_ecc(args)

    if args.action == "create-chain-of-trust":
        logger.info("Creating chain of trust")

        # Generate output
        output_path = args.output_path
        if output_path is None:
            output_path = '.'
        else:
            if not os.path.isdir(output_path):
                logger.info("Create Output folder '%s'", output_path)
                os.mkdir(output_path)

        # generate filename with full path
        root_key_filename = os.path.join(output_path, ROOT_CA_KEY_FILENAME)
        root_cert_filename = os.path.join(output_path, ROOT_CA_CERT_FILENAME)
        signer_key_filename = os.path.join(output_path, SIGNER_CA_KEY_FILENAME)
        signer_csr_filename = os.path.join(output_path, SIGNER_CA_CSR_FILENAME)
        signer_cert_filename = os.path.join(output_path, SIGNER_CA_CERT_FILENAME)

        # Create Root
        ca_create_root(root_ca_key_path=root_key_filename,
                       root_ca_cert_path=root_cert_filename, force=args.force,
                       org_name=args.organization_name, common_name=args.root_common_name)

        # Create signer CSR
        ca_create_signer_csr(signer_ca_key_path=signer_key_filename,
                             signer_ca_csr_path=signer_csr_filename, force=args.force,
                             org_name=args.organization_name, common_name=args.signer_common_name)

        # Create signer
        ca_create_signer(signer_ca_csr_path=signer_csr_filename,
                         signer_ca_cert_path=signer_cert_filename,
                         root_ca_key_path=root_key_filename,
                         root_ca_cert_path=root_cert_filename, force=args.force)


    if args.action == "read-ecc-serialnumber":
        logger.debug("Fetching protocol object from pykitcommander")
        try:
            protocol, port = get_iot_provision_protocol(args.skip_target_programming, serialnumber=args.serialnumber)
        except KitConnectionError as e:
            print_kit_status(e)
            return STATUS_FAILURE

        logger.debug("Opening port: %s", port)
        # Verify access to this port is permitted
        if not check_access(port):
            logger.critical("Port '%s' is not accessible", port)
            return STATUS_FAILURE

        with KitSerialConnection(protocol, port):
            try:
                # Read ECC using raw call with protocol string from here
                logger.info("Reading ECC serial number from kit")
                ecc_serial_number = protocol.read_ecc_serialnumber()
                print(ecc_serial_number)
            except Exception as e:
                logger.error("Read ECC serial number failed with %s: %s", type(e).__name__, e)
                logger.debug(e, exc_info=True)    # get traceback if debug loglevel
                return STATUS_FAILURE


    if args.action == "fingerprint":
        logger.info("Creating fingerprint of the certificate")

        fingerprint = create_cert_fingerprint(args.certificate_file)
        print("fingerprint: {}".format(fingerprint))

    if args.action == "get-skid":
        skid = cert_get_skid(args.certificate_file)
        print("Subject Key Identifier (hex): {}".format(skid))
        print("Subject Key Identifier Length: {}".format(len(skid)))

    if args.action == "get-common-name":
        print("Common Name: {}".format(cert_get_common_name(args.certificate_file)))

    if args.action == "create-from-csr":
        return _action_create_from_csr(args)

    if args.action == "create-verification":
        return _action_create_verification(args)

    return STATUS_SUCCESS

def _action_create_from_csr(args):
    """Create Device certificate from CSR (Certificate Signing Request)

    This action will first create a CSR based on a public key read from the target ECC device and then use this CSR to
    create a device certificate.  Both the generated CSR and the certificate will be written to file.
    :param args: command line arguments
    :type args: class:`argparse.Namespace`
    :return: Status code (STATUS_SUCCESS or STATUS_FAILURE)
    :rtype: int
    """
    logger = getLogger(__name__)

    output_path = _create_output_folder(args)

    csr_filename = os.path.join(output_path, "device.csr")
    cert_filename = os.path.join(output_path, "device.crt")

    try:
        protocol, port = get_iot_provision_protocol(skip_programming=args.skip_target_programming,
                                                    serialnumber=args.serialnumber)
    except KitConnectionError as e:
        print_kit_status(e)
        return STATUS_FAILURE

    # Verify access to this port is permitted
    if not check_access(port):
        logger.critical("Port '%s' is not accessible", port)
        return STATUS_FAILURE

    with KitSerialConnection(protocol, port):
        try:
            build_device_cert(args.signer_ca_certificate_file, args.signer_ca_key_file, protocol,
                              csr_filename, cert_filename, force=args.force)
        except Exception as error:
            logger.error(error)
            print("returning failure")
            return STATUS_FAILURE

    return STATUS_SUCCESS

def _action_create_from_ecc(args):
    """Create Device certificate and Signer certificate using compressed data read from ECC device

    Both certificates will be written to file
    :param args: command line arguments
    :type args: class:`argparse.Namespace`
    :return: Status code (STATUS_SUCCESS or STATUS_FAILURE)
    :rtype: int
    """
    logger = getLogger(__name__)
    logger.info("Connecting to kit...")
    try:
        protocol, port = get_iot_provision_protocol(skip_programming=args.skip_target_programming,
                                                    serialnumber=args.serialnumber)
    except KitConnectionError as e:
        print_kit_status(e)
        return STATUS_FAILURE

    # Verify access to this port is permitted
    if not check_access(port):
        logger.critical("Port '%s' is not accessible", port)
        return STATUS_FAILURE

    output_path = _create_output_folder(args)

    device_cert_filename = os.path.join(output_path, "device_ecc608.crt")
    signer_cert_filename = os.path.join(output_path, "signer_ecc608.crt")

    with KitSerialConnection(protocol, port):
        try:
            build_certs_from_ecc(protocol,
                                 signer_cert_filename,
                                 device_cert_filename,
                                 args.device_certificate_template,
                                 args.signer_certificate_template,
                                 args.force)
        except Exception as error:
            logger.error(error)
            return STATUS_FAILURE

    return STATUS_SUCCESS

def _action_create_verification(args):
    """Create verification certificate

    This action will create a verification certificate from a signer CA certificate and private key and write the
    verification certificate to file
    :param args: command line arguments
    :type args: class:`argparse.Namespace`
    :return: Status code (STATUS_SUCCESS or STATUS_FAILURE)
    :rtype: int
    """
    logger = getLogger(__name__)
    output_path = _create_output_folder(args)

    ver_cert_filename = os.path.join(output_path, "verification.crt")

    try:
        build_verification_cert(args.signer_ca_certificate_file, args.signer_ca_key_file, args.registration_code,
                                ver_cert_filename)
    except Exception as error:
        logger.error(error)
        return STATUS_FAILURE

    return STATUS_SUCCESS

def _create_output_folder(args):
    """
    Create output folder if it does not exist

    Output folder is either given by the -o argument or if not specified the current working directory will be used
    :return: output path
    :rtype: str
    """
    # Output path is optional, if not specified use current directory
    output_path = args.output_path
    if output_path is None:
        output_path = '.'

    # Create output folder
    os.makedirs(output_path, exist_ok=True)

    return output_path
