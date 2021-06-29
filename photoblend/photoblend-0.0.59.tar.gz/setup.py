from setuptools import find_packages, setup
from distutils.core import Extension
from glob import glob

module = Extension("blendlib",
                    define_macros = [("MAJOR_VERSION", "1"),
                                     ("MINOR_VERSION", "0")],
                    include_dirs = ["/library"],
                    libraries = ["library/blendlib"],
                    library_dirs = ["/library"],
                    sources = ["library/blendlib.c"])

setup(
    name="photoblend",
    version="0.0.59",
    url="https://github.com/aausek/PhotoBlend",
    description="Photoblend is a custom PyQt5 & C++ image editor app with blending mode features, filters and other"
                "manipulation options to render unique and creative images.",
    license="MIT",
    author="Team Senioritis",
    install_requires=["PySide2", "Pillow", "numpy", "wsl"],
    packages=find_packages(include=["library", "library.*", ""]),
    include_package_data=True,
    data_files=["library/blendlib.so","resources/icon.png", "resources/car.jpg", "resources/green.jpg",
                "resources/layer.jpg", "resources/layer.png"],
    ext_modules=[module],
    #entry_points={"console_scripts": ["photoblend=library.main:main"]},
    entry_points={"console_scripts": ["photoblend=library.main:main"]},
    # Issue here is that the library/main.py file that launches the app does not have a main() to call because
    # the class launches it.
    # Is icon not including? Present in tar file but not wheel
)