import sys
import os
import platform
import click
import re
import yaml
import json
import csv
import subprocess
import tempfile
import glob
import jmespath
from pathlib import Path
from stdiomask import getpass
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
from .utils import flatten_dict, is_file_binary, print_list
from version import dso_version

is_windows = sys.platform == 'win32'
if is_windows:
    default_pager = 'more'
else:
    default_pager = 'less -SR'


DEFAULT_CLICK_CONTEXT = dict(help_option_names=['-h', '--help'])

###--------------------------------------------------------------------------------------------

@click.group(context_settings=DEFAULT_CLICK_CONTEXT)
def cli():
    """DevSecOps CLI"""
    pass

###--------------------------------------------------------------------------------------------

@cli.group(context_settings=DEFAULT_CLICK_CONTEXT)
def config():
    """
    Manage DSO application configuration.
    """
    pass

###--------------------------------------------------------------------------------------------

@cli.group(context_settings=DEFAULT_CLICK_CONTEXT)
def parameter():
    """
    Manage parameters.
    """
    pass

###--------------------------------------------------------------------------------------------

@cli.group(context_settings=DEFAULT_CLICK_CONTEXT)
def secret():
    """
    Manage secrets.
    """
    pass

###--------------------------------------------------------------------------------------------

@cli.group(context_settings=DEFAULT_CLICK_CONTEXT)
def template():
    """
    Manage templates.
    """
    pass

###--------------------------------------------------------------------------------------------

@cli.group(context_settings=DEFAULT_CLICK_CONTEXT)
def package():
    """
    Manage build packages.
    """
    pass

###--------------------------------------------------------------------------------------------

@cli.group(context_settings=DEFAULT_CLICK_CONTEXT)
def release():
    """
    Manage deployment releases.
    """
    pass

###--------------------------------------------------------------------------------------------

@cli.group(context_settings=DEFAULT_CLICK_CONTEXT)
def provision():
    """
    Provision resources.
    """
    pass

###--------------------------------------------------------------------------------------------

@cli.group(context_settings=DEFAULT_CLICK_CONTEXT)
def deploy():
    """
    Deploy releases.
    """
    pass

###--------------------------------------------------------------------------------------------
###--------------------------------------------------------------------------------------------
###--------------------------------------------------------------------------------------------

@cli.command('version', context_settings=DEFAULT_CLICK_CONTEXT, short_help=f"{CLI_COMMANDS_SHORT_HELP['version']}")
def version():
    """
    Display versions.
    """
    click.echo(f"DSO CLI: {dso_version}\nPython: {platform.sys.version}")


###--------------------------------------------------------------------------------------------
###--------------------------------------------------------------------------------------------
###--------------------------------------------------------------------------------------------

@parameter.command('add', context_settings=DEFAULT_CLICK_CONTEXT, short_help=f"{CLI_COMMANDS_SHORT_HELP['parameter']['add']}")
@command_doc(CLI_COMMANDS_HELP['parameter']['add'])
@click.argument('key', required=False)
@click.option('-k', '--key', 'key_option', required=False, metavar='<key>', help=f"{CLI_PARAMETERS_HELP['parameter']['key']}")
@click.argument('value', required=False)
@click.option('-v', '--value', 'value_option', metavar='<value>', required=False, help=f"{CLI_PARAMETERS_HELP['parameter']['value']}")
@click.option('-s', '--stage', metavar='<name>[/<number>]', default='default', help=f"{CLI_PARAMETERS_HELP['common']['stage']}")
@click.option('-i', '--input', metavar='<path>', required=False, type=click.File(encoding='utf-8', mode='r'), help=f"{CLI_PARAMETERS_HELP['common']['input']}")
@click.option('-f', '--format', required=False, type=click.Choice(['shell','json', 'yaml', 'text', 'csv']), default='shell', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['format']}")
@click.option('-b', '--verbosity', metavar='<number>', required=False, type=RangeParamType(click.INT, minimum=0, maximum=5), default='2', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['verbosity']}")
@click.option('--config', metavar='<key>=<value>,...', required=False, help=f"{CLI_PARAMETERS_HELP['common']['config']}")
@click.option('-w','--working-dir', metavar='<path>', type=click.Path(exists=True, file_okay=False), required=False, default='.', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['working_dir']}")
def add_parameter(stage, key, key_option, value, value_option, input, format, working_dir, config, verbosity):
    
    parameters = []

    def check_command_usage():
        nonlocal stage, parameters
        stage = Stages.normalize(stage)
        if input:
            if key or key_option:
                Logger.error(CLI_MESSAGES['ArgumentsMutualExclusive'].format("'-k' / '--key'","'-i' / '--input'"))
                Logger.info(CLI_MESSAGES['TryHelp'], stress = False, force=True)
                exit(1)
            if format == 'json':
                try:
                    parameters = json.load(input)['Parameters']
                # except json.JSONDecodeError as e:
                except:
                    Logger.error(CLI_MESSAGES['InvalidFileFormat'].format(format))
                    exit(1)
            elif format == 'yaml':
                try:
                    parameters = yaml.load(input, yaml.SafeLoader)['Parameters']
                # except yaml.YAMLError as e:
                except:
                    Logger.error(CLI_MESSAGES['InvalidFileFormat'].format(format))
                    exit(1)
            elif format == 'csv':
                try:
                    _parameters = list(csv.reader(input))
                    if not len(_parameters): return
                except:
                    Logger.error(CLI_MESSAGES['InvalidFileFormat'].format(format))
                    exit(1)

                header = _parameters[0]
                if len(header) < 2:
                    raise DSOException(CLI_MESSAGES['InvalidFileFormat'].format(format))
                if not header[0].strip() == 'Key':
                    raise DSOException(CLI_MESSAGES['MissingCSVField'].format("Key"))
                if not header[1].strip() == 'Value':
                    raise DSOException(CLI_MESSAGES['MissingCSVField'].format("Value"))

                for parameter in _parameters[1:]:
                    _key = parameter[0].strip()
                    _value = parameter[1].strip()
                    parameters.append({'Key': _key, 'Value': _value})

            elif format == 'text':
                _parameters = input.readlines()
                try:
                    if len(_parameters):
                        header = _parameters[0]
                        Key = header.split('\t')[0].strip()
                        Value = header.split('\t')[1].strip()
                        for param in _parameters[1:]:
                            _key = param.split('\t')[0].strip()
                            _value = param.split('\t')[1].strip()
                            parameters.append({Key: _key, Value: _value})
                except:
                    Logger.error(CLI_MESSAGES['InvalidFileFormat'].format(format))
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
                    Logger.error(CLI_MESSAGES['InvalidFileFormat'].format(format))
                    exit(1)

        ### not input
        else:
            if key and key_option:
                Logger.error(CLI_MESSAGES['ArgumentsOrOption'].format("Parameter key", "'KEY'", "'-k' / '--key'"))
                Logger.info(CLI_MESSAGES['TryHelp'], stress = False, force=True)
                exit(1)
    
            _key = key or key_option

            if not _key:
                Logger.error(CLI_MESSAGES['AtleastOneofTwoNeeded'].format("'-k' / '--key'","'-i' / '--input'"))
                Logger.info(CLI_MESSAGES['TryHelp'], stress = False, force=True)
                exit(1)

            if value and value_option:
                Logger.error(CLI_MESSAGES['ArgumentsMutualExclusive'].format("'value'", "'-v' / '--value'"))
                Logger.info(CLI_MESSAGES['TryHelp'], stress = False, force=True)
                exit(1)

            _value = value or value_option

            if not _value:
                Logger.error(CLI_MESSAGES['MissingOption'].format("'-v' / '--value'"))
                Logger.info(CLI_MESSAGES['TryHelp'], stress = False, force=True)
                exit(1)

            parameters.append({'Key': _key, 'Value': _value})


        # invalid = False
        # for param in parameters:
        #     invalid = not Parameters.validate_key(param['Key']) or invalid

        # if invalid:
        #     Logger.info(CLI_MESSAGES['TryHelp'], stress = False, force=True)
        #     exit(1)

    try:
        Logger.set_verbosity(verbosity)
        check_command_usage()
        Config.load(working_dir if working_dir else os.getcwd(), config)

        result = []
        for param in parameters:
            key = param['Key']
            value = param['Value']
            result.append(Parameters.add(stage, key, value))

    except DSOException as e:
        Logger.error(e.message)
    except Exception as e:
        msg = getattr(e, 'message', getattr(e, 'msg', str(e)))
        Logger.critical(msg)
        if verbosity >= log_levels['full']:
            raise
    finally:
        print_list(result)

###--------------------------------------------------------------------------------------------

@parameter.command('list', context_settings=DEFAULT_CLICK_CONTEXT, short_help=f"{CLI_COMMANDS_SHORT_HELP['parameter']['list']}")
@command_doc(CLI_COMMANDS_HELP['parameter']['list'])
@click.option('-s', '--stage', metavar='<name>[/<number>]', default='default', help=f"{CLI_PARAMETERS_HELP['common']['stage']}")
@click.option('-u','--uninherited', 'uninherited', is_flag=True, default=False, help=f"{CLI_PARAMETERS_HELP['parameter']['uninherited']}")
@click.option('-v', '--query-values', required=False, is_flag=True, default=False, show_default=True, help=f"{CLI_PARAMETERS_HELP['parameter']['query_values']}")
@click.option('-a', '--query-all', required=False, is_flag=True, default=False, show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['query_all']}")
@click.option('-q', '--query', metavar='<jmespath>', required=False, help=f"{CLI_PARAMETERS_HELP['common']['query']}")
@click.option('-f', '--format', required=False, type=click.Choice(['shell','json', 'yaml', 'text', 'csv']), default='shell', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['format']}")
@click.option('-b', '--verbosity', metavar='<number>', required=False, type=RangeParamType(click.INT, minimum=0, maximum=5), default='2', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['verbosity']}")
@click.option('--config', metavar='<key>=<value>,...', required=False, help=f"{CLI_PARAMETERS_HELP['common']['config']}")
@click.option('-w','--working-dir', metavar='<path>', type=click.Path(exists=True, file_okay=False), required=False, default='.', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['working_dir']}")
def list_parameter(stage, uninherited, query_values, query_all, query, format, working_dir, config, verbosity):

    def check_command_usage():
        nonlocal stage
        stage = Stages.normalize(stage)

        if query:
            try:
                jmespath.compile(query)
            except jmespath.exceptions.ParseError as e:
                raise DSOException(f"Invalid JMESPath query '{query}': {e.msg}")

        if query and not format in ['json', 'yaml']:
            Logger.error(CLI_MESSAGES['QueryOptionCompatibleFormats'])
            Logger.info(CLI_MESSAGES['TryHelp'], stress = False, force=True)
            exit(1)

        if query_all and format == 'shell':
            Logger.error(CLI_MESSAGES['QueryAllOptionNonCompatibleFormats'])
            Logger.info(CLI_MESSAGES['TryHelp'], stress = False, force=True)
            exit(1)

        if query and query_all:
            Logger.error(CLI_MESSAGES['ArgumentsMutualExclusive'].format("'-q' / '--query'", "'-a' / '--query-all'"))
            Logger.info(CLI_MESSAGES['TryHelp'], stress = False, force=True)
            exit(1)

        if query and query_values:
            Logger.error(CLI_MESSAGES['ArgumentsMutualExclusive'].format("'-q' / '--query'", "'-v' / '--query-values'"))
            Logger.info(CLI_MESSAGES['TryHelp'], stress = False, force=True)
            exit(1)

        if query_all and query_values:
            Logger.error(CLI_MESSAGES['ArgumentsMutualExclusive'].format("'-a' / '--query-all'", "'-v' / '--query-values'"))
            Logger.info(CLI_MESSAGES['TryHelp'], stress = False, force=True)
            exit(1)


    def print_result(result):
        if not len(result['Parameters']): return
        if format == 'shell':
            if query_values:
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
            if query_all:
                keys = list(result['Parameters'][0].keys())
                if len(keys): print(','.join(keys), flush=True)
                for item in result['Parameters']:
                    values = list(item.values())
                    print(','.join(values), flush=True)
            elif query_values:
                print('Key,Value', flush=True)
                for item in result['Parameters']:
                    key = item['Key']
                    value = item['Value']
                    print(f"{key},{value}", flush=True)
            else:
                for item in result['Parameters']:
                    key = item['Key']
                    print(f"{key}", flush=True)
        elif format == 'text':
            if query_all:
                keys = list(result['Parameters'][0].keys())
                if len(keys): print('\t'.join(keys), flush=True)
                for item in result['Parameters']:
                    values = list(item.values())
                    print('\t'.join(values), flush=True)
            elif query_values:
                print('Key\tValue', flush=True)
                for item in result['Parameters']:
                    key = item['Key']
                    value = item['Value']
                    print(f"{key}\t{value}", flush=True)
            else:
                for item in result['Parameters']:
                    key = item['Key']
                    print(f"{key}", flush=True)
        elif format in ['json', 'yaml']:
            if query:
                jmespathQuery = query
            else:
                if query_all:
                    jmespathQuery = '{Parameters: Parameters[*].{'
                    keys = list(result['Parameters'][0].keys())
                    for i in range(0, len(keys)-1):
                        jmespathQuery += f"{keys[i]}: {keys[i]},"
                    if len(keys):
                        jmespathQuery += f"{keys[len(keys)-1]}: {keys[len(keys)-1]}"
                    jmespathQuery += '}}'
                else:
                    jmespathQuery = '{Parameters: Parameters[*].{Key: Key'
                    if query_values:
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

@parameter.command('get', context_settings=DEFAULT_CLICK_CONTEXT, short_help=f"{CLI_COMMANDS_SHORT_HELP['parameter']['get']}")
@command_doc(CLI_COMMANDS_HELP['parameter']['get'])
@click.argument('key', required=False)
@click.option('-k', '--key', 'key_option', required=False, metavar='<key>', help=f"{CLI_PARAMETERS_HELP['parameter']['key']}")
@click.option('-s', '--stage', metavar='<name>[/<number>]', default='default', help=f"{CLI_PARAMETERS_HELP['common']['stage']}")
@click.option('-b', '--verbosity', metavar='<number>', required=False, type=RangeParamType(click.INT, minimum=0, maximum=5), default='2', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['verbosity']}")
@click.option('--config', metavar='<key>=<value>,...', required=False, help=f"{CLI_PARAMETERS_HELP['common']['config']}")
@click.option('-w','--working-dir', metavar='<path>', type=click.Path(exists=True, file_okay=False), required=False, default='.', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['working_dir']}")
def get_parameter(stage, key, key_option, working_dir, config, verbosity):

    def check_command_usage():
        nonlocal stage, key
        stage = Stages.normalize(stage)
        if key and key_option:
            Logger.error(CLI_MESSAGES['ArgumentsMutualExclusive'].format("'key'", "'-k' / '--key'"))
            Logger.info(CLI_MESSAGES['TryHelp'], stress = False, force=True)
            exit(1)

        key = key or key_option

        if not key:
            Logger.error(CLI_MESSAGES['MissingArgument'].format("'KEY'"))
            Logger.info(CLI_MESSAGES['TryHelp'], stress = False, force=True)
            exit(1)

    try:
        Logger.set_verbosity(verbosity)
        check_command_usage()
        Config.load(working_dir if working_dir else os.getcwd(), config)
        print(Parameters.get(stage, key), flush=True)
    
    except DSOException as e:
        Logger.error(e.message)
    except Exception as e:
        msg = getattr(e, 'message', getattr(e, 'msg', str(e)))
        Logger.critical(msg)
        if verbosity >= log_levels['full']:
            raise

###--------------------------------------------------------------------------------------------

@parameter.command('delete', context_settings=DEFAULT_CLICK_CONTEXT, short_help=f"{CLI_COMMANDS_SHORT_HELP['parameter']['delete']}")
@command_doc(CLI_COMMANDS_HELP['parameter']['delete'])
@click.argument('key', required=False)
@click.option('-k', '--key', 'key_option', metavar='<key>', required=False, help=f"{CLI_PARAMETERS_HELP['parameter']['key']}")
@click.option('-s', '--stage', default='', metavar='<name>[/<number>]', help=f"{CLI_PARAMETERS_HELP['common']['stage']}")
@click.option('-i', '--input', metavar='<path>', required=False, type=click.File(encoding='utf-8', mode='r'), help=f"{CLI_PARAMETERS_HELP['common']['input']}")
@click.option('-f', '--format', required=False, type=click.Choice(['shell','json', 'yaml','text', 'csv']), default='shell', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['format']}")
@click.option('-b', '--verbosity', metavar='<number>', required=False, type=RangeParamType(click.INT, minimum=0, maximum=5), default='2', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['verbosity']}")
@click.option('--config', metavar='<key>=<value>,...', required=False, help=f"{CLI_PARAMETERS_HELP['common']['config']}")
@click.option('-w','--working-dir', metavar='<path>', type=click.Path(exists=True, file_okay=False), required=False, default='.', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['working_dir']}")
def delete_parameter(key, key_option, input, format, stage, working_dir, config, verbosity):

    parameters = []

    def check_command_usage():
        nonlocal stage, parameters, key, key_option
        stage = Stages.normalize(stage)
        if input:
            if key or key_option:
                Logger.error(CLI_MESSAGES['ArgumentsMutualExclusive'].format("'-k' / '--key'","'-i' / '--input'"))
                Logger.info(CLI_MESSAGES['TryHelp'], stress = False, force=True)
                exit(1)
            if format == 'json':
                try:
                    parameters = json.load(input)['Parameters']
                # except json.JSONDecodeError as e:
                except:
                    Logger.error(CLI_MESSAGES['InvalidFileFormat'].format(format))
                    exit(1)
            elif format == 'yaml':
                try:
                    parameters = yaml.load(input, yaml.SafeLoader)['Parameters']
                # except yaml.YAMLError as e:
                except:
                    Logger.error(CLI_MESSAGES['InvalidFileFormat'].format(format))
                    exit(1)
            elif format == 'shell':
                _parameters = input.readlines()
                try:
                    for param in _parameters:
                        _key = param.split('=', 1)[0].strip()
                        # _value = param.split('=', 1)[1].strip()
                        parameters.append({'Key': _key})

                except:
                    Logger.error(CLI_MESSAGES['InvalidFileFormat'].format(format))
                    exit(1)
            elif format == 'csv':
                try:
                    _parameters = list(csv.reader(input))
                    if not len(_parameters): return
                except:
                    Logger.error(CLI_MESSAGES['InvalidFileFormat'].format(format))
                    exit(1)

                ### No header is assumed for single field CSV files
                if len(_parameters[0]) > 1:
                    header = _parameters[0]
                    if not header[0].strip() == 'Key':
                        raise DSOException(CLI_MESSAGES['MissingCSVField'].format("Key"))
                    _parameters.pop(0)

                for parameter in _parameters:
                    _key = parameter[0].strip()
                    parameters.append({'Key': _key})

            elif format == 'text':
                _parameters = input.readlines()
                try:
                    if len(_parameters):
                        if '\t' in _parameters[0]:
                            header = _parameters[0]
                            Key = header.split('\t')[0].strip()
                            _parameters.pop(0)
                        else:
                            Key = 'Key'
                        for parameter in _parameters:
                            _key = parameter.split('\t')[0].strip()
                            parameters.append({Key: _key})

                except:
                    Logger.error(CLI_MESSAGES['InvalidFileFormat'].format(format))
                    exit(1)
            # for param in parameters:
            #     Parameters.validate_key(param['Key'])



        ### not input
        else:
            if key and key_option:
                Logger.error(CLI_MESSAGES['ArgumentsMutualExclusive'].format("'key'", "'-k' / '--key'"))
                Logger.info(CLI_MESSAGES['TryHelp'], stress = False, force=True)
                exit(1)
    
            key = key or key_option

            if not key:
                Logger.error(CLI_MESSAGES['AtleastOneofTwoNeeded'].format("'-k' / '--key'","'-i' / '--input'"))
                Logger.info(CLI_MESSAGES['TryHelp'], stress = False, force=True)
                exit(1)

            # Parameters.validate_key(key) 

            parameters.append({'Key': key})



        # invalid = False
        # for param in parameters:
        #     invalid = not Parameters.validate_key(param['Key']) or invalid

        # if invalid:
        #     Logger.info(CLI_MESSAGES['TryHelp'], stress = False, force=True)
        #     exit(1)


    try:
        Logger.set_verbosity(verbosity)
        check_command_usage()
        Config.load(working_dir if working_dir else os.getcwd(), config)

        result = []
        for param in parameters:
            result.append(Parameters.delete(stage, param['Key']))

    except DSOException as e:
        Logger.error(e.message)
    except Exception as e:
        msg = getattr(e, 'message', getattr(e, 'msg', str(e)))
        Logger.critical(msg)
        if verbosity >= log_levels['full']:
            raise
    finally:
        print_list(result)

###--------------------------------------------------------------------------------------------
###--------------------------------------------------------------------------------------------
###--------------------------------------------------------------------------------------------

@secret.command('list', context_settings=DEFAULT_CLICK_CONTEXT, short_help=f"{CLI_COMMANDS_SHORT_HELP['secret']['list']}")
@command_doc(CLI_COMMANDS_HELP['secret']['list'])
@click.option('-s', '--stage', 'stage', metavar='<name>[/<number>]', default='default', help=f"{CLI_PARAMETERS_HELP['common']['stage']}")
@click.option('-u','--uninherited', 'uninherited', is_flag=True, default=False, help=f"{CLI_PARAMETERS_HELP['secret']['uninherited']}")
@click.option('-f', '--format', required=False, type=click.Choice(['shell','json', 'yaml', 'text', 'csv']), default='shell', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['format']}")
@click.option('-v', '--query-values', required=False, is_flag=True, default=False, show_default=True, help=f"{CLI_PARAMETERS_HELP['parameter']['query_values']}")
@click.option('-a', '--query-all', required=False, is_flag=True, default=False, show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['query_all']}")
@click.option('-q', '--query', metavar='<jmespath>', required=False, help=f"{CLI_PARAMETERS_HELP['common']['query']}")
@click.option('-d', '--decrypt', required=False, is_flag=True, default=False, show_default=True, help=f"{CLI_PARAMETERS_HELP['parameter']['query_values']}")
@click.option('-b', '--verbosity', metavar='<number>', required=False, type=RangeParamType(click.INT, minimum=0, maximum=5), default='2', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['verbosity']}")
@click.option('--config', metavar='<key>=<value>,...', required=False, help=f"{CLI_PARAMETERS_HELP['common']['config']}")
@click.option('-w','--working-dir', metavar='<path>', type=click.Path(exists=True, file_okay=False), required=False, default='.', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['working_dir']}")
def list_secret(stage, uninherited, decrypt, query_values, query_all, query, format, working_dir, config, verbosity):

    def check_command_usage():
        nonlocal stage
        stage = Stages.normalize(stage)

        if query:
            try:
                jmespath.compile(query)
            except jmespath.exceptions.ParseError as e:
                raise DSOException(f"Invalid JMESPath query '{query}': {e.msg}")

        if query and not format in ['json', 'yaml']:
            Logger.error(CLI_MESSAGES['QueryOptionCompatibleFormats'])
            Logger.info(CLI_MESSAGES['TryHelp'], stress = False, force=True)
            exit(1)

        if query_all and format == 'shell':
            Logger.error(CLI_MESSAGES['QueryAllOptionNonCompatibleFormats'])
            Logger.info(CLI_MESSAGES['TryHelp'], stress = False, force=True)
            exit(1)

        if query and query_all:
            Logger.error(CLI_MESSAGES['ArgumentsMutualExclusive'].format("'-q' / '--query'", "'-a' / '--query-all'"))
            Logger.info(CLI_MESSAGES['TryHelp'], stress = False, force=True)
            exit(1)

        if query and query_values:
            Logger.error(CLI_MESSAGES['ArgumentsMutualExclusive'].format("'-q' / '--query'", "'-v' / '--query-values'"))
            Logger.info(CLI_MESSAGES['TryHelp'], stress = False, force=True)
            exit(1)

        if query_all and query_values:
            Logger.error(CLI_MESSAGES['ArgumentsMutualExclusive'].format("'-a' / '--query-all'", "'-v' / '--query-values'"))
            Logger.info(CLI_MESSAGES['TryHelp'], stress = False, force=True)
            exit(1)

        if decrypt:
            if not (query_values or query_all or query):
                Logger.error(CLI_MESSAGES['ArgumentsMutualInclusive'].format("Either '-v' / '--query-values' or '-a' / '--query-all' or '-q' / '--query'", "'-d' / '--decrypt'"))
                Logger.info(CLI_MESSAGES['TryHelp'], stress = False, force=True)
                exit(1)


    def print_result(result):
        if not len(result['Secrets']): return
        if format == 'shell':
            if query_values:
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
                    p = subprocess.Popen(default_pager.split(' ') + [f.name])
                    p.wait()
                if not f == sys.stdout: f.close()
            else:
                for item in result['Secrets']:
                    key = item['Key']
                    print(f"{key}", flush=True)
        elif format == 'csv':
            if query_all:
                f = tempfile.NamedTemporaryFile("w") if decrypt else sys.stdout
                keys = list(result['Secrets'][0].keys())
                if len(keys): f.write(','.join(keys)+'\n')
                for item in result['Secrets']:
                    values = list(item.values())
                    f.write(','.join(values)+'\n')
                f.flush()
                if decrypt: 
                    p = subprocess.Popen(default_pager.split(' ') + [f.name])
                    p.wait()
                if not f == sys.stdout: f.close()
            elif query_values:
                f = tempfile.NamedTemporaryFile("w") if decrypt else sys.stdout
                f.write('Key,Value\n')
                for item in result['Secrets']:
                    key = item['Key']
                    value = item['Value']
                    f.write(f"{key},{value}\n")
                f.flush()
                if decrypt: 
                    p = subprocess.Popen(default_pager.split(' ') + [f.name])
                    p.wait()
                if not f == sys.stdout: f.close()
            else:
                for item in result['Secrets']:
                    key = item['Key']
                    f.write(f"{key}")
        elif format == 'text':
            if query_all:
                f = tempfile.NamedTemporaryFile("w") if decrypt else sys.stdout
                keys = list(result['Secrets'][0].keys())
                if len(keys): f.write('\t'.join(keys)+'\n')
                for item in result['Secrets']:
                    values = list(item.values())
                    f.write('\t'.join(values)+'\n')
                f.flush()
                if decrypt: 
                    p = subprocess.Popen(default_pager.split(' ') + [f.name])
                    p.wait()
                if not f == sys.stdout: f.close()
            elif query_values:
                f = tempfile.NamedTemporaryFile("w") if decrypt else sys.stdout
                f.write('Key\tValue\n')
                for item in result['Secrets']:
                    key = item['Key']
                    value = item['Value']
                    f.write(f"{key}\t{value}\n")
                f.flush()
                if decrypt: 
                    p = subprocess.Popen(default_pager.split(' ') + [f.name])
                    p.wait()
                if not f == sys.stdout: f.close()
            else:
                for item in result['Secrets']:
                    key = item['Key']
                    f.write(f"{key}")
        elif format in ['json', 'yaml']:
            if query:
                jmespathQuery = query
            else:
                if query_all:
                    jmespathQuery = '{Secrets: Secrets[*].{'
                    keys = list(result['Secrets'][0].keys())
                    for i in range(0, len(keys)-1):
                        jmespathQuery += f"{keys[i]}: {keys[i]},"
                    if len(keys):
                        jmespathQuery += f"{keys[len(keys)-1]}: {keys[len(keys)-1]}"
                    jmespathQuery += '}}'
                else:
                    jmespathQuery = '{Secrets: Secrets[*].{Key: Key'
                    if query_values:
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
                p = subprocess.Popen(default_pager.split(' ') + [f.name])
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

@secret.command('get', context_settings=DEFAULT_CLICK_CONTEXT, short_help=f"{CLI_COMMANDS_SHORT_HELP['secret']['get']}")
@command_doc(CLI_COMMANDS_HELP['secret']['get'])
@click.argument('key', required=False)
@click.option('-s', '--stage', metavar='<name>[/<number>]', default='default', help=f"{CLI_PARAMETERS_HELP['common']['stage']}")
@click.option('-k', '--key', 'key_option', required=False, metavar='<key>', help=f"{CLI_PARAMETERS_HELP['parameter']['key']}")
@click.option('-b', '--verbosity', metavar='<number>', required=False, type=RangeParamType(click.INT, minimum=0, maximum=5), default='2', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['verbosity']}")
@click.option('--config', metavar='<key>=<value>,...', required=False, help=f"{CLI_PARAMETERS_HELP['common']['config']}")
@click.option('-w','--working-dir', metavar='<path>', type=click.Path(exists=True, file_okay=False), required=False, default='.', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['working_dir']}")
def get_secret(stage, key, key_option, working_dir, config, verbosity):

    def check_command_usage():
        nonlocal stage, key, key_option
        stage = Stages.normalize(stage)
        if key and key_option:
            Logger.error(CLI_MESSAGES['ArgumentsMutualExclusive'].format("'key'", "'-k' / '--key'"))
            Logger.info(CLI_MESSAGES['TryHelp'], stress = False, force=True)
            exit(1)

        key = key or key_option

        if not key:
            Logger.error(CLI_MESSAGES['MissingArgument'].format("'KEY'"))
            Logger.info(CLI_MESSAGES['TryHelp'], stress = False, force=True)
            exit(1)

    def print_result(output):
        with tempfile.NamedTemporaryFile("w") as f:
            f.write(str(output))
            f.flush()
            p = subprocess.Popen(default_pager.split(' ') + [f.name])
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

@secret.command('add', context_settings=DEFAULT_CLICK_CONTEXT, short_help=f"{CLI_COMMANDS_SHORT_HELP['secret']['add']}")
@command_doc(CLI_COMMANDS_HELP['secret']['add'])
@click.argument('key', required=False)
@click.option('-s', '--stage', metavar='<name>[/<number>]', default='default', help=f"{CLI_PARAMETERS_HELP['common']['stage']}")
@click.option('-k', '--key', 'key_option', required=False, metavar='<key>', help=f"{CLI_PARAMETERS_HELP['secret']['key']}")
@click.option('-i', '--input', metavar='<path>', required=False, type=click.File(encoding='utf-8', mode='r'), help=f"{CLI_PARAMETERS_HELP['common']['input']}")
@click.option('-f', '--format', required=False, type=click.Choice(['shell','json', 'yaml', 'text', 'csv']), default='shell', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['format']}")
@click.option('-b', '--verbosity', metavar='<number>', required=False, type=RangeParamType(click.INT, minimum=0, maximum=5), default='2', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['verbosity']}")
@click.option('--config', metavar='<key>=<value>,...', required=False, help=f"{CLI_PARAMETERS_HELP['common']['config']}")
@click.option('-w','--working-dir', metavar='<path>', type=click.Path(exists=True, file_okay=False), required=False, default='.', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['working_dir']}")
def add_secret(stage, key, key_option, input, format, working_dir, config, verbosity):

    secrets = []

    def check_command_usage():
        nonlocal stage, secrets, key
        stage = Stages.normalize(stage)
        if input:
            if key or key_option:
                Logger.error(CLI_MESSAGES['ArgumentsMutualExclusive'].format("'-k' / '--key'","'-i' / '--input'"))
                Logger.info(CLI_MESSAGES['TryHelp'], stress = False, force=True)
                exit(1)
            if format == 'json':
                try:
                    secrets = json.load(input)['Secrets']
                # except json.JSONDecodeError as e:
                except:
                    Logger.error(CLI_MESSAGES['InvalidFileFormat'].format(format))
                    exit(1)
            elif format == 'yaml':
                try:
                    secrets = yaml.load(input, yaml.SafeLoader)['Secrets']
                # except yaml.YAMLError as e:
                except:
                    Logger.error(CLI_MESSAGES['InvalidFileFormat'].format(format))
                    exit(1)
            elif format == 'csv':
                try:
                    _secrets = list(csv.reader(input))
                    if not len(_secrets): return
                except:
                    Logger.error(CLI_MESSAGES['InvalidFileFormat'].format(format))
                    exit(1)

                header = _secrets[0]
                if len(header) < 2:
                    raise DSOException(CLI_MESSAGES['InvalidFileFormat'].format(format))
                if not header[0].strip() == 'Key':
                    raise DSOException(CLI_MESSAGES['MissingCSVField'].format("Key"))
                if not header[1].strip() == 'Value':
                    raise DSOException(CLI_MESSAGES['MissingCSVField'].format("Value"))

                for secret in _secrets[1:]:
                    _key = secret[0].strip()
                    _value = secret[1].strip()
                    secrets.append({'Key': _key, 'Value': _value})

            elif format == 'text':
                _secrets = input.readlines()
                try:
                    if len(_secrets):
                        header = _secrets[0]
                        Key = header.split('\t')[0].strip()
                        Value = header.split('\t')[1].strip()
                        for secret in _secrets[1:]:
                            _key = secret.split('\t')[0].strip()
                            _value = secret.split('\t')[1].strip()
                            secrets.append({Key: _key, Value: _value})
                except:
                    Logger.error(CLI_MESSAGES['InvalidFileFormat'].format(format))
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
                    Logger.error(CLI_MESSAGES['InvalidFileFormat'].format(format))
                    exit(1)
                
        ### not input
        else:
            if key and key_option:
                Logger.error(CLI_MESSAGES['ArgumentsOrOption'].format("Secert key", "'KEY'", "'-k' / '--key'"))
                Logger.info(CLI_MESSAGES['TryHelp'], stress = False, force=True)
                exit(1)
    
            key = key or key_option

            if not key:
                Logger.error(CLI_MESSAGES['AtleastOneofTwoNeeded'].format("'-k' / '--key'","'-i' / '--input'"))
                Logger.info(CLI_MESSAGES['TryHelp'], stress = False, force=True)
                exit(1)

            # if not value:
            #     Logger.error(CLI_MESSAGES['MissingOption'].format("'-v' / '--value'"))
            #     Logger.info(CLI_MESSAGES['TryHelp'], stress = False, force=True)
            #     exit(1)

            Secrets.validate_key(key)
                
            value = getpass("Enter secret value: ")
            value2 = getpass("Verify secret value: ")
            if not value == value2:
                Logger.error(CLI_MESSAGES['EnteredSecretValuesNotMatched'].format(format))
                exit(1)

            secrets.append({'Key': key, 'Value': value})

    try:
        Logger.set_verbosity(verbosity)
        check_command_usage()
        Config.load(working_dir if working_dir else os.getcwd(), config)

        result = []
        for secret in secrets:
            key = secret['Key']
            value = secret['Value']
            # Secrets.validate_key(secret['Key'])
            result.append(Secrets.add(stage, key, value))

    except DSOException as e:
        Logger.error(e.message)
    except Exception as e:
        msg = getattr(e, 'message', getattr(e, 'msg', str(e)))
        Logger.critical(msg)
        if verbosity >= log_levels['full']:
            raise
    finally:
        print_list(result)

###--------------------------------------------------------------------------------------------

@secret.command('delete', context_settings=DEFAULT_CLICK_CONTEXT, short_help=f"{CLI_COMMANDS_SHORT_HELP['secret']['delete']}")
@command_doc(CLI_COMMANDS_HELP['secret']['delete'])
@click.argument('key', required=False)
@click.option('-s', '--stage', metavar='<name>[/<number>]', default='default', help=f"{CLI_PARAMETERS_HELP['common']['stage']}")
@click.option('-k', '--key', 'key_option', metavar='<key>', required=False, help=f"{CLI_PARAMETERS_HELP['secret']['key']}")
@click.option('-i', '--input', metavar='<path>', required=False, type=click.File(encoding='utf-8', mode='r'), help=f"{CLI_PARAMETERS_HELP['common']['input']}")
@click.option('-f', '--format', required=False, type=click.Choice(['shell','json', 'yaml', 'text', 'csv']), default='shell', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['format']}")
@click.option('-b', '--verbosity', metavar='<number>', required=False, type=RangeParamType(click.INT, minimum=0, maximum=5), default='2', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['verbosity']}")
@click.option('--config', metavar='<key>=<value>,...', required=False, help=f"{CLI_PARAMETERS_HELP['common']['config']}")
@click.option('-w','--working-dir', metavar='<path>', type=click.Path(exists=True, file_okay=False), required=False, default='.', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['working_dir']}")
def delete_secret(key, key_option, input, format, stage, working_dir, config, verbosity):

    secrets = []

    def check_command_usage():
        nonlocal stage, secrets, key, key_option
        stage = Stages.normalize(stage)
        if input:
            if key or key_option:
                Logger.error(CLI_MESSAGES['ArgumentsMutualExclusive'].format("'-k' / '--key'","'-i' / '--input'"))
                Logger.info(CLI_MESSAGES['TryHelp'], stress = False, force=True)
                exit(1)
            if format == 'json':
                try:
                    secrets = json.load(input)['Secrets']
                # except json.JSONDecodeError as e:
                except:
                    Logger.error(CLI_MESSAGES['InvalidFileFormat'].format(format))
                    exit(1)
            elif format == 'yaml':
                try:
                    secrets = yaml.load(input, yaml.SafeLoader)['Secrets']
                # except yaml.YAMLError as e:
                except:
                    Logger.error(CLI_MESSAGES['InvalidFileFormat'].format(format))
                    exit(1)
            elif format == 'shell':
                _secrets = input.readlines()
                try:
                    for secret in _secrets:
                        _key = secret.split('=', 1)[0].strip()
                        # _value = secret.split('=', 1)[1].strip()
                        secrets.append({'Key': _key})
                except:
                    Logger.error(CLI_MESSAGES['InvalidFileFormat'].format(format))
                    exit(1)
            elif format == 'csv':
                try:
                    _secrets = list(csv.reader(input))
                    if not len(_secrets): return
                except:
                    Logger.error(CLI_MESSAGES['InvalidFileFormat'].format(format))
                    exit(1)

                ### No header is assumed for single field CSV files
                if len(_secrets[0]) > 1:
                    header = _secrets[0]
                    if not header[0].strip() == 'Key':
                        raise DSOException(CLI_MESSAGES['MissingCSVField'].format("Key"))
                    _secrets.pop(0)

                for secret in _secrets:
                    _key = secret[0].strip()
                    secrets.append({'Key': _key})

            elif format == 'text':
                _secrets = input.readlines()
                try:
                    if len(_secrets):
                        if '\t' in _secrets[0]:
                            header = _secrets[0]
                            Key = header.split('\t')[0].strip()
                            _secrets.pop(0)
                        else:
                            Key = 'Key'
                        for secret in _secrets:
                            _key = secret.split('\t')[0].strip()
                            secrets.append({Key: _key})
                except:
                    Logger.error(CLI_MESSAGES['InvalidFileFormat'].format(format))
                    exit(1)

            # for secret in secrets:
            #     Secrets.validate_key(secret['Key'])

        ### not input
        else:
            if key and key_option:
                Logger.error(CLI_MESSAGES['ArgumentsMutualExclusive'].format("'key'", "'-k' / '--key'"))
                Logger.info(CLI_MESSAGES['TryHelp'], stress = False, force=True)
                exit(1)
    
            key = key or key_option

            if not key:
                Logger.error(CLI_MESSAGES['AtleastOneofTwoNeeded'].format("'-k' / '--key'","'-i' / '--input'"))
                Logger.info(CLI_MESSAGES['TryHelp'], stress = False, force=True)
                exit(1)

            secrets.append({'Key': key})

        # invalid = False
            # Secrets.validate_key(key)

        # if invalid:
        #     Logger.info(CLI_MESSAGES['TryHelp'], stress = False, force=True)
        #     exit(1)

    try:
        Logger.set_verbosity(verbosity)
        check_command_usage()
        Config.load(working_dir if working_dir else os.getcwd(), config)

        result = []
        for secret in secrets:
            result.append(Secrets.delete(stage, secret['Key']))

    except DSOException as e:
        Logger.error(e.message)
    except Exception as e:
        msg = getattr(e, 'message', getattr(e, 'msg', str(e)))
        Logger.critical(msg)
        if verbosity >= log_levels['full']:
            raise
    finally:
        print_list(result)

###--------------------------------------------------------------------------------------------
###--------------------------------------------------------------------------------------------
###--------------------------------------------------------------------------------------------

@template.command('list', context_settings=DEFAULT_CLICK_CONTEXT, short_help=f"{CLI_COMMANDS_SHORT_HELP['template']['list']}")
@click.option('-r', '--query-render-path', 'query_render_path', required=False, is_flag=True, default=False, show_default=True, help=f"{CLI_PARAMETERS_HELP['template']['query_render_path']}")
@click.option('-f', '--format', required=False, type=click.Choice(['json', 'yaml', 'text', 'csv']), default='text', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['format']}")
@click.option('-b', '--verbosity', metavar='<number>', required=False, type=RangeParamType(click.INT, minimum=0, maximum=5), default='2', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['verbosity']}")
@click.option('--config', metavar='<key>=<value>,...', required=False, help=f"{CLI_PARAMETERS_HELP['common']['config']}")
@click.option('-w','--working-dir', metavar='<path>', type=click.Path(exists=True, file_okay=False), required=False, default='.', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['working_dir']}")
def list_template(query_render_path, format, working_dir, config, verbosity):
    """
    Return the list of templates added to the application.\n
    """
    def check_command_usage():
        pass

    def print_result(templates):
        if query_render_path:
            if format == 'csv':
                if len(templates): print("Key,RenderTo", flush=True)
                for template in templates:
                    print(f"{template['Key']},{template['RenderTo']}", flush=True)
            if format == 'text':
                if len(templates): print("Key\tRenderTo", flush=True)
                for template in templates:
                    print(f"{template['Key']}\t{template['RenderTo']}", flush=True)
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
            elif format == 'text':
                # if len(templates): print("Key", flush=True)
                for item in templates:
                    print(f"{item['Key']}", flush=True)
            elif format == 'json':
                print(json.dumps({'Templates' : [x['Key'] for x in templates]}, sort_keys=False, indent=2), flush=True)
            elif format == 'yaml':
                print(yaml.dump({'Templates' : [x['Key'] for x in templates]}, sort_keys=False, indent=2), flush=True)

    try:
        Logger.set_verbosity(verbosity)
        check_command_usage()
        Config.load(working_dir if working_dir else os.getcwd(), config)
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

@template.command('get', context_settings=DEFAULT_CLICK_CONTEXT, short_help=f"{CLI_COMMANDS_SHORT_HELP['template']['get']}")
@click.argument('key', required=False)
@click.option('-k', '--key', 'key_option', metavar='<key>', required=False, help=f"{CLI_PARAMETERS_HELP['template']['key']}")
@click.option('-b', '--verbosity', metavar='<number>', required=False, type=RangeParamType(click.INT, minimum=0, maximum=5), default='2', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['verbosity']}")
@click.option('--config', metavar='<key>=<value>,...', required=False, help=f"{CLI_PARAMETERS_HELP['common']['config']}")
@click.option('-w','--working-dir', metavar='<path>', type=click.Path(exists=True, file_okay=False), required=False, default='.', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['working_dir']}")
def get_template(key, key_option, working_dir, config, verbosity):
    """
    Return the content of a template.\n
    \tKEY: The key of the template. It may also be provided using the '--key' option.\n
    """

    def check_command_usage():
        nonlocal key, key_option
        if key and key_option:
            Logger.error(CLI_MESSAGES['ArgumentsOrOption'].format("Template key", "'KEY'", "'-k' / '--key'"))
            Logger.info(CLI_MESSAGES['TryHelp'], stress = False, force=True)
            exit(1)

        key = key or key_option

        if not key:
            Logger.error(CLI_MESSAGES['MissingOption'].format("'KEY"))
            Logger.info(CLI_MESSAGES['TryHelp'], stress = False, force=True)
            exit(1)

        # if not Templates.validate_key(key):
        #     Logger.info(CLI_MESSAGES['TryHelp'], stress = False, force=True)
        #     exit(1)


    try:
        Logger.set_verbosity(verbosity)
        check_command_usage()
        Config.load(working_dir if working_dir else os.getcwd(), config)
        print(Templates.get(key), flush=True)
    
    except DSOException as e:
        Logger.error(e.message)
    except Exception as e:
        msg = getattr(e, 'message', getattr(e, 'msg', str(e)))
        Logger.critical(msg)
        if verbosity >= log_levels['full']:
            raise

###--------------------------------------------------------------------------------------------

@template.command('add', context_settings=DEFAULT_CLICK_CONTEXT, short_help=f"{CLI_COMMANDS_SHORT_HELP['template']['add']}")
@click.argument('key', required=False)
@click.option('-k', '--key', 'key_option', metavar='<key>', required=False, help=f"{CLI_PARAMETERS_HELP['template']['key']}")
@click.option('-r', '--render-path', default='.', show_default=True, metavar='<path>', required=False, help=f"{CLI_PARAMETERS_HELP['template']['render_path']}")
# @click.option('-i', '--input', metavar='<path>', required=True, type=click.File(encoding='utf-8', mode='r'), help=f"{CLI_PARAMETERS_HELP['template']['input']}")
@click.option('-i', '--input', metavar='<path>', required=True, type=click.Path(exists=True, file_okay=True, dir_okay=True), help=f"{CLI_PARAMETERS_HELP['template']['input']}")
# @click.option('-i', '--input', metavar='<path>', required=True, help=f"{CLI_PARAMETERS_HELP['template']['input']}")
@click.option('--recursive', required=False, is_flag=True, help=f"{CLI_PARAMETERS_HELP['template']['recursive']}")
@click.option('-b', '--verbosity', metavar='<number>', required=False, type=RangeParamType(click.INT, minimum=0, maximum=5), default='2', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['verbosity']}")
@click.option('--config', metavar='<key>=<value>,...', required=False, help=f"{CLI_PARAMETERS_HELP['common']['config']}")
@click.option('-w','--working-dir', metavar='<path>', type=click.Path(exists=True, file_okay=False), required=False, default='.', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['working_dir']}")
def add_template(key, key_option, render_path, input, recursive, working_dir, config, verbosity):
    """
    Add a template to the application, or update it if already existing.\n
    \tKEY: The key of the template. It may also be provided using the '--key' option.\n
    """


    templates = []

    def process_key_from_path(_path):
        if not key or key in ['.' , './']:
            return _path[len(input)+1:]

        result = key
        ### if **/ exist in key, replace it with _path dirname
        print(os.path.dirname(_path)[len(input)+1:])
        if os.path.dirname(_path)[len(input):]:
            result = result.replace('**', os.path.dirname(_path)[len(input)+1:])
        else:
            result = result.replace(f'**{os.sep}', '')
            result = result.replace('**', '')
        result = result.replace('*', os.path.basename(_path))
        result = result.replace(f"{os.sep}{os.sep}", os.sep)

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
                result = re.sub(os.sep + r'[*][*]', '', render_path)
            result = re.sub(r'[*]', os.path.basename(_key), result)

        return result


    def check_command_usage():
        nonlocal templates, input, key, render_path

        if key and key_option:
            Logger.error(CLI_MESSAGES['ArgumentsOrOption'].format("Template key", "'KEY'", "'-k' / '--key'"))
            Logger.info(CLI_MESSAGES['TryHelp'], stress = False, force=True)
            exit(1)

        key = key or key_option

        if os.path.isdir(input):
            ### remove possible trailing /
            input = re.sub(f'{os.sep}$', '', input)
            if recursive:
                globe =  f'{os.sep}**'
            else:
                globe = f'{os.sep}*'
            path = input + globe
        else:
            path = input

        for item in glob.glob(path, recursive=recursive):
            if not Path(item).is_file(): continue
            if is_file_binary(item):
                Logger.warn(f"Binary file '{item}' ignored.")
                continue
            _path = str(item)
            _key = process_key_from_path(_path)

            _render_path = process_render_path_from_key(_key)
            templates.append({'Path': _path, 'Key': _key, 'RenderPath': _render_path})

    try:
        Logger.set_verbosity(verbosity)
        check_command_usage()
        Config.load(working_dir if working_dir else os.getcwd(), config)
        result = []
        for template in templates:
            # if not Templates.validate_key(template['Key']):
            #     Logger.info(CLI_MESSAGES['TryHelp'], stress = False, force=True)
            #     exit(1)
            result.append(Templates.add(template['Key'], open(template['Path'], encoding='utf-8', mode='r').read(), template['RenderPath']))

    except DSOException as e:
        Logger.error(e.message)
    except Exception as e:
        msg = getattr(e, 'message', getattr(e, 'msg', str(e)))
        Logger.critical(msg)
        if verbosity >= log_levels['full']:
            raise
    finally:
        print_list(result)

###--------------------------------------------------------------------------------------------

@template.command('delete', context_settings=DEFAULT_CLICK_CONTEXT, short_help=f"{CLI_COMMANDS_SHORT_HELP['template']['delete']}")
@click.argument('key', required=False)
@click.option('-k', '--key', 'key_option', metavar='<key>', required=False, help=f"{CLI_PARAMETERS_HELP['template']['key']}")
@click.option('-i', '--input', metavar='<path>', required=False, type=click.File(encoding='utf-8', mode='r'), help=f"{CLI_PARAMETERS_HELP['common']['input']}")
@click.option('--recursive', required=False, is_flag=True, help=f"{CLI_PARAMETERS_HELP['template']['recursive']}")
@click.option('-f', '--format', required=False, type=click.Choice(['json', 'yaml', 'text', 'csv']), default='csv', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['format']}")
@click.option('-b', '--verbosity', metavar='<number>', required=False, type=RangeParamType(click.INT, minimum=0, maximum=5), default='2', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['verbosity']}")
@click.option('--config', metavar='<key>=<value>,...', required=False, help=f"{CLI_PARAMETERS_HELP['common']['config']}")
@click.option('-w','--working-dir', metavar='<path>', type=click.Path(exists=True, file_okay=False), required=False, default='.', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['working_dir']}")
def delete_template(key, key_option, input, recursive, format, working_dir, config, verbosity):
    """
    Delete a template from the application.\n
    \tKEY: The key of the template. It may also be provided using the '--key' option.\n
    \nTip: Multiple templates may be deleted at once using the '--input' option.
    """

    templates = []

    def check_command_usage():
        nonlocal templates, key
        if input:
            if key or key_option:
                Logger.error(CLI_MESSAGES['ArgumentsMutualExclusive'].format("'-k' / '--key'","'-i' / '--input'"))
                Logger.info(CLI_MESSAGES['TryHelp'], stress = False, force=True)
                exit(1)

            if format == 'json':
                try:
                    templates = json.load(input)['Templates']
                # except json.JSONDecodeError as e:
                except:
                    Logger.error(CLI_MESSAGES['InvalidFileFormat'].format(format))
                    exit(1)
            elif format == 'yaml':
                try:
                    templates = yaml.load(input, yaml.SafeLoader)['Templates']
                # except yaml.YAMLError as e:
                except:
                    Logger.error(CLI_MESSAGES['InvalidFileFormat'].format(format))
                    exit(1)
            elif format == 'csv':
                try:
                    _templates = list(csv.reader(input))
                    if not len(_templates): return
                except:
                    Logger.error(CLI_MESSAGES['InvalidFileFormat'].format(format))
                    exit(1)

                ### No header is assumed for single field CSV files
                if len(_templates[0]) > 1:
                    header = _templates[0]
                    if not header[0].strip() == 'Key':
                        raise DSOException(CLI_MESSAGES['MissingCSVField'].format("Key"))
                    _templates.pop(0)

                for template in _templates:
                    _key = template[0].strip()
                    templates.append({'Key': _key})

            elif format == 'text':
                try:
                    _templates = input.readlines()
                    if len(_templates):
                        if '\t' in _templates[0]:
                            header = _templates[0]
                            Key = header.split('\t')[0].strip()
                            _templates.pop(0)
                        else:
                            Key = 'Key'

                        for template in _templates:
                            _key = template.split('\t')[0].strip()
                            # _value = param.split('=', 1)[1].strip()
                            templates.append({Key: _key})
                except:
                    Logger.error(CLI_MESSAGES['InvalidFileFormat'].format(format))
                    exit(1)

        ### not input
        else:
            if key and key_option:
                Logger.error(CLI_MESSAGES['ArgumentsMutualExclusive'].format("'key'", "'-k' / '--key'"))
                Logger.info(CLI_MESSAGES['TryHelp'], stress = False, force=True)
                exit(1)
    
            key = key or key_option

            if not key:
                Logger.error(CLI_MESSAGES['AtleastOneofTwoNeeded'].format("'-k' / '--key'","'-i' / '--input'"))
                Logger.info(CLI_MESSAGES['TryHelp'], stress = False, force=True)
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
        #     Logger.info(CLI_MESSAGES['TryHelp'], stress = False, force=True)
        #     exit(1)

    try:
        Logger.set_verbosity(verbosity)
        check_command_usage()
        Config.load(working_dir if working_dir else os.getcwd(), config)

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

@template.command('render', context_settings=DEFAULT_CLICK_CONTEXT, short_help=f"{CLI_COMMANDS_SHORT_HELP['template']['render']}")
@click.option('-s', '--stage', metavar='<name>[/<number>]', default='default', help=f"{CLI_PARAMETERS_HELP['common']['stage']}")
@click.option('-l', '--limit', required=False, default='', help=f"{CLI_PARAMETERS_HELP['template']['limit']}")
@click.option('-b', '--verbosity', metavar='<number>', required=False, type=RangeParamType(click.INT, minimum=0, maximum=5), default='2', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['verbosity']}")
@click.option('--config', metavar='<key>=<value>,...', required=False, help=f"{CLI_PARAMETERS_HELP['common']['config']}")
@click.option('-w','--working-dir', metavar='<path>', type=click.Path(exists=True, file_okay=False), required=False, default='.', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['working_dir']}")
def render_template(stage, limit, working_dir, config, verbosity):
    """
    Render templates using parameters in a stage.\n
    """

    def check_command_usage():
        pass

    try:
        Logger.set_verbosity(verbosity)
        check_command_usage()
        Config.load(working_dir if working_dir else os.getcwd(), config)

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

@package.command('list', context_settings=DEFAULT_CLICK_CONTEXT, short_help="List available packages")
@click.argument('stage')
@click.option('-f', '--format', required=False, type=click.Choice(['csv','json', 'yaml']), default='csv', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['format']}")
@click.option('-b', '--verbosity', metavar='<number>', required=False, type=RangeParamType(click.INT, minimum=0, maximum=5), default='2', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['verbosity']}")
@click.option('--config', metavar='<key>=<value>,...', required=False, help=f"{CLI_PARAMETERS_HELP['common']['config']}")
@click.option('-w','--working-dir', metavar='<path>', type=click.Path(exists=True, file_okay=False), required=False, default='.', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['working_dir']}")
def list_package(stage, format, working_dir, config, verbosity):
    """
    Return the list of all available packages generated for a stage.\n
    \tENV: Name of the environment
    """
    
    print(Packages.list(stage))

###--------------------------------------------------------------------------------------------

@package.command('download', context_settings=DEFAULT_CLICK_CONTEXT, short_help="Download a package")
@click.argument('stage')
@click.argument('package')
@click.option('-f', '--format', required=False, type=click.Choice(['csv','json', 'yaml']), default='csv', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['format']}")
@click.option('-b', '--verbosity', metavar='<number>', required=False, type=RangeParamType(click.INT, minimum=0, maximum=5), default='2', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['verbosity']}")
@click.option('--config', metavar='<key>=<value>,...', required=False, help=f"{CLI_PARAMETERS_HELP['common']['config']}")
@click.option('-w','--working-dir', metavar='<path>', type=click.Path(exists=True, file_okay=False), required=False, default='.', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['working_dir']}")
def download_package(stage, package, format, working_dir, config, verbosity):
    """
    Downlaod a package generated for a stage.\n
    \tENV: Name of the environment\n
    \tPACKAGE: Version of the package to download
    """

    Packages.download(stage, name)

###--------------------------------------------------------------------------------------------

@package.command('create', context_settings=DEFAULT_CLICK_CONTEXT, short_help="Create a package")
@click.argument('stage')
@click.argument('description', required=False)
@click.option('-f', '--format', required=False, type=click.Choice(['csv','json', 'yaml']), default='csv', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['format']}")
@click.option('-b', '--verbosity', metavar='<number>', required=False, type=RangeParamType(click.INT, minimum=0, maximum=5), default='2', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['verbosity']}")
@click.option('--config', metavar='<key>=<value>,...', required=False, help=f"{CLI_PARAMETERS_HELP['common']['config']}")
@click.option('-w','--working-dir', metavar='<path>', type=click.Path(exists=True, file_okay=False), required=False, default='.', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['working_dir']}")
def generate_package(stage, verbosity, format, description=''):
    """
    Create a new build package for the application.\n
    \tENV: Name of the environment\n
    \tDESCRIPTION (optional): Description of the package
    """





###--------------------------------------------------------------------------------------------

@package.command('delete', context_settings=DEFAULT_CLICK_CONTEXT, short_help="Delete a package")
@click.argument('stage')
@click.argument('package')
@click.option('-f', '--format', required=False, type=click.Choice(['csv','json', 'yaml']), default='csv', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['format']}")
@click.option('-b', '--verbosity', metavar='<number>', required=False, type=RangeParamType(click.INT, minimum=0, maximum=5), default='2', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['verbosity']}")
@click.option('--config', metavar='<key>=<value>,...', required=False, help=f"{CLI_PARAMETERS_HELP['common']['config']}")
@click.option('-w','--working-dir', metavar='<path>', type=click.Path(exists=True, file_okay=False), required=False, default='.', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['working_dir']}")
def delete_package(stage, package, format, working_dir, config, verbosity):
    """
    Delete a package from a stage.\n
    \tENV: Name of the environment\n
    \tPACKAGE: Version of the package to be deleted
    """

    Packages.delete(stage, name)


###--------------------------------------------------------------------------------------------

@release.command('list', context_settings=DEFAULT_CLICK_CONTEXT, short_help="List available releases")
@click.argument('stage')
@click.option('-f', '--format', required=False, type=click.Choice(['csv','json', 'yaml']), default='csv', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['format']}")
@click.option('-b', '--verbosity', metavar='<number>', required=False, type=RangeParamType(click.INT, minimum=0, maximum=5), default='2', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['verbosity']}")
@click.option('--config', metavar='<key>=<value>,...', required=False, help=f"{CLI_PARAMETERS_HELP['common']['config']}")
@click.option('-w','--working-dir', metavar='<path>', type=click.Path(exists=True, file_okay=False), required=False, default='.', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['working_dir']}")
def list_release(stage, format, working_dir, config, verbosity):
    """
    Return the list of all available releases generated for a stage.\n
    \tENV: Name of the environment
    """

    print(Releases.list(stage))


###--------------------------------------------------------------------------------------------

@release.command('download', context_settings=DEFAULT_CLICK_CONTEXT, short_help="Download a release")
@click.argument('stage')
@click.argument('release')
@click.option('-f', '--format', required=False, type=click.Choice(['csv','json', 'yaml']), default='csv', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['format']}")
@click.option('-b', '--verbosity', metavar='<number>', required=False, type=RangeParamType(click.INT, minimum=0, maximum=5), default='2', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['verbosity']}")
@click.option('--config', metavar='<key>=<value>,...', required=False, help=f"{CLI_PARAMETERS_HELP['common']['config']}")
@click.option('-w','--working-dir', metavar='<path>', type=click.Path(exists=True, file_okay=False), required=False, default='.', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['working_dir']}")
def download_release(stage, release, format, working_dir, config, verbosity):
    """
    Downlaod a release generated for a stage.\n
    \tENV: Name of the environment\n
    \tRELEASE: Version of the release
    """

    Releases.download(stage, release)

###--------------------------------------------------------------------------------------------

@release.command('create', context_settings=DEFAULT_CLICK_CONTEXT, short_help="Create a release")
@click.argument('stage')
@click.argument('package')
@click.argument('description', required=False)
@click.option('-f', '--format', required=False, type=click.Choice(['csv','json', 'yaml']), default='csv', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['format']}")
@click.option('-b', '--verbosity', metavar='<number>', required=False, type=RangeParamType(click.INT, minimum=0, maximum=5), default='2', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['verbosity']}")
@click.option('--config', metavar='<key>=<value>,...', required=False, help=f"{CLI_PARAMETERS_HELP['common']['config']}")
@click.option('-w','--working-dir', metavar='<path>', type=click.Path(exists=True, file_okay=False), required=False, default='.', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['working_dir']}")
def generate_release(stage, verbosity, format, package, description=''):
    """
    Create a new release for a stage.\n
    \tENV: Name of the environment\n
    \tPACKAGE: Version of the package to be used for creating the release\n
    \tDESCRIPTION (optional): Description of the release
    """

    Releases.generate(stage, package, description)


###--------------------------------------------------------------------------------------------

@release.command('delete', context_settings=DEFAULT_CLICK_CONTEXT, short_help="Delete a release")
@click.argument('stage')
@click.argument('release')
@click.option('-f', '--format', required=False, type=click.Choice(['csv','json', 'yaml']), default='csv', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['format']}")
@click.option('-b', '--verbosity', metavar='<number>', required=False, type=RangeParamType(click.INT, minimum=0, maximum=5), default='2', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['verbosity']}")
@click.option('--config', metavar='<key>=<value>,...', required=False, help=f"{CLI_PARAMETERS_HELP['common']['config']}")
@click.option('-w','--working-dir', metavar='<path>', type=click.Path(exists=True, file_okay=False), required=False, default='.', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['working_dir']}")
def delete_release(stage, release, format, working_dir, config, verbosity):
    """
    Delete a release from a stage.\n
    \tENV: Name of the environment\n
    \tRELEASE: Version of the release to be deleted
    """

    Releases.delete(stage, release)

###--------------------------------------------------------------------------------------------

@config.command('get', context_settings=DEFAULT_CLICK_CONTEXT, short_help=f"{CLI_COMMANDS_SHORT_HELP['config']['get']}")
@click.argument('key', required=False)
@click.option('-l','--local', is_flag=True, default=False, help=f"{CLI_PARAMETERS_HELP['config']['local']}")
@click.option('-g','--global', '_global', is_flag=True, default=False, help=f"{CLI_PARAMETERS_HELP['config']['global']}")
@click.option('-b', '--verbosity', metavar='<number>', required=False, type=RangeParamType(click.INT, minimum=0, maximum=5), default='2', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['verbosity']}")
@click.option('--config', metavar='<key>=<value>,...', required=False, help=f"{CLI_PARAMETERS_HELP['common']['config']}")
@click.option('-w','--working-dir', metavar='<path>', type=click.Path(exists=True, file_okay=False), required=False, default='.', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['working_dir']}")
def get_config(key, local, _global, working_dir, config, verbosity):
    """
    Get DSO application configuration.\n
    \tKEY: The key of the configuration
    """

    scope = ''

    def check_command_usage():
        nonlocal scope
        if local and _global:
            Logger.error(CLI_MESSAGES['ArgumentsMutualExclusive'].format("'-l' / '--local'", "'-g' / '--global'"))
            Logger.info(CLI_MESSAGES['TryHelp'], stress = False, force=True)
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

@config.command('set', context_settings=DEFAULT_CLICK_CONTEXT, short_help=f"{CLI_COMMANDS_SHORT_HELP['config']['set']}")
@click.argument('key', required=False)
@click.option('-k', '--key', 'key_option', metavar='<value>', required=False, help=f"{CLI_PARAMETERS_HELP['config']['key']}")
@click.argument('value', required=False)
@click.option('-v', '--value', 'value_option', metavar='<value>', required=False, help=f"{CLI_PARAMETERS_HELP['config']['value']}")
@click.option('-g','--global', '_global', is_flag=True, default=False, help=f"{CLI_PARAMETERS_HELP['config']['global']}")
@click.option('-i', '--input', metavar='<path>', required=False, type=click.File(encoding='utf-8', mode='r'), help=f"{CLI_PARAMETERS_HELP['config']['input']}")
@click.option('-b', '--verbosity', metavar='<number>', required=False, type=RangeParamType(click.INT, minimum=0, maximum=5), default='2', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['verbosity']}")
@click.option('--config', metavar='<key>=<value>,...', required=False, help=f"{CLI_PARAMETERS_HELP['common']['config']}")
@click.option('-w','--working-dir', metavar='<path>', type=click.Path(exists=True, file_okay=False), required=False, default='.', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['working_dir']}")
def set_config(key, key_option, value, value_option, _global, input, working_dir, config, verbosity):
    """
    Set DSO application configuration.\n
    \tKEY: The key of the configuration. It may also be provided using the '--key' option.\n
    \tVALUE: The value for the configuration. It may also be provided using the '--value' option.\n
    """

    def check_command_usage():
        nonlocal key, value
        if key and key_option:
            Logger.error(CLI_MESSAGES['ArgumentsMutualExclusive'].format("'key'", "'-k' / '--key'"))
            Logger.info(CLI_MESSAGES['TryHelp'], stress = False, force=True)
            exit(1)

        key = key or key_option

        if not key:
            Logger.error(CLI_MESSAGES['AtleastOneofTwoNeeded'].format("'-k' / '--key'","'-i' / '--input'"))
            Logger.info(CLI_MESSAGES['TryHelp'], stress = False, force=True)
            exit(1)

        if value and value_option:
            Logger.error(CLI_MESSAGES['ArgumentsMutualExclusive'].format("'value'", "'-v' / '--value'"))
            Logger.info(CLI_MESSAGES['TryHelp'], stress = False, force=True)
            exit(1)

        value = value or value_option

        # if not _value:
        #     Logger.error(CLI_MESSAGES['MissingOption'].format("'-v' / '--value'"))
        #     Logger.info(CLI_MESSAGES['TryHelp'], stress = False, force=True)
        #     exit(1)

        if value and input:
            Logger.error(CLI_MESSAGES['ArgumentsMutualExclusive'].format("'-v' / '--value'","'-i' / '--input'"))
            Logger.info(CLI_MESSAGES['TryHelp'], stress = False, force=True)
            exit(1)

        if not (value or input):
            Logger.error(CLI_MESSAGES['AtleastOneofTwoNeeded'].format("'-v' / '--value'","'-i' / '--input'"))
            Logger.info(CLI_MESSAGES['TryHelp'], stress = False, force=True)
            exit(1)

        if input:
            try:
                value = yaml.load(input, yaml.SafeLoader)
            # except yaml.YAMLError as e:
            except:
                Logger.error(CLI_MESSAGES['InvalidFileFormat'].format(format))
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

@config.command('delete', context_settings=DEFAULT_CLICK_CONTEXT, short_help=f"{CLI_COMMANDS_SHORT_HELP['config']['delete']}")
@click.argument('key', required=False)
@click.option('-k', '--key', 'key_option', metavar='<value>', required=False, help=f"{CLI_PARAMETERS_HELP['config']['key']}")
@click.option('-g','--global', '_global', is_flag=True, default=False, help=f"{CLI_PARAMETERS_HELP['config']['global']}")
@click.option('-b', '--verbosity', metavar='<number>', required=False, type=RangeParamType(click.INT, minimum=0, maximum=5), default='2', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['verbosity']}")
@click.option('--config', metavar='<key>=<value>,...', required=False, help=f"{CLI_PARAMETERS_HELP['common']['config']}")
@click.option('-w','--working-dir', metavar='<path>', type=click.Path(exists=True, file_okay=False), required=False, default='.', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['working_dir']}")
def delete_config(key, key_option, _global, working_dir, config, verbosity):
    """
    Dlete a DSO application configuration.\n
    \tKEY: The key of the configuration
    """

    def check_command_usage():
        nonlocal key
        if key and key_option:
            Logger.error(CLI_MESSAGES['ArgumentsMutualExclusive'].format("'key'", "'-k' / '--key'"))
            Logger.info(CLI_MESSAGES['TryHelp'], stress = False, force=True)
            exit(1)

        key = key or key_option

        if not key:
            Logger.error(CLI_MESSAGES['AtleastOneofTwoNeeded'].format("'-k' / '--key'","'-i' / '--input'"))
            Logger.info(CLI_MESSAGES['TryHelp'], stress = False, force=True)
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

# @config.command('setup', context_settings=DEFAULT_CLICK_CONTEXT, short_help=f"{CLI_COMMANDS_SHORT_HELP['config']['setup']}")
# @click.option('-w','--working-dir', metavar='<path>', type=click.Path(exists=True, file_okay=False), required=False, default='.', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['working_dir']}")
# @click.option('--config', metavar='<key>=<value>,...', required=False, help=f"{CLI_PARAMETERS_HELP['common']['config']}")
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

@config.command('init', context_settings=DEFAULT_CLICK_CONTEXT, short_help=f"{CLI_COMMANDS_SHORT_HELP['config']['init']}")
@click.option('--setup', is_flag=True, required=False, help=f"{CLI_PARAMETERS_HELP['config']['setup']}")
@click.option('-l','--local', is_flag=True, default=False, help=f"{CLI_PARAMETERS_HELP['config']['init_local']}")
@click.option('-i', '--input', metavar='<path>', required=False, type=click.File(encoding='utf-8', mode='r'), help=f"{CLI_PARAMETERS_HELP['config']['input']}")
@click.option('-b', '--verbosity', metavar='<number>', required=False, type=RangeParamType(click.INT, minimum=0, maximum=5), default='2', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['verbosity']}")
@click.option('--config', metavar='<key>=<value>,...', required=False, help=f"{CLI_PARAMETERS_HELP['common']['config']}")
@click.option('-w','--working-dir', metavar='<path>', type=click.Path(exists=True, file_okay=False), required=False, default='.', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['working_dir']}")
def init_config(setup, local, input, working_dir, config, verbosity):
    """
    Initialize DSO configuration for the working directory.\n
    The option '--working-dir' can be used to specify a different working directory than the current directory where dso is running in.
    """

    init_config = None

    def check_command_usage():
        nonlocal init_config

        if input:
            # if local:
            #     Logger.warn("Option '--local' is not needed when '--input' specifies the initial configuration, as it will always be overriden locally.")
            try:
                init_config = yaml.load(input, yaml.SafeLoader)
            except:
                Logger.error(CLI_MESSAGES['InvalidFileFormat'].format('yaml'))
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
    
modify_click_usage_error()
