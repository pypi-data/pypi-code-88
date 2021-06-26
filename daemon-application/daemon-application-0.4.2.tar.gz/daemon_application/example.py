import time
import click
from daemon_application import DaemonApplication

class HelloApplication(DaemonApplication):

    def get_main_options(self):
        options = [
            click.option("-m", "--message", default="hello")
        ]
        return options + super().get_main_options()

    def main(self):
        while True:
            print(self.config["message"])
            time.sleep(1)

controller = HelloApplication().get_controller()

if __name__ == "__main__":
    controller()
