import os
from setuptools import setup, find_packages
from setuptools import Extension
from distutils.command.build import build as build_orig

__version__ = "0.1.0b10"

exts = [Extension(name='vlkit.nms.nms_ext',
                  sources=["vlkit/nms/_nms_ext.c", "vlkit/nms/nms_ext.pyx"],
                  include_dirs=["vlkit/nms"],
                  extra_compile_args=['-std=c99'])]

class build(build_orig):

    def finalize_options(self):
        super().finalize_options()
        __builtins__.__NUMPY_SETUP__ = False
        import numpy
        for extension in self.distribution.ext_modules:
            extension.include_dirs.append(numpy.get_include())
        from Cython.Build import cythonize
        self.distribution.ext_modules = cythonize(self.distribution.ext_modules,
                                                  language_level=3)

setup(name='vlkit',
    version=__version__,
    description='vision and learning kit',
    url='https://github.com/vlkit/vlkit',
    author_email='kz@kaizhao.net',
    license='MIT',
    packages=find_packages(),
    ext_modules=exts,
    setup_requires=["cython", "numpy"],
    install_requires=["numpy"],
    zip_safe=False,
    data_files=[("data", ["vlkit/data/imagenet1000_clsidx_to_labels.txt"])],
    package_data={"vlkit.nms": ["nms.h", "nms_ext.pyx"]},
    cmdclass={"build": build},
)
