import json
import snappi
from trex.stl.api import *
from snappi_trex.validation import Validation
from snappi_trex.setconfig import SetConfig


class Api(snappi.Api):
    """T-Rex implementation of the abstract-open-traffic-generator package

    Args
    ----
    - host (str): The address and port of the T-Rex Server
    - port (str): The rest port of the T-Rex Server
    - username (str): The username for T-Rex Server
    """
    def __init__(self,
                 host=None,
                 username='admin',
                 password='admin',
                 license_servers=[],
                 log_level='info'):
        """Create a session
        - address (str): The ip address of the TestPlatform to connect to
        where test sessions will be created or connected to.
        - port (str): The rest port of the TestPlatform to connect to.
        - username (str): The username to be used for authentication
        """
        super(Api, self).__init__(
            host='https://127.0.0.1:11009' if host is None else host
        )
        self._c = STLClient()
        self._port_ids = []
        self._captures = []
        self._transmit_state = 'stop'
        try:
            # connect to server
            self._c.connect()
        except STLError as e:
            print(e)
        

    # try to disconnect when object is deleted
    def __del__(self):
        try:
            self._c.disconnect()
        except STLError as e:
            print(e)


    # Maps port names used in Snappi to port index for T-Rex
    def _loadPorts(self):
        if 'ports' in self._cfg:
            i = 0
            for p in self._cfg['ports']:
                self._port_ids.append(p['name'])


    def set_config(self, config):
        """Set or update the configuration
        """
        # Create response
        res = {'warnings': []}

        # print(config.serialize())
        self._cfg = json.loads(config.serialize())
        self._loadPorts()

        try:
            # prepare our ports
            self._c.reset(ports = list(range(len(self._port_ids))))

            # for each Snappi flow, construct the equivalent T-Rex stream
            for f in self._cfg["flows"]:
                # Configure variable manager commands
                vmCmds = []

                # Configure flow rate
                pps, bps, percent = SetConfig.set_rate(rate=f['rate'])

                # Configure duration and initialize the transmit mode using rate and duration info
                mode = SetConfig.set_duration(duration=f['duration'], pps=pps, bps=bps, percent=percent)

                # Parse config all packet headers. Creates a Scapy packet with provided packet headers
                headerCmds, pkt_headers, layers = SetConfig.set_packet_headers(f['packet'])
                vmCmds += headerCmds
                
                #Constructs the packet base using all headers
                pkt_base = None
                for header in pkt_headers:
                    pkt_base = header if pkt_base is None else pkt_base/header

                # Configure packet size: increment, random, or fixed
                sizeCmds, pad = SetConfig.set_packet_size(
                    f_size=f['size'], pkt_base=pkt_base, layers=layers
                )
                vmCmds += sizeCmds
                
                # TODO: Now fix the checksum of modified packets
                

                # Construct the packet with given Flow Variables
                vm = STLScVmRaw(vmCmds)
                pkt = STLPktBuilder(pkt = pkt_base/pad, vm = vm)

                # Create the stream with given config
                s1 = STLStream(packet = pkt,
                            mode = mode)

                # Add the stream to the client
                self._c.add_streams([s1], ports=[self._port_ids.index(f['tx_rx']['port']['tx_name'])])

        # Disconnect on error
        except STLError as e:
            res = {'errors': [e]}
            self._c.disconnect()
            print(e)

        return res


    def set_transmit_state(self, payload):
        """Set the transmit state of flows
        """
        ts = json.loads(payload.serialize())
        ports = list(range(len(self._port_ids)))
        if ts['flow_names'] is not None:
            ports = []
            for f_name in ts['flow_names']:
                ports.append(self._flow_ids.index(f_name))
        try:
            if ts['state'] == 'start':
                if self._transmit_state == 'stop':
                    self._c.clear_stats()
                    self._c.start(ports = ports)
                elif self._transmit_state == 'pause':
                    self._c.resume(ports = ports)
            elif ts['state'] == 'stop':
                self._c.stop(ports = ports)
            elif ts['state'] == 'pause':
                self._c.pause(ports = ports)
            
            self._transmit_state = ts['state']
            self._c.wait_on_traffic(ports = ports)
        except STLError as e:
            self._c.disconnect()
            print(e)

    
    def set_capture_state(self, payload):
        """Starts capture on all ports that have capture enabled.
        """
        cs = json.loads(payload.serialize())
        ports = list(range(len(self._port_ids)))
        if cs['port_names'] is not None:
            ports = []
            for f_name in cs['port_names']:
                ports.append(self._port_ids.index(f_name))
        try:
            if cs['state'] == 'start':
                self._captures.append(self._c.start_capture(rx_ports = ports))
            elif cs['state'] == 'stop':
                while len(self._captures) > 0:
                    cap = self._captures.pop(0)
                    self._c.stop_capture(cap['id'], "/home/frederick/cap/cap_{}.pcap".format(cap['id']))
        except STLError as e:
            self._c.disconnect()
            print(e)
        

    def get_capture(self, request):
        """Gets capture file and returns it as a byte stream
        """
        

    def get_metrics(self, request):
        """
        Gets port, flow and protocol metrics.

        Args
        ----
        - request (Union[MetricsRequest, str]): A request for Port, Flow and
          protocol metrics.
          The request content MUST be vase on the OpenAPI model,
          #/components/schemas/Result.MetricsRequest
          See the docs/openapi.yaml document for all model details
        """


    def get_config(self):
        return self._config

