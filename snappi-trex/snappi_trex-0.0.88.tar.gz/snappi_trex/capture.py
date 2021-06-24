import io
import json

class Capture(object):

    def __init__(self, trexclient):
        self._client = trexclient
        self._captures = {}

    def set_capture(self, payload, port_ids):
        self._state = payload
        self._port_ids = port_ids
        cs = json.loads(payload.serialize())
        ports = list(range(len(port_ids)))
        if cs['port_names'] is not None:
            ports = []
            for f_name in cs['port_names']:
                ports.append(port_ids.index(f_name))

        if cs['state'] == 'start':
            for p in ports:
                self._captures[p] = self._client.start_capture(rx_ports = [p])
        elif cs['state'] == 'stop':
            for cap in self._captures.values():
                self._client.stop_capture(cap['id'])
            self._captures = {}

    def get_capture(self, request):
        port_idx = self._port_ids.index(request.port_name)
        pkt_list = []
        self._client.fetch_capture_packets(self._captures[port_idx]['id'], pkt_list)
        res = io.BytesIO()
        for pkt in pkt_list:
            res.write(pkt['binary'])
        #     if binary is None:
        #         binary = pkt['binary']
        #     else:
        #         binary += pkt['binary']
        # res = io.BytesIO(binary)
        return res