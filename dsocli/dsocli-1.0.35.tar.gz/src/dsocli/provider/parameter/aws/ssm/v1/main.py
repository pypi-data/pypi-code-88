import os
import re
import yaml
import json
import pathlib
import numbers
import boto3
from botocore.exceptions import ClientError
from dsocli.exceptions import DSOException
from dsocli.logger import Logger
from dsocli.config import Config
from dsocli.providers import ProviderManager
from dsocli.parameters import ParameterProvider
from dsocli.stages import Stages
from dsocli.constants import *
from dsocli.utils import set_dict_value


default_spec = {
}


session = boto3.session.Session()
ssm = session.client(
    service_name='ssm',
    region_name='ap-southeast-2',
)


class AwsSsmParameterProvider(ParameterProvider):

    def __init__(self):
        super().__init__('parameter/aws/ssm/v1')

###--------------------------------------------------------------------------------------------

    def get_parameter_prefix(self, project, application, stage, key=None):
        # output = f"/dso/{project}/{application}/{stage}"
        output = "/dso"
        output += f"/{project}"
        ### every application must belong to a project, no application overrides allowed in the default project
        if not project == 'default':
            output += f"/{application}"
        else:
            output += "/default"
        stage = Stages.normalize(stage)
        output += f"/{stage}"
        if key:
            output += f"/{key}"
        return output

###--------------------------------------------------------------------------------------------
###--------------------------------------------------------------------------------------------

    def get_key_validator(self):

        # return r"^([a-zA-Z][a-zA-Z0-9]*/)?([a-zA-Z][a-zA-Z0-9_.-]*)$"
        return r"^([a-zA-Z][a-zA-Z0-9_.-]*)$"

###--------------------------------------------------------------------------------------------

    def assert_no_scope_overwrites(self, project, application, stage, key):
        """
            check if a parameter will overwrite parent or childern parameters (with the same scopes) in the same stage (always uninherited)
            e.g.: 
                parameter a.b.c would overwrite a.b (super scope)
                parameter a.b would overwrite a.b.c (sub scope)
        """
        Logger.debug(f"Checking parameter overwrites: project={project}, application={application}, stage={stage}, key={key}")
        
        ### check children parameters
        path = self.get_parameter_prefix(project, application, stage, key)
        # parameters = ssm.describe_parameters(ParameterFilters=[{'Key':'Type','Values':['String', 'StringList']},{'Key':'Name', 'Option': 'BeginsWith', 'Values':[f"{path}."]}])
        parameters = ssm.describe_parameters(ParameterFilters=[{'Key':'Name', 'Option': 'BeginsWith', 'Values':[f"{path}."]}])
        if len(parameters['Parameters']) > 0:
            raise DSOException("Parameter key '{0}' is not allowed in the given stage becasue it would overwrite all the parameters in '{0}.*', such as '{0}.{1}'.".format(key,parameters['Parameters'][0]['Name'][len(path)+1:]))

        ### check parent parameters
        scopes = key.split('.')
        for n in range(len(scopes)-1):
            subKey = '.'.join(scopes[0:n+1])
            path = self.get_parameter_prefix(project, application, stage, subKey)
            Logger.debug(f"Describing parameters: path={path}")
            # parameters = ssm.describe_parameters(ParameterFilters=[{'Key':'Type', 'Values':['String', 'StringList']},{'Key':'Name', 'Values':[path]}])
            parameters = ssm.describe_parameters(ParameterFilters=[{'Key':'Name', 'Values':[path]}])
            if len(parameters['Parameters']) > 0:
                raise DSOException("Parameter key '{0}' is not allowed in the given stage becasue it would overwrite parameter '{1}'.".format(key, subKey))

###--------------------------------------------------------------------------------------------

    def locate_parameter(self, project, application, stage, key, uninherited=False):
        Logger.debug(f"Locating SSM parameter: project={project}, application={application}, stage={stage}, key={key}")
        paths = self.get_ssm_search_paths(project, application, stage, key, uninherited)
        Logger.debug(f"SSM paths to search in order: {paths}")
        for path in paths:
            Logger.debug(f"Describing SSM parameters: path={path}")
            # result = ssm.describe_parameters(ParameterFilters=[{'Key':'Type','Values':['String', 'StringList']},{'Key':'Name', 'Values':[path]}])
            result = ssm.describe_parameters(ParameterFilters=[{'Key':'Name', 'Values':[path]}])
            if len(result['Parameters']) > 0: return result['Parameters']

###--------------------------------------------------------------------------------------------

    def load_ssm_path(self, parameters, path, recurisve=True):
        Logger.debug(f"Loading SSM parameters: path={path}")
        p = ssm.get_paginator('get_parameters_by_path')
        paginator = p.paginate(Path=path, Recursive=recurisve, ParameterFilters=[{'Key': 'Type','Values': ['String', 'StringList']}]).build_full_result()
        for parameter in paginator['Parameters']:
            key = parameter['Name'][len(path)+1:]
            value = parameter['Value']
            if key in parameters:
                Logger.warn("Inherited parameter '{0}' overridden.".format(key))
            parameters[key] = {'Value': value, 'Path': path}
        return parameters

###--------------------------------------------------------------------------------------------

    def get_ssm_search_paths(self, project, application, stage, key, uninherited):
        paths = []
        if uninherited:
            paths.append(self.get_parameter_prefix(project, application, stage, key))
        else:
            ### check /dso/project/application/stage/env
            paths.append(self.get_parameter_prefix(project, application, stage, key))
            if not Stages.is_stage_default_env(stage): ### otherwise already added above
                ### check /dso/project/application/stage/default
                paths.append(self.get_parameter_prefix(project, application, Stages.get_stage_default_env(stage), key))
            if not Stages.is_default(stage): ### otherwise already added above
                ### check /dso/project/application/default
                 paths.append(self.get_parameter_prefix(project, application, Stages.default_stage(), key))
            if not application == 'default': ### otherwise already added above
                ### check /dso/project/default/stage/env
                paths.append(self.get_parameter_prefix(project, 'default', stage, key))
                if not Stages.is_stage_default_env(stage): ### otherwise already added above
                    ### check /dso/project/default/stage/default
                    paths.append(self.get_parameter_prefix(project, 'default', Stages.get_stage_default_env(stage), key))
                if not Stages.is_default(stage): ### otherwise already added above
                    ### check /dso/project/default/default
                    paths.append(self.get_parameter_prefix(project, 'default', Stages.default_stage(), key))
                if not project == 'default': ### otherwise already added above
                    ### check /dso/default/default/stage/env
                    paths.append(self.get_parameter_prefix('default', 'default', stage, key))
                    if not Stages.is_stage_default_env(stage): ### otherwise already added above
                        ### check /dso/default/default/stage/default
                        paths.append(self.get_parameter_prefix('default', 'default', Stages.get_stage_default_env(stage), key))
                    if not Stages.is_default(stage): ### otherwise already added above
                        ### check /dso/default/default/default
                        paths.append(self.get_parameter_prefix('default', 'default', Stages.default_stage(), key))

        return paths

###--------------------------------------------------------------------------------------------

    def list(self, project, application, stage, uninherited):
        ### construct search path in hierachy with no key specified in reverse order
        paths = list(reversed(self.get_ssm_search_paths(project, application, stage, None, uninherited)))
        # Logger.debug(f"SSM paths to search in order: {paths}")
        parameters = {}
        for path in paths:
            self.load_ssm_path(parameters, path)

        result = {'Parameters': []}
        for item in parameters.items():
            result['Parameters'].append({'Key': item[0], 'Value': item[1]['Value'], 'Path': item[1]['Path']})

        return result

###--------------------------------------------------------------------------------------------

    def add(self, project, application, stage, key, value):
        self.assert_no_scope_overwrites(project, application, stage, key)
        found = self.locate_parameter(project, application, stage, key, True)
        if found and len(found) > 0 and not found[0]['Type'] in ['String', 'StringList']:
            raise DSOException(f"Failed to add parameter '{key}' becasue there is already a SSM secret with the same key in the given stage.")
        path = self.get_parameter_prefix(project, application, stage=stage, key=key)
        Logger.info(f"Adding SSM parameter: path={path}")
        ssm.put_parameter(Name=path, Value=value, Type='String', Overwrite=True)

###--------------------------------------------------------------------------------------------

    def get(self, project, application, stage, key):
        found = self.locate_parameter(project, application, stage, key)
        if not found or len(found) == 0:
            raise DSOException(f"Parameter '{key}' not found: project={project}, application={application}, stage={Stages.shorten(stage)}")
        else:
            # if len(found) > 1:
            #     Logger.warn(f"More than one parameter found at '{found[0]['Name']}'. The first one taken, and the rest were discarded.")
            if not found[0]['Type'] in ['String', 'StringList']:
                raise DSOException(f"Parameter '{key}' not found: project={project}, application={application}, stage={Stages.shorten(stage)}")
        Logger.info(f"Getting SSM parameter: path={found[0]['Name']}")
        result = ssm.get_parameter(Name=found[0]['Name'], WithDecryption=True)
        return result['Parameter']['Value']

###--------------------------------------------------------------------------------------------

    def delete(self, project, application, stage, key):
        ### only parameters owned by the stage can be deleted, hence uninherited=True
        found = self.locate_parameter(project, application, stage, key, uninherited=True)
        if not found or len(found) == 0:
            raise DSOException(f"Parameter '{key}' not found: project={project}, application={application}, stage={Stages.shorten(stage)}")
        else:
            # if len(found) > 1:
            #     Logger.warn(f"More than one parameter found at '{found[0]['Name']}'. The first one taken, and the rest were discarded.")
            if not found[0]['Type'] in ['String', 'StringList']:
                raise DSOException(f"Parameter '{key}' not found: project={project}, application={application}, stage={Stages.shorten(stage)}")
        Logger.info(f"Deleting SSM parameter: path={found[0]['Name']}")
        ssm.delete_parameter(Name=found[0]['Name'])


###--------------------------------------------------------------------------------------------
###--------------------------------------------------------------------------------------------
###--------------------------------------------------------------------------------------------

ProviderManager.register(AwsSsmParameterProvider())
