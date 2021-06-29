import sys

# This is the ovito.plugins Python package. It hosts the C++ extension modules of OVITO.


# First, check if the user did accidentally install the PyPI package via 'pip install'
# in an Anaconda environment. Warn the user if this is the case, because the PySide2 loading 
# will probably fail due to conflicting versions of the Qt framework libraries.
# Using https://stackoverflow.com/questions/47608532/how-to-detect-from-within-python-whether-packages-are-managed-with-conda/47610844#47610844
# to detect Anaconda environment.
import sys, os
if os.path.exists(os.path.join(sys.prefix, 'conda-meta')):
    import warnings
    warnings.warn("Did you accidentally install the OVITO package from the PyPI repository in an Anaconda/Miniconda Python interpreter using the 'pip' command? "
        "Note that this will likely lead to conflicts with existing libraries in the Anaconda environment and loading of the OVITO module may subsequently fail with an error related to the Qt framework. "
        "In such a case, please uninstall the OVITO pip package first by running 'pip uninstall -y ovito PySide2' and then "
        "install the OVITO for Anaconda package using the correct command: \n\n    conda install --strict-channel-priority -c https://conda.ovito.org -c conda-forge ovito\n\n"
        "Visit https://www.ovito.org/python-downloads/ for further installation instructions.",
        stacklevel=3)

# Load all the PySide2 modules first before the OVITO C++ modules get loaded.
# This ensures that the right Qt5 shared libraries get loaded when
# running in a system Python interpreter.
#
# Note: No need to load Qt5 modules that are specific to the OVITO desktop application (e.g. QtWidgets).

import PySide2
import PySide2.QtCore
import PySide2.QtGui
import PySide2.QtNetwork
import PySide2.QtXml

# Load the C++ extension module containing the OVITO bindings.
import ovito.plugins.ovito_bindings
