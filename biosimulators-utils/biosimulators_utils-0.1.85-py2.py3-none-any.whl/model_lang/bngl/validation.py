""" Utilities for validating BNGL models

:Author: Jonathan Karr <karr@mssm.edu>
:Date: 2021-04-13
:Copyright: 2021, Center for Reproducible Biomedical Modeling
:License: MIT
"""

from ...log.data_model import StandardOutputErrorCapturerLevel
from ...log.utils import StandardOutputErrorCapturer
import bionetgen
import os
import shutil
import tempfile


def validate_model(filename, name=None):
    """ Check that a model is valid

    Args:
        filename (:obj:`str`): path to model
        name (:obj:`str`, optional): name of model for use in error messages

    Returns:
        :obj:`tuple`:

            * nested :obj:`list` of :obj:`str`: nested list of errors (e.g., required ids missing or ids not unique)
            * nested :obj:`list` of :obj:`str`: nested list of errors (e.g., required ids missing or ids not unique)
            * :obj:`bionetgen.xmlapi.model.bngmodel`: model
    """
    errors = []
    warnings = []
    model = None

    if filename:
        if os.path.isfile(filename):
            if os.path.splitext(filename)[1] == '.bngl':
                bngl_filename = filename
            else:
                fid, bngl_filename = tempfile.mkstemp(dir=os.path.dirname(filename), suffix='.bngl')
                os.close(fid)
                shutil.copyfile(filename, bngl_filename)

            model, temp_errors, stdout = read_model(bngl_filename, filename)
            errors.extend(temp_errors)

            if bngl_filename != filename:
                os.remove(bngl_filename)

        else:
            errors.append(['`{}` is not a file.'.format(filename or '')])

    else:
        errors.append(['`filename` must be a path to a file, not `{}`.'.format(filename or '')])

    return (errors, warnings, model)


def read_model(bngl_filename, filename):
    model = None
    errors = []
    cur_dir = os.getcwd()  # todo: remove once fixed in bionetgen
    with StandardOutputErrorCapturer(level=StandardOutputErrorCapturerLevel.c, relay=False) as captured:
        try:
            model = bionetgen.bngmodel(bngl_filename)
        except Exception as exception:
            errors.append(['`{}` is not a valid BNGL or BGNL XML file.'.format(filename or ''), [[str(exception)]]])
        os.chdir(cur_dir)  # todo: remove once fixed in bionetgen
    return model, errors, captured.get_text()
