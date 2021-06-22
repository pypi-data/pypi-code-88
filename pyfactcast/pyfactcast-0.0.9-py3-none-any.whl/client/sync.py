import json
import logging
import grpc
import struct
from types import TracebackType
from typing import Dict, Iterable, List, Optional, Type, Union
from json import dumps
from uuid import UUID


from pyfactcast.grpc.generated.FactStore_pb2_grpc import RemoteFactStoreStub
from pyfactcast.grpc.generated.FactStore_pb2 import (
    MSG_Empty,
    MSG_Fact,
    MSG_Facts,
    MSG_String,
    MSG_SubscriptionRequest,
    MSG_Notification,
    MSG_UUID,
)

from pyfactcast.client.auth.basic import BasicAuth
from pyfactcast.client.config import (
    ClientConfiguration,
    get_client_configuration,
    log_level,
)
from pyfactcast.client.entities import Fact, SubscriptionSpec

log = logging.getLogger()
log.setLevel(log_level)


def get_synchronous_grpc_client(
    client_configuration: Optional[ClientConfiguration] = None,
) -> RemoteFactStoreStub:
    log.info("Getting sync client")

    if not client_configuration:
        client_configuration = get_client_configuration()

    if client_configuration.insecure:
        log.warning("Using insecure connection. Only do this for testing!")
        return RemoteFactStoreStub(grpc.insecure_channel(client_configuration.server))

    options = None
    if client_configuration.ssl_target_override:
        log.debug("Setting SSL name override")
        options = (
            (
                "grpc.ssl_target_name_override",
                client_configuration.ssl_target_override,
            ),
        )

    root_cert = None
    if client_configuration.root_cert_path:
        log.debug("Setting SSL certificate path")
        with open(client_configuration.root_cert_path) as f:
            root_cert = f.read().encode("UTF-8")

    channel_credentials = grpc.ssl_channel_credentials(root_certificates=root_cert)

    call_credentials = _construct_call_credentials(client_configuration)

    if call_credentials:
        log.debug("Generating composite credentials")
        grpc_credentials = grpc.composite_channel_credentials(
            channel_credentials, call_credentials
        )
    else:
        grpc_credentials = channel_credentials

    log.debug("Creating channel")
    channel = grpc.secure_channel(
        target=client_configuration.server,
        credentials=grpc_credentials,
        options=options,
    )

    log.debug("Returning stub")
    return RemoteFactStoreStub(channel)


def _construct_call_credentials(
    client_configuration: ClientConfiguration,
) -> Optional[grpc.CallCredentials]:

    if client_configuration.credentials:  # Upgrade 3.8 Walrus
        call_credentials = grpc.metadata_call_credentials(
            BasicAuth(
                client_configuration.credentials.username,
                client_configuration.credentials.password,
            )
        )
        return call_credentials
    return None


def _fact_filter(msg: MSG_Notification) -> bool:
    if msg.type == msg.Fact:
        return True
    elif msg.type == msg.Catchup:
        log.info("Caught up!")
    elif msg.type == msg.Facts:
        log.error("Multiple facts per Notification not implemented.")
    elif msg.type == msg.Complete:
        log.debug("Received stream complete.")
    else:
        log.debug(f"Received Notification of type: {msg.type}")
    return False


class FactStore:
    """The pythonic way of representing a factstore

    Args:
        client (Optional[RemoteFactStoreStub], optional): A remote client stub that
            points towards the server. It will be provisioned on use if None.
            Defaults to None.
    """

    def __init__(self, client: Optional[RemoteFactStoreStub] = None) -> None:
        """ """
        self._client = client

    def __enter__(self) -> "FactStore":
        log.info("Entering FactStore")
        if not self._client:
            self.client = get_synchronous_grpc_client()
        else:
            self.client = self._client
        return self

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_value: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> Optional[bool]:
        # TODO: Implement proper channel termination
        pass

    def enumerate_namespaces(self) -> List[str]:
        """List all namespaces the current user has access to.

        Returns:
            List[str]: All namespaces available to the current user.
        """
        res: List[str] = self.client.enumerateNamespaces(MSG_Empty()).embeddedString

        return res

    def enumerate_types(self, namespace: str) -> List[str]:
        """Provide a list of all event types of a given namespace.

        Args:
            namespace (str): The namespace to enumerate.

        Returns:
            List[str]: All event types in the given namespace.
        """
        message = MSG_String()
        message.embeddedString = namespace
        res: List[str] = self.client.enumerateTypes(message).embeddedString

        return res

    def subscribe(
        self,
        *,
        subscription_specs: Iterable[SubscriptionSpec],
        continuous: bool = False,
        from_now: bool = False,
        after_fact: Optional[UUID] = None,
    ) -> Iterable[Fact]:
        """Creates a fact stream subscription.

        Args:
            subscription_specs (Iterable[SubscriptionSpec]): Used select namespaces and
                to filter the stream for specific versions and types of events.
            continuous (bool, optional): If True the connection will stay open and stream
                new facts as they are received from the factstore. Defaults to False.
            from_now (bool, optional): If True events will only be retrieved from now going forward
                i.e. you will not get any history. Defaults to False.
            after_fact (Optional[UUID], optional): If given and it exists, you will only get facts published
                after the given fact instead of from the beginning of time onwards. Defaults to None.

        Returns:
            Iterable[Fact]: The resulting fact stream.
        """

        specs: List[Dict[str, Union[str, int]]] = []

        for sub_spec in subscription_specs:
            if sub_spec.type:
                specs.append(
                    {
                        "ns": sub_spec.ns,
                        "type": sub_spec.type.name,
                        "version": sub_spec.type.version,
                    }
                )
            else:
                specs.append({"ns": sub_spec.ns})

        log.info(f"Subscribing to {specs}")

        subscription_request_body = {
            "specs": specs,
            "continuous": continuous,
        }

        if from_now:
            subscription_request_body["ephemeral"] = True
            subscription_request_body["continuous"] = True

        if after_fact:
            subscription_request_body["startingAfter"] = str(after_fact)

        msg = MSG_SubscriptionRequest(json=dumps(subscription_request_body))

        log.debug("Calling client subscribe")
        res = self.client.subscribe(msg)
        log.debug(f"Got Result: {res}")

        return map(Fact.from_msg, filter(_fact_filter, res))

    def serial_of(self, *, fact_id: UUID) -> Optional[str]:
        """Returns the serial id of the fact with the given UUID.

        If the fact does not exist will return None.

        Args:
            fact_id (UUID): The UUID of the fact you need a serial for.

        Returns:
            Optional[str]: The serial of the fact as string or None.
        """
        msb, lsb = struct.unpack(">qq", fact_id.bytes)
        msg = MSG_UUID()
        msg.lsb = lsb
        msg.msb = msb
        res = self.client.serialOf(msg)

        if res.present:
            return str(res.serial)
        return None

    def publish(self, *, fact: Fact, conditional: bool = False) -> None:
        """Publishes a fact.

        Args:
            fact (Fact): The fact to publish
            conditional (bool, optional): Whether or not the publish is conditional.
                Defaults to False.

        Raises:
            NotImplementedError: Conditional publication has not been implemented yet.
        """
        if conditional:
            raise NotImplementedError()
        else:
            fact_msg = MSG_Fact(
                header=fact.header.json(), payload=json.dumps(fact.payload)
            )
            msg = MSG_Facts(fact=[fact_msg])
            self.client.publish(msg)
