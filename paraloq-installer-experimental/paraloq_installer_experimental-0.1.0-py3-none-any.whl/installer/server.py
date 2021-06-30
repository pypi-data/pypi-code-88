import threading
import uvicorn


class Server(uvicorn.Server):
    def __init__(self, **kwargs):
        super(Server, self).__init__(**kwargs)
        self.thread = threading.Thread(target=self.run)

    def install_signal_handlers(self):
        pass

    def run_in_thread(self):
        self.thread.start()

    def stop(self):
        self.should_exit = True
        self.thread.join()
