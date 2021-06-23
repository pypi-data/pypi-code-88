from typing import Tuple
from subprocess import Popen, PIPE
from abc import ABC, abstractclassmethod

class IDnsLeakTest(ABC):
    @abstractclassmethod
    def request(self) -> Tuple[bytes, bytes]:
        raise NotImplementedError

class DnsLeakTest(IDnsLeakTest):
    def request(self) -> Tuple[bytes, bytes]:
        try:
            # Run the bash.ws.sh script to retreive the dnsleaktest results.
            dnsleaktestProcess = Popen( \
                ['/etc/NetworkManager/dispatcher.d/network-manager-dispatcher-app-scripts/dnsleak.sh'],\
                    stdout=PIPE, \
                    stderr=PIPE \
            )
            return dnsleaktestProcess.communicate()
        except TimeoutError:
            dnsleaktestProcess.kill()
            return dnsleaktestProcess.communicate()

