from copy import deepcopy

import click
from click import Option, Argument

from hpogrid.components.defaults import *
from hpogrid.clis.core import ListOption, DictOption

config_params = {
    'hpo': [
        Argument(('NAME',)),
        Option(('-a', '--algorithm',), default=kDefaultSearchAlgorithm,
               type=click.Choice(kSearchAlgorithms, case_sensitive=False),
               help='algorithm for hyperparameter optimization', show_default=True),
        Option(('-s', '--scheduler',), default=kDefaultScheduler,
               type=click.Choice(kSchedulers, case_sensitive=False),
               help='trial scheduling method for hyperparameter optimization', show_default=True),
        Option(('-m', '--metric',), default=kDefaultMetric,
               help='evaluation metric to be optimized', show_default=True),
        ListOption(('-e', '--extra_metrics',), default=kDefaultMetric,
               help='additional metrics to be saved during the training', show_default=True),
        Option(('-o', '--mode',), default=kDefaultMetricMode,
               type=click.Choice(kMetricMode, case_sensitive=False),
               help='mode of optimization (either "min" or "max")', show_default=True),
        DictOption(('-r', '--resource',), default=None, 
               help='a json decodable string defining the resource allocated to each trial, use all cpu and gpu by default'),
        Option(('-n', '--num_trials',), type=int, required=True,
               help='number of trials (search points) to run'),
        Option(('-l', '--log_dir',), default=None,
               help='directory for saving Ray Tune logs, default is /tmp/'),
        Option(('-v', '--verbose',), default=0, type=int,
               help='verbosity level of Ray Tune', show_default=True),
        Option(('-c', '--max_concurrent',), type=int, default=kDefaultMaxConcurrent,
               help='maximum number of trials to run concurrently', show_default=True),
        DictOption(('--stop',), default=kDefaultStopping,
               help='a json decodable string defining the stopping criteria for the training', show_default=True),
        DictOption(('--scheduler_param',), default=None,
               help='a json decodable string defining the extra parameters given to the trial scheduler'),
        DictOption(('--algorithm_param',), default=None,
               help='a json decodable string defining the extra parameters given to the hyperparameter optimization algorithm')
    ],
    'grid':[
        Argument(('NAME',)),
        ListOption(('-s', '--site',), default=None,
               help='name of the grid site(s) to where the jobs are submitted, separated by commas'),
        Option(('-c', '--container',), default=kDefaultContainer,
               help='name of the docker or singularity container in which the jobs are run', show_default=True),
        Option(('-i', '--inDS', 'inDS',), default=None,
               help='name of (rucio) input dataset'),
        Option(('-o', '--outDS', 'outDS',), default=kDefaultOutDS,
               help='name of output dataset', show_default=True),
        Option(('-r', '--retry',), is_flag=True,
               help='retry failed jobs'),
        DictOption(('-e', '--extra',), default={},
               help='a json decodable string defining the extra options passed to prun command', show_default=True)
    ],
    'model':[
        Argument(('NAME',)),
        Option(('-s', '--script',), required=True,
               help='name of the training script where the function or class that defines'
               ' the training model will be called to perform the training'),
        Option(('-m', '--model',), required=True,
               help='name of the function or class that defines the training model'),
        DictOption(('-p', '--param',), default={},
               help='a json decodable string defining the extra parameters to be passed to the training model',
               show_default=True)
    ],
    'search_space':[
        Argument(('NAME',)),
        DictOption(('-s', '--search_space',), default={},
               help='a json decodable string defining the search space', show_default=True)
    ],
    'project':[
        Argument(('NAME',)),
        Option(('-p', '--scripts_path',), required=True,
               help='path to the location of training scripts '
               ' (or the directory containing the training scripts)'),
        Option(('-m', '--model_config',), required=True,
               help='name of the model configuration to use'),
        Option(('-s', '--search_space',), required=True,
               help='name of the search space configuration to use'),
        Option(('-o', '--hpo_config',), required=True,
               help='name of the hpo configuration to use'),
        Option(('-g', '--grid_config',), required=True,
               help='name of the grid configuration to use')
    ]
}


@click.group(name='hpo_config')
@click.pass_context
def hpo_config(ctx):
    """
    Manage HPO configuration
    """
    from hpogrid.configuration import HPOConfiguration
    ctx.obj = {"class": HPOConfiguration}
    

@click.group(name='grid_config')
@click.pass_context
def grid_config(ctx):
    """
    Manage configuration for grid job submission
    """
    from hpogrid.configuration import GridConfiguration
    ctx.obj = {"class": GridConfiguration}
        
    
@click.group(name='model_config')
@click.pass_context
def model_config(ctx):
    """
    Manage model configuration
    """
    from hpogrid.configuration import ModelConfiguration
    ctx.obj = {"class": ModelConfiguration}
    
@click.group(name='search_space')
@click.pass_context
def search_space_config(ctx):
    """
    Manage search space
    """
    from hpogrid.configuration import SearchSpaceConfiguration
    ctx.obj = {"class": SearchSpaceConfiguration}
    
    
@click.group(name='project')
@click.pass_context
def project_config(ctx):
    """
    Manage a project
    """
    from hpogrid.configuration import ProjectConfiguration
    ctx.obj = {"class": ProjectConfiguration}
    

@click.command(name='list')
@click.option("-e", "--expr", help="filter out configuration files that matches the expression")
@click.pass_context
def list_config(ctx, **kwargs):
    """
    List configuration files
    """
    cls = ctx.obj["class"]()
    cls.list(**kwargs)
    
@click.command(name='show', short_help="Display the contents of a configuration file")
@click.argument("NAME")
@click.pass_context
def show_config(ctx, **kwargs):
    """
    Display the contents of a configuration file
    
    NAME: Name of the configuration file
    """    
    cls = ctx.obj["class"]()
    cls.show(**kwargs)
    
@click.command(name='remove', short_help="Remove configuration file(s)")
@click.argument("NAME")
@click.pass_context
def remove_config(ctx, **kwargs):
    """
    Remove configuration file(s)
    
    NAME: Name of the configuration file (accept wildcard)
    """ 
    
    cls = ctx.obj["class"]()
    cls.remove(**kwargs)
    
@click.pass_context 
def create_config(ctx, **kwargs):
    """
    Create a configuration file
    
    NAME: Name of the configuration file
    """
    cls = ctx.obj["class"]()
    cls.parser_mode = True
    cls.create(**kwargs)
    
@click.pass_context
def update_config(ctx, **kwargs):
    """
    Update a configuration file
    
    NAME: Name of the configuration file
    """
    cls = ctx.obj["class"]()
    cls.parser_mode = True
    cls.udpate(**kwargs)
    
@click.pass_context
def recreate_config(ctx, **kwargs):
    """
    Recreate a configuration file
    
    NAME: Name of the configuration file
    """
    cls = ctx.obj["class"]()
    cls.parser_mode = True
    cls.recreate(**kwargs)
    
for gp in [hpo_config, grid_config, model_config, search_space_config, project_config]:
    gp.add_command(list_config)
    gp.add_command(show_config)
    gp.add_command(remove_config)
    
for gp, params in [(hpo_config, config_params['hpo']),
                     (grid_config, config_params['grid']),
                     (model_config, config_params['model']),
                     (search_space_config, config_params['search_space']),
                     (project_config, config_params['project'])]:
    cmd_create = click.Command('create', callback=create_config, params=params, 
                               short_help="Create a configuration file")
    cmd_update = click.Command('update', callback=update_config, params=deepcopy(params),
                               short_help="Update a configuration file")
    cmd_recreate = click.Command('recreate',  callback=recreate_config, params=params,
                               short_help="Recreate a configuration file")
    for param in cmd_update.params:
        if isinstance(param, click.Option):
            param.required = False
            param.default = kDefaultNonUpdatedArgs
            
    gp.add_command(cmd_create)
    gp.add_command(cmd_update)
    gp.add_command(cmd_recreate)