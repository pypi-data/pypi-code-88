import os
from queue import Queue
from typing import List, Literal
from abc import ABC, abstractclassmethod

from .app_logger import IAppLogger
from .device_state import DeviceState
from .dnsleaktest import IDnsLeakTest
from .sox_player import ISoXPlayer
from .sound_thread import SoundThread

class INetworkManagerDispatcherApp(ABC):
    @abstractclassmethod
    def __init__(self, device, state, logger: IAppLogger, play: ISoXPlayer, dnsleaktest: IDnsLeakTest):
        pass
    @abstractclassmethod
    def down(self) -> Literal[DeviceState.DOWN]:
        pass
    @abstractclassmethod
    def up(self) -> Literal[DeviceState.UP, DeviceState.NO_INTERNET]:
        pass
    @abstractclassmethod
    def connectivity_change(self) -> Literal[DeviceState.NO_INTERNET, DeviceState.UP]:
        pass
    @abstractclassmethod
    def main(self, args: List[str]) -> None:
        pass

class NetworkManagerDispatcherApp:
    def __init__(self, args: List[str], logger: IAppLogger, play: ISoXPlayer, dnsleaktest: IDnsLeakTest):
        self.device = args[1] # the network device name wlp1s0
        self.state = args[2]   # up,down,connectivity-change etc.
        self.args = args
        self.logger = logger
        self.play = play
        self.dnsleaktest = dnsleaktest

    def down(self) -> Literal[DeviceState.DOWN]:
        self.play.dialTone()
        return DeviceState.DOWN

    def up(self) -> Literal[DeviceState.NO_INTERNET, DeviceState.UP]:
        # Create a Queue for the soundThread to check at some frequency to determine when it should quit.
        soundQueue = Queue(1)

        dialerThread = SoundThread(soundQueue, self.play)
        stdout = None
        stderr = None
        
        try:
            dialerThread.start()
            stdout, stderr = self.dnsleaktest.request()
        except Exception as ex:
            self.logger.log_error(f"Exception dnsleaktest.request.\n {ex.__traceback__}")
        finally:
            # Notify the soundThread that it can quit processing.
            soundQueue.put('quit')

            # Wait for the soundThread to terminate.
            dialerThread.join()

            # If there was an error, log it and return.
            if stderr:
                err = stderr.decode("utf-8")
                self.logger.log_error(err)
                self.play.playSoundForTestResult(err)
                return DeviceState.NO_INTERNET

            out = stdout.decode("utf-8")
            self.logger.log_info(out)

            self.play.playSoundForTestResult(out)
            return DeviceState.UP

    def connectivity_change(self) -> Literal[DeviceState.NO_INTERNET, DeviceState.UP]:
        NM_APP_STATE = os.environ.get("NM_APP_STATE")
        NM_APP_PREV_EVENT = os.environ.get("NM_APP_PREV_EVENT")

        self.logger.log_info(f"""
        From os.environ.get call*

        NM_APP_STATE: {NM_APP_STATE}
        NM_APP_PREV_EVENT: {NM_APP_PREV_EVENT}
        """)

        # If we connected to the router which was broadcasting succesfully but the router couldn't establish
        # a connection through the gateway to any external domain when we performed the DNSLEAK test then the
        # las state will be NO_INTERNET. Finally since we are in the connectivity-change handler, then go ahead
        # and attempt the DNSLEAK test again.
        if NM_APP_STATE is not None and NM_APP_PREV_EVENT is not None:
            if int(NM_APP_STATE) == DeviceState.NO_INTERNET and NM_APP_PREV_EVENT == "up":
                return self.up()

    def main(self) -> None:
        try:

            self.logger.log_state(self.state)
            NM_APP_STATE = None

            
            if self.state == 'connectivity-change':
                NM_APP_STATE = self.connectivity_change()
 
            if self.state == "up":
                NM_APP_STATE = self.up()

            elif self.state == "down":
                NM_APP_STATE = self.down()

            os.environ.setdefault("NM_APP_PREV_EVENT", self.state)
            os.environ.setdefault("NM_APP_STATE", str(NM_APP_STATE))
        except Exception as ex:
            self.logger.log_error(f"Exception oops.\n {ex}")
        finally:
            self.logger.close()

    def print_env(self) -> None:
        # The dispatcher action like "up" or "dhcp4-change", identical to the first command line argument. Since NetworkManager 1.12.0.
        NM_DISPATCHER_ACTION = os.environ.get("NM_DISPATCHER_ACTION")

        # The UUID of the connection profile.
        CONNECTION_UUID = os.environ.get("CONNECTION_UUID")

        # The name (ID) of the connection profile.
        CONNECTION_ID = os.environ.get("CONNECTION_ID")

        # The NetworkManager D-Bus path of the connection.
        CONNECTION_DBUS_PATH = os.environ.get("CONNECTION_DBUS_PATH")

        # The backing file name of the connection profile (if any).
        CONNECTION_FILENAME = os.environ.get("CONNECTION_FILENAME")

        # If "1", this indicates that the connection describes a network configuration created outside of NetworkManager.
        CONNECTION_EXTERNAL = os.environ.get("CONNECTION_EXTERNAL")

        # The interface name of the control interface of the device. Depending on the device type, this differs from DEVICE_IP_IFACE. For example for ADSL devices, this could be 'atm0' or for WWAN devices it might be 'ttyUSB0'.
        DEVICE_IFACE = os.environ.get("DEVICE_IFACE")

        # The IP interface name of the device. This is the network interface on which IP addresses and routes will be configured.
        DEVICE_IP_IFACE = os.environ.get("DEVICE_IP_IFACE")

        # The IPv4 address in the format "address/prefix gateway", where N is a number from 0 to (# IPv4 addresses - 1). gateway item in this variable is deprecated, use IP4_GATEWAY instead.
        IP4_ADDRESS_N = os.environ.get("IP4_ADDRESS_N")

        # The variable contains the number of IPv4 addresses the script may expect.
        IP4_NUM_ADDRESSES = os.environ.get("IP4_NUM_ADDRESSES")

        # The gateway IPv4 address in traditional numbers-and-dots notation.
        IP4_GATEWAY = os.environ.get("IP4_GATEWAY")

        # The IPv4 route in the format "address/prefix next-hop metric", where N is a number from 0 to (# IPv4 routes - 1).
        IP4_ROUTE_N = os.environ.get("IP4_ROUTE_N")

        # The variable contains the number of IPv4 routes the script may expect.
        IP4_NUM_ROUTES = os.environ.get("IP4_NUM_ROUTES")

        # The variable contains a space-separated list of the DNS servers.
        IP4_NAMESERVERS = os.environ.get("IP4_NAMESERVERS")

        # The variable contains a space-separated list of the search domains.
        IP4_DOMAINS = os.environ.get("IP4_DOMAINS")

        # DHCP4_<dhcp-option-name>
        #     If the connection used DHCP for address configuration, the received DHCP configuration is passed in the environment using standard DHCP option names, prefixed with "DHCP4_", like
        #     "DHCP4_HOST_NAME=foobar".
        #
        # IP6_<name> and DHCP6_<name>
        #     The same variables as for IPv4 are available for IPv6, but the prefixes are IP6_ and DHCP6_ instead.

        # The network connectivity state, which can take the values defined by the NMConnectivityState type, from the org.freedesktop.NetworkManager D-Bus API: unknown, none, portal, limited or full.
        # Note: this variable will only be set for connectivity-change actions.
        CONNECTIVITY_STATE = os.environ.get("CONNECTIVITY_STATE")

        # In case of VPN, VPN_IP_IFACE is set, and IP4_*, IP6_* variables with VPN prefix are exported too, like VPN_IP4_ADDRESS_0, VPN_IP4_NUM_ADDRESSES.

        # Dispatcher scripts are run one at a time, but asynchronously from the main NetworkManager process, and will be killed if they run for too long. If your script might take arbitrarily long to
        # complete, you should spawn a child process and have the parent return immediately. Scripts that are symbolic links pointing inside the /etc/NetworkManager/dispatcher.d/no-wait.d/ directory are run
        # immediately, without waiting for the termination of previous scripts, and in parallel. Also beware that once a script is queued, it will always be run, even if a later event renders it obsolete.
        # (Eg, if an interface goes up, and then back down again quickly, it is possible that one or more "up" scripts will be run after the interface has gone down.)

        print(f"""
            NM_APP_PREV_EVENT: {os.environ.get("NM_APP_PREV_EVENT")}
            NM_APP_STATE: {os.environ.get("NM_APP_STATE")}
            
            NM_DISPATCHER_ACTION:   {NM_DISPATCHER_ACTION}
            
            CONNECTION_UUID:        {CONNECTION_UUID}
            CONNECTION_ID:          {CONNECTION_ID}
            CONNECTION_DBUS_PATH:   {CONNECTION_DBUS_PATH}
            CONNECTION_FILENAME:    {CONNECTION_FILENAME}
            CONNECTION_EXTERNAL:    {CONNECTION_EXTERNAL}
            
            DEVICE_IFACE:           {DEVICE_IFACE}
            DEVICE_IP_IFACE:        {DEVICE_IP_IFACE}
            
            IP4_ADDRESS_N:      {IP4_ADDRESS_N}
            IP4_NUM_ADDRESSES:  {IP4_NUM_ADDRESSES}
            IP4_GATEWAY:        {IP4_GATEWAY}
            IP4_ROUTE_N:        {IP4_ROUTE_N}
            IP4_NUM_ROUTES:     {IP4_NUM_ROUTES}
            IP4_NAMESERVERS:    {IP4_NAMESERVERS}
            IP4_DOMAINS:        {IP4_DOMAINS}
            
            CONNECTIVITY_STATE: {CONNECTIVITY_STATE}
        """)
