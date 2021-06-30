from flask.app import Flask

from .factory import DevConfig, ProdConfig, create_app
from .utils import Arguments, Constant, open_browser_tab, quiet_mode


def tilescopegui_app() -> Flask:
    """Set up app before its run."""
    args = Arguments.parse()
    if args.debug:
        return create_app(DevConfig())
    print("Running server now. Ctrl+C to quit.")
    app = create_app(ProdConfig())
    quiet_mode()
    if args.browser:
        open_browser_tab(args.url, delay=Constant.BROWSER_OPEN_DELAY)
    return app


def main() -> None:
    """Starting point."""
    tilescopegui_app().run()


if __name__ == "__main__":
    main()
