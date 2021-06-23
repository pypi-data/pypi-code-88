from queue import Queue

from .app_logger import IAppLogger
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

    def up(self):
        # Create a Queue for the soundThread to check at some frequency to determine when it should quit.
        soundQueue = Queue(1)

        # Create the soundThread and start it.
        dialerThread = SoundThread(soundQueue, self.play)
        dialerThread.start()
        
        stdout, stderr = self.dnsleaktest.request()
       
        # Notify the soundThread that it can quit processing.
        soundQueue.put('quit')

        # Wait for the soundThread to terminate.
        dialerThread.join()

        # If there was an error, log it and return.
        if stderr:
            self.logger.log_error(stderr.decode("utf-8"))
            return
        
        out = stdout.decode("utf-8")
        self.logger.log_info(out)

        self.play.playSoundForTestResult(out)        

    def main(self):
        try:
            self.logger.log_state(self.state)

            # Ignore connnectivity-change event for now.
            if self.state == 'connectivity-change':
                return
 
            if self.state == "up":
                self.up()

            elif self.state == "down":
                self.down()

        except Exception as ex:
            self.logger.log_error(f"Exception oops.\n {ex}")
        finally:
            self.logger.close()
