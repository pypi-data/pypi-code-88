from pyrustic.app import App
from jupitest.misc.builder import MainViewBuilder
from jupitest.misc import my_theme


def main():
    # The App
    app = App()
    # Title
    app.title = "Jupitest"
    # Geometry
    app.geometry = "900x550+0+0"
    # Resizable
    app.resizable = (False, False)
    # Set theme
    app.theme = my_theme.get_theme()
    # Set view
    app.view = MainViewBuilder().build(app)
    # Center the window
    app.center()
    # Lift off !
    app.start()


if __name__ == "__main__":
    main()
