from time import time, sleep
from plyer import notification
import click
from apollopy.config import Config
import pyttsx3

def speak(text:str) -> None:
    """
    Speaks the given text.
    """
    e = pyttsx3.init()
    e.setProperty("rate", 150)
    e.say(text)
    e.runAndWait()


def alert(text: str) -> None:
    """
    Alerts the user.
    """
    click.echo(text)
    notification.notify(title="Apollo Alarm",
                        message=text,
                        app_name="Apollo",
                        timeout=15)
    speak(text)


NAME = "apollo"
VERSION = "1.1.0"

@click.group(NAME)
@click.version_option(VERSION, prog_name=NAME)
def base():
    """
    apollo is a command line utility which helps you being healthy by reminding you to take breaks at fixed
    intervals of time.
    """
    pass


temp_config = Config()

@base.command("config")
@click.option("--eyes-timeout", default=temp_config.load_config()["eyes_timeout"])
@click.option("--water-timeout", default=temp_config.load_config()["water_timeout"])
@click.option("--exercise-timeout", default=temp_config.load_config()["exercise_timeout"])
def config(eyes_timeout, water_timeout, exercise_timeout):
    """
    Configure apollo.
    """
    c = Config()
    config = c.load_config()
    config["eyes_timeout"] = eyes_timeout
    config["water_timeout"] = water_timeout
    config["exercise_timeout"] = exercise_timeout
    c.set_config(config)


@base.command("start")
def main():
    """
    Starts reminding about taking breaks.
    """
    alert("Apollo has been started.")
    try:
        c = Config()
        config = c.load_config()
        eyes_timeout = config["eyes_timeout"]
        water_timeout = config["water_timeout"]
        exercise_timeout = config["exercise_timeout"]

        eyes_init = time()
        water_init = time()
        exercise_init = time()
        while True:
            current_time = time()
            if current_time - eyes_init > eyes_timeout:
                alert("Eyes timeout: Take a break.")
                eyes_init = time()

            if current_time - water_init > water_timeout:
                alert("Water timeout: Drink some water.")
                water_init = time()

            if current_time - exercise_init > exercise_timeout:
                alert("Exception timeout: Do some exercise.")
                exercise_init = time()

            click.echo(f"Time passed since last eyes timeout: {round(current_time - eyes_init):.2f}s.")
            click.echo(f"Time passed since last water timeout: {round(current_time - water_init):.2f}s.") 
            click.echo(f"Time passed since last exercise timeout: {round(current_time - exercise_init):.2f}s.")
            sleep(1)
            click.clear()

    except Exception as e:
        click.echo(e)

if __name__ == "__main__":
    main()
