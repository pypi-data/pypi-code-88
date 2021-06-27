import json
from snappi_trex.util import Util

class Metrics(object):

    def __init__(self, trexclient):
        self._client = trexclient


    def get_metrics(self, request, port_ids, capture):
        req = json.loads(request.serialize())
        mc = Util.get_metrics_columns()

        ports = list(range(len(port_ids)))
        if req['port']['port_names'] is not None:
            ports = []
            for p_name in req['port']['port_names']:
                ports.append(port_ids.index(p_name))

        col_names = ['location', 'link', 'capture', 'frames_tx', 'frames_rx',
                    'bytes_tx', 'bytes_rx', 'frames_tx_rate', 'frames_rx_rate', 
                    'bytes_tx_rate', 'bytes_rx_rate']
        if req['port']['column_names'] is not None:
            col_names = req['port']['column_names']

        metrics = self._client.get_stats(ports=ports)
        res = []
        for p in ports:
            m = {}
            m['name'] = port_ids[p]

            if 'capture' in col_names:
                m['capture'] = 'stopped'
                if capture.is_started(p):
                    m['capture'] = 'started'

            metrics_p = metrics[p]
            for col in mc:
                if col in col_names:
                    metric_name_trex = mc[col]
                    m[col] = metrics_p[metric_name_trex]

            res.append(m)
        return res
     