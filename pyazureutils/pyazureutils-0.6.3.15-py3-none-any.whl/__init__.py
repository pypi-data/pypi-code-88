"""
Python Microsoft Azure Web Services Utilities
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

pyazureutils is a collection of utilities for interacting with Microsoft Azure Web Services.

pyazureutils can be used as a library by instantiating any of the contained classes.

Dependencies
~~~~~~~~~~~~
This package uses pyedbglib through other libraries for USB communications.
For more information see: https://pypi.org/project/pyedbglib/

Usage example
~~~~~~~~~~~~~
Example showing how to provision for Azure IoT:

pyazureutils uses the Python logging module, in this example only a simple basicConfig setup of logging is used
    >>> import logging
    >>> logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.WARNING)

The target must be running provisioning firmware, pykitcommander is used to accomplish this.
It locates the bundled firmware for the function requested, programs it onto the MCU on the kit
and returns a protocol object and port for communicating with the application
    >>> from pykitcommander.kitprotocols import get_protocol
    >>> protocol, port = get_protocol("iotprovision-azure")

Instantiate the provisioner
    >>> from pyazureutils.custom_provision import AzureCustomProvisioner
    >>> provider_provisioner = AzureCustomProvisioner("my_signer_ca_key_file",
                                                      "my_signer_ca_cert_file",
                                                      "generated_device_csr_file",
                                                      "generated_device_cert_file")

Do the actual provisioning
    >>> device_id = provider_provisioner.provision(protocol, port)

This example will generate a device certificate and save it along with the CA signer certificate in WINC flash.
Generated certificates and Device ID are saved to files as well.

Logging
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This package uses the Python logging module for publishing log messages to library users.
A basic configuration can be used (see example), but for best results a more thorough configuration is
recommended in order to control the verbosity of output from dependencies in the stack which also use logging.
"""
import logging
logging.getLogger(__name__).addHandler(logging.NullHandler())
