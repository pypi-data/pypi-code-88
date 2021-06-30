import webbrowser
from threading import Timer


def open_browser_tab(url: str, delay: float) -> None:
    """Open `url` in a webbrowser after `delay` seconds."""
    Timer(delay, lambda: webbrowser.open_new(url)).start()
