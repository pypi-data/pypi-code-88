""" Utilities for working with models referenced by SED documents

:Author: Jonathan Karr <karr@mssm.edu>
:Date: 2021-04-05
:Copyright: 2021, Center for Reproducible Biomedical Modeling
:License: MIT
"""

from ..combine.data_model import CombineArchive, CombineArchiveContent, CombineArchiveContentFormat
from ..combine.io import CombineArchiveWriter
from .data_model import (  # noqa: F401
    SedDocument, Model, ModelLanguage, ModelLanguagePattern, ModelAttributeChange, Simulation,
    Task, Variable, DataGenerator, Report, DataSet)
from .exceptions import UnsupportedModelLanguageError
from .io import SedmlSimulationWriter
import copy
import datetime
import dateutil.tz
import os
import re
import shutil
import tempfile
import types  # noqa: F401


__all__ = ['get_parameters_variables_for_simulation', 'build_combine_archive_for_model']


def get_parameters_variables_for_simulation(model_filename, model_language, simulation_type, algorithm=None, **model_language_options):
    """ Get the possible observables for a simulation of a model

    This method supports the following formats

    * SBML
    * SBML-fbc
    * SBML-qual

    Args:
        model_filename (:obj:`str`): path to model file
        model_language (:obj:`str`): model language (e.g., ``urn:sedml:language:sbml``)
        simulation_type (:obj:`types.Type`): subclass of :obj:`Simulation`
        algorithm (:obj:`str`, optional): KiSAO id of the algorithm for simulating the model (e.g., ``KISAO_0000019``
            for CVODE)
        **model_language_options: additional options to pass to the methods for individual model formats

    Returns:
        :obj:`list` of :obj:`ModelAttributeChange`: possible attributes of a model that can be changed and their default values
        :obj:`Simulation`: simulation of the model
        :obj:`list` of :obj:`Variable`: possible observables for a simulation of the model

    Raises:
        :obj:`UnsupportedModelLanguageError`: if :obj:`model_language` is not a supported language
    """
    # functions are imported here to only import libraries for required model languages
    if re.match(ModelLanguagePattern.BNGL.value, model_language):
        from biosimulators_utils.model_lang.bngl.utils import get_parameters_variables_for_simulation

    elif re.match(ModelLanguagePattern.CellML.value, model_language):
        from biosimulators_utils.model_lang.cellml.utils import get_parameters_variables_for_simulation

    elif re.match(ModelLanguagePattern.LEMS.value, model_language):
        # from biosimulators_utils.model_lang.lems.utils import get_parameters_variables_for_simulation
        raise UnsupportedModelLanguageError(
            'Models of language `{}` are not supported'.format(model_language))

    elif re.match(ModelLanguagePattern.SBML.value, model_language):
        from biosimulators_utils.model_lang.sbml.utils import get_parameters_variables_for_simulation

    elif re.match(ModelLanguagePattern.Smoldyn.value, model_language):
        from biosimulators_utils.model_lang.smoldyn.utils import get_parameters_variables_for_simulation

    else:
        raise UnsupportedModelLanguageError(
            'Models of language `{}` are not supported'.format(model_language))

    return get_parameters_variables_for_simulation(
        model_filename, model_language, simulation_type, algorithm=algorithm,
        **model_language_options,
    )


def build_combine_archive_for_model(model_filename, model_language, simulation_type, archive_filename):
    """ Build A COMBINE/OMEX archive with a SED-ML file for a model

    Args:
        model_filename (:obj:`str`): path to model file
        model_language (:obj:`ModelLanguage`): model language
        simulation_type (:obj:`type`): subclass of :obj:`Simulation`
        archive_filename (:obj:`str`): path to save COMBINE/OMEX archive
    """

    # make a SED-ML document for the model
    params, sim, vars = get_parameters_variables_for_simulation(model_filename, model_language, simulation_type)

    sedml_doc = SedDocument()
    model = Model(
        id='model',
        source=os.path.basename(model_filename),
        language=model_language.value,
        changes=params,
    )
    sedml_doc.models.append(model)
    sedml_doc.simulations.append(sim)
    task = Task(
        id='task',
        model=model,
        simulation=sim,
    )
    sedml_doc.tasks.append(task)
    report = Report(id='report')
    sedml_doc.outputs.append(report)
    for var in vars:
        var = copy.copy(var)
        var.task = task
        data_gen = DataGenerator(
            id='data_generator_' + var.id,
            name=var.name,
            variables=[var],
            math=var.id,
        )
        sedml_doc.data_generators.append(data_gen)
        report.data_sets.append(DataSet(
            id='data_set_' + var.id,
            label=var.id,
            name=var.name,
            data_generator=data_gen,
        ))

    # make temporary directory for archive
    archive_dirname = tempfile.mkdtemp()
    shutil.copyfile(model_filename, os.path.join(archive_dirname, os.path.basename(model_filename)))

    SedmlSimulationWriter().run(sedml_doc, os.path.join(archive_dirname, 'simulation.sedml'))

    # form a description of the archive
    utc_now = datetime.datetime.utcnow()
    now = datetime.datetime(utc_now.year, utc_now.month, utc_now.day, utc_now.hour, utc_now.minute, utc_now.second,
                            tzinfo=dateutil.tz.tzutc())

    archive = CombineArchive(created=now, updated=now)
    archive.contents.append(CombineArchiveContent(
        location=os.path.basename(model_filename),
        format=CombineArchiveContentFormat[model_language.name].value,
        created=now,
        updated=now,
    ))
    archive.contents.append(CombineArchiveContent(
        location='simulation.sedml',
        format=CombineArchiveContentFormat.SED_ML.value,
        created=now,
        updated=now,
    ))

    # save archive to file
    CombineArchiveWriter().run(archive, archive_dirname, archive_filename)

    # clean up temporary directory for archive
    shutil.rmtree(archive_dirname)
