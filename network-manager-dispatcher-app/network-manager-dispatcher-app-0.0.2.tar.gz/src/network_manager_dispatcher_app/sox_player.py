import time
from subprocess import call
from abc import ABC, abstractclassmethod


class ISoXPlayer(ABC):
    @abstractclassmethod
    def bell(self):
        pass
    
    @abstractclassmethod
    def dialer(self):
        pass
    
    @abstractclassmethod
    def dialTone(self):
        pass
    
    @abstractclassmethod
    def leakTone(self):
        pass

    @abstractclassmethod
    def playSoundForTestResult(self, dns_leak_test_result: str):
        pass


class SoXPlayer(ISoXPlayer):
    def bell(self):        
        call('play -q -n synth 3 sin 960 vol 0.1 fade l 0 3 2.8 2>/dev/null', shell=True)
    
    def dialer(self):
        call("play -q -n synth 0.1 sine 440 sine 480 channels 1 repeat 20 2>/dev/null", shell=True)
        time.sleep(4)
    
    def dialTone(self):
        call('play -q -n synth 0.1 sine 350 sine 440 channels 1 repeat 20 2>/dev/null', shell=True)

    def leakTone(self):
        call('play -q -n -c1 synth sin %-0 sin %-1 fade h 0.1 1 0.1 2>/dev/null', shell=True)

    def playSoundForTestResult(self, dns_leak_test_result: str):
        if 'DNS is not leaking' in dns_leak_test_result:
            self.bell()     
        elif 'DNS may be leaking' in dns_leak_test_result: 
            self.leakTone() 
        else:
            self.dialTone()
