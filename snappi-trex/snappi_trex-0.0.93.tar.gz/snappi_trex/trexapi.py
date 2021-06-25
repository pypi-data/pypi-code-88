import json
import snappi
from trex.stl.api import *
from snappi_trex.validation import Validation
from snappi_trex.setconfig import SetConfig
from snappi_trex.capture import Capture


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
        self._transmit_states = {}
        self._capture = Capture(self._c)

        try:
            # connect to server
            self._c.connect()
        except STLError as e:
            print(e)
        

    # try to disconnect when object is deleted
    def __del__(self):
        try:
            self.wait_on_traffic(list(range(len(self._port_ids))))
            self._c.disconnect()
        except STLError as e:
            print(e)

    
    def wait_on_traffic(self, ports):
        self._c.wait_on_traffic(ports = ports)


    # Maps port names used in Snappi to port index for T-Rex
    def _loadPorts(self):
        cfg_obj = json.loads(self._config.serialize())
        if 'ports' in cfg_obj:
            for p in cfg_obj['ports']:
                self._port_ids.append(p['name'])


    def set_config(self, config):
        """Set or update the configuration
        """
        # Create response
        res = {'warnings': []}

        # print(config.serialize())
        self._config = config
        cfg_obj = json.loads(self._config.serialize())
        self._loadPorts()

        try:
            self._c.reset(ports = list(range(len(self._port_ids))))
            # for each Snappi flow, construct the equivalent T-Rex stream
            for f in cfg_obj["flows"]:
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
        cfg_obj = json.loads(self._config.serialize())
        ports = list(range(len(self._port_ids)))

        if payload.flow_names is not None:
            # Get all transmit ports names from each flow
            port_names = []
            for f in cfg_obj['flows']:
                if f['name'] in ts['flow_names']:
                    port_names.append(f['tx_rx']['port']['tx_name'])

            # Create port ID list from port names
            ports = []
            for p_name in port_names:
                p_idx = self._port_ids.index(p_name)
                if p_idx not in ports:
                    ports.append(p_idx)

        try:
            ports_start = []
            ports_stop = []
            ports_resume = []
            ports_pause = []
            # Sort each port into start, stop, resume, or pause based on current state
            for p in ports:
                if ts['state'] == 'start':
                    if p not in self._transmit_states or self._transmit_states[p] == 'stop':
                        ports_start.append(p)
                    elif self._transmit_states[p] == 'pause':
                        ports_resume.append(p)
                elif ts['state'] == 'stop':
                    ports_stop.append(p)
                elif ts['state'] == 'pause':
                    ports_pause.append(p)

                self._transmit_states[p] = ts['state']

            if len(ports_start) > 0:
                self._c.clear_stats(ports = ports_start)
                self._c.start(ports = ports_start)
            if len(ports_stop) > 0:
                self._c.stop(ports = ports_stop)
            if len(ports_resume) > 0:
                self._c.resume(ports = ports_resume)
            if len(ports_pause) > 0:
                self._c.pause(ports = ports_pause)

        except STLError as e:
            self._c.disconnect()
            print(e)


    def set_link_state(self, payload):
        ls = json.loads(payload.serialize())
        ports = list(range(len(self._port_ids)))
        if ls['port_names'] is not None:
            ports = []
            for p_name in ls['port_names']:
                ports.append(self._port_ids.index(p_name))

        if ls['state'] == 'up':
            self._c.set_port_attr(ports=ports, link_up=True)
        elif ls['state'] == 'down':
            self._c.set_port_attr(ports=ports, link_up=False)

    
    def set_capture_state(self, payload):
        """Starts capture on all ports that have capture enabled.
        """
        try:
            Validation.validate_capture(payload, self._port_ids)
            self._capture.set_capture(payload, self._port_ids)
        except STLError as e:
            self._c.disconnect()
            print(e)
        

    def get_capture(self, request):
        """Gets capture file and returns it as a byte stream
        """
        Validation.validate_capture_request(request, self._port_ids)
        return self._capture.get_capture(request)
        

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

