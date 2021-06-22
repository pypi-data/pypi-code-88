import psutil
from .service_response import success_response_with_data, format_service_response

class NodeInfo:

    unit = 1024*1024*1024
    def __init__(self):
        self.totol_cpu = None
        self.totol_memory = None
        self. idle_cpu_rate = None
        self.idle_memory_rate = None
        self.net_io = None
        self.block_io = None

    def get_memory(self):
        data = psutil.virtual_memory()
        self.totol_memory = data.total / self.unit  # 总内存,单位为byte
        self.idle_memory_rate = round(data.available / data.total, 2)

    def get_cpu(self):
        self.totol_cpu = psutil.cpu_count(logical=True)
        self.idle_cpu_rate = round((100 - psutil.cpu_percent(interval=1)) /100, 2)

    def get_io(self):
        netio = psutil.net_io_counters()
        self.net_io = str(round(netio.bytes_sent/self.unit, 1)) + "/" + str(round(netio.bytes_recv/self.unit, 1))

        blockio = psutil.disk_io_counters()
        print(blockio)
        self.block_io = str(round(blockio.read_bytes/self.unit, 1)) + "/" + str(round(blockio.write_bytes/self.unit, 1))

    def statistics(self):
        self.get_cpu()
        self.get_memory()
        self.get_io()
        result = {"totol_memory": self.totol_memory,
                  "totol_cpu": self.totol_cpu,
                  "idle_memory_rate": self.idle_memory_rate,
                  "idle_cpu_rate": self.idle_cpu_rate,
                  "net_io": self.net_io,
                  "block_io": self.block_io}
        return format_service_response(success_response_with_data(result))

node_info = NodeInfo()




