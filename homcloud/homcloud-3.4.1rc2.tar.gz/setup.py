# You should run this script in the same directory of this file.

import os
import platform
import re

from setuptools import setup, Extension

import numpy as np

with open(os.path.join(os.path.dirname(__file__), "homcloud", "version.py")) as f:
    for line in f:
        m = re.match(r"__version__ = \"([\d.a-z]+)\"", line)
        if m:
            __version__ = m.group(1)


with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'README.md'), encoding='utf-8') as f:
    long_description = f.read()
    

if re.match(r'^MSC', platform.python_compiler()):
    CPPLANGOPTS = []
else:
    CPPLANGOPTS = ["-std=c++14", "-Wno-unknown-pragmas"]

if platform.system() == 'Windows' and os.environ.get("HOMCLOUD_CONDA", "0") == "0":
    LIBS = ["mpfr", "mpir"]
else:
    LIBS = ["mpfr", "gmp"]

if os.environ.get("HOMCLOUD_BUILD_WITH_OPENMP", "0") == "1":
    openmp_compile_args = ["-fopenmp", "-DHOMCLOUD_OPENMP"]
    openmp_link_args = ["-fopenmp"]
else:
    openmp_compile_args = []
    openmp_link_args = []

PHAT_INCLUDE_DIR = "ext/external/phat/include"
MSGPACK_INCLUDE_DIR = "ext/external/msgpack-c/include"
HERA_BOTTLENECK_INCLUDE_DIR = "ext/external/hera/bottleneck/include"
HERA_WASSERSTEIN_INCLUDE_DIR = "ext/external/hera/wasserstein/include"

EXT_MODULES = [
    Extension("homcloud.modp_reduction_ext",
              sources=["ext/modp_reduction_ext.cc"],
              extra_compile_args=(CPPLANGOPTS + ["-DPYTHON"]),
              depends=[]),
    Extension("homcloud.alpha_shape3",
              include_dirs=[np.get_include()],
              libraries=LIBS,
              extra_compile_args=CPPLANGOPTS,
              define_macros=[("CGAL_HEADER_ONLY", None)],
              sources=["ext/alpha_shape3.cc"],
              depends=["ext/alpha_shape_common.h",
                       "ext/homcloud_common.h"]),
    Extension("homcloud.alpha_shape2",
              include_dirs=[np.get_include()],
              libraries=LIBS,
              extra_compile_args=CPPLANGOPTS,
              define_macros=[("CGAL_HEADER_ONLY", None)],
              sources=["ext/alpha_shape2.cc"],
              depends=["ext/alpha_shape_common.h",
                       "ext/homcloud_common.h"]),
    Extension("homcloud.periodic_alpha_shape3",
              include_dirs=[np.get_include()],
              libraries=LIBS,
              extra_compile_args=CPPLANGOPTS,
              define_macros=[("CGAL_HEADER_ONLY", None)],
              sources=["ext/periodic_alpha_shape3.cc"],
              depends=["ext/alpha_shape_common.h",
                       "ext/homcloud_common.h"]),
    Extension("homcloud.pict_tree",
              include_dirs=[np.get_include()],
              extra_compile_args=CPPLANGOPTS,
              sources=["ext/pict_tree.cc"],
              depends=["ext/homcloud_common.h"]),
    Extension("homcloud.cubical_ext",
              include_dirs=[np.get_include(), PHAT_INCLUDE_DIR, MSGPACK_INCLUDE_DIR],
              extra_compile_args=CPPLANGOPTS,
              sources=["ext/cubical_ext.cc"],
              depends=["ext/phat_ext.h"]),
    Extension("homcloud.phat_ext",
              include_dirs=[np.get_include(), PHAT_INCLUDE_DIR, MSGPACK_INCLUDE_DIR],
              extra_compile_args=(CPPLANGOPTS +
                                  openmp_compile_args),
              extra_link_args=openmp_link_args,
              sources=["ext/phat.cc"],
              depends=["ext/phat_ext.h"]),
    Extension("homcloud.distance_transform_ext",
              include_dirs=[np.get_include()],
              extra_compile_args=CPPLANGOPTS,
              sources=["ext/distance_transform_ext.cc"],
              depends=["ext/homcloud_common.h"]),
    Extension("homcloud.int_reduction_ext",
              extra_compile_args=CPPLANGOPTS,
              sources=["ext/int_reduction_ext.cc"],
              depends=[]),
    Extension("homcloud.homccube",
              include_dirs=[np.get_include()],
              extra_compile_args=CPPLANGOPTS,
              sources=["ext/homccube.cc"],
              depends=["ext/homcloud_common.h"]),
    Extension("homcloud.optimal_one_cycle_ext",
              include_dirs=[MSGPACK_INCLUDE_DIR],
              extra_compile_args=CPPLANGOPTS,
              sources=["ext/optimal_one_cycle_ext.cc"],
              depends=["ext/homcloud_common.h"]),
    Extension("homcloud.hera_bottleneck",
              include_dirs=[np.get_include(), HERA_BOTTLENECK_INCLUDE_DIR],
              extra_compile_args=CPPLANGOPTS,
              sources=["ext/hera_bottleneck.cc"],
              depends=["ext/homcloud_common.h", "ext/homcloud_numpy.h", "ext/hera_common.h"]),
    Extension("homcloud.hera_wasserstein",
              extra_compile_args=CPPLANGOPTS,
              include_dirs=[np.get_include(), HERA_WASSERSTEIN_INCLUDE_DIR],
              sources=["ext/hera_wasserstein.cc"],
              depends=["ext/homcloud_common.h", "ext/homcloud_numpy.h", "ext/hera_common.h"]),
]


ENTRY_POINTS = {
    'console_scripts': [
        "homcloud-pc-alpha = homcloud.pc_alpha:main",
        "homcloud-pict-binarize-nd = homcloud.pict.binarize_nd:main",
        "homcloud-pict-pixel-levelset-nd = homcloud.pict.pixel_levelset_nd:main",
        "homcloud-pict-merge-tree-levelset = homcloud.pict.merge_tree_levelset:main",
        "homcloud-pict-tree = homcloud.pict.tree:main",
        "homcloud-dump-diagram = homcloud.dump_diagram:main",
        "homcloud-plot-PD = homcloud.plot_PD:main",
        "homcloud-plot-PD-gui = homcloud.plot_PD_gui:main",
        "homcloud-proj-histo = homcloud.proj_histo:main",
        "homcloud-pwgk = homcloud.pwgk:main",
        "homcloud-vectorize-PD = homcloud.vectorize_PD:main",
        "homcloud-view-index-pict = homcloud.view_index_pict:main",
        "homcloud-view-index-pict3d = homcloud.view_index_pict3d:main",
        "homcloud-view-index-pict-gui = homcloud.view_index_pict_gui:main",
        "homcloud-view-vectorized-PD = homcloud.view_vectorized_PD:main",
        "homcloud-full-ph-tree = homcloud.full_ph_tree:main",
        "homcloud-query-full-ph-tree = homcloud.query_full_ph_tree:main",
        "homcloud-optimal-cycle = homcloud.optimal_cycle:main",
        "homcloud-optimal-volume = homcloud.optimal_volume:main",
        "homcloud-plot-PD-slice = homcloud.plot_PD_slice:main",
        "homcloud-pict-show-volume-2d = homcloud.pict.show_volume_2d:main",
        "homcloud-query-pht = homcloud.query_pht:main",
        "homcloud-pict-pict3d-vtk = homcloud.pict.pict3d_vtk:main",
        "homcloud-pict-slice3d = homcloud.pict.slice3d:main",
        "homcloud-pict-to-npy = homcloud.pict.to_npy:main",
        "homcloud-rips = homcloud.rips:main",
        "homcloud-abstract-filtration = homcloud.abstract_filtration:main",
        "homcloud-idiagram2diagram = homcloud.idiagram2diagram:main",
        "homcloud-build-phtrees = homcloud.build_phtrees:main",
        "homcloud-phtrees = homcloud.phtrees:main",
        "homcloud-optvol = homcloud.optvol:main",
    ],
}

    
setup(
    name="homcloud",
    version=__version__,
    description="HomCloud, persistent homology based data analysis package",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author="Ippei Obayashi",
    author_email="ippei.obayashi@riken.jp",
    url="http://homcloud.dev",
    ext_modules=EXT_MODULES,
    packages=[
        "homcloud",
        "homcloud.histopixels",
        "homcloud.pict",
        "homcloud.deprecated",
        "homcloud.interface",
    ],
    entry_points=ENTRY_POINTS,
    install_requires=[
        "numpy",
        "matplotlib",
        "scipy",
        "scikit-learn",
        "msgpack",
        "Pillow",
        "pulp",
        "forwardable",
        "imageio",
        "Cython",
        "ripser",
        "cached-property",
        "plotly",
    ],
    setup_requires=["pytest-runner"],
    tests_require=[
        "pytest>=3.0",
        "pytest-mock",
        "pytest-qt",
    ],
    classifiers=[
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Intended Audience :: Science/Research",
    ],
)
