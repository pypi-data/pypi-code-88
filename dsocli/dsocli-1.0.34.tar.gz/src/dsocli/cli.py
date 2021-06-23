import sys
import os
import platform
import click
import re
import yaml
import json
import subprocess
import tempfile
import glob
import jmespath
from pathlib import Path
from stdiomask import getpass
from .version import __version__
from .constants import *
from .exceptions import DSOException
from .config import Config
from .logger import Logger, log_levels
from .stages import Stages
from .parameters import Parameters
from .secrets import Secrets
from .templates import Templates
from .packages import Packages
from .releases import Releases
from .click_extend import *
from click_params import RangeParamType
from .utils import flatten_dict, is_file_binary


DEFAULT_CONTEXT = dict(help_option_names=['-h', '--help'])

###--------------------------------------------------------------------------------------------

@click.group(context_settings=DEFAULT_CONTEXT)
def cli():
    """DevSecOps CLI"""
    pass

###--------------------------------------------------------------------------------------------

@cli.group(context_settings=DEFAULT_CONTEXT)
def config():
    """
    Manage DSO application configuration.
    """
    pass

###--------------------------------------------------------------------------------------------

@cli.group(context_settings=DEFAULT_CONTEXT)
def parameter():
    """
    Manage parameters.
    """
    pass

###--------------------------------------------------------------------------------------------

@cli.group(context_settings=DEFAULT_CONTEXT)
def secret():
    """
    Manage secrets.
    """
    pass

###--------------------------------------------------------------------------------------------

@cli.group(context_settings=DEFAULT_CONTEXT)
def template():
    """
    Manage templates.
    """
    pass

###--------------------------------------------------------------------------------------------

@cli.group(context_settings=DEFAULT_CONTEXT)
def package():
    """
    Manage build packages.
    """
    pass

###--------------------------------------------------------------------------------------------

@cli.group(context_settings=DEFAULT_CONTEXT)
def release():
    """
    Manage deployment releases.
    """
    pass

###--------------------------------------------------------------------------------------------

@cli.group(context_settings=DEFAULT_CONTEXT)
def provision():
    """
    Provision resources.
    """
    pass

###--------------------------------------------------------------------------------------------

@cli.group(context_settings=DEFAULT_CONTEXT)
def deploy():
    """
    Deploy releases.
    """
    pass

###--------------------------------------------------------------------------------------------
###--------------------------------------------------------------------------------------------
###--------------------------------------------------------------------------------------------

@cli.command('version', context_settings=DEFAULT_CONTEXT, short_help=f"{CLI_COMMANDS_SHORT_HELP['version']}")
def version():
    """
    Display versions.
    """
    click.echo(f"DevSecOps Tool CLI: {__version__}\nPython: {platform.sys.version}")


###--------------------------------------------------------------------------------------------
###--------------------------------------------------------------------------------------------
###--------------------------------------------------------------------------------------------

@parameter.command('add', context_settings=DEFAULT_CONTEXT, short_help=f"{CLI_COMMANDS_SHORT_HELP['parameter']['add']}")
@click.option('-s', '--stage', metavar='<name>[/<number>]', default='default', help=f"{CLI_PARAMETERS_HELP['common']['stage']}")
@click.argument('key', required=False)
@click.option('-k', '--key', 'key_option', required=False, metavar='<key>', help=f"{CLI_PARAMETERS_HELP['parameter']['key']}")
@click.argument('value', required=False)
@click.option('-v', '--value', 'value_option', metavar='<value>', required=False, help=f"{CLI_PARAMETERS_HELP['parameter']['value']}")
@click.option('-i', '--input', metavar='<path>', required=False, type=click.File(encoding='utf-8', mode='r'), help=f"{CLI_PARAMETERS_HELP['common']['input']}")
@click.option('-f', '--format', required=False, type=click.Choice(['csv','json', 'yaml', 'shell']), default='shell', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['format']}")
@click.option('-w','--working-dir', metavar='<path>', type=click.Path(exists=True, file_okay=False), required=False, default='.', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['working_dir']}")
@click.option('--config', metavar='<key>=<value>, ...', required=False, help=f"{CLI_PARAMETERS_HELP['common']['config']}")
@click.option('-b', '--verbosity', metavar='<number>', required=False, type=RangeParamType(click.INT, minimum=0, maximum=5), default='2', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['verbosity']}")
def add_parameter(stage, key, key_option, value, value_option, input, format, working_dir, config, verbosity):
    """
    Add a parameter to the application, or update its value if already existing.\n
    \tKEY: The key of the parameter. It may be also provided via '--key' option.\n
    \tVALUE: The value for the parameter. It may be also provided via '-v' / '--value' option.\n
    \nMultiple parmeters may be added at once from an input file using '-i' / '--input' option. Use '-f' / '--format' to specify the format of the input if neeeded.
    """

    parameters = []

    def check_command_usage():
        nonlocal stage, parameters
        stage = Stages.normalize(stage)
        if input:
            if key or key_option:
                Logger.error(MESSAGES['ArgumentsMutualExclusive'].format("'--key'","'-i' / '--input'"))
                Logger.info(MESSAGES['TryHelp'], stress = False, force=True)
                exit(1)
            if format == 'json':
                try:
                    parameters = json.load(input)['Parameters']
                # except json.JSONDecodeError as e:
                except:
                    Logger.error(MESSAGES['InvalidFileFormat'].format(f"'{format}'"))
                    exit(1)
            elif format == 'yaml':
                try:
                    parameters = yaml.load(input, yaml.SafeLoader)['Parameters']
                # except yaml.YAMLError as e:
                except:
                    Logger.error(MESSAGES['InvalidFileFormat'].format(f"'{format}'"))
                    exit(1)
            elif format == 'csv':
                _parameters = input.readlines()
                try:
                    if len(_parameters):
                        header = _parameters[0]
                        Key = header.split(',')[0].strip()
                        Value = header.split(',')[1].strip()
                        for param in _parameters[1:]:
                            _key = param.split(',')[0].strip()
                            _value = param.split(',')[1].strip()
                            parameters.append({Key: _key, Value: _value})
                except:
                    Logger.error(MESSAGES['InvalidFileFormat'].format(f"'{format}'"))
                    exit(1)
            elif format == 'shell':
                _parameters = input.readlines()
                try:
                    for param in _parameters:
                        _key = param.split('=', 1)[0].strip()
                        _value = param.split('=', 1)[1].strip()
                        ### eat possible enclosing quotes and double quotes when source is file, stdin has already eaten them!
                        if re.match(r'^".*"$', _value):
                            _value = re.sub(r'^"|"$', '', _value)
                        elif re.match(r"^'.*'$", _value):
                            _value = re.sub(r"^'|'$", '', _value)
                        parameters.append({'Key': _key, 'Value': _value})
                except:
                    Logger.error(MESSAGES['InvalidFileFormat'].format(f"'{format}'"))
                    exit(1)

        ### not input
        else:
            if key and key_option:
                Logger.error(MESSAGES['ArgumentsOrOption'].format("Parameter key", "'KEY'", "'--key'"))
                Logger.info(MESSAGES['TryHelp'], stress = False, force=True)
                exit(1)
    
            _key = key or key_option

            if not _key:
                Logger.error(MESSAGES['AtleastOneofTwoNeeded'].format("'--key'","'-i' / '--input'"))
                Logger.info(MESSAGES['TryHelp'], stress = False, force=True)
                exit(1)

            if value and value_option:
                Logger.error(MESSAGES['ArgumentsMutualExclusive'].format("'value'", "'-v' / '--value'"))
                Logger.info(MESSAGES['TryHelp'], stress = False, force=True)
                exit(1)

            _value = value or value_option

            if not _value:
                Logger.error(MESSAGES['MissingOption'].format("'-v' / '--value'"))
                Logger.info(MESSAGES['TryHelp'], stress = False, force=True)
                exit(1)

            parameters.append({'Key': _key, 'Value': _value})


        # invalid = False
        # for param in parameters:
        #     invalid = not Parameters.validate_key(param['Key']) or invalid

        # if invalid:
        #     Logger.info(MESSAGES['TryHelp'], stress = False, force=True)
        #     exit(1)

    try:
        Logger.set_verbosity(verbosity)
        Config.load(working_dir if working_dir else os.getcwd(), config)
        check_command_usage()

        for param in parameters:
            key = param['Key']
            value = param['Value']
            Parameters.add(stage, key, value)

    except DSOException as e:
        Logger.error(e.message)
    except Exception as e:
        msg = getattr(e, 'message', getattr(e, 'msg', str(e)))
        Logger.critical(msg)
        if verbosity >= log_levels['full']:
            raise

###--------------------------------------------------------------------------------------------

@parameter.command('list', context_settings=DEFAULT_CONTEXT, short_help=f"{CLI_COMMANDS_SHORT_HELP['parameter']['list']}")
@click.option('-s', '--stage', metavar='<name>[/<number>]', default='default', help=f"{CLI_PARAMETERS_HELP['common']['stage']}")
@click.option('-u','--uninherited', 'uninherited', is_flag=True, default=False, help=f"{CLI_PARAMETERS_HELP['parameter']['uninherited']}")
@click.option('-f', '--format', required=False, type=click.Choice(['csv','json', 'yaml', 'shell']), default='shell', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['format']}")
@click.option('-v', '--show-values', required=False, is_flag=True, default=False, show_default=True, help=f"{CLI_PARAMETERS_HELP['parameter']['show_values']}")
@click.option('-a', '--show-all', required=False, is_flag=True, default=False, show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['show_all']}")
@click.option('-q', '--query', required=False, help=f"{CLI_PARAMETERS_HELP['common']['query']}")
@click.option('-w','--working-dir', metavar='<path>', type=click.Path(exists=True, file_okay=False), required=False, default='.', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['working_dir']}")
@click.option('--config', metavar='<key>=<value>, ...', required=False, help=f"{CLI_PARAMETERS_HELP['common']['config']}")
@click.option('-b', '--verbosity', metavar='<number>', required=False, type=RangeParamType(click.INT, minimum=0, maximum=5), default='2', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['verbosity']}")
def list_parameter(stage, uninherited, show_values, show_all, query, format, working_dir, config, verbosity):
    """
    Return the list of parameters added to an application.\n
    """

    def check_command_usage():
        nonlocal stage
        stage = Stages.normalize(stage)

        if query:
            try:
                jmespath.compile(query)
            except jmespath.exceptions.ParseError as e:
                raise DSOException(f"Invalid JMESPath query '{query}': {e.msg}")

        if query and not format in ['json', 'yaml']:
            Logger.error("Option '--query' can be used only with 'json'/'yaml' output formats.")
            Logger.info(MESSAGES['TryHelp'], stress = False, force=True)
            exit(1)

        if show_all and format == 'shell':
            Logger.error("Option '--show-all' cannot be used with 'shell' output formats.")
            Logger.info(MESSAGES['TryHelp'], stress = False, force=True)
            exit(1)

        if query and show_all:
            Logger.error(MESSAGES['ArgumentsMutualExclusive'].format("'--query'", "'--show-all'"))
            Logger.info(MESSAGES['TryHelp'], stress = False, force=True)
            exit(1)

        if query and show_values:
            Logger.error(MESSAGES['ArgumentsMutualExclusive'].format("'--query'", "'--show-values'"))
            Logger.info(MESSAGES['TryHelp'], stress = False, force=True)
            exit(1)

        if show_all and show_values:
            Logger.error(MESSAGES['ArgumentsMutualExclusive'].format("'--show-all'", "'--show-values'"))
            Logger.info(MESSAGES['TryHelp'], stress = False, force=True)
            exit(1)


    def print_result(result):
        if not len(result['Parameters']): return
        if format == 'shell':
            if show_values:
                for item in result['Parameters']:
                    key = item['Key']
                    value = item['Value']
                    if re.match(r"^[1-9][0-9]*$", value):
                        print(f'{key}={value}', flush=True)
                    ### No quoting for float numbers
                    elif re.match(r"^[0-9]*\.[0-9]*$", value):
                        print(f'{key}={value}', flush=True)
                    ### Double quote if there is single quote
                    elif re.match(r"^.*[']+.*$", value):
                        print(f'{key}="{value}"', flush=True)
                    ### sinlge quote by default
                    else:
                        print(f"{key}='{value}'", flush=True)
            else:
                for item in result['Parameters']:
                    key = item['Key']
                    print(f"{key}", flush=True)
        elif format == 'csv':
            if show_all:
                keys = list(result['Parameters'][0].keys())
                if len(keys): print(','.join(keys), flush=True)
                for item in result['Parameters']:
                    values = list(item.values())
                    print(','.join(values), flush=True)
            elif show_values:
                print('Key,Value', flush=True)
                for item in result['Parameters']:
                    key = item['Key']
                    value = item['Value']
                    print(f"{key},{value}", flush=True)
            else:
                for item in result['Parameters']:
                    key = item['Key']
                    print(f"{key}", flush=True)
        elif format in ['json', 'yaml']:
            if query:
                jmespathQuery = query
            else:
                if show_all:
                    jmespathQuery = '{Parameters: Parameters[*].{'
                    keys = list(result['Parameters'][0].keys())
                    for i in range(0, len(keys)-1):
                        jmespathQuery += f"{keys[i]}: {keys[i]},"
                    if len(keys):
                        jmespathQuery += f"{keys[len(keys)-1]}: {keys[len(keys)-1]}"
                    jmespathQuery += '}}'
                else:
                    jmespathQuery = '{Parameters: Parameters[*].{Key: Key'
                    if show_values:
                        jmespathQuery += ', Value: Value'
                    jmespathQuery += '}}'
            
            result = jmespath.search(jmespathQuery, result)

            if format == 'json':
                print(json.dumps(result, sort_keys=False, indent=2), flush=True)
            else:
                print(yaml.dump(result, sort_keys=False, indent=2), flush=True)

    try:
        Logger.set_verbosity(verbosity)
        check_command_usage()
        Config.load(working_dir if working_dir else os.getcwd(), config)
        # check_command_usage()
        print_result(Parameters.list(stage, uninherited))
        # if len(duplicates) > 0:
        #     Logger.warn('Duplicate parameters found:', force=True)
        #     print(*duplicates, sep="\n")
    except DSOException as e:
        Logger.error(e.message)
    except Exception as e:
        msg = getattr(e, 'message', getattr(e, 'msg', str(e)))
        Logger.critical(msg)
        if verbosity >= log_levels['full']:
            raise

###--------------------------------------------------------------------------------------------

@parameter.command('get', context_settings=DEFAULT_CONTEXT, short_help=f"{CLI_COMMANDS_SHORT_HELP['parameter']['get']}")
@click.option('-s', '--stage', metavar='<name>[/<number>]', default='default', help=f"{CLI_PARAMETERS_HELP['common']['stage']}")
@click.argument('key', required=False)
@click.option('-k', '--key', 'key_option', required=False, metavar='<key>', help=f"{CLI_PARAMETERS_HELP['parameter']['key']}")
@click.option('-w','--working-dir', metavar='<path>', type=click.Path(exists=True, file_okay=False), required=False, default='.', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['working_dir']}")
@click.option('--config', metavar='<key>=<value>, ...', required=False, help=f"{CLI_PARAMETERS_HELP['common']['config']}")
@click.option('-b', '--verbosity', metavar='<number>', required=False, type=RangeParamType(click.INT, minimum=0, maximum=5), default='2', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['verbosity']}")
def get_parameter(stage, key, key_option, working_dir, config, verbosity):
    """
    Return the value of a parameter in the application.\n
    \tKEY: The key of the parameter. It may also be provided via '--key' option.
    """

    def check_command_usage():
        nonlocal stage, key, key_option
        stage = Stages.normalize(stage)
        if key and key_option:
            Logger.error(MESSAGES['ArgumentsMutualExclusive'].format("'key'", "'--key'"))
            Logger.info(MESSAGES['TryHelp'], stress = False, force=True)
            exit(1)

        key = key or key_option

        if not key:
            Logger.error(MESSAGES['MissingArgument'].format("'KEY'"))
            Logger.info(MESSAGES['TryHelp'], stress = False, force=True)
            exit(1)


    try:
        Logger.set_verbosity(verbosity)
        Config.load(working_dir if working_dir else os.getcwd(), config)
        check_command_usage()
        print(Parameters.get(stage, key), flush=True)
    
    except DSOException as e:
        Logger.error(e.message)
    except Exception as e:
        msg = getattr(e, 'message', getattr(e, 'msg', str(e)))
        Logger.critical(msg)
        if verbosity >= log_levels['full']:
            raise

###--------------------------------------------------------------------------------------------

@parameter.command('delete', context_settings=DEFAULT_CONTEXT, short_help=f"{CLI_COMMANDS_SHORT_HELP['parameter']['delete']}")
@click.option('-s', '--stage', default='', metavar='<name>[/<number>]', help=f"{CLI_PARAMETERS_HELP['common']['stage']}")
@click.argument('key', required=False)
@click.option('-k', '--key', 'key_option', metavar='<key>', required=False, help=f"{CLI_PARAMETERS_HELP['parameter']['key']}")
@click.option('-i', '--input', metavar='<path>', required=False, type=click.File(encoding='utf-8', mode='r'), help=f"{CLI_PARAMETERS_HELP['common']['input']}")
@click.option('-f', '--format', required=False, type=click.Choice(['csv','json', 'yaml','shell']), default='shell', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['format']}")
@click.option('-w','--working-dir', metavar='<path>', type=click.Path(exists=True, file_okay=False), required=False, default='.', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['working_dir']}")
@click.option('--config', metavar='<key>=<value>, ...', required=False, help=f"{CLI_PARAMETERS_HELP['common']['config']}")
@click.option('-b', '--verbosity', metavar='<number>', required=False, type=RangeParamType(click.INT, minimum=0, maximum=5), default='2', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['verbosity']}")
def delete_parameter(key, key_option, input, format, stage, working_dir, config, verbosity):
    """
    Delete a parameter from the application.\n
    \tKEY: The key of the parameter. It may also be provided via '--key' option.\n
    \nMultiple parmeters may be added at once from an input file using '-i' / '--input' option. Use '-f' / '--format' to specify the format of the input if neeeded.
    """

    parameters = []

    def check_command_usage():
        nonlocal stage, parameters, key, key_option
        stage = Stages.normalize(stage)
        if input:
            if key or key_option:
                Logger.error(MESSAGES['ArgumentsMutualExclusive'].format("'--key'","'-i' / '--input'"))
                Logger.info(MESSAGES['TryHelp'], stress = False, force=True)
                exit(1)
            if format == 'json':
                try:
                    parameters = json.load(input)['Parameters']
                # except json.JSONDecodeError as e:
                except:
                    Logger.error(MESSAGES['InvalidFileFormat'].format(f"'{format}'"))
                    exit(1)
            elif format == 'yaml':
                try:
                    parameters = yaml.load(input, yaml.SafeLoader)['Parameters']
                # except yaml.YAMLError as e:
                except:
                    Logger.error(MESSAGES['InvalidFileFormat'].format(f"'{format}'"))
                    exit(1)
            elif format == 'shell':
                _parameters = input.readlines()
                try:
                    for param in _parameters:
                        _key = param.split('=', 1)[0].strip()
                        # _value = param.split('=', 1)[1].strip()
                        parameters.append({'Key': _key})

                except:
                    Logger.error(MESSAGES['InvalidFileFormat'].format(f"'{format}'"))
                    exit(1)
            elif format == 'csv':
                _parameters = input.readlines()
                try:
                    if len(_parameters):
                        if ',' in _parameters[0]:
                            header = _parameters[0]
                            Key = header.split(',')[0].strip()
                            _parameters.pop(0)
                        else:
                            Key = 'Key'
                        for parameter in _parameters:
                            _key = parameter.split(',')[0].strip()
                            parameters.append({Key: _key})

                except:
                    Logger.error(MESSAGES['InvalidFileFormat'].format(f"'{format}'"))
                    exit(1)

            # for param in parameters:
            #     Parameters.validate_key(param['Key'])



        ### not input
        else:
            if key and key_option:
                Logger.error(MESSAGES['ArgumentsMutualExclusive'].format("'key'", "'--key'"))
                Logger.info(MESSAGES['TryHelp'], stress = False, force=True)
                exit(1)
    
            key = key or key_option

            if not key:
                Logger.error(MESSAGES['AtleastOneofTwoNeeded'].format("'--key'","'-i' / '--input'"))
                Logger.info(MESSAGES['TryHelp'], stress = False, force=True)
                exit(1)

            # Parameters.validate_key(key) 

            parameters.append({'Key': key})



        # invalid = False
        # for param in parameters:
        #     invalid = not Parameters.validate_key(param['Key']) or invalid

        # if invalid:
        #     Logger.info(MESSAGES['TryHelp'], stress = False, force=True)
        #     exit(1)


    try:
        Logger.set_verbosity(verbosity)
        Config.load(working_dir if working_dir else os.getcwd(), config)
        check_command_usage()

        for param in parameters:
            Parameters.delete(stage, param['Key'])

    except DSOException as e:
        Logger.error(e.message)
    except Exception as e:
        msg = getattr(e, 'message', getattr(e, 'msg', str(e)))
        Logger.critical(msg)
        if verbosity >= log_levels['full']:
            raise

###--------------------------------------------------------------------------------------------
###--------------------------------------------------------------------------------------------
###--------------------------------------------------------------------------------------------

@secret.command('list', context_settings=DEFAULT_CONTEXT, short_help=f"{CLI_COMMANDS_SHORT_HELP['secret']['list']}")
@click.option('-s', '--stage', 'stage', metavar='<name>[/<number>]', default='default', help=f"{CLI_PARAMETERS_HELP['common']['stage']}")
@click.option('-u','--uninherited', 'uninherited', is_flag=True, default=False, help=f"{CLI_PARAMETERS_HELP['secret']['uninherited']}")
@click.option('-f', '--format', required=False, type=click.Choice(['csv','json', 'yaml', 'shell']), default='shell', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['format']}")
@click.option('-v', '--show-values', required=False, is_flag=True, default=False, show_default=True, help=f"{CLI_PARAMETERS_HELP['parameter']['show_values']}")
@click.option('-a', '--show-all', required=False, is_flag=True, default=False, show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['show_all']}")
@click.option('-q', '--query', required=False, help=f"{CLI_PARAMETERS_HELP['common']['query']}")
@click.option('-d', '--decrypt', required=False, is_flag=True, default=False, show_default=True, help=f"{CLI_PARAMETERS_HELP['parameter']['show_values']}")
@click.option('-w','--working-dir', metavar='<path>', type=click.Path(exists=True, file_okay=False), required=False, default='.', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['working_dir']}")
@click.option('--config', metavar='<key>=<value>, ...', required=False, help=f"{CLI_PARAMETERS_HELP['common']['config']}")
@click.option('-b', '--verbosity', metavar='<number>', required=False, type=RangeParamType(click.INT, minimum=0, maximum=5), default='2', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['verbosity']}")
def list_secret(stage, uninherited, decrypt, show_values, show_all, query, format, working_dir, config, verbosity):

    """
    Return the list of secrets added to the application.\n
    """
    def check_command_usage():
        nonlocal stage
        stage = Stages.normalize(stage)

        if query:
            try:
                jmespath.compile(query)
            except jmespath.exceptions.ParseError as e:
                raise DSOException(f"Invalid JMESPath query '{query}': {e.msg}")

        if query and not format in ['json', 'yaml']:
            Logger.error("Option '--query' can be used only with 'json'/'yaml' output formats.")
            Logger.info(MESSAGES['TryHelp'], stress = False, force=True)
            exit(1)

        if show_all and format == 'shell':
            Logger.error("Option '--show-all' cannot be used with 'shell' output formats.")
            Logger.info(MESSAGES['TryHelp'], stress = False, force=True)
            exit(1)

        if query and show_all:
            Logger.error(MESSAGES['ArgumentsMutualExclusive'].format("'--query'", "'--show-all'"))
            Logger.info(MESSAGES['TryHelp'], stress = False, force=True)
            exit(1)

        if query and show_values:
            Logger.error(MESSAGES['ArgumentsMutualExclusive'].format("'--query'", "'--show-values'"))
            Logger.info(MESSAGES['TryHelp'], stress = False, force=True)
            exit(1)

        if show_all and show_values:
            Logger.error(MESSAGES['ArgumentsMutualExclusive'].format("'--show-all'", "'--show-values'"))
            Logger.info(MESSAGES['TryHelp'], stress = False, force=True)
            exit(1)

        if decrypt:
            if not (show_values or show_all or query):
                raise DSOException("Secret values is supressed in the output, while decryption is enabled. Use either '--show-values' or '--show-all' or '--query' to show values in the output.")

    def print_result(result):
        if not len(result['Secrets']): return
        if format == 'shell':
            if show_values:
                f = tempfile.NamedTemporaryFile("w") if decrypt else sys.stdout
                for item in result['Secrets']:
                    key = item['Key']
                    value = item['Value']
                    if re.match(r"^[1-9][0-9]*$", value):
                        f.write(f'{key}={value}\n')
                    ### No quoting for float numbers
                    elif re.match(r"^[0-9]*\.[0-9]*$", value):
                        f.write(f'{key}={value}\n')
                    ### Double quote if there is single quote
                    elif re.match(r"^.*[']+.*$", value):
                        f.write(f'{key}="{value}"\n')
                    ### sinlge quote by default
                    else:
                        f.write(f"{key}='{value}'\n")
                f.flush()
                if decrypt: 
                    p = subprocess.Popen(["less", f.name])  ### TO-DO: make it platform agnostic
                    p.wait()
                if not f == sys.stdout: f.close()
            else:
                for item in result['Secrets']:
                    key = item['Key']
                    print(f"{key}", flush=True)
        elif format == 'csv':
            if show_all:
                f = tempfile.NamedTemporaryFile("w") if decrypt else sys.stdout
                keys = list(result['Secrets'][0].keys())
                if len(keys): print(','.join(keys), flush=True)
                for item in result['Secrets']:
                    values = list(item.values())
                    f.write(','.join(values)+'\n')
                f.flush()
                if decrypt: 
                    p = subprocess.Popen(["less", f.name])  ### TO-DO: make it platform agnostic
                    p.wait()
                if not f == sys.stdout: f.close()
            elif show_values:
                f = tempfile.NamedTemporaryFile("w") if decrypt else sys.stdout
                f.write('Key,Value\n')
                for item in result['Secrets']:
                    key = item['Key']
                    value = item['Value']
                    f.write(f"{key},{value}\n")
                f.flush()
                if decrypt: 
                    p = subprocess.Popen(["less", f.name])  ### TO-DO: make it platform agnostic
                    p.wait()
                if not f == sys.stdout: f.close()
            else:
                for item in result['Secrets']:
                    key = item['Key']
                    print(f"{key}", flush=True)
        elif format in ['json', 'yaml']:
            if query:
                jmespathQuery = query
            else:
                if show_all:
                    jmespathQuery = '{Secrets: Secrets[*].{'
                    keys = list(result['Secrets'][0].keys())
                    for i in range(0, len(keys)-1):
                        jmespathQuery += f"{keys[i]}: {keys[i]},"
                    if len(keys):
                        jmespathQuery += f"{keys[len(keys)-1]}: {keys[len(keys)-1]}"
                    jmespathQuery += '}}'
                else:
                    jmespathQuery = '{Secrets: Secrets[*].{Key: Key'
                    if show_values:
                        jmespathQuery += ', Value: Value'
                    jmespathQuery += '}}'
            
            result = jmespath.search(jmespathQuery, result)

            f = tempfile.NamedTemporaryFile("w") if decrypt else sys.stdout
            if format == 'json':
                f.write(json.dumps(result, sort_keys=False, indent=2))
            else:
                f.write(yaml.dump(result, sort_keys=False, indent=2))
            f.flush()
            if decrypt: 
                p = subprocess.Popen(["less", f.name])  ### TO-DO: make it platform agnostic
                p.wait()
            if not f == sys.stdout: f.close()
    try:
        Logger.set_verbosity(verbosity)
        check_command_usage()
        Config.load(working_dir if working_dir else os.getcwd(), config)
        print_result(Secrets.list(stage, uninherited, decrypt))

    except DSOException as e:
        Logger.error(e.message)
    except Exception as e:
        msg = getattr(e, 'message', getattr(e, 'msg', str(e)))
        Logger.critical(msg)
        if verbosity >= log_levels['full']:
            raise


###--------------------------------------------------------------------------------------------

@secret.command('get', context_settings=DEFAULT_CONTEXT, short_help=f"{CLI_COMMANDS_SHORT_HELP['secret']['get']}")
@click.option('-s', '--stage', metavar='<name>[/<number>]', default='default', help=f"{CLI_PARAMETERS_HELP['common']['stage']}")
@click.argument('key', required=False)
@click.option('-k', '--key', 'key_option', required=False, metavar='<key>', help=f"{CLI_PARAMETERS_HELP['parameter']['key']}")
@click.option('-w','--working-dir', metavar='<path>', type=click.Path(exists=True, file_okay=False), required=False, default='.', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['working_dir']}")
@click.option('--config', metavar='<key>=<value>, ...', required=False, help=f"{CLI_PARAMETERS_HELP['common']['config']}")
@click.option('-b', '--verbosity', metavar='<number>', required=False, type=RangeParamType(click.INT, minimum=0, maximum=5), default='2', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['verbosity']}")
def get_secret(stage, key, key_option, working_dir, config, verbosity):
    """
    Return the value of a secret in the application.\n
    \tKEY: The key of the secret. It may be also provided via '--key' option.\n

    """

    def check_command_usage():
        nonlocal stage, key, key_option
        stage = Stages.normalize(stage)
        if key and key_option:
            Logger.error(MESSAGES['ArgumentsMutualExclusive'].format("'key'", "'--key'"))
            Logger.info(MESSAGES['TryHelp'], stress = False, force=True)
            exit(1)

        key = key or key_option

        if not key:
            Logger.error(MESSAGES['MissingArgument'].format("'KEY'"))
            Logger.info(MESSAGES['TryHelp'], stress = False, force=True)
            exit(1)

    def print_result(output):
        with tempfile.NamedTemporaryFile("w") as f:
            f.write(str(output))
            f.flush()
            p = subprocess.Popen(["less", f.name])  ### TO-DO: make it platform agnostic
            p.wait()

    try:
        Logger.set_verbosity(verbosity)
        Config.load(working_dir if working_dir else os.getcwd(), config)
        check_command_usage()
        output = Secrets.get(stage, key) 
        print_result(output)

    except DSOException as e:
        Logger.error(e.message)
    except Exception as e:
        msg = getattr(e, 'message', getattr(e, 'msg', str(e)))
        Logger.critical(msg)
        if verbosity >= log_levels['full']:
            raise


###--------------------------------------------------------------------------------------------

@secret.command('add', context_settings=DEFAULT_CONTEXT, short_help=f"{CLI_COMMANDS_SHORT_HELP['secret']['add']}")
@click.option('-s', '--stage', metavar='<name>[/<number>]', default='default', help=f"{CLI_PARAMETERS_HELP['common']['stage']}")
@click.argument('key', required=False)
@click.option('-k', '--key', 'key_option', required=False, metavar='<key>', help=f"{CLI_PARAMETERS_HELP['secret']['key']}")
# @click.option('-v', '--value', metavar='<value>', required=False, help=f"{CLI_PARAMETERS_HELP['secret']['value']}")
@click.option('-i', '--input', metavar='<path>', required=False, type=click.File(encoding='utf-8', mode='r'), help=f"{CLI_PARAMETERS_HELP['common']['input']}")
@click.option('-f', '--format', required=False, type=click.Choice(['csv','json', 'yaml', 'shell']), default='shell', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['format']}")
@click.option('-w','--working-dir', metavar='<path>', type=click.Path(exists=True, file_okay=False), required=False, default='.', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['working_dir']}")
@click.option('--config', metavar='<key>=<value>, ...', required=False, help=f"{CLI_PARAMETERS_HELP['common']['config']}")
@click.option('-b', '--verbosity', metavar='<number>', required=False, type=RangeParamType(click.INT, minimum=0, maximum=5), default='2', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['verbosity']}")
def add_secret(stage, key, key_option, input, format, working_dir, config, verbosity):
    """
    Add a secret to the application, or update its value if already existing.\n
    \tKEY: The key of the secret. It may be also provided via '--key' option.\n
    \nMultiple parmeters may be added at once from an input file using '-i' / '--input' option. Use '-f' / '--format' to specify the format of the input if neeeded.
    """

    secrets = []

    def check_command_usage():
        nonlocal stage, secrets, key, key_option
        stage = Stages.normalize(stage)
        if input:
            if key or key_option:
                Logger.error(MESSAGES['ArgumentsMutualExclusive'].format("'--key'","'-i' / '--input'"))
                Logger.info(MESSAGES['TryHelp'], stress = False, force=True)
                exit(1)
            if format == 'json':
                try:
                    secrets = json.load(input)['Secrets']
                # except json.JSONDecodeError as e:
                except:
                    Logger.error(MESSAGES['InvalidFileFormat'].format(f"'{format}'"))
                    exit(1)
            elif format == 'yaml':
                try:
                    secrets = yaml.load(input, yaml.SafeLoader)['Secrets']
                # except yaml.YAMLError as e:
                except:
                    Logger.error(MESSAGES['InvalidFileFormat'].format(f"'{format}'"))
                    exit(1)
            elif format == 'csv':
                _secrets = input.readlines()
                try:
                    if len(_secrets):
                        header = _secrets[0]
                        Key = header.split(',')[0].strip()
                        Value = header.split(',')[1].strip()
                        for secret in _secrets[1:]:
                            _key = secret.split(',')[0].strip()
                            _value = secret.split(',')[1].strip()
                            secrets.append({Key: _key, Value: _value})
                except:
                    Logger.error(MESSAGES['InvalidFileFormat'].format(f"'{format}'"))
                    exit(1)
            elif format == 'shell':
                _secrets = input.readlines()
                try:
                    for secret in _secrets:
                        _key = secret.split('=', 1)[0].strip()
                        _value = secret.split('=', 1)[1].strip()
                        ### eat possible enclosing quotes and double quotes when source is file, stdin has already eaten them!
                        if re.match(r'^".*"$', _value):
                            _value = re.sub(r'^"|"$', '', _value)
                        elif re.match(r"^'.*'$", _value):
                            _value = re.sub(r"^'|'$", '', _value)
                        secrets.append({'Key': _key, 'Value': _value})
                except:
                    Logger.error(MESSAGES['InvalidFileFormat'].format(f"'{format}'"))
                    exit(1)
                
        ### not input
        else:
            if key and key_option:
                Logger.error(MESSAGES['ArgumentsOrOption'].format("Secert key", "'KEY'", "'--key'"))
                Logger.info(MESSAGES['TryHelp'], stress = False, force=True)
                exit(1)
    
            key = key or key_option

            if not key:
                Logger.error(MESSAGES['AtleastOneofTwoNeeded'].format("'--key'","'-i' / '--input'"))
                Logger.info(MESSAGES['TryHelp'], stress = False, force=True)
                exit(1)

            # if not value:
            #     Logger.error(MESSAGES['MissingOption'].format("'-v' / '--value'"))
            #     Logger.info(MESSAGES['TryHelp'], stress = False, force=True)
            #     exit(1)

            Secrets.validate_key(key)
                
            value = getpass("Enter secret value: ")
            value2 = getpass("Verify secret value: ")
            if not value == value2:
                Logger.error(MESSAGES['EnteredSecretValuesNotMatched'].format(f"'{format}'"))
                exit(1)

            secrets.append({'Key': key, 'Value': value})


    try:
        Logger.set_verbosity(verbosity)
        Config.load(working_dir if working_dir else os.getcwd(), config)
        check_command_usage()

        for secret in secrets:
            key = secret['Key']
            value = secret['Value']
            # Secrets.validate_key(secret['Key'])
            Secrets.add(stage, key, value)

    except DSOException as e:
        Logger.error(e.message)
    except Exception as e:
        msg = getattr(e, 'message', getattr(e, 'msg', str(e)))
        Logger.critical(msg)
        if verbosity >= log_levels['full']:
            raise


###--------------------------------------------------------------------------------------------

@secret.command('delete', context_settings=DEFAULT_CONTEXT, short_help=f"{CLI_COMMANDS_SHORT_HELP['secret']['delete']}")
@click.option('-s', '--stage', metavar='<name>[/<number>]', default='default', help=f"{CLI_PARAMETERS_HELP['common']['stage']}")
@click.argument('key', required=False)
@click.option('-k', '--key', 'key_option', metavar='<key>', required=False, help=f"{CLI_PARAMETERS_HELP['secret']['key']}")
@click.option('-i', '--input', metavar='<path>', required=False, type=click.File(encoding='utf-8', mode='r'), help=f"{CLI_PARAMETERS_HELP['common']['input']}")
@click.option('-f', '--format', required=False, type=click.Choice(['csv','json', 'yaml', 'shell']), default='shell', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['format']}")
@click.option('-w','--working-dir', metavar='<path>', type=click.Path(exists=True, file_okay=False), required=False, default='.', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['working_dir']}")
@click.option('--config', metavar='<key>=<value>, ...', required=False, help=f"{CLI_PARAMETERS_HELP['common']['config']}")
@click.option('-b', '--verbosity', metavar='<number>', required=False, type=RangeParamType(click.INT, minimum=0, maximum=5), default='2', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['verbosity']}")
def delete_secret(key, key_option, input, format, stage, working_dir, config, verbosity):
    """
    Delete a secret from the application.\n
    \tKEY: The key of the secret. It may also be provided via '--key' option.\n
    \nMultiple secrets may be added at once from an input file using '-i' / '--input' option. Use '-f' / '--format' to specify the format of the input if neeeded.
    """

    secrets = []

    def check_command_usage():
        nonlocal stage, secrets, key, key_option
        stage = Stages.normalize(stage)
        if input:
            if key or key_option:
                Logger.error(MESSAGES['ArgumentsMutualExclusive'].format("'--key'","'-i' / '--input'"))
                Logger.info(MESSAGES['TryHelp'], stress = False, force=True)
                exit(1)
            if format == 'json':
                try:
                    secrets = json.load(input)['Secrets']
                # except json.JSONDecodeError as e:
                except:
                    Logger.error(MESSAGES['InvalidFileFormat'].format(f"'{format}'"))
                    exit(1)
            elif format == 'yaml':
                try:
                    secrets = yaml.load(input, yaml.SafeLoader)['Secrets']
                # except yaml.YAMLError as e:
                except:
                    Logger.error(MESSAGES['InvalidFileFormat'].format(f"'{format}'"))
                    exit(1)
            elif format == 'shell':
                _secrets = input.readlines()
                try:
                    for secret in _secrets:
                        _key = secret.split('=', 1)[0].strip()
                        # _value = secret.split('=', 1)[1].strip()
                        secrets.append({'Key': _key})
                except:
                    Logger.error(MESSAGES['InvalidFileFormat'].format(f"'{format}'"))
                    exit(1)
            elif format == 'csv':
                _secrets = input.readlines()
                try:
                    if len(_secrets):
                        if ',' in _secrets[0]:
                            header = _secrets[0]
                            Key = header.split(',')[0].strip()
                            _secrets.pop(0)
                        else:
                            Key = 'Key'
                        for secret in _secrets:
                            _key = secret.split(',')[0].strip()
                            secrets.append({Key: _key})

                except:
                    Logger.error(MESSAGES['InvalidFileFormat'].format(f"'{format}'"))
                    exit(1)

            # for secret in secrets:
            #     Secrets.validate_key(secret['Key'])

        ### not input
        else:
            if key and key_option:
                Logger.error(MESSAGES['ArgumentsMutualExclusive'].format("'key'", "'--key'"))
                Logger.info(MESSAGES['TryHelp'], stress = False, force=True)
                exit(1)
    
            key = key or key_option

            if not key:
                Logger.error(MESSAGES['AtleastOneofTwoNeeded'].format("'--key'","'-i' / '--input'"))
                Logger.info(MESSAGES['TryHelp'], stress = False, force=True)
                exit(1)

            secrets.append({'Key': key})

        # invalid = False
            # Secrets.validate_key(key)

        # if invalid:
        #     Logger.info(MESSAGES['TryHelp'], stress = False, force=True)
        #     exit(1)

    try:
        Logger.set_verbosity(verbosity)
        Config.load(working_dir if working_dir else os.getcwd(), config)
        check_command_usage()

        for secret in secrets:
            Secrets.delete(stage, secret['Key'])

    except DSOException as e:
        Logger.error(e.message)
    except Exception as e:
        msg = getattr(e, 'message', getattr(e, 'msg', str(e)))
        Logger.critical(msg)
        if verbosity >= log_levels['full']:
            raise


###--------------------------------------------------------------------------------------------
###--------------------------------------------------------------------------------------------
###--------------------------------------------------------------------------------------------

@template.command('list', context_settings=DEFAULT_CONTEXT, short_help=f"{CLI_COMMANDS_SHORT_HELP['template']['list']}")
@click.option('-r', '--render-path', 'show_render_path', required=False, is_flag=True, default=False, show_default=True, help=f"{CLI_PARAMETERS_HELP['template']['show_render_path']}")
@click.option('-f', '--format', required=False, type=click.Choice(['csv','json', 'yaml']), default='csv', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['format']}")
@click.option('-w','--working-dir', metavar='<path>', type=click.Path(exists=True, file_okay=False), required=False, default='.', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['working_dir']}")
@click.option('--config', metavar='<key>=<value>, ...', required=False, help=f"{CLI_PARAMETERS_HELP['common']['config']}")
@click.option('-b', '--verbosity', metavar='<number>', required=False, type=RangeParamType(click.INT, minimum=0, maximum=5), default='2', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['verbosity']}")
def list_template(show_render_path, format, working_dir, config, verbosity):
    """
    Return the list of templates added to the application.\n
    """
    def check_command_usage():
        pass

    def print_result(templates):
        if show_render_path:
            if format == 'csv':
                if len(templates): print("Key,RenderTo", flush=True)
                for template in templates:
                    print(f"{template['Key']},{template['RenderTo']}", flush=True)
            elif format == 'json':
                print(json.dumps({'Templates' : templates}, sort_keys=False, indent=2), flush=True)
            elif format == 'yaml':
                print(yaml.dump({'Templates' : templates}, sort_keys=False, indent=2), flush=True)
        else:
            if format == 'shell':
                for item in templates:
                    print(f"{item['Key']}", flush=True)
            elif format == 'csv':
                # if len(templates): print("Key", flush=True)
                for item in templates:
                    print(f"{item['Key']}", flush=True)
            elif format == 'json':
                print(json.dumps({'Templates' : [x['Key'] for x in templates]}, sort_keys=False, indent=2), flush=True)
            elif format == 'yaml':
                print(yaml.dump({'Templates' : [x['Key'] for x in templates]}, sort_keys=False, indent=2), flush=True)

    try:
        Logger.set_verbosity(verbosity)
        Config.load(working_dir if working_dir else os.getcwd(), config)
        check_command_usage()
        templates = Templates.list()
        print_result(templates)
    except DSOException as e:
        Logger.error(e.message)
    except Exception as e:
        msg = getattr(e, 'message', getattr(e, 'msg', str(e)))
        Logger.critical(msg)
        if verbosity >= log_levels['full']:
            raise


###--------------------------------------------------------------------------------------------

@template.command('get', context_settings=DEFAULT_CONTEXT, short_help=f"{CLI_COMMANDS_SHORT_HELP['template']['get']}")
@click.argument('key', required=False)
@click.option('-k', '--key', 'key_option', metavar='<key>', required=False, help=f"{CLI_PARAMETERS_HELP['template']['key']}")
@click.option('-w','--working-dir', metavar='<path>', type=click.Path(exists=True, file_okay=False), required=False, default='.', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['working_dir']}")
@click.option('--config', metavar='<key>=<value>, ...', required=False, help=f"{CLI_PARAMETERS_HELP['common']['config']}")
@click.option('-b', '--verbosity', metavar='<number>', required=False, type=RangeParamType(click.INT, minimum=0, maximum=5), default='2', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['verbosity']}")
def get_template(key, key_option, working_dir, config, verbosity):
    """
    Return the content of a template.\n
    \tKEY: The key of the template. It may also be provided via '--key' option.\n
    """

    def check_command_usage():
        nonlocal key, key_option
        if key and key_option:
            Logger.error(MESSAGES['ArgumentsOrOption'].format("Template key", "'KEY'", "'--key'"))
            Logger.info(MESSAGES['TryHelp'], stress = False, force=True)
            exit(1)

        key = key or key_option

        if not key:
            Logger.error(MESSAGES['MissingOption'].format("'KEY"))
            Logger.info(MESSAGES['TryHelp'], stress = False, force=True)
            exit(1)

        # if not Templates.validate_key(key):
        #     Logger.info(MESSAGES['TryHelp'], stress = False, force=True)
        #     exit(1)


    try:
        Logger.set_verbosity(verbosity)
        Config.load(working_dir if working_dir else os.getcwd(), config)
        check_command_usage()
        print(Templates.get(key), flush=True)
    
    except DSOException as e:
        Logger.error(e.message)
    except Exception as e:
        msg = getattr(e, 'message', getattr(e, 'msg', str(e)))
        Logger.critical(msg)
        if verbosity >= log_levels['full']:
            raise

###--------------------------------------------------------------------------------------------

@template.command('add', context_settings=DEFAULT_CONTEXT, short_help=f"{CLI_COMMANDS_SHORT_HELP['template']['add']}")
@click.argument('key', required=False)
@click.option('-k', '--key', 'key_option', metavar='<key>', required=False, help=f"{CLI_PARAMETERS_HELP['template']['key']}")
@click.option('-r', '--render-path', default='.', show_default=True, metavar='<path>', required=False, help=f"{CLI_PARAMETERS_HELP['template']['render_path']}")
# @click.option('-i', '--input', metavar='<path>', required=True, type=click.File(encoding='utf-8', mode='r'), help=f"{CLI_PARAMETERS_HELP['template']['input']}")
# @click.option('-i', '--input', metavar='<path>', required=True, type=click.Path(exists=True, file_okay=True, dir_okay=True), help=f"{CLI_PARAMETERS_HELP['template']['input']}")
@click.option('-i', '--input', metavar='<path>', required=True, help=f"{CLI_PARAMETERS_HELP['template']['input']}")
@click.option('--recursive', required=False, is_flag=True, help=f"{CLI_PARAMETERS_HELP['template']['recursive']}")
@click.option('-w','--working-dir', metavar='<path>', type=click.Path(exists=True, file_okay=False), required=False, default='.', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['working_dir']}")
@click.option('--config', metavar='<key>=<value>, ...', required=False, help=f"{CLI_PARAMETERS_HELP['common']['config']}")
@click.option('-b', '--verbosity', metavar='<number>', required=False, type=RangeParamType(click.INT, minimum=0, maximum=5), default='2', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['verbosity']}")
def add_template(key, key_option, render_path, input, recursive, working_dir, config, verbosity):
    """
    Add a template to the application, or update it if already existing.\n
    \tKEY: The key of the template. It may also be provided via '--key' option.\n
    """


    templates = []
    inputDir = ''

    def process_key_from_path(_path):
        nonlocal inputDir
        result = ''
        if not key or key in ['.' , './']:
            result = _path[len(inputDir)+1:]
        else:
            if os.path.dirname(_path)[len(inputDir):]:
                result = re.sub(r'[*][*]', os.path.dirname(_path)[len(inputDir)+1:], key)
            else:
                result = re.sub(r'/[*][*]', '', key)
            result = re.sub(r'[*]', os.path.basename(_path), result)

        return result


    def process_render_path_from_key(_key):
        nonlocal render_path
        ### by default render_path is '.'
        result = ''
        if render_path == '.' or render_path == './':
            result = _key
        else:
            if os.path.dirname(_key):
                result = re.sub(r'[*][*]', os.path.dirname(_key), render_path)
            else:
                result = re.sub(r'/[*][*]', '', render_path)
            result = re.sub(r'[*]', os.path.basename(_key), result)

        return result


    def check_command_usage():
        nonlocal templates, input, key, render_path, inputDir

        if key and key_option:
            Logger.error(MESSAGES['ArgumentsOrOption'].format("Template key", "'KEY'", "'--key'"))
            Logger.info(MESSAGES['TryHelp'], stress = False, force=True)
            exit(1)

        key = key or key_option
        
        m = re.match(r'^.*?(/[^/]*[*]+.*)$', input)
        if m:
            globe = m.groups()[0]
            inputDir = input[:-len(globe)]
            inputDir = re.sub('/$', '', inputDir)
        else:
            globe = ''
            inputDir = input

        for item in glob.glob(input, recursive=recursive):
            if not Path(item).is_file(): continue
            if is_file_binary(item):
                Logger.warn(f"Binary file '{item}' ignored.")
                continue
            _path = str(item)
            _key = process_key_from_path(_path)
            if not _key:
                raise DSOException(f"The provided key '{key}' is not valid, becasue input '{input}' is a directoty.")
            _render_path = process_render_path_from_key(_key)
            templates.append({'Path': _path, 'Key': _key, 'RenderPath': _render_path})

        
        # m = re.match(r'^.*?([*][*/*|*/**]*)$', input)
        # if m:
        #     globe = m.groups()[0]
        #     inputDir = input[:-len(globe)]
        #     inputDir = re.sub('/$', '', inputDir)
        # else:
        #     globe = ''
        #     inputDir = input
        

        # if os.path.isdir(inputDir):

        #     if not globe:
        #         raise DSOException(f"The provided input '{input}' is a directoty.")

        #     if key and not (key in ['.' , './'] or key.endswith(globe)):
        #         raise DSOException(f"The provided key '{key}' is not valid, becasue input '{input}' is a directoty.")

        #     if render_path and not (render_path in ['.' , './'] or render_path.endswith(globe)):
        #         raise DSOException(f"The provided render path '{render_path}' is not valid, becasue input '{input}' is a directoty.")

        #     for item in Path(inputDir).glob(globe):
        #         if not Path(item).is_file(): continue
        #         if is_file_binary(item):
        #             Logger.warn(f"Binary file '{item}' ignored.")
        #             continue
                
        #         _path = str(item)

        #         _key = process_key_from_path(_path)
        #         if not _key:
        #             raise DSOException(f"The provided key '{key}' is not valid, becasue input '{input}' is a directoty.")

        #         _render_path = process_render_path_from_key(_key)

        #         templates.append({'Path': _path, 'Key': _key, 'RenderPath': _render_path})

        #  ### input not a directory
        # else:
        #     if not os.path.isfile(inputDir):
        #         raise DSOException(f"Path '{inputDir}' does not exist.")

        #     if key and '**' in key:
        #         raise DSOException(f"The provided key '{key}' is not valid, becasue input '{input}' is not a directoty.")


        #     inputDir = os.path.dirname(input)
        #     _path = input

        #     _key = process_key_from_path(input)
        #     if not _key:
        #         raise DSOException(f"The provided key '{key}' is not valid, becasue input '{input}' is a directoty.")

        #     _render_path = process_render_path_from_key(_key)

        #     templates.append({'Path': _path, 'Key': _key, 'RenderPath': _render_path})


    try:
        Logger.set_verbosity(verbosity)
        Config.load(working_dir if working_dir else os.getcwd(), config)
        check_command_usage()
        for template in templates:
            # if not Templates.validate_key(template['Key']):
            #     Logger.info(MESSAGES['TryHelp'], stress = False, force=True)
            #     exit(1)
            print(Templates.add(template['Key'], open(template['Path'], encoding='utf-8', mode='r').read(), template['RenderPath']), flush=True)

    
    except DSOException as e:
        Logger.error(e.message)
    except Exception as e:
        msg = getattr(e, 'message', getattr(e, 'msg', str(e)))
        Logger.critical(msg)
        if verbosity >= log_levels['full']:
            raise

###--------------------------------------------------------------------------------------------

@template.command('delete', context_settings=DEFAULT_CONTEXT, short_help=f"{CLI_COMMANDS_SHORT_HELP['template']['delete']}")
@click.argument('key', required=False)
@click.option('-k', '--key', 'key_option', metavar='<key>', required=False, help=f"{CLI_PARAMETERS_HELP['template']['key']}")
@click.option('-i', '--input', metavar='<path>', required=False, type=click.File(encoding='utf-8', mode='r'), help=f"{CLI_PARAMETERS_HELP['common']['input']}")
@click.option('--recursive', required=False, is_flag=True, help=f"{CLI_PARAMETERS_HELP['template']['recursive']}")
@click.option('-f', '--format', required=False, type=click.Choice(['csv','json', 'yaml']), default='csv', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['format']}")
@click.option('-w','--working-dir', metavar='<path>', type=click.Path(exists=True, file_okay=False), required=False, default='.', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['working_dir']}")
@click.option('--config', metavar='<key>=<value>, ...', required=False, help=f"{CLI_PARAMETERS_HELP['common']['config']}")
@click.option('-b', '--verbosity', metavar='<number>', required=False, type=RangeParamType(click.INT, minimum=0, maximum=5), default='2', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['verbosity']}")
def delete_template(key, key_option, input, recursive, format, working_dir, config, verbosity):
    """
    Delete a template from the application.\n
    \tKEY: The key of the template. It may also be provided via '--key' option.\n
    \nMultiple templates may be deleted at once from an input file using '-i' / '--input' option. Use '-f' / '--format' to specify the format of the input if neeeded.
    """

    templates = []

    def check_command_usage():
        nonlocal templates, key
        if input:
            if key or key_option:
                Logger.error(MESSAGES['ArgumentsMutualExclusive'].format("'--key'","'-i' / '--input'"))
                Logger.info(MESSAGES['TryHelp'], stress = False, force=True)
                exit(1)

            if format == 'json':
                try:
                    templates = json.load(input)['Templates']
                # except json.JSONDecodeError as e:
                except:
                    Logger.error(MESSAGES['InvalidFileFormat'].format(f"'{format}'"))
                    exit(1)
            elif format == 'yaml':
                try:
                    templates = yaml.load(input, yaml.SafeLoader)['Templates']
                # except yaml.YAMLError as e:
                except:
                    Logger.error(MESSAGES['InvalidFileFormat'].format(f"'{format}'"))
                    exit(1)
            elif format == 'csv':
                try:
                    _templates = input.readlines()
                    if len(_templates):
                        if ',' in _templates[0]:
                            header = _templates[0]
                            Key = header.split(',')[0].strip()
                            _templates.pop(0)
                        else:
                            Key = 'Key'
                        for template in _templates:
                            _key = template.split(',')[0].strip()
                            # _value = param.split('=', 1)[1].strip()
                            templates.append({Key: _key})
                except:
                    Logger.error(MESSAGES['InvalidFileFormat'].format(f"'{format}'"))
                    exit(1)
        ### not input
        else:
            if key and key_option:
                Logger.error(MESSAGES['ArgumentsMutualExclusive'].format("'key'", "'--key'"))
                Logger.info(MESSAGES['TryHelp'], stress = False, force=True)
                exit(1)
    
            key = key or key_option

            if not key:
                Logger.error(MESSAGES['AtleastOneofTwoNeeded'].format("'--key'","'-i' / '--input'"))
                Logger.info(MESSAGES['TryHelp'], stress = False, force=True)
                exit(1)

            # m = re.match(r'^.*?([*][*/*|*/**]*)$', key)
            # if m:
            #     globe_filter = m.groups()[0]
            #     key = key[:-len(globe_filter)]


            templates.append({'Key': key})

        # invalid = False
        # for template in templates:
        #     invalid = not Templates.validate_key(template['Key']) or invalid

        # if invalid:
        #     Logger.info(MESSAGES['TryHelp'], stress = False, force=True)
        #     exit(1)

    try:
        Logger.set_verbosity(verbosity)
        Config.load(working_dir if working_dir else os.getcwd(), config)
        check_command_usage()

        for template in templates:
            for deleted in Templates.delete(template['Key'], recursive):
                print(deleted, flush=True)
    
    except DSOException as e:
        Logger.error(e.message)
    except Exception as e:
        msg = getattr(e, 'message', getattr(e, 'msg', str(e)))
        Logger.critical(msg)
        if verbosity >= log_levels['full']:
            raise

###--------------------------------------------------------------------------------------------

@template.command('render', context_settings=DEFAULT_CONTEXT, short_help=f"{CLI_COMMANDS_SHORT_HELP['template']['render']}")
@click.option('-s', '--stage', metavar='<name>[/<number>]', default='default', help=f"{CLI_PARAMETERS_HELP['common']['stage']}")
@click.option('-l', '--limit', required=False, default='', help=f"{CLI_PARAMETERS_HELP['template']['limit']}")
@click.option('-w','--working-dir', metavar='<path>', type=click.Path(exists=True, file_okay=False), required=False, default='.', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['working_dir']}")
@click.option('--config', metavar='<key>=<value>, ...', required=False, help=f"{CLI_PARAMETERS_HELP['common']['config']}")
@click.option('-b', '--verbosity', metavar='<number>', required=False, type=RangeParamType(click.INT, minimum=0, maximum=5), default='2', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['verbosity']}")
def render_template(stage, limit, working_dir, config, verbosity):
    """
    Render templates using parameters in a stage.\n
    """

    def check_command_usage():
        pass

    try:
        Logger.set_verbosity(verbosity)
        Config.load(working_dir if working_dir else os.getcwd(), config)
        check_command_usage()

        rendered = Templates.render(stage, limit)
        print(*rendered, sep='\n')

    
    except DSOException as e:
        Logger.error(e.message)
    except Exception as e:
        msg = getattr(e, 'message', getattr(e, 'msg', str(e)))
        Logger.critical(msg)
        if verbosity >= log_levels['full']:
            raise


###--------------------------------------------------------------------------------------------
###--------------------------------------------------------------------------------------------
###--------------------------------------------------------------------------------------------

@package.command('list', context_settings=DEFAULT_CONTEXT, short_help="List available packages")
@click.argument('stage')
@click.option('-f', '--format', required=False, type=click.Choice(['csv','json', 'yaml']), default='csv', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['format']}")
@click.option('-w','--working-dir', metavar='<path>', type=click.Path(exists=True, file_okay=False), required=False, default='.', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['working_dir']}")
@click.option('--config', metavar='<key>=<value>, ...', required=False, help=f"{CLI_PARAMETERS_HELP['common']['config']}")
@click.option('-b', '--verbosity', metavar='<number>', required=False, type=RangeParamType(click.INT, minimum=0, maximum=5), default='2', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['verbosity']}")
def list_package(stage, format, working_dir, config, verbosity):
    """
    Return the list of all available packages generated for a stage.\n
    \tENV: Name of the environment
    """
    
    print(Packages.list(stage))

###--------------------------------------------------------------------------------------------

@package.command('download', context_settings=DEFAULT_CONTEXT, short_help="Download a package")
@click.argument('stage')
@click.argument('package')
@click.option('-f', '--format', required=False, type=click.Choice(['csv','json', 'yaml']), default='csv', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['format']}")
@click.option('-w','--working-dir', metavar='<path>', type=click.Path(exists=True, file_okay=False), required=False, default='.', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['working_dir']}")
@click.option('--config', metavar='<key>=<value>, ...', required=False, help=f"{CLI_PARAMETERS_HELP['common']['config']}")
@click.option('-b', '--verbosity', metavar='<number>', required=False, type=RangeParamType(click.INT, minimum=0, maximum=5), default='2', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['verbosity']}")
def download_package(stage, package, format, working_dir, config, verbosity):
    """
    Downlaod a package generated for a stage.\n
    \tENV: Name of the environment\n
    \tPACKAGE: Version of the package to download
    """

    Packages.download(stage, name)

###--------------------------------------------------------------------------------------------

@package.command('create', context_settings=DEFAULT_CONTEXT, short_help="Create a package")
@click.argument('stage')
@click.argument('description', required=False)
@click.option('-f', '--format', required=False, type=click.Choice(['csv','json', 'yaml']), default='csv', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['format']}")
@click.option('-w','--working-dir', metavar='<path>', type=click.Path(exists=True, file_okay=False), required=False, default='.', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['working_dir']}")
@click.option('--config', metavar='<key>=<value>, ...', required=False, help=f"{CLI_PARAMETERS_HELP['common']['config']}")
@click.option('-b', '--verbosity', metavar='<number>', required=False, type=RangeParamType(click.INT, minimum=0, maximum=5), default='2', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['verbosity']}")
def generate_package(stage, verbosity, format, description=''):
    """
    Create a new build package for the application.\n
    \tENV: Name of the environment\n
    \tDESCRIPTION (optional): Description of the package
    """





###--------------------------------------------------------------------------------------------

@package.command('delete', context_settings=DEFAULT_CONTEXT, short_help="Delete a package")
@click.argument('stage')
@click.argument('package')
@click.option('-f', '--format', required=False, type=click.Choice(['csv','json', 'yaml']), default='csv', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['format']}")
@click.option('-w','--working-dir', metavar='<path>', type=click.Path(exists=True, file_okay=False), required=False, default='.', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['working_dir']}")
@click.option('--config', metavar='<key>=<value>, ...', required=False, help=f"{CLI_PARAMETERS_HELP['common']['config']}")
@click.option('-b', '--verbosity', metavar='<number>', required=False, type=RangeParamType(click.INT, minimum=0, maximum=5), default='2', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['verbosity']}")
def delete_package(stage, package, format, working_dir, config, verbosity):
    """
    Delete a package from a stage.\n
    \tENV: Name of the environment\n
    \tPACKAGE: Version of the package to be deleted
    """

    Packages.delete(stage, name)


###--------------------------------------------------------------------------------------------

@release.command('list', context_settings=DEFAULT_CONTEXT, short_help="List available releases")
@click.argument('stage')
@click.option('-f', '--format', required=False, type=click.Choice(['csv','json', 'yaml']), default='csv', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['format']}")
@click.option('-w','--working-dir', metavar='<path>', type=click.Path(exists=True, file_okay=False), required=False, default='.', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['working_dir']}")
@click.option('--config', metavar='<key>=<value>, ...', required=False, help=f"{CLI_PARAMETERS_HELP['common']['config']}")
@click.option('-b', '--verbosity', metavar='<number>', required=False, type=RangeParamType(click.INT, minimum=0, maximum=5), default='2', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['verbosity']}")
def list_release(stage, format, working_dir, config, verbosity):
    """
    Return the list of all available releases generated for a stage.\n
    \tENV: Name of the environment
    """

    print(Releases.list(stage))


###--------------------------------------------------------------------------------------------

@release.command('download', context_settings=DEFAULT_CONTEXT, short_help="Download a release")
@click.argument('stage')
@click.argument('release')
@click.option('-f', '--format', required=False, type=click.Choice(['csv','json', 'yaml']), default='csv', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['format']}")
@click.option('-w','--working-dir', metavar='<path>', type=click.Path(exists=True, file_okay=False), required=False, default='.', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['working_dir']}")
@click.option('--config', metavar='<key>=<value>, ...', required=False, help=f"{CLI_PARAMETERS_HELP['common']['config']}")
@click.option('-b', '--verbosity', metavar='<number>', required=False, type=RangeParamType(click.INT, minimum=0, maximum=5), default='2', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['verbosity']}")
def download_release(stage, release, format, working_dir, config, verbosity):
    """
    Downlaod a release generated for a stage.\n
    \tENV: Name of the environment\n
    \tRELEASE: Version of the release
    """

    Releases.download(stage, release)

###--------------------------------------------------------------------------------------------

@release.command('create', context_settings=DEFAULT_CONTEXT, short_help="Create a release")
@click.argument('stage')
@click.argument('package')
@click.argument('description', required=False)
@click.option('-f', '--format', required=False, type=click.Choice(['csv','json', 'yaml']), default='csv', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['format']}")
@click.option('-w','--working-dir', metavar='<path>', type=click.Path(exists=True, file_okay=False), required=False, default='.', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['working_dir']}")
@click.option('--config', metavar='<key>=<value>, ...', required=False, help=f"{CLI_PARAMETERS_HELP['common']['config']}")
@click.option('-b', '--verbosity', metavar='<number>', required=False, type=RangeParamType(click.INT, minimum=0, maximum=5), default='2', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['verbosity']}")
def generate_release(stage, verbosity, format, package, description=''):
    """
    Create a new release for a stage.\n
    \tENV: Name of the environment\n
    \tPACKAGE: Version of the package to be used for creating the release\n
    \tDESCRIPTION (optional): Description of the release
    """

    Releases.generate(stage, package, description)


###--------------------------------------------------------------------------------------------

@release.command('delete', context_settings=DEFAULT_CONTEXT, short_help="Delete a release")
@click.argument('stage')
@click.argument('release')
@click.option('-f', '--format', required=False, type=click.Choice(['csv','json', 'yaml']), default='csv', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['format']}")
@click.option('-w','--working-dir', metavar='<path>', type=click.Path(exists=True, file_okay=False), required=False, default='.', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['working_dir']}")
@click.option('--config', metavar='<key>=<value>, ...', required=False, help=f"{CLI_PARAMETERS_HELP['common']['config']}")
@click.option('-b', '--verbosity', metavar='<number>', required=False, type=RangeParamType(click.INT, minimum=0, maximum=5), default='2', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['verbosity']}")
def delete_release(stage, release, format, working_dir, config, verbosity):
    """
    Delete a release from a stage.\n
    \tENV: Name of the environment\n
    \tRELEASE: Version of the release to be deleted
    """

    Releases.delete(stage, release)

###--------------------------------------------------------------------------------------------

@config.command('get', context_settings=DEFAULT_CONTEXT, short_help=f"{CLI_COMMANDS_SHORT_HELP['config']['get']}")
@click.argument('key', required=False)
@click.option('-l','--local', is_flag=True, default=False, help=f"{CLI_PARAMETERS_HELP['config']['local']}")
@click.option('-g','--global', '_global', is_flag=True, default=False, help=f"{CLI_PARAMETERS_HELP['config']['global']}")
@click.option('-w','--working-dir', metavar='<path>', type=click.Path(exists=True, file_okay=False), required=False, default='.', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['working_dir']}")
@click.option('--config', metavar='<key>=<value>, ...', required=False, help=f"{CLI_PARAMETERS_HELP['common']['config']}")
@click.option('-b', '--verbosity', metavar='<number>', required=False, type=RangeParamType(click.INT, minimum=0, maximum=5), default='2', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['verbosity']}")
def get_config(key, local, _global, working_dir, config, verbosity):
    """
    Get DSO application configuration.\n
    \tKEY: The key of the configuration
    """

    scope = ''

    def check_command_usage():
        nonlocal scope
        if local and _global:
            Logger.error(MESSAGES['ArgumentsMutualExclusive'].format("'-l' / '--local'", "'-g' / '--global'"))
            Logger.info(MESSAGES['TryHelp'], stress = False, force=True)
            exit(1)
        
        scope='local' if local else 'global' if _global else ''

    def print_result(output):
        if not output: return
        if isinstance(output, dict):
            print(yaml.dump(output, sort_keys=False, indent=2), flush=True)
        else:
            print(output, flush=True)

    try:
        Logger.set_verbosity(verbosity)
        Config.load(working_dir if working_dir else os.getcwd(), config)
        check_command_usage()
        print_result(Config.get(key, scope))

    except DSOException as e:
        Logger.error(e.message)
    except Exception as e:
        msg = getattr(e, 'message', getattr(e, 'msg', str(e)))
        Logger.critical(msg)
        if verbosity >= log_levels['full']:
            raise

###--------------------------------------------------------------------------------------------

@config.command('set', context_settings=DEFAULT_CONTEXT, short_help=f"{CLI_COMMANDS_SHORT_HELP['config']['set']}")
@click.argument('key', required=False)
@click.option('-k', '--key', 'key_option', metavar='<value>', required=False, help=f"{CLI_PARAMETERS_HELP['config']['key']}")
@click.argument('value', required=False)
@click.option('-v', '--value', 'value_option', metavar='<value>', required=False, help=f"{CLI_PARAMETERS_HELP['config']['value']}")
@click.option('-g','--global', '_global', is_flag=True, default=False, help=f"{CLI_PARAMETERS_HELP['config']['global']}")
@click.option('-i', '--input', metavar='<path>', required=False, type=click.File(encoding='utf-8', mode='r'), help=f"{CLI_PARAMETERS_HELP['config']['input']}")
@click.option('-w','--working-dir', metavar='<path>', type=click.Path(exists=True, file_okay=False), required=False, default='.', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['working_dir']}")
@click.option('--config', metavar='<key>=<value>, ...', required=False, help=f"{CLI_PARAMETERS_HELP['common']['config']}")
@click.option('-b', '--verbosity', metavar='<number>', required=False, type=RangeParamType(click.INT, minimum=0, maximum=5), default='2', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['verbosity']}")
def set_config(key, key_option, value, value_option, _global, input, working_dir, config, verbosity):
    """
    Set DSO application configuration.\n
    \tKEY: The key of the configuration. It may be also provided via '--key' option.\n
    \tVALUE: The value for the configuration. It may be also provided via '-v' / '--value' option.\n
    """

    def check_command_usage():
        nonlocal key, value
        if key and key_option:
            Logger.error(MESSAGES['ArgumentsMutualExclusive'].format("'key'", "'--key'"))
            Logger.info(MESSAGES['TryHelp'], stress = False, force=True)
            exit(1)

        key = key or key_option

        if not key:
            Logger.error(MESSAGES['AtleastOneofTwoNeeded'].format("'--key'","'-i' / '--input'"))
            Logger.info(MESSAGES['TryHelp'], stress = False, force=True)
            exit(1)

        if value and value_option:
            Logger.error(MESSAGES['ArgumentsMutualExclusive'].format("'value'", "'-v' / '--value'"))
            Logger.info(MESSAGES['TryHelp'], stress = False, force=True)
            exit(1)

        value = value or value_option

        # if not _value:
        #     Logger.error(MESSAGES['MissingOption'].format("'-v' / '--value'"))
        #     Logger.info(MESSAGES['TryHelp'], stress = False, force=True)
        #     exit(1)

        if value and input:
            Logger.error(MESSAGES['ArgumentsMutualExclusive'].format("'-v' / '--value'","'-i' / '--input'"))
            Logger.info(MESSAGES['TryHelp'], stress = False, force=True)
            exit(1)

        if not (value or input):
            Logger.error(MESSAGES['AtleastOneofTwoNeeded'].format("'-v' / '--value'","'-i' / '--input'"))
            Logger.info(MESSAGES['TryHelp'], stress = False, force=True)
            exit(1)

        if input:
            try:
                value = yaml.load(input, yaml.SafeLoader)
            # except yaml.YAMLError as e:
            except:
                Logger.error(MESSAGES['InvalidFileFormat'].format(f"'{format}'"))
                exit(1)


    try:
        Logger.set_verbosity(verbosity)
        Config.load(working_dir if working_dir else os.getcwd(), config)
        check_command_usage()
        Config.set(key, value, _global)

    except DSOException as e:
        Logger.error(e.message)
    except Exception as e:
        msg = getattr(e, 'message', getattr(e, 'msg', str(e)))
        Logger.critical(msg)
        if verbosity >= log_levels['full']:
            raise

###--------------------------------------------------------------------------------------------

@config.command('delete', context_settings=DEFAULT_CONTEXT, short_help=f"{CLI_COMMANDS_SHORT_HELP['config']['delete']}")
@click.argument('key', required=False)
@click.option('-k', '--key', 'key_option', metavar='<value>', required=False, help=f"{CLI_PARAMETERS_HELP['config']['key']}")
@click.option('-g','--global', '_global', is_flag=True, default=False, help=f"{CLI_PARAMETERS_HELP['config']['global']}")
@click.option('-w','--working-dir', metavar='<path>', type=click.Path(exists=True, file_okay=False), required=False, default='.', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['working_dir']}")
@click.option('--config', metavar='<key>=<value>, ...', required=False, help=f"{CLI_PARAMETERS_HELP['common']['config']}")
@click.option('-b', '--verbosity', metavar='<number>', required=False, type=RangeParamType(click.INT, minimum=0, maximum=5), default='2', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['verbosity']}")
def delete_config(key, key_option, _global, working_dir, config, verbosity):
    """
    Dlete a DSO application configuration.\n
    \tKEY: The key of the configuration
    """

    def check_command_usage():
        nonlocal key
        if key and key_option:
            Logger.error(MESSAGES['ArgumentsMutualExclusive'].format("'key'", "'--key'"))
            Logger.info(MESSAGES['TryHelp'], stress = False, force=True)
            exit(1)

        key = key or key_option

        if not key:
            Logger.error(MESSAGES['AtleastOneofTwoNeeded'].format("'--key'","'-i' / '--input'"))
            Logger.info(MESSAGES['TryHelp'], stress = False, force=True)
            exit(1)


    def print_result(output):
        pass

    try:
        Logger.set_verbosity(verbosity)
        Config.load(working_dir if working_dir else os.getcwd(), config)
        check_command_usage()
        Config.delete(key, _global)

    except DSOException as e:
        Logger.error(e.message)
    except Exception as e:
        msg = getattr(e, 'message', getattr(e, 'msg', str(e)))
        Logger.critical(msg)
        if verbosity >= log_levels['full']:
            raise

###--------------------------------------------------------------------------------------------

# @config.command('setup', context_settings=DEFAULT_CONTEXT, short_help=f"{CLI_COMMANDS_SHORT_HELP['config']['setup']}")
# @click.option('-w','--working-dir', metavar='<path>', type=click.Path(exists=True, file_okay=False), required=False, default='.', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['working_dir']}")
# @click.option('--config', metavar='<key>=<value>, ...', required=False, help=f"{CLI_PARAMETERS_HELP['common']['config']}")
# @click.option('-b', '--verbosity', metavar='<number>', required=False, type=RangeParamType(click.INT, minimum=0, maximum=5), default='2', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['verbosity']}")
# def setup_config(working_dir, config, verbosity):
#     """
#     Run a setup wizard to configure a DSO application.\n
#     """

#     def check_command_usage():
#         pass

#     try:
#         Logger.set_verbosity(verbosity)
#         Config.load(working_dir if working_dir else os.getcwd(), config)
#         check_command_usage()


#     except DSOException as e:
#         Logger.error(e.message)
#     except Exception as e:
#         msg = getattr(e, 'message', getattr(e, 'msg', str(e)))
#         Logger.critical(msg)
#         if verbosity >= log_levels['full']:
#             raise

###--------------------------------------------------------------------------------------------

@config.command('init', context_settings=DEFAULT_CONTEXT, short_help=f"{CLI_COMMANDS_SHORT_HELP['config']['init']}")
@click.option('--setup', is_flag=True, required=False, help=f"{CLI_PARAMETERS_HELP['config']['setup']}")
@click.option('-l','--local', is_flag=True, default=False, help=f"{CLI_PARAMETERS_HELP['config']['init_local']}")
@click.option('-i', '--input', metavar='<path>', required=False, type=click.File(encoding='utf-8', mode='r'), help=f"{CLI_PARAMETERS_HELP['config']['input']}")
@click.option('-w','--working-dir', metavar='<path>', type=click.Path(exists=True, file_okay=False), required=False, default='.', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['working_dir']}")
@click.option('--config', metavar='<key>=<value>, ...', required=False, help=f"{CLI_PARAMETERS_HELP['common']['config']}")
@click.option('-b', '--verbosity', metavar='<number>', required=False, type=RangeParamType(click.INT, minimum=0, maximum=5), default='2', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['verbosity']}")
def init_config(setup, local, input, working_dir, config, verbosity):
    """
    Initialize DSO configuration for the working directory.\n
    The option '-w-' / '--working-dir' can be used to specify a different working directory than the current directory where dso is running in.
    """

    init_config = None

    def check_command_usage():
        nonlocal init_config

        if input:
            # if local:
            #     Logger.warn("Option '-l' / '--local' is not needed when '-i' / '--input' specifies the initial configuration, as it will always be overriden locally.")
            try:
                init_config = yaml.load(input, yaml.SafeLoader)
            except:
                Logger.error(MESSAGES['InvalidFileFormat'].format('yaml'))
                exit(1)

    try:
        Logger.set_verbosity(verbosity)
        check_command_usage()
        # Config.load(working_dir if working_dir else os.getcwd(), config)
        Config.init(working_dir, init_config, config, local)

    except DSOException as e:
        Logger.error(e.message)
    except Exception as e:
        msg = getattr(e, 'message', getattr(e, 'msg', str(e)))
        Logger.critical(msg)
        if verbosity >= log_levels['full']:
            raise

###--------------------------------------------------------------------------------------------


if __name__ == '__main__':
    cli()

# ### Zsh workaround: Zsh puts args not passed asd $@ and starting with --/- first when calling the function via alias
# ### does not work for flag options!
# if len(sys.argv)>3 and ( sys.argv[1].startswith('-') or sys.argv[1] == '--' ):
#     sys.argv.append(sys.argv[1])  ### add --<option> to last
#     sys.argv.append(sys.argv[2]) ### add value of the option to last
#     sys.argv.pop(1)  ### remove original --<option>
#     sys.argv.pop(1)  ### remove original value of the option

modify_click_usage_error()
