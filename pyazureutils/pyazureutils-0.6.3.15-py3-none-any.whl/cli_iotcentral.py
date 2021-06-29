"""
Azure IoT Central registration
"""
import os
from logging import getLogger
from pykitinfo import pykitinfo
from pytrustplatform.cert_get_data import cert_get_common_name_from_pem
from .iotcentral import AzureIotCentralSession, AzureIotCentral
from .status_codes import STATUS_SUCCESS, STATUS_FAILURE

def iotcentral_cli_handler(args):
    """
    CLI entry point for command: iotcentral
    """
    if args.action == "register-device":
        return _action_register_device(args)

def _action_register_device(args):
    """
    CLI entry point for action: register-device
    """
    return iotcentral_register_device(args.app_name, args.certificate_file, args.display_name)

def iotcentral_register_device(app_name=None, certificate_file=None, display_name=None):
    """
    Register an IoT device in Azure's IoTCentral

    Registration requires that the user logs into Azure using the Azure CLI "az"
    Tokens will be collected from the user's Azure local token storage

    Registration uses an application name which is either:
    - collected from IoTCentral account (first one found is used)
    - passed in as an argument

    Registration uses a certificate which is either:
    - collected from local certificate storage for a kit, if a kit has been provisioned using this machine
    - passed in as a filename argument

    Registration uses a device name which is derived from the subject common name of the certificate used

    Registration uses a display name which is either:
    - derived from the kit serial number (if a kit is connected)
    - passed in as an argument

    :param app_name: Application Name to register device with
    :param certificate_file: Device certificate PEM file
    :param display_name: Display name to register device with
    """
    logger = getLogger(__name__)

    # Start a session communicating with IoTCentral
    azuresession = AzureIotCentralSession()
    azuresession.connect()

    az = AzureIotCentral(azuresession, app_name)
    if not app_name:
        # No app name given: query the server
        apps = az.list_applications()
        logger.info("%d app(s) found", len(apps))
        if len(apps) == 0:
            raise Exception("No applications found on Azure IoTCentral!")
        if len(apps) > 1:
            logger.warning("%d applications found on Azure IoTCentral - selecting the first one found.")

        logger.info("Using application: %s (%s)", apps[0]['name'], apps[0]['displayName'])
        az.set_app_name(apps[0]['name'])


    #admin_role_id = az.get_admin_role_id()
    #logger.info("Admin id: %s", admin_role_id)

    #operator_role_id = az.get_operator_role_id()
    #logger.info("Operator id: %s", operator_role_id)

    #az.get_subscriptions()
    #az.get_roles()
    #az.get_users()

    # Certificate is taken from a local cert storage, which contains certificates for kits which have been provisioned
    # or passed in by CLI argument
    if certificate_file:
        cert_file_name = certificate_file
        logger.info("Using certificate file '%s'", cert_file_name)
        try:
            # Try to open the certificate file
            with open(cert_file_name, "r") as cert_file:
                certificate = cert_file.read()
        except FileNotFoundError:
            logger.error("Unable to load certificate from file: '%s'", cert_file_name)
            return STATUS_FAILURE
    else:
        # Look for connected kits
        kits = pykitinfo.detect_all_kits()
        if not kits:
            raise Exception("No kit found. Either connect a kit or use the CLI arguments to provide certificate.")
        if len(kits) > 1:
            raise Exception("Too many kits connected!")

        serialnumber = kits[0]['usb']['serial_number']
        logger.info("Using kit '%s'", serialnumber)

        # Check in local folder
        certs_dir = os.path.join(os.path.expanduser("~"), ".microchip-iot", serialnumber)
        cert_file_name = os.path.abspath(os.path.join(certs_dir, "device.crt"))
        logger.info("Using certificate file '%s'", cert_file_name)

        try:
            # Try to open the certificate file
            with open(cert_file_name, "r") as cert_file:
                certificate = cert_file.read()
        except FileNotFoundError:
            logger.error("Unable to load certificate from file: '%s' - has the kit been provisioned?", cert_file_name)
            return STATUS_FAILURE
    
    logger.info("Certificate loaded")

    # Extract from certificate
    logger.info("Extracting common name from certificate (to use as device ID")
    device_id = cert_get_common_name_from_pem(certificate)
    logger.info("Device ID will be: '%s'", device_id)

    # Retrieve device templates from the server
    logger.info("Retrieving device templates")
    templates = az.get_device_templates()

    # Check template
    if 'error' in templates.keys():
        logger.error("Unable to find device templates for application '%s' - is this name correct?", app_name)
        logger.error(templates['error']['message'])
        return STATUS_FAILURE

    template_device_displayname = templates['value'][0]['displayName']
    template_device_id = templates['value'][0]['@id']
    logger.info("Using device template: %s (%s)", template_device_displayname, template_device_id)

    # Now create the device
    logger.info("Creating device '%s' from template '%s'", device_id, template_device_id)
    az.create_device(device_id, template_device_id, display_name)

    # Check by read-back
    logger.info("Checking device")
    az.get_device(device_id)

    # Do device attestation
    logger.info("Creating device attestation using certificate")
    az.create_device_attestation(device_id, certificate)

    # Check by readback
    logger.info("Checking device attestation")
    az.get_device_attestation(device_id)

    # Done
    logger.info("Registration complete!")
    return STATUS_SUCCESS
