import os
from queue import Queue

from .app_logger import IAppLogger
from .device_state import DeviceState
from .dnsleaktest import IDnsLeakTest
from .sox_player import ISoXPlayer
from .sound_thread import SoundThread

class NetworkManagerDispatcherApp:
    def __init__(self, device, state, logger: IAppLogger, play: ISoXPlayer, dnsleaktest: IDnsLeakTest):
        self.device = device # the network device name wlp1s0
        self.state = state   # up,down,connectivity-change etc.
        self.logger = logger
        self.play = play
        self.dnsleaktest = dnsleaktest

    def down(self):
        self.play.dialTone()
        return DeviceState.DOWN

    def up(self):
        # Create a Queue for the soundThread to check at some frequency to determine when it should quit.
        soundQueue = Queue(1)

        dialerThread = SoundThread(soundQueue, self.play)
        stdout = None
        stderr = None
        
        try:
            dialerThread.start()
            stdout, stderr = self.dnsleaktest.request()
        except Exception as ex:
            self.logger.log_error(f"Exception dnsleaktest.request.\n {ex}")
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

    def connectivity_change(self):
        NM_APP_STATE = os.environ.get("NM_APP_STATE")
        NM_APP_PREV_EVENT = os.environ.get("NM_APP_PREV_EVENT")
        
        # If we connected to the router which was broadcasting succesfully but the router couldn't establish
        # a connection through the gateway to any external domain when we performed the DNSLEAK test then the
        # las state will be NO_INTERNET. Finally since we are in the connectivity-change handler, then go ahead
        # and attempt the DNSLEAK test again.
        if NM_APP_STATE is not None and NM_APP_PREV_EVENT is not None:
            if int(NM_APP_STATE) == DeviceState.NO_INTERNET and NM_APP_PREV_EVENT == "up":
                return self.up()

    def main(self):
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
