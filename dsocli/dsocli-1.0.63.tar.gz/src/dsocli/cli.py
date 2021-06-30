import sys
import os
import platform
import click
import re
import yaml
import json
import csv
import subprocess
import glob
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
from .cli_utils import *
from .file_utils import *
from .version import dso_version
from functools import reduce
from .pager import Pager



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

# @cli.group(context_settings=DEFAULT_CLICK_CONTEXT)
# def provision():
#     """
#     Provision resources.
#     """
#     pass

# ###--------------------------------------------------------------------------------------------

# @cli.group(context_settings=DEFAULT_CLICK_CONTEXT)
# def deploy():
#     """
#     Deploy releases.
#     """
#     pass

###--------------------------------------------------------------------------------------------
###--------------------------------------------------------------------------------------------
###--------------------------------------------------------------------------------------------

@cli.command('version', context_settings=DEFAULT_CLICK_CONTEXT, short_help=f"{CLI_COMMANDS_SHORT_HELP['version']}")
def version():
    """
    Display version details.
    """
    click.echo(f"DSO CLI: {dso_version}\nPython: {platform.sys.version}")


###--------------------------------------------------------------------------------------------
###--------------------------------------------------------------------------------------------
###--------------------------------------------------------------------------------------------

@parameter.command('add', context_settings=DEFAULT_CLICK_CONTEXT, short_help=f"{CLI_COMMANDS_SHORT_HELP['parameter']['add']}")
@command_doc(CLI_COMMANDS_HELP['parameter']['add'])
@click.argument('key', required=False)
@click.argument('value', required=False)
@click.option('-k', '--key', 'key_option', required=False, metavar='<key>', help=f"{CLI_PARAMETERS_HELP['parameter']['key']}")
@click.option('-v', '--value', 'value_option', metavar='<value>', required=False, help=f"{CLI_PARAMETERS_HELP['parameter']['value']}")
@click.option('-s', '--stage', metavar='<name>[/<number>]', default='default', help=f"{CLI_PARAMETERS_HELP['common']['stage']}")
@click.option('-i', '--input', metavar='<path>', required=False, type=click.File(encoding='utf-8', mode='r'), help=f"{CLI_PARAMETERS_HELP['common']['input']}")
@click.option('-f', '--format', required=False, type=click.Choice(['json', 'yaml', 'raw', 'csv', 'shell']), default='json', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['format']}")
@click.option('-b', '--verbosity', metavar='<number>', required=False, type=RangeParamType(click.INT, minimum=0, maximum=5), default='2', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['verbosity']}")
@click.option('--config', metavar='<key>=<value>,...', required=False, help=f"{CLI_PARAMETERS_HELP['common']['config']}")
@click.option('-w','--working-dir', metavar='<path>', type=click.Path(exists=True, file_okay=False), required=False, default='.', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['working_dir']}")
def add_parameter(key, key_option, value, value_option, stage, input, format, verbosity, config, working_dir):
    
    parameters = []

    def validate_command_usage():
        nonlocal stage, key, value, parameters
        stage = Stages.normalize(stage)

        if input:
            validate_none_provided([key, key_option], ["KEY", "'-k' / '--key'"], ["'-i' / '--input'"])
            parameters = read_data(input, 'Parameters', ['Key', 'Value'], format)

            ### eat possible enclosing (double) quotes when source is file, stdin has already eaten them!
            if format == 'shell': 
                for param in parameters:
                    if re.match(r'^".*"$', param['Value']):
                        param['Value'] = re.sub(r'^"|"$', '', param['Value'])
                    elif re.match(r"^'.*'$", param['Value']):
                        param['Value'] = re.sub(r"^'|'$", '', param['Value'])

        ### no input file
        else:
            validate_not_all_provided([key, key_option], ["KEY", "'-k' / '--key'"])
            key = validate_only_one_provided([key, key_option], ["KEY", "'-k' / '--key'"])
            validate_not_all_provided([key, key_option], ["VALUE", "'-v' / '--value'"])
            value = validate_only_one_provided([value, value_option], ["VALUE", "'-v' / '--value'"])
            parameters.append({'Key': key, 'Value': value})

    success = []
    failed = []
    try:
        Logger.set_verbosity(verbosity)
        validate_command_usage()
        Config.load(working_dir if working_dir else os.getcwd(), config)

        failed = [x['Key'] for x in parameters]
        for param in parameters:
            success.append(Parameters.add(stage, param['Key'], param['Value']))
            failed.remove(param['Key'])

    except DSOException as e:
        Logger.error(e.message)
    except Exception as e:
        msg = getattr(e, 'message', getattr(e, 'msg', str(e)))
        Logger.critical(msg)
        if verbosity >= log_levels['full']:
            raise
    finally:
        if parameters:
            if len(failed):
                failure = [{'Key': x for x in failed}]
            else:
                failure = []
            result = {'Success': success, 'Failure': failure}
            output = format_data(result, '', 'json') ### FIXME: use a global output format setting
            if output: Pager.page(output)

###--------------------------------------------------------------------------------------------

@parameter.command('list', context_settings=DEFAULT_CLICK_CONTEXT, short_help=f"{CLI_COMMANDS_SHORT_HELP['parameter']['list']}")
@command_doc(CLI_COMMANDS_HELP['parameter']['list'])
@click.option('-s', '--stage', metavar='<name>[/<number>]', default='default', help=f"{CLI_PARAMETERS_HELP['common']['stage']}")
@click.option('-u','--uninherited', 'uninherited', is_flag=True, default=False, help=f"{CLI_PARAMETERS_HELP['parameter']['uninherited']}")
@click.option('-a', '--query-all', required=False, is_flag=True, default=False, show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['query_all']}")
@click.option('-q', '--query', metavar='<jmespath>', required=False, help=f"{CLI_PARAMETERS_HELP['common']['query']}")
@click.option('-f', '--format', required=False, type=click.Choice(['json', 'yaml', 'csv', 'raw', 'shell']), default='json', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['format']}")
@click.option('-b', '--verbosity', metavar='<number>', required=False, type=RangeParamType(click.INT, minimum=0, maximum=5), default='2', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['verbosity']}")
@click.option('--config', metavar='<key>=<value>,...', required=False, help=f"{CLI_PARAMETERS_HELP['common']['config']}")
@click.option('-w','--working-dir', metavar='<path>', type=click.Path(exists=True, file_okay=False), required=False, default='.', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['working_dir']}")
def list_parameter(stage, uninherited, query_all, query, format, verbosity, config, working_dir):

    def validate_command_usage():
        nonlocal stage, query
        stage = Stages.normalize(stage)
        query = validate_query_argument(query, query_all, '{Parameters: Parameters[*].{Key: Key, Value: Value}}')

    try:
        Logger.set_verbosity(verbosity)
        validate_command_usage()
        Config.load(working_dir if working_dir else os.getcwd(), config)
        result = Parameters.list(stage, uninherited)
        output = format_data(result, query, format)
        if output: Pager.page(output)

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
@click.option('--revision', required=False, help=f"{CLI_PARAMETERS_HELP['parameter']['revision']}")
@click.option('--history', required=False, is_flag=True, help=f"{CLI_PARAMETERS_HELP['parameter']['history']}")
@click.option('-a', '--query-all', required=False, is_flag=True, default=False, show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['query_all']}")
@click.option('-q', '--query', metavar='<jmespath>', required=False, help=f"{CLI_PARAMETERS_HELP['common']['query']}")
@click.option('-f', '--format', required=False, type=click.Choice(['json', 'yaml', 'raw', 'csv']), default='json', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['format']}")
@click.option('-b', '--verbosity', metavar='<number>', required=False, type=RangeParamType(click.INT, minimum=0, maximum=5), default='2', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['verbosity']}")
@click.option('--config', metavar='<key>=<value>,...', required=False, help=f"{CLI_PARAMETERS_HELP['common']['config']}")
@click.option('-w','--working-dir', metavar='<path>', type=click.Path(exists=True, file_okay=False), required=False, default='.', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['working_dir']}")
def get_parameter(key, key_option, stage, revision, history, query_all, query, format, verbosity, config, working_dir):

    def validate_command_usage():
        nonlocal stage, key, query
        stage = Stages.normalize(stage)
        validate_not_all_provided([key, key_option], ["KEY", "'-k' / '--key'"])
        key = validate_at_least_one_provided([key, key_option], ["KEY", "'-k' / '--key'"])
        validate_not_all_provided([history, revision], ["'--history'", "'--revision'"])
        query = validate_query_argument(query, query_all, '{Revisions: Revisions[*].{Revision: Revision, Value: Value, Date: Date}}' if history else '{Value: Value}')
        
    try:
        Logger.set_verbosity(verbosity)
        validate_command_usage()
        Config.load(working_dir if working_dir else os.getcwd(), config)
        if history:
            result = Parameters.history(stage, key)
        else:
            result = Parameters.get(stage, key, revision)
        output = format_data(result, query, format)
        if output: Pager.page(output)
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
@click.option('-f', '--format', required=False, type=click.Choice(['json', 'yaml', 'raw', 'csv', 'shell']), default='json', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['format']}")
@click.option('-b', '--verbosity', metavar='<number>', required=False, type=RangeParamType(click.INT, minimum=0, maximum=5), default='2', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['verbosity']}")
@click.option('--config', metavar='<key>=<value>,...', required=False, help=f"{CLI_PARAMETERS_HELP['common']['config']}")
@click.option('-w','--working-dir', metavar='<path>', type=click.Path(exists=True, file_okay=False), required=False, default='.', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['working_dir']}")
def delete_parameter(key, key_option, input, format, stage, verbosity, config, working_dir):

    parameters = []

    def validate_command_usage():
        nonlocal stage, key, parameters
        stage = Stages.normalize(stage)

        if input:
            validate_none_provided([key, key_option], ["KEY", "'-k' / '--key'"], ["'-i' / '--input'"])
            parameters = read_data(input, 'Parameters', ['Key'], format)

        ### no input file
        else:
            validate_not_all_provided([key, key_option], ["KEY", "'-k' / '--key'"])
            key = validate_only_one_provided([key, key_option], ["KEY", "'-k' / '--key'"])
            parameters.append({'Key': key})

    success = []
    failed = []
    try:
        Logger.set_verbosity(verbosity)
        validate_command_usage()
        Config.load(working_dir if working_dir else os.getcwd(), config)

        failed = [x['Key'] for x in parameters]
        for parameter in parameters:
            success.append(Parameters.delete(stage, parameter['Key']))
            failed.remove(parameter['Key'])

    except DSOException as e:
        Logger.error(e.message)
    except Exception as e:
        msg = getattr(e, 'message', getattr(e, 'msg', str(e)))
        Logger.critical(msg)
        if verbosity >= log_levels['full']:
            raise
    finally:
        if parameters:
            if len(failed):
                failure = [{'Key': x for x in failed}]
            else:
                failure = []
            result = {'Success': success, 'Failure': failure}
            output = format_data(result, '', 'json') ### FIXME: use a global output format setting
            if output: Pager.page(output)

###--------------------------------------------------------------------------------------------
###--------------------------------------------------------------------------------------------
###--------------------------------------------------------------------------------------------

@secret.command('add', context_settings=DEFAULT_CLICK_CONTEXT, short_help=f"{CLI_COMMANDS_SHORT_HELP['secret']['add']}")
@command_doc(CLI_COMMANDS_HELP['secret']['add'])
@click.argument('key', required=False)
@click.option('-k', '--key', 'key_option', required=False, metavar='<key>', help=f"{CLI_PARAMETERS_HELP['secret']['key']}")
@click.option('-s', '--stage', metavar='<name>[/<number>]', default='default', help=f"{CLI_PARAMETERS_HELP['common']['stage']}")
@click.option('-i', '--input', metavar='<path>', required=False, type=click.File(encoding='utf-8', mode='r'), help=f"{CLI_PARAMETERS_HELP['common']['input']}")
@click.option('-f', '--format', required=False, type=click.Choice(['json', 'yaml', 'raw', 'csv', 'shell']), default='json', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['format']}")
@click.option('-b', '--verbosity', metavar='<number>', required=False, type=RangeParamType(click.INT, minimum=0, maximum=5), default='2', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['verbosity']}")
@click.option('--config', metavar='<key>=<value>,...', required=False, help=f"{CLI_PARAMETERS_HELP['common']['config']}")
@click.option('-w','--working-dir', metavar='<path>', type=click.Path(exists=True, file_okay=False), required=False, default='.', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['working_dir']}")
def add_secret(key, key_option, stage, input, format, verbosity, config, working_dir):

    secrets = []

    def validate_command_usage():
        nonlocal stage, key, secrets
        stage = Stages.normalize(stage)

        if input:
            validate_none_provided([key, key_option], ["KEY", "'-k' / '--key'"], ["'-i' / '--input'"])
            secrets = read_data(input, 'Secrets', ['Key', 'Value'], format)

            ### eat possible enclosing (double) quotes when source is file, stdin has already eaten them!
            if format == 'shell': 
                for secret in secrets:
                    if re.match(r'^".*"$', secret['Value']):
                        secret['Value'] = re.sub(r'^"|"$', '', secret['Value'])
                    elif re.match(r"^'.*'$", secret['Value']):
                        secret['Value'] = re.sub(r"^'|'$", '', secret['Value'])

        ### no input file
        else:
            validate_not_all_provided([key, key_option], ["KEY", "'-k' / '--key'"])
            key = validate_only_one_provided([key, key_option], ["KEY", "'-k' / '--key'"])
            value = getpass("Enter secret value: ")
            value2 = getpass("Verify secret value: ")
            if not value == value2:
                raise DSOException(CLI_MESSAGES['EnteredSecretValuesNotMatched'].format(format))

            secrets.append({'Key': key, 'Value': value})

    success = []
    failed = []
    try:
        Logger.set_verbosity(verbosity)
        validate_command_usage()
        Config.load(working_dir if working_dir else os.getcwd(), config)

        failed = [x['Key'] for x in secrets]
        for secret in secrets:
            success.append(Secrets.add(stage, secret['Key'], secret['Value']))
            failed.remove(secret['Key'])

    except DSOException as e:
        Logger.error(e.message)
    except Exception as e:
        msg = getattr(e, 'message', getattr(e, 'msg', str(e)))
        Logger.critical(msg)
        if verbosity >= log_levels['full']:
            raise
    finally:
        if secrets:
            if len(failed):
                failure = [{'Key': x for x in failed}]
            else:
                failure = []
            result = {'Success': success, 'Failure': failure}
            output = format_data(result, '', 'json') ### FIXME: use a global output format setting
            if output: Pager.page(output)

###--------------------------------------------------------------------------------------------

@secret.command('list', context_settings=DEFAULT_CLICK_CONTEXT, short_help=f"{CLI_COMMANDS_SHORT_HELP['secret']['list']}")
@command_doc(CLI_COMMANDS_HELP['secret']['list'])
@click.option('-s', '--stage', 'stage', metavar='<name>[/<number>]', default='default', help=f"{CLI_PARAMETERS_HELP['common']['stage']}")
@click.option('-d', '--decrypt', required=False, is_flag=True, default=False, show_default=True, help=f"{CLI_PARAMETERS_HELP['parameter']['query_values']}")
@click.option('-u','--uninherited', 'uninherited', is_flag=True, default=False, help=f"{CLI_PARAMETERS_HELP['secret']['uninherited']}")
@click.option('-a', '--query-all', required=False, is_flag=True, default=False, show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['query_all']}")
@click.option('-q', '--query', metavar='<jmespath>', required=False, help=f"{CLI_PARAMETERS_HELP['common']['query']}")
@click.option('-f', '--format', required=False, type=click.Choice(['json', 'yaml', 'raw', 'csv', 'shell']), default='json', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['format']}")
@click.option('-b', '--verbosity', metavar='<number>', required=False, type=RangeParamType(click.INT, minimum=0, maximum=5), default='2', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['verbosity']}")
@click.option('--config', metavar='<key>=<value>,...', required=False, help=f"{CLI_PARAMETERS_HELP['common']['config']}")
@click.option('-w','--working-dir', metavar='<path>', type=click.Path(exists=True, file_okay=False), required=False, default='.', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['working_dir']}")
def list_secret(stage, uninherited, decrypt, query_all, query, format, verbosity, config, working_dir):

    def validate_command_usage():
        nonlocal stage, query
        stage = Stages.normalize(stage)
        query = validate_query_argument(query, query_all, '{Secrets: Secrets[*].{Key: Key, Value: Value}}')

    try:
        Logger.set_verbosity(verbosity)
        validate_command_usage()
        Config.load(working_dir if working_dir else os.getcwd(), config)
        result = Secrets.list(stage, uninherited, decrypt)
        output = format_data(result, query, format)
        if output: Pager.page(output)

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
@click.option('-k', '--key', 'key_option', required=False, metavar='<key>', help=f"{CLI_PARAMETERS_HELP['parameter']['key']}")
@click.option('-s', '--stage', metavar='<name>[/<number>]', default='default', help=f"{CLI_PARAMETERS_HELP['common']['stage']}")
@click.option('--revision', required=False, help=f"{CLI_PARAMETERS_HELP['secret']['revision']}")
@click.option('--history', required=False, is_flag=True, help=f"{CLI_PARAMETERS_HELP['secret']['history']}")
@click.option('-a', '--query-all', required=False, is_flag=True, default=False, show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['query_all']}")
@click.option('-q', '--query', metavar='<jmespath>', required=False, help=f"{CLI_PARAMETERS_HELP['common']['query']}")
@click.option('-f', '--format', required=False, type=click.Choice(['json', 'yaml', 'raw', 'csv']), default='json', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['format']}")
@click.option('-b', '--verbosity', metavar='<number>', required=False, type=RangeParamType(click.INT, minimum=0, maximum=5), default='2', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['verbosity']}")
@click.option('--config', metavar='<key>=<value>,...', required=False, help=f"{CLI_PARAMETERS_HELP['common']['config']}")
@click.option('-w','--working-dir', metavar='<path>', type=click.Path(exists=True, file_okay=False), required=False, default='.', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['working_dir']}")
def get_secret(key, key_option, stage, revision, history, query_all, query, format, verbosity, config, working_dir):

    def validate_command_usage():
        nonlocal stage, key, query
        stage = Stages.normalize(stage)
        validate_not_all_provided([key, key_option], ["KEY", "'-k' / '--key'"])
        key = validate_at_least_one_provided([key, key_option], ["KEY", "'-k' / '--key'"])
        validate_not_all_provided([history, revision], ["'--history'", "'--revision'"])
        query = validate_query_argument(query, query_all, '{Revisions: Revisions[*].{Revision: Revision, Value: Value, Date: Date}}' if history else '{Value: Value}')
        
    try:
        Logger.set_verbosity(verbosity)
        validate_command_usage()
        Config.load(working_dir if working_dir else os.getcwd(), config)
        if history:
            result = Secrets.history(stage, key)
        else:
            result = Secrets.get(stage, key, revision)
        output = format_data(result, query, format)
        if output: Pager.page(output)

    except DSOException as e:
        Logger.error(e.message)
    except Exception as e:
        msg = getattr(e, 'message', getattr(e, 'msg', str(e)))
        Logger.critical(msg)
        if verbosity >= log_levels['full']:
            raise

###--------------------------------------------------------------------------------------------

@secret.command('delete', context_settings=DEFAULT_CLICK_CONTEXT, short_help=f"{CLI_COMMANDS_SHORT_HELP['secret']['delete']}")
@command_doc(CLI_COMMANDS_HELP['secret']['delete'])
@click.argument('key', required=False)
@click.option('-k', '--key', 'key_option', metavar='<key>', required=False, help=f"{CLI_PARAMETERS_HELP['secret']['key']}")
@click.option('-s', '--stage', metavar='<name>[/<number>]', default='default', help=f"{CLI_PARAMETERS_HELP['common']['stage']}")
@click.option('-i', '--input', metavar='<path>', required=False, type=click.File(encoding='utf-8', mode='r'), help=f"{CLI_PARAMETERS_HELP['common']['input']}")
@click.option('-f', '--format', required=False, type=click.Choice(['json', 'yaml', 'raw', 'csv', 'shell']), default='json', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['format']}")
@click.option('-b', '--verbosity', metavar='<number>', required=False, type=RangeParamType(click.INT, minimum=0, maximum=5), default='2', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['verbosity']}")
@click.option('--config', metavar='<key>=<value>,...', required=False, help=f"{CLI_PARAMETERS_HELP['common']['config']}")
@click.option('-w','--working-dir', metavar='<path>', type=click.Path(exists=True, file_okay=False), required=False, default='.', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['working_dir']}")
def delete_secret(key, key_option, input, format, stage, verbosity, config, working_dir):

    secrets = []

    def validate_command_usage():
        nonlocal stage, key, secrets
        stage = Stages.normalize(stage)

        if input:
            validate_none_provided([key, key_option], ["KEY", "'-k' / '--key'"], ["'-i' / '--input'"])
            secrets = read_data(input, 'Secrets', ['Key'], format)

        ### no input file
        else:
            validate_not_all_provided([key, key_option], ["KEY", "'-k' / '--key'"])
            key = validate_only_one_provided([key, key_option], ["KEY", "'-k' / '--key'"])
            secrets.append({'Key': key})

    success = []
    failed = []
    try:
        Logger.set_verbosity(verbosity)
        validate_command_usage()
        Config.load(working_dir if working_dir else os.getcwd(), config)

        failed = [x['Key'] for x in secrets]
        for secret in secrets:
            success.append(Secrets.delete(stage, secret['Key']))
            failed.remove(secret['Key'])

    except DSOException as e:
        Logger.error(e.message)
    except Exception as e:
        msg = getattr(e, 'message', getattr(e, 'msg', str(e)))
        Logger.critical(msg)
        if verbosity >= log_levels['full']:
            raise
    finally:
        if secrets:
            if len(failed):
                failure = [{'Key': x for x in failed}]
            else:
                failure = []
            result = {'Success': success, 'Failure': failure}
            output = format_data(result, '', 'json') ### FIXME: use a global output format setting
            if output: Pager.page(output)

###--------------------------------------------------------------------------------------------
###--------------------------------------------------------------------------------------------
###--------------------------------------------------------------------------------------------

@template.command('list', context_settings=DEFAULT_CLICK_CONTEXT, short_help=f"{CLI_COMMANDS_SHORT_HELP['template']['list']}")
@command_doc(CLI_COMMANDS_HELP['template']['list'])
@click.option('-u','--uninherited', 'uninherited', is_flag=True, default=False, help=f"{CLI_PARAMETERS_HELP['template']['uninherited']}")
@click.option('-a', '--query-all', required=False, is_flag=True, default=False, show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['query_all']}")
@click.option('-q', '--query', metavar='<jmespath>', required=False, help=f"{CLI_PARAMETERS_HELP['common']['query']}")
@click.option('-f', '--format', required=False, type=click.Choice(['json', 'yaml', 'csv', 'raw']), default='json', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['format']}")
@click.option('-b', '--verbosity', metavar='<number>', required=False, type=RangeParamType(click.INT, minimum=0, maximum=5), default='2', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['verbosity']}")
@click.option('--config', metavar='<key>=<value>,...', required=False, help=f"{CLI_PARAMETERS_HELP['common']['config']}")
@click.option('-w','--working-dir', metavar='<path>', type=click.Path(exists=True, file_okay=False), required=False, default='.', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['working_dir']}")
def list_template(uninherited, query_all, query, format, verbosity, config, working_dir):

    def validate_command_usage():
        nonlocal query
        query = validate_query_argument(query, query_all, '{Templates: Templates[*].{Key: Key, RenderTo: RenderTo}}')

    try:
        Logger.set_verbosity(verbosity)
        validate_command_usage()
        Config.load(working_dir if working_dir else os.getcwd(), config)
        result = Templates.list(uninherited)
        output = format_data(result, query, format)
        if output: Pager.page(output)
    except DSOException as e:
        Logger.error(e.message)
    except Exception as e:
        msg = getattr(e, 'message', getattr(e, 'msg', str(e)))
        Logger.critical(msg)
        if verbosity >= log_levels['full']:
            raise

###--------------------------------------------------------------------------------------------

@template.command('get', context_settings=DEFAULT_CLICK_CONTEXT, short_help=f"{CLI_COMMANDS_SHORT_HELP['template']['get']}")
@command_doc(CLI_COMMANDS_HELP['template']['get'])
@click.argument('key', required=False)
@click.option('-k', '--key', 'key_option', metavar='<key>', required=False, help=f"{CLI_PARAMETERS_HELP['template']['key']}")
@click.option('-b', '--verbosity', metavar='<number>', required=False, type=RangeParamType(click.INT, minimum=0, maximum=5), default='2', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['verbosity']}")
@click.option('--config', metavar='<key>=<value>,...', required=False, help=f"{CLI_PARAMETERS_HELP['common']['config']}")
@click.option('-w','--working-dir', metavar='<path>', type=click.Path(exists=True, file_okay=False), required=False, default='.', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['working_dir']}")
def get_template(key, key_option, verbosity, config, working_dir):

    def validate_command_usage():
        nonlocal key
        validate_not_all_provided([key, key_option], ["KEY", "'-k' / '--key'"])
        key = validate_at_least_one_provided([key, key_option], ["KEY", "'-k' / '--key'"])

    try:
        Logger.set_verbosity(verbosity)
        validate_command_usage()
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
@command_doc(CLI_COMMANDS_HELP['template']['add'])
@click.argument('key', required=False)
@click.option('-k', '--key', 'key_option', metavar='<key>', required=False, help=f"{CLI_PARAMETERS_HELP['template']['key']}")
@click.option('-r', '--render-path', default='.', show_default=True, metavar='<path>', required=False, help=f"{CLI_PARAMETERS_HELP['template']['render_path']}")
@click.option('-i', '--input', metavar='<path>', required=True, type=click.Path(exists=True, file_okay=True, dir_okay=True), help=f"{CLI_PARAMETERS_HELP['template']['input']}")
@click.option('--recursive', required=False, is_flag=True, help=f"{CLI_PARAMETERS_HELP['template']['recursive']}")
@click.option('-b', '--verbosity', metavar='<number>', required=False, type=RangeParamType(click.INT, minimum=0, maximum=5), default='2', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['verbosity']}")
@click.option('--config', metavar='<key>=<value>,...', required=False, help=f"{CLI_PARAMETERS_HELP['common']['config']}")
@click.option('-w','--working-dir', metavar='<path>', type=click.Path(exists=True, file_okay=False), required=False, default='.', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['working_dir']}")
def add_template(key, key_option, render_path, input, recursive, verbosity, config, working_dir):

    templates = []

    def process_key_from_path(_path):
        if not key or key in ['.' , './']:
            return _path[len(input)+1:]

        result = key
        ### if **/ exist in key, replace it with _path dirname
        if os.path.dirname(_path)[len(input):]:
            result = result.replace('**', os.path.dirname(_path)[len(input)+1:])
        else:
            result = result.replace(f'**{os.sep}', '')
            result = result.replace('**', '')
        result = result.replace('*', os.path.basename(_path))
        result = result.replace(f"{os.sep}{os.sep}", os.sep)

        return result


    def process_render_path_from_key(_key):
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

    def validate_command_usage():
        nonlocal input, key, templates

        key = validate_not_all_provided([key, key_option], ["KEY", "'-k' / '--key'"])

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
            if is_binary_file(item):
                Logger.warn(f"Binary file '{item}' ignored.")
                continue
            _path = str(item)
            _key = process_key_from_path(_path)
            _render_path = process_render_path_from_key(_key)

            templates.append({'Key': _key, 'Path': _path, 'RenderPath': _render_path})

    success = []
    failed = []
    try:
        Logger.set_verbosity(verbosity)
        validate_command_usage()
        Config.load(working_dir if working_dir else os.getcwd(), config)

        failed = [x['Key'] for x in templates]
        for template in templates:
            success.append(Templates.add(template['Key'], open(template['Path'], encoding='utf-8', mode='r').read(), template['RenderPath']))
            failed.remove(template['Key'])

    except DSOException as e:
        Logger.error(e.message)
    except Exception as e:
        msg = getattr(e, 'message', getattr(e, 'msg', str(e)))
        Logger.critical(msg)
        if verbosity >= log_levels['full']:
            raise
    finally:
        if templates:
            if len(failed):
                failure = [{'Key': x for x in failed}]
            else:
                failure = []
            result = {'Success': success, 'Failure': failure}
            output = format_data(result, '', 'json') ### FIXME: use a global output format setting
            if output: Pager.page(output)

###--------------------------------------------------------------------------------------------

@template.command('delete', context_settings=DEFAULT_CLICK_CONTEXT, short_help=f"{CLI_COMMANDS_SHORT_HELP['template']['delete']}")
@command_doc(CLI_COMMANDS_HELP['template']['delete'])
@click.argument('key', required=False)
@click.option('-k', '--key', 'key_option', metavar='<key>', required=False, help=f"{CLI_PARAMETERS_HELP['template']['key']}")
@click.option('-i', '--input', metavar='<path>', required=False, type=click.File(encoding='utf-8', mode='r'), help=f"{CLI_PARAMETERS_HELP['common']['input']}")
# @click.option('--recursive', required=False, is_flag=True, help=f"{CLI_PARAMETERS_HELP['template']['recursive']}")
@click.option('-f', '--format', required=False, type=click.Choice(['json', 'yaml', 'raw', 'csv']), default='json', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['format']}")
@click.option('-b', '--verbosity', metavar='<number>', required=False, type=RangeParamType(click.INT, minimum=0, maximum=5), default='2', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['verbosity']}")
@click.option('--config', metavar='<key>=<value>,...', required=False, help=f"{CLI_PARAMETERS_HELP['common']['config']}")
@click.option('-w','--working-dir', metavar='<path>', type=click.Path(exists=True, file_okay=False), required=False, default='.', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['working_dir']}")
def delete_template(key, key_option, input, format, verbosity, config, working_dir):

    templates = []

    def validate_command_usage():
        nonlocal key, templates

        if input:
            validate_none_provided([key, key_option], ["KEY", "'-k' / '--key'"], ["'-i' / '--input'"])
            templates = read_data(input, 'Templates', ['Key'], format)
        ### no input file
        else:
            key = validate_only_one_provided([key, key_option], ["KEY", "'-k' / '--key'"])
            templates.append({'Key': key})

    success = []
    failed = []
    try:
        Logger.set_verbosity(verbosity)
        validate_command_usage()
        Config.load(working_dir if working_dir else os.getcwd(), config)

        failed = [x['Key'] for x in templates]
        for template in templates:
            success.append(Templates.delete(template['Key']))
            failed.remove(template['Key'])
    except DSOException as e:
        Logger.error(e.message)
    except Exception as e:
        msg = getattr(e, 'message', getattr(e, 'msg', str(e)))
        Logger.critical(msg)
        if verbosity >= log_levels['full']:
            raise
    finally:
        if templates:
            if len(failed):
                failure = [{'Key': x for x in failed}]
            else:
                failure = []
            result = {'Success': success, 'Failure': failure}
            output = format_data(result, '', 'json') ### FIXME: use a global output format setting
            if output: Pager.page(output)

###--------------------------------------------------------------------------------------------

@template.command('render', context_settings=DEFAULT_CLICK_CONTEXT, short_help=f"{CLI_COMMANDS_SHORT_HELP['template']['render']}")
@command_doc(CLI_COMMANDS_HELP['template']['render'])
@click.option('-s', '--stage', metavar='<name>[/<number>]', default='default', help=f"{CLI_PARAMETERS_HELP['common']['stage']}")
@click.option('-l', '--limit', required=False, default='', help=f"{CLI_PARAMETERS_HELP['template']['limit']}")
@click.option('-b', '--verbosity', metavar='<number>', required=False, type=RangeParamType(click.INT, minimum=0, maximum=5), default='2', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['verbosity']}")
@click.option('--config', metavar='<key>=<value>,...', required=False, help=f"{CLI_PARAMETERS_HELP['common']['config']}")
@click.option('-w','--working-dir', metavar='<path>', type=click.Path(exists=True, file_okay=False), required=False, default='.', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['working_dir']}")
def render_template(stage, limit, verbosity, config, working_dir):

    def validate_command_usage():
        pass

    try:
        Logger.set_verbosity(verbosity)
        validate_command_usage()
        Config.load(working_dir if working_dir else os.getcwd(), config)

        success = Templates.render(stage, limit)
        result = {'Success': success, 'Failure': []}
        output = format_data(result, '', 'json') ### FIXME: use a global output format setting
        if output: Pager.page(output)
    
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
@click.option('-s', '--stage', metavar='<name>[/<number>]', default='default', help=f"{CLI_PARAMETERS_HELP['common']['stage']}")
@click.option('-f', '--format', required=False, type=click.Choice(['json', 'yaml', 'raw', 'csv']), default='json', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['format']}")
@click.option('-b', '--verbosity', metavar='<number>', required=False, type=RangeParamType(click.INT, minimum=0, maximum=5), default='2', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['verbosity']}")
@click.option('--config', metavar='<key>=<value>,...', required=False, help=f"{CLI_PARAMETERS_HELP['common']['config']}")
@click.option('-w','--working-dir', metavar='<path>', type=click.Path(exists=True, file_okay=False), required=False, default='.', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['working_dir']}")
def list_package(stage, format, verbosity, config, working_dir):
    """
    Return the list of all available packages generated for a stage.\n
    \tENV: Name of the environment
    """
    
    def validate_command_usage():
        pass

    try:
        Logger.set_verbosity(verbosity)
        validate_command_usage()
        Config.load(working_dir if working_dir else os.getcwd(), config)

        raise NotImplementedError("Not implemented.")
    
    except DSOException as e:
        Logger.error(e.message)
    except Exception as e:
        msg = getattr(e, 'message', getattr(e, 'msg', str(e)))
        Logger.critical(msg)
        if verbosity >= log_levels['full']:
            raise

###--------------------------------------------------------------------------------------------

@package.command('download', context_settings=DEFAULT_CLICK_CONTEXT, short_help="Download a package")
@click.option('-s', '--stage', metavar='<name>[/<number>]', default='default', help=f"{CLI_PARAMETERS_HELP['common']['stage']}")
@click.option('-p', '--package', default='default', help=f"{CLI_PARAMETERS_HELP['common']['stage']}")
@click.option('-f', '--format', required=False, type=click.Choice(['json', 'yaml', 'raw', 'csv']), default='json', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['format']}")
@click.option('-b', '--verbosity', metavar='<number>', required=False, type=RangeParamType(click.INT, minimum=0, maximum=5), default='2', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['verbosity']}")
@click.option('--config', metavar='<key>=<value>,...', required=False, help=f"{CLI_PARAMETERS_HELP['common']['config']}")
@click.option('-w','--working-dir', metavar='<path>', type=click.Path(exists=True, file_okay=False), required=False, default='.', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['working_dir']}")
def download_package(stage, package, format, verbosity, config, working_dir):
    """
    Downlaod a package generated for a stage.\n
    \tENV: Name of the environment\n
    \tPACKAGE: Version of the package to download
    """

    def validate_command_usage():
        pass

    try:
        Logger.set_verbosity(verbosity)
        validate_command_usage()
        Config.load(working_dir if working_dir else os.getcwd(), config)

        raise NotImplementedError("Not implemented.")
    
    except DSOException as e:
        Logger.error(e.message)
    except Exception as e:
        msg = getattr(e, 'message', getattr(e, 'msg', str(e)))
        Logger.critical(msg)
        if verbosity >= log_levels['full']:
            raise

###--------------------------------------------------------------------------------------------

@package.command('create', context_settings=DEFAULT_CLICK_CONTEXT, short_help="Create a package")
@click.option('-s', '--stage', metavar='<name>[/<number>]', default='default', help=f"{CLI_PARAMETERS_HELP['common']['stage']}")
@click.option('-d', '--description', default='default', help=f"{CLI_PARAMETERS_HELP['common']['stage']}")
@click.option('-f', '--format', required=False, type=click.Choice(['json', 'yaml', 'raw', 'csv']), default='json', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['format']}")
@click.option('-b', '--verbosity', metavar='<number>', required=False, type=RangeParamType(click.INT, minimum=0, maximum=5), default='2', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['verbosity']}")
@click.option('--config', metavar='<key>=<value>,...', required=False, help=f"{CLI_PARAMETERS_HELP['common']['config']}")
@click.option('-w','--working-dir', metavar='<path>', type=click.Path(exists=True, file_okay=False), required=False, default='.', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['working_dir']}")
def create_package(stage, description, format, verbosity, config, working_dir):
    """
    Create a new build package for the application.\n
    \tENV: Name of the environment\n
    \tDESCRIPTION (optional): Description of the package
    """

    def validate_command_usage():
        pass

    try:
        Logger.set_verbosity(verbosity)
        validate_command_usage()
        Config.load(working_dir if working_dir else os.getcwd(), config)

        raise NotImplementedError("Not implemented.")
    
    except DSOException as e:
        Logger.error(e.message)
    except Exception as e:
        msg = getattr(e, 'message', getattr(e, 'msg', str(e)))
        Logger.critical(msg)
        if verbosity >= log_levels['full']:
            raise

###--------------------------------------------------------------------------------------------

@package.command('delete', context_settings=DEFAULT_CLICK_CONTEXT, short_help="Delete a package")
@click.option('-s', '--stage', metavar='<name>[/<number>]', default='default', help=f"{CLI_PARAMETERS_HELP['common']['stage']}")
@click.option('-p', '--package', default='default', help=f"{CLI_PARAMETERS_HELP['common']['stage']}")
@click.option('-f', '--format', required=False, type=click.Choice(['json', 'yaml', 'raw', 'csv']), default='json', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['format']}")
@click.option('-b', '--verbosity', metavar='<number>', required=False, type=RangeParamType(click.INT, minimum=0, maximum=5), default='2', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['verbosity']}")
@click.option('--config', metavar='<key>=<value>,...', required=False, help=f"{CLI_PARAMETERS_HELP['common']['config']}")
@click.option('-w','--working-dir', metavar='<path>', type=click.Path(exists=True, file_okay=False), required=False, default='.', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['working_dir']}")
def delete_package(stage, package, format, verbosity, config, working_dir):
    """
    Delete a package from a stage.\n
    \tENV: Name of the environment\n
    \tPACKAGE: Version of the package to be deleted
    """

    def validate_command_usage():
        pass

    try:
        Logger.set_verbosity(verbosity)
        validate_command_usage()
        Config.load(working_dir if working_dir else os.getcwd(), config)

        raise NotImplementedError("Not implemented.")
    
    except DSOException as e:
        Logger.error(e.message)
    except Exception as e:
        msg = getattr(e, 'message', getattr(e, 'msg', str(e)))
        Logger.critical(msg)
        if verbosity >= log_levels['full']:
            raise

###--------------------------------------------------------------------------------------------

@release.command('list', context_settings=DEFAULT_CLICK_CONTEXT, short_help="List available releases")
@click.option('-s', '--stage', metavar='<name>[/<number>]', default='default', help=f"{CLI_PARAMETERS_HELP['common']['stage']}")
@click.option('-f', '--format', required=False, type=click.Choice(['json', 'yaml', 'raw', 'csv']), default='json', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['format']}")
@click.option('-b', '--verbosity', metavar='<number>', required=False, type=RangeParamType(click.INT, minimum=0, maximum=5), default='2', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['verbosity']}")
@click.option('--config', metavar='<key>=<value>,...', required=False, help=f"{CLI_PARAMETERS_HELP['common']['config']}")
@click.option('-w','--working-dir', metavar='<path>', type=click.Path(exists=True, file_okay=False), required=False, default='.', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['working_dir']}")
def list_release(stage, format, verbosity, config, working_dir):
    """
    Return the list of all available releases generated for a stage.\n
    \tENV: Name of the environment
    """

    def validate_command_usage():
        pass

    try:
        Logger.set_verbosity(verbosity)
        validate_command_usage()
        Config.load(working_dir if working_dir else os.getcwd(), config)

        raise NotImplementedError("Not implemented.")
    
    except DSOException as e:
        Logger.error(e.message)
    except Exception as e:
        msg = getattr(e, 'message', getattr(e, 'msg', str(e)))
        Logger.critical(msg)
        if verbosity >= log_levels['full']:
            raise

###--------------------------------------------------------------------------------------------

@release.command('download', context_settings=DEFAULT_CLICK_CONTEXT, short_help="Download a release")
@click.option('-s', '--stage', metavar='<name>[/<number>]', default='default', help=f"{CLI_PARAMETERS_HELP['common']['stage']}")
@click.option('-r', '--release', default='default', help=f"{CLI_PARAMETERS_HELP['common']['stage']}")
@click.option('-f', '--format', required=False, type=click.Choice(['json', 'yaml', 'raw', 'csv']), default='json', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['format']}")
@click.option('-b', '--verbosity', metavar='<number>', required=False, type=RangeParamType(click.INT, minimum=0, maximum=5), default='2', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['verbosity']}")
@click.option('--config', metavar='<key>=<value>,...', required=False, help=f"{CLI_PARAMETERS_HELP['common']['config']}")
@click.option('-w','--working-dir', metavar='<path>', type=click.Path(exists=True, file_okay=False), required=False, default='.', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['working_dir']}")
def download_release(stage, release, format, verbosity, config, working_dir):
    """
    Downlaod a release generated for a stage.\n
    \tENV: Name of the environment\n
    \tRELEASE: Version of the release
    """

    def validate_command_usage():
        pass

    try:
        Logger.set_verbosity(verbosity)
        validate_command_usage()
        Config.load(working_dir if working_dir else os.getcwd(), config)

        raise NotImplementedError("Not implemented.")
    
    except DSOException as e:
        Logger.error(e.message)
    except Exception as e:
        msg = getattr(e, 'message', getattr(e, 'msg', str(e)))
        Logger.critical(msg)
        if verbosity >= log_levels['full']:
            raise

###--------------------------------------------------------------------------------------------

@release.command('create', context_settings=DEFAULT_CLICK_CONTEXT, short_help="Create a release")
@click.option('-s', '--stage', metavar='<name>[/<number>]', default='default', help=f"{CLI_PARAMETERS_HELP['common']['stage']}")
@click.option('-d', '--description', help=f"{CLI_PARAMETERS_HELP['common']['stage']}")
@click.option('-f', '--format', required=False, type=click.Choice(['json', 'yaml', 'raw', 'csv']), default='json', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['format']}")
@click.option('-b', '--verbosity', metavar='<number>', required=False, type=RangeParamType(click.INT, minimum=0, maximum=5), default='2', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['verbosity']}")
@click.option('--config', metavar='<key>=<value>,...', required=False, help=f"{CLI_PARAMETERS_HELP['common']['config']}")
@click.option('-w','--working-dir', metavar='<path>', type=click.Path(exists=True, file_okay=False), required=False, default='.', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['working_dir']}")
def create_release(stage, description, format, verbosity, config, working_dir):
    """
    Create a new release for a stage.\n
    \tENV: Name of the environment\n
    \tPACKAGE: Version of the package to be used for creating the release\n
    \tDESCRIPTION (optional): Description of the release
    """

    def validate_command_usage():
        pass

    try:
        Logger.set_verbosity(verbosity)
        validate_command_usage()
        Config.load(working_dir if working_dir else os.getcwd(), config)

        raise NotImplementedError("Not implemented.")
    
    except DSOException as e:
        Logger.error(e.message)
    except Exception as e:
        msg = getattr(e, 'message', getattr(e, 'msg', str(e)))
        Logger.critical(msg)
        if verbosity >= log_levels['full']:
            raise


###--------------------------------------------------------------------------------------------

@release.command('delete', context_settings=DEFAULT_CLICK_CONTEXT, short_help="Delete a release")
@click.option('-s', '--stage', metavar='<name>[/<number>]', default='default', help=f"{CLI_PARAMETERS_HELP['common']['stage']}")
@click.option('-r', '--release', default='default', help=f"{CLI_PARAMETERS_HELP['common']['stage']}")
@click.option('-f', '--format', required=False, type=click.Choice(['json', 'yaml', 'raw', 'csv']), default='json', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['format']}")
@click.option('-b', '--verbosity', metavar='<number>', required=False, type=RangeParamType(click.INT, minimum=0, maximum=5), default='2', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['verbosity']}")
@click.option('--config', metavar='<key>=<value>,...', required=False, help=f"{CLI_PARAMETERS_HELP['common']['config']}")
@click.option('-w','--working-dir', metavar='<path>', type=click.Path(exists=True, file_okay=False), required=False, default='.', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['working_dir']}")
def delete_release(stage, release, format, verbosity, config, working_dir):
    """
    Delete a release from a stage.\n
    \tENV: Name of the environment\n
    \tRELEASE: Version of the release to be deleted
    """

    def validate_command_usage():
        pass

    try:
        Logger.set_verbosity(verbosity)
        validate_command_usage()
        Config.load(working_dir if working_dir else os.getcwd(), config)

        raise NotImplementedError("Not implemented.")
    
    except DSOException as e:
        Logger.error(e.message)
    except Exception as e:
        msg = getattr(e, 'message', getattr(e, 'msg', str(e)))
        Logger.critical(msg)
        if verbosity >= log_levels['full']:
            raise

###--------------------------------------------------------------------------------------------

@release.command('deploy', context_settings=DEFAULT_CLICK_CONTEXT, short_help="Deploy a release")
@click.option('-s', '--stage', metavar='<name>[/<number>]', default='default', help=f"{CLI_PARAMETERS_HELP['common']['stage']}")
@click.option('-r', '--release', default='default', help=f"{CLI_PARAMETERS_HELP['common']['stage']}")
@click.option('-f', '--format', required=False, type=click.Choice(['json', 'yaml', 'raw', 'csv']), default='json', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['format']}")
@click.option('-b', '--verbosity', metavar='<number>', required=False, type=RangeParamType(click.INT, minimum=0, maximum=5), default='2', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['verbosity']}")
@click.option('--config', metavar='<key>=<value>,...', required=False, help=f"{CLI_PARAMETERS_HELP['common']['config']}")
@click.option('-w','--working-dir', metavar='<path>', type=click.Path(exists=True, file_okay=False), required=False, default='.', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['working_dir']}")
def deploy_release(stage, release, format, verbosity, config, working_dir):
    """
    Delete a release from a stage.\n
    \tENV: Name of the environment\n
    \tRELEASE: Version of the release to be deleted
    """

    def validate_command_usage():
        pass

    try:
        Logger.set_verbosity(verbosity)
        validate_command_usage()
        Config.load(working_dir if working_dir else os.getcwd(), config)

        raise NotImplementedError("Not implemented.")
    
    except DSOException as e:
        Logger.error(e.message)
    except Exception as e:
        msg = getattr(e, 'message', getattr(e, 'msg', str(e)))
        Logger.critical(msg)
        if verbosity >= log_levels['full']:
            raise

###--------------------------------------------------------------------------------------------

@config.command('get', context_settings=DEFAULT_CLICK_CONTEXT, short_help=f"{CLI_COMMANDS_SHORT_HELP['config']['get']}")
@command_doc(CLI_COMMANDS_HELP['config']['get'])
@click.argument('key', required=False)
@click.option('-l','--local', is_flag=True, default=False, help=f"{CLI_PARAMETERS_HELP['config']['local']}")
@click.option('-g','--global', 'global_', is_flag=True, default=False, help=f"{CLI_PARAMETERS_HELP['config']['global']}")
@click.option('-b', '--verbosity', metavar='<number>', required=False, type=RangeParamType(click.INT, minimum=0, maximum=5), default='2', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['verbosity']}")
@click.option('--config', metavar='<key>=<value>,...', required=False, help=f"{CLI_PARAMETERS_HELP['common']['config']}")
@click.option('-w','--working-dir', metavar='<path>', type=click.Path(exists=True, file_okay=False), required=False, default='.', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['working_dir']}")
def get_config(key, local, global_, verbosity, config, working_dir):

    scope = None

    def validate_command_usage():
        nonlocal scope
        validate_not_all_provided([local, global_], ["'-l' / '--local'", "'-g' / '--global'"])
        scope = 'local' if local else 'global' if global_ else ''

    try:
        Logger.set_verbosity(verbosity)
        validate_command_usage()
        Config.load(working_dir if working_dir else os.getcwd(), config)

        print(yaml.dump(Config.get(key, scope), sort_keys=False, indent=2), flush=True)

    except DSOException as e:
        Logger.error(e.message)
    except Exception as e:
        msg = getattr(e, 'message', getattr(e, 'msg', str(e)))
        Logger.critical(msg)
        if verbosity >= log_levels['full']:
            raise

###--------------------------------------------------------------------------------------------

@config.command('set', context_settings=DEFAULT_CLICK_CONTEXT, short_help=f"{CLI_COMMANDS_SHORT_HELP['config']['set']}")
@command_doc(CLI_COMMANDS_HELP['config']['set'])
@click.argument('key', required=False)
@click.option('-k', '--key', 'key_option', metavar='<value>', required=False, help=f"{CLI_PARAMETERS_HELP['config']['key']}")
@click.argument('value', required=False)
@click.option('-v', '--value', 'value_option', metavar='<value>', required=False, help=f"{CLI_PARAMETERS_HELP['config']['value']}")
@click.option('-g','--global', 'global_', is_flag=True, default=False, help=f"{CLI_PARAMETERS_HELP['config']['global']}")
@click.option('-i', '--input', metavar='<path>', required=False, type=click.File(encoding='utf-8', mode='r'), help=f"{CLI_PARAMETERS_HELP['config']['input']}")
@click.option('-b', '--verbosity', metavar='<number>', required=False, type=RangeParamType(click.INT, minimum=0, maximum=5), default='2', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['verbosity']}")
@click.option('--config', metavar='<key>=<value>,...', required=False, help=f"{CLI_PARAMETERS_HELP['common']['config']}")
@click.option('-w','--working-dir', metavar='<path>', type=click.Path(exists=True, file_okay=False), required=False, default='.', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['working_dir']}")
def set_config(key, key_option, value, value_option, global_, input, verbosity, config, working_dir):

    def validate_command_usage():
        nonlocal key, value
        validate_not_all_provided([key, key_option], ["KEY", "'-k' / '--key'"])
        key = validate_at_least_one_provided([key, key_option], ["KEY", "'-k' / '--key'"])

        if input:
            validate_none_provided([value, value_option], ["VALUE", "'-v' / '--value'"], ["'-i' / '--input'"])
            try:
                value = yaml.load(input, yaml.SafeLoader)
            # except yaml.YAMLError as e:
            except:
                raise DSOException(CLI_MESSAGES['InvalidFileFormat'].format('yaml'))
        else:
            validate_not_all_provided([key, key_option], ["VALUE", "'-v' / '--value'"])
            value = validate_only_one_provided([value, value_option], ["VALUE", "'-v' / '--value'"])

    try:
        Logger.set_verbosity(verbosity)
        Config.load(working_dir if working_dir else os.getcwd(), config)
        validate_command_usage()
        Config.set(key, value, global_)

    except DSOException as e:
        Logger.error(e.message)
    except Exception as e:
        msg = getattr(e, 'message', getattr(e, 'msg', str(e)))
        Logger.critical(msg)
        if verbosity >= log_levels['full']:
            raise

###--------------------------------------------------------------------------------------------

@config.command('delete', context_settings=DEFAULT_CLICK_CONTEXT, short_help=f"{CLI_COMMANDS_SHORT_HELP['config']['delete']}")
@command_doc(CLI_COMMANDS_HELP['config']['set'])
@click.argument('key', required=False)
@click.option('-k', '--key', 'key_option', metavar='<value>', required=False, help=f"{CLI_PARAMETERS_HELP['config']['key']}")
@click.option('-g','--global', 'global_', is_flag=True, default=False, help=f"{CLI_PARAMETERS_HELP['config']['global']}")
@click.option('-b', '--verbosity', metavar='<number>', required=False, type=RangeParamType(click.INT, minimum=0, maximum=5), default='2', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['verbosity']}")
@click.option('--config', metavar='<key>=<value>,...', required=False, help=f"{CLI_PARAMETERS_HELP['common']['config']}")
@click.option('-w','--working-dir', metavar='<path>', type=click.Path(exists=True, file_okay=False), required=False, default='.', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['working_dir']}")
def delete_config(key, key_option, global_, verbosity, config, working_dir):

    def validate_command_usage():
        nonlocal key
        validate_not_all_provided([key, key_option], ["KEY", "'-k' / '--key'"])
        key = validate_at_least_one_provided([key, key_option], ["KEY", "'-k' / '--key'"])

    try:
        Logger.set_verbosity(verbosity)
        Config.load(working_dir if working_dir else os.getcwd(), config)
        validate_command_usage()
        Config.delete(key, global_)

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

#     def validate_command_usage():
#         pass

#     try:
#         Logger.set_verbosity(verbosity)
#         Config.load(working_dir if working_dir else os.getcwd(), config)
#         validate_command_usage()


#     except DSOException as e:
#         Logger.error(e.message)
#     except Exception as e:
#         msg = getattr(e, 'message', getattr(e, 'msg', str(e)))
#         Logger.critical(msg)
#         if verbosity >= log_levels['full']:
#             raise

###--------------------------------------------------------------------------------------------

@config.command('init', context_settings=DEFAULT_CLICK_CONTEXT, short_help=f"{CLI_COMMANDS_SHORT_HELP['config']['init']}")
@command_doc(CLI_COMMANDS_HELP['config']['init'])
@click.option('--setup', is_flag=True, required=False, help=f"{CLI_PARAMETERS_HELP['config']['setup']}")
@click.option('-l','--local', is_flag=True, default=False, help=f"{CLI_PARAMETERS_HELP['config']['init_local']}")
@click.option('-i', '--input', metavar='<path>', required=False, type=click.File(encoding='utf-8', mode='r'), help=f"{CLI_PARAMETERS_HELP['config']['input']}")
@click.option('-b', '--verbosity', metavar='<number>', required=False, type=RangeParamType(click.INT, minimum=0, maximum=5), default='2', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['verbosity']}")
@click.option('--config', metavar='<key>=<value>,...', required=False, help=f"{CLI_PARAMETERS_HELP['common']['config']}")
@click.option('-w','--working-dir', metavar='<path>', type=click.Path(exists=True, file_okay=False), required=False, default='.', show_default=True, help=f"{CLI_PARAMETERS_HELP['common']['working_dir']}")
def init_config(setup, local, input, verbosity, config, working_dir):

    init_config = None

    def validate_command_usage():
        nonlocal init_config

        if input:
            # if local:
            #     Logger.warn("Option '--local' is not needed when '--input' specifies the initial configuration, as it will always be overriden locally.")
            try:
                init_config = yaml.load(input, yaml.SafeLoader)
            except:
                raise DSOException(CLI_MESSAGES['InvalidFileFormat'].format('yaml'))

    try:
        Logger.set_verbosity(verbosity)
        validate_command_usage()
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
