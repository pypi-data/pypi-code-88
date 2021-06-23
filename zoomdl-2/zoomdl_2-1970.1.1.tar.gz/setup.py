from setuptools import setup
import zoom_dl
from zoom_dl.version import __version__

def main():
    setup(
        version=__version__,
        packages=["zoom_dl/"],
        install_requires=["requests", "demjson", "tqdm"]
    )


if __name__ == "__main__":
    main()