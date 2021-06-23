from __future__ import annotations
import asyncio
import logging
import socket
import struct
from functools import partial
import typing

from pymodbus.server.asyncio import ModbusTcpServer
from pymodbus.datastore import ModbusServerContext
from pymodbus.datastore import ModbusSlaveContext, ModbusSparseDataBlock

import pyaware.data_types.modbus
import pyaware.triggers.process
from pyaware import events
import pyaware.triggers
import pyaware.data_types
import pyaware.aggregations
import pyaware.config
from pyaware.transformations import scale_values
from pyaware.data_types.modbus import AddressMapUint16

log = logging.getLogger(__file__)

if typing.TYPE_CHECKING:
    pass


class RequestException(ValueError):
    pass


class IllegalFunction(RequestException):
    pass


class IllegalDataAddress(RequestException):
    pass


class IllegalDataValue(RequestException):
    pass


class MemoryParityError(IOError):
    pass


class SlaveDeviceFailure(IOError):
    pass


class AcknowledgeError(IOError):
    pass


class DeviceBusy(IOError):
    pass


class NegativeAcknowledgeError(IOError):
    pass


class GatewayPathUnavailable(IOError):
    pass


class GatewayDeviceFailedToRespond(IOError):
    pass


modbus_exception_codes = {
    1: IllegalFunction,
    2: IllegalDataAddress,
    3: IllegalDataValue,
    4: SlaveDeviceFailure,
    5: AcknowledgeError,
    6: DeviceBusy,
    7: NegativeAcknowledgeError,
    8: MemoryParityError,
    10: GatewayPathUnavailable,
    11: GatewayDeviceFailedToRespond,
    12: ConnectionError,
}


class ModbusException(IOError):
    pass


class AsyncWrapper:
    def __init__(self, client, loop=None):
        self.client = client
        self.lock = asyncio.Lock()
        self.loop = loop or asyncio.get_event_loop()

    async def _async(self, func, *args, **kwargs):
        func = partial(func, *args, **kwargs)
        async with self.lock:
            resp = await self.loop.run_in_executor(None, func)
            if resp.isError():
                raise ModbusException(
                    f"{modbus_exception_codes.get(getattr(resp, 'exception_code', 12))}"
                )
            return resp

    async def read_coils(self, address, count=1, **kwargs):
        """

        :param address: The starting address to read from
        :param count: The number of coils to read
        :param unit: The slave unit this request is targeting
        :returns: A deferred response handle
        """
        return await self._async(self.client.read_coils, address, count, **kwargs)

    async def read_discrete_inputs(self, address, count=1, **kwargs):
        """

        :param address: The starting address to read from
        :param count: The number of discretes to read
        :param unit: The slave unit this request is targeting
        :returns: A deferred response handle
        """
        return await self._async(
            self.client.read_discrete_inputs, address, count, **kwargs
        )

    async def write_coil(self, address, value, **kwargs):
        """

        :param address: The starting address to write to
        :param value: The value to write to the specified address
        :param unit: The slave unit this request is targeting
        :returns: A deferred response handle
        """
        return await self._async(self.client.write_coil, address, value, **kwargs)

    async def write_coils(self, address, values, **kwargs):
        """

        :param address: The starting address to write to
        :param values: The values to write to the specified address
        :param unit: The slave unit this request is targeting
        :returns: A deferred response handle
        """
        return await self._async(self.client.write_coils, address, values, **kwargs)

    async def write_register(self, address, value, **kwargs):
        """

        :param address: The starting address to write to
        :param value: The value to write to the specified address
        :param unit: The slave unit this request is targeting
        :returns: A deferred response handle
        """
        return await self._async(self.client.write_register, address, value, **kwargs)

    async def write_registers(self, address, values, **kwargs):
        """

        :param address: The starting address to write to
        :param values: The values to write to the specified address
        :param unit: The slave unit this request is targeting
        :returns: A deferred response handle
        """
        return await self._async(self.client.write_registers, address, values, **kwargs)

    async def read_holding_registers(self, address, count=1, **kwargs):
        """

        :param address: The starting address to read from
        :param count: The number of registers to read
        :param unit: The slave unit this request is targeting
        :returns: A deferred response handle
        """
        return await self._async(
            self.client.read_holding_registers, address, count, **kwargs
        )

    async def read_input_registers(self, address, count=1, **kwargs):
        """

        :param address: The starting address to read from
        :param count: The number of registers to read
        :param unit: The slave unit this request is targeting
        :returns: A deferred response handle
        """
        return await self._async(
            self.client.read_input_registers, address, count, **kwargs
        )

    async def readwrite_registers(self, *args, **kwargs):
        """

        :param read_address: The address to start reading from
        :param read_count: The number of registers to read from address
        :param write_address: The address to start writing to
        :param write_registers: The registers to write to the specified address
        :param unit: The slave unit this request is targeting
        :returns: A deferred response handle
        """
        return await self._async(self.client.readwrite_registers, *args, **kwargs)

    async def mask_write_register(self, *args, **kwargs):
        """

        :param address: The address of the register to write
        :param and_mask: The and bitmask to apply to the register address
        :param or_mask: The or bitmask to apply to the register address
        :param unit: The slave unit this request is targeting
        :returns: A deferred response handle
        """
        return await self._async(self.client.mask_write_register, *args, **kwargs)


class ModbusAsyncSerialClient:
    def __init__(
        self, port, stopbits, parity, baudrate, bytesize=8, timeout=3, loop=None
    ):
        from pymodbus.client.sync import ModbusSerialClient

        client = ModbusSerialClient(
            method="rtu",
            port=port,
            stopbits=stopbits,
            parity=parity,
            baudrate=baudrate,
            bytesize=bytesize,
            timeout=timeout,
            strict=False,
        )
        self.protocol = AsyncWrapper(client, loop)
        client.connect()
        self.connected = asyncio.Event()
        self.connected.set()

    def stop(self):
        self.protocol.client.close()


class ModbusAsyncTcpClient:
    """
    Client to connect to modbus device repeatedly over TCP/IP."
    """

    #: Minimum delay in milli seconds before reconnect is attempted.
    DELAY_MIN_MS = 1000
    #: Maximum delay in milli seconds before reconnect is attempted.
    DELAY_MAX_MS = 1000

    def __init__(self, host, port=502, client_port=0):
        from pymodbus.client.asynchronous.asyncio import ModbusClientProtocol

        self.host = host
        self.port = port
        self.client_port = client_port
        #: Protocol used to talk to modbus device.
        self.protocol_class = ModbusClientProtocol
        #: Current protocol instance.
        self.protocol = None
        #: Event loop to use.
        self.loop = asyncio.get_event_loop()
        self.connected = asyncio.Event()
        #: Reconnect delay in milli seconds.
        self.delay_ms = self.DELAY_MIN_MS

    def reset_delay(self):
        """
        Resets wait before next reconnect to minimal period.
        """
        self.delay_ms = self.DELAY_MIN_MS

    async def start(self):
        """
        Initiates connection to start client
        :param host:
        :param port:
        :return:
        """
        # force reconnect if required:
        if self.connected.is_set():
            if self.protocol:
                if self.protocol.transport:
                    self.protocol.transport.close()

        log.debug("Connecting to %s:%s." % (self.host, self.port))

        await self._connect()

    def stop(self):
        """
        Stops client
        :return:
        """
        # prevent reconnect:
        self.host = None

        if self.connected.is_set():
            if self.protocol:
                if self.protocol.transport:
                    self.protocol.transport.close()

    def disconnect(self):
        self.stop()

    def _create_protocol(self):
        """
        Factory function to create initialized protocol instance.
        """
        protocol = self.protocol_class(source_address=("", self.client_port))
        protocol.factory = self
        return protocol

    async def _connect(self):
        """
        iMAC can only have 3 open TCP sockets which it doesn’t close unless it receives an explicit disconnect packet.
        This work around allows you to reserve a socket port pairing that can linger forever that you can reconnect to
        multiple times without sending a disconnect packet.

        Summary:
        Create a TCP socket
        Set socket options SO_REUSEADDR : True
        Set Socket options SO_LINGER : 1 (8 bytes where LSB is 1) Linger On with 0 seconds (infinite linger,
        tell imac not to close socket/port even with keep alive timeout)

        :return:
        """
        log.debug("Connecting.")
        if self.host is None:
            return
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            # https://stackoverflow.com/questions/6439790/sending-a-reset-in-tcp-ip-socket-connection
            sock.setsockopt(
                socket.SOL_SOCKET, socket.SO_LINGER, struct.pack("ii", 1, 0)
            )
            sock.settimeout(10)
            socket_config_path = pyaware.config.aware_path / f"{self.host}.yaml"
            self.client_port = pyaware.config.load_config(socket_config_path)
            if not self.client_port:
                sock.bind(("", 0))
                self.client_port = sock.getsockname()[1]
            else:
                sock.bind(("", self.client_port))
            pyaware.config.save_config(socket_config_path, self.client_port)
            sock.setblocking(False)
            await asyncio.wait_for(
                asyncio.get_event_loop().sock_connect(sock, (self.host, self.port)),
                timeout=1,
            )
            # sock.connect((self.host, self.port))
            await asyncio.wait_for(
                self.loop.create_connection(
                    self._create_protocol,
                    # self.host,
                    # self.port,
                    sock=sock,
                    # local_addr=('', self.client_port)
                ),
                timeout=1,
            )
        except Exception as ex:
            log.warning("Failed to connect: %s" % ex)
            asyncio.create_task(self._reconnect())
        else:
            log.info("Connected to %s:%s." % (self.host, self.port))
            self.reset_delay()

    def protocol_made_connection(self, protocol):
        """
        Protocol notification of successful connection.
        """
        log.info("Protocol made connection.")
        if not self.connected.is_set():
            self.connected.set()
            self.protocol = protocol
        else:
            log.error("Factory protocol connect " "callback called while connected.")

    def protocol_lost_connection(self, protocol):
        """
        Protocol notification of lost connection.
        """
        if events.evt_stop.is_set():
            self.stop()
            return
        if self.connected.is_set():
            log.info("Protocol lost connection.")
            if protocol is not self.protocol:
                log.error(
                    "Factory protocol callback called "
                    "from unexpected protocol instance."
                )
            try:
                self.protocol.transport.close()
            except AttributeError:
                pass
            self.connected.clear()
            self.protocol = None
            if self.host:
                asyncio.create_task(self._reconnect())
        else:
            log.error(
                "Factory protocol disconnect callback called while not connected."
            )

    async def _reconnect(self):
        log.debug(f"Waiting {self.delay_ms} ms before next connection attempt.")
        await asyncio.sleep(self.delay_ms / 1000)
        self.delay_ms = min(2 * self.delay_ms, self.DELAY_MAX_MS)
        await self._connect()


@events.enable
class ModbusAsyncTcpServer:
    """
    Asynchronous Modbus Server to serve over TCP/IP."
    """

    def __init__(
        self,
        host: str,
        server_id: str,
        coil_register_blocks: typing.List = None,
        discrete_input_register_blocks: typing.List = None,
        holding_register_blocks: typing.List = None,
        input_register_blocks: typing.List = None,
        port: int = 502,
    ):
        self.host = host
        self.port = port
        self.server_id = server_id
        # Initialises data blocks to ensure bounds are maintained
        self.ir = self._initialise_addresses(input_register_blocks)
        self.ir_blocks = ModbusSparseDataBlock(self.ir._buf)
        self.hr = self._initialise_addresses(holding_register_blocks)
        self.hr_blocks = ModbusSparseDataBlock(self.hr._buf)
        self.di = self._initialise_addresses(discrete_input_register_blocks)
        self.di_blocks = ModbusSparseDataBlock(self.di._buf)
        self.coil = self._initialise_addresses(coil_register_blocks)
        self.coil_blocks = ModbusSparseDataBlock(self.coil._buf)
        # TODO: Work out a method to set unused data blocks to nothing.
        # Initialise slave context
        self.block_store = self.ModbusSlaveContext(
            ir=self.ir_blocks,
            hr=self.hr_blocks,
            di=self.di_blocks,
            co=self.coil_blocks,
            zero_mode=True,
        )
        self.server = None
        self.context = self._initialise_data_block()
        # Subscribes to server update events
        events.subscribe(self.update_modbus_server, topic=f"update_server/{id(self)}")
        events.subscribe(
            self.write_request, topic=f"server_write/{id(self.block_store)}"
        )

    # --------------------------------------------------------------------
    # Pymodbus patch to get data from server writes
    # --------------------------------------------------------------------
    @events.enable
    class ModbusSlaveContext(ModbusSlaveContext):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

        def setValues(self, fx, address, values):
            if not self.zero_mode:
                address = address + 1
            events.publish(
                f"server_write/{id(self)}", start_addr=address, values=values
            )
            self.store[self.decode(fx)].setValues(address, values)

    # --------------------------------------------------------------------

    def _initialise_addresses(
        self, blocks: typing.List, initialise_as: int = 0
    ) -> AddressMapUint16:
        """
        Initialises addresses to 0 based on a set of address blocks.

        :param blocks: Address blocks in the format [[start_addr1, end_addr1], [start_addr2, end_addr2], ...]
        :param initialise_as: Value to initialise the addresses to as an integer. Defaults to 0.
        :return: Initialised address map
        """
        if blocks is None:
            return pyaware.data_types.modbus.AddressMapUint16(
                {i: initialise_as for i in range(0, 65536)}
            )
        map = {}
        for block in blocks:
            d = {k: initialise_as for k in range(block[0], block[1] + 1)}
            map.update(d)
        return pyaware.data_types.modbus.AddressMapUint16(map)

    def _initialise_data_block(self):
        """
        Initialises data block of modbus server to self.block values with device config mapping information
        """
        context = ModbusServerContext(slaves=self.block_store, single=True)
        return context

    async def update_modbus_server(
        self, addr_map: AddressMapUint16, register: str
    ) -> None:
        """
        Updates the current block of values with the received address map values

        :param addr_map: Address Map of values to update the server with.
        """
        if register == "holding":
            self.hr.update(addr_map)
            self.hr_blocks.values.update(self.hr._buf)
        if register == "input":
            self.ir.update(addr_map)
            self.ir_blocks.values.update(self.ir._buf)
        elif register == "discrete":
            self.di.update(addr_map)
            self.di_blocks.values.update(self.di._buf)
        elif register == "coils":
            self.coil.update(addr_map)
            self.coil_blocks.values.update(self.coil._buf)
        return

    async def write_request(self, start_addr, values):
        log.info(
            f"Request to write to server {self.server_id} received at start address: {start_addr}"
        )
        await events.publish(
            f"device_update/{id(self)}",
            start_addr=start_addr,
            values=values,
            server_id=self.server_id,
        ).all()

    async def start(self):
        """
        Start Modbus TCP Server
        """
        log.info("Starting Modbus TCP Server at %s:%s." % (self.host, self.port))
        self.server = ModbusTcpServer(
            context=self.context, address=(self.host, self.port)
        )
        await self.server.serve_forever()
