"""
Python Trust Platform utilities
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

pytrustplatform is a collection of utilities for interacting with Microchip
Trust Platform and Microchip CryptoAuthentication(TM) devices

Fetching data from a certificate
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The cert_get_data module contains functions to fetch various information from
a certificate.

Fetch the Subject Key Identifier from a certificate
    >>> from pytrustplatform.cert_get_data import cert_get_skid
    >>> skid = cert_get_skid("mycertificate.crt")

Fetch Common Name from a certificate:
    >>> from pytrustplatform.cert_get_data import cert_get_common_name
    >>> common_name = cert_get_common_name("mycertificate.crt")

Create Fingerprint from a certificate:
    >>> from pytrustplatform.cert_get_data import create_cert_fingerprint
    >>> fingerprint = create_cert_fingerprint("mycertificate.crt")

Create device certificate and CSR
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The device_cert_builder module contains functions to create device certificates
and Certificate Signing Requests (CSR) for a connected Microchip IoT kit.

Fetch a protocol object from pykitcommander
    >>> from pykitcommander.kitprotocols import get_iot_provision_protocol
    >>> protocol, port = get_iot_provision_protocol()

Build the device certificate.  A CSR will be generated as part of the process.
Both will be written to file.  The KitSerialConnection context manager
provided by pykitcommander is used to manage the port open and close.

    >>> from pytrustplatform.device_cert_builder import build_device_cert
    >>> from pykitcommander.firmwareinterface import KitSerialConnection
    >>> with KitSerialConnection(protocol, port):
    >>>     device_cert = build_device_cert("my_signer-ca.crt",
                                            "my_signer-ca.key",
                                            protocol,
                                            "generated.csr",
                                            "generated_device.crt")

Create verification certificate
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The verification_cert_builder module contains a function to create verification
certificates.  A verification certificate is typically used when registering a
Certificate Authority (CA) with a cloud provider.

Create a verification certificate from a signer CA certificate and private key
    >>> from pytrustplatform.verification_cert_builder import build_verification_cert
    >>> verification_cert = build_verification_cert("my_signer-ca.crt",
                                                    "my_signer-ca.key",
                                                    "MY_REGCODE_0123456789",
                                                    "generated_verification.crt")

Logging
~~~~~~~
This package uses the Python logging module for publishing log messages to
library users.  A basic configuration can be used (see example below), but for
best results a more thorough configuration is recommended in order to control
the verbosity of output from dependencies in the stack which also use logging.
See logging.yaml which is included in the package (although only used for CLI)

Simple logging configuration example:
    >>> import logging
    >>> logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.WARNING)

Dependencies
~~~~~~~~~~~~
pytrustplatform depends on pykitcommander to manage Microchip IoT kit firmware
and connection.
pytrustplatform depends on pyedbglib for its transport protocol.
pyedbglib requires a USB transport library like libusb.
See pyedbglib package for more information.
"""

import logging
logging.getLogger(__name__).addHandler(logging.NullHandler())
