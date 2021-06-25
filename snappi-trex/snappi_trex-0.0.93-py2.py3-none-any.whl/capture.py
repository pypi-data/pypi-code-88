import io
import json
from snappi_trex.validation import Validation

class Capture(object):

    def __init__(self, trexclient):
        self._client = trexclient
        self._captures = {}
        self._port_ids = []

    def set_capture(self, payload, port_ids):
        self._state = payload
        self._port_ids = port_ids
        cs = json.loads(payload.serialize())
        ports = list(range(len(port_ids)))
        if cs['port_names'] is not None:
            ports = []
            for p_name in cs['port_names']:
                ports.append(port_ids.index(p_name))

        if cs['state'] == 'start':
            for p in ports:
                if p not in self._captures:
                    self._captures[p] = self._client.start_capture(rx_ports = [p])
        elif cs['state'] == 'stop':
            for p in ports:
                if p in self._captures:
                    self._client.stop_capture(self._captures[p]['id'])
                    self._captures.pop(p)

    def get_capture(self, request):
        port_idx = self._port_ids.index(request.port_name)
        res = io.BytesIO()
        if port_idx in self._captures:
            pkt_list = []
            self._client.fetch_capture_packets(self._captures[port_idx]['id'], pkt_list)
            for pkt in pkt_list:
                res.write(pkt['binary'])
        return res