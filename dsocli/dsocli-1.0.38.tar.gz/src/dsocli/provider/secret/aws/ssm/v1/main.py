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
from dsocli.secrets import SecretProvider
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


class AwsSsmSecretProvider(SecretProvider):

    def __init__(self):
        super().__init__('secret/aws/ssm/v1')

###--------------------------------------------------------------------------------------------
###--------------------------------------------------------------------------------------------

    def get_secret_prefix(self, project, application, stage, key=None):
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

    def get_key_validator(self):

        # return r"^([a-zA-Z][a-zA-Z0-9]*/)?([a-zA-Z][a-zA-Z0-9_.-]*)$"
        return r"^([a-zA-Z][a-zA-Z0-9_.-]*)$"

###--------------------------------------------------------------------------------------------

    def assert_no_scope_overwrites(self, project, application, stage, key):
        """
            check if a secret will overwrite parent or childern secrets (with the same scopes) in the same stage (always uninherited)
            e.g.: 
                secret a.b.c would overwrite a.b (super scope)
                secret a.b would overwrite a.b.c (sub scope)
        """
        Logger.debug(f"Checking secret overwrites: project={project}, application={application}, stage={stage}, key={key}")
        
        ### check children secrets
        path = self.get_secret_prefix(project, application, stage, key)
        # secrets = ssm.describe_parameters(ParameterFilters=[{'Key':'Type','Values':['SecureString']},{'Key':'Name', 'Option': 'BeginsWith', 'Values':[f"{path}."]}])
        secrets = ssm.describe_parameters(ParameterFilters=[{'Key':'Name', 'Option': 'BeginsWith', 'Values':[f"{path}."]}])
        if len(secrets['Parameters']) > 0:
            raise DSOException("Secret key '{0}' is not allowed in the given stage becasue it would overwrite all the secrets in '{0}.*', such as '{0}.{1}'.".format(key,secrets['Parameters'][0]['Name'][len(path)+1:]))

        ### check parent secrets
        scopes = key.split('.')
        for n in range(len(scopes)-1):
            subKey = '.'.join(scopes[0:n+1])
            path = self.get_secret_prefix(project, application, stage, subKey)
            Logger.debug(f"Describing secrets: path={path}")
            # secrets = ssm.describe_parameters(ParameterFilters=[{'Key':'Type', 'Values':['SecureString']},{'Key':'Name', 'Values':[path]}])
            secrets = ssm.describe_parameters(ParameterFilters=[{'Key':'Name', 'Values':[path]}])
            if len(secrets['Parameters']) > 0:
                raise DSOException("Secret key '{0}' is not allowed in the given stage becasue it would overwrite secret '{1}'.".format(key, subKey))

###--------------------------------------------------------------------------------------------

    def locate_secret(self, project, application, stage, key, uninherited=False):
        Logger.debug(f"Locating SSM secret: project={project}, application={application}, stage={stage}, key={key}")
        paths = self.get_ssm_search_paths(project, application, stage, key, uninherited)
        Logger.debug(f"SSM paths to search in order: {paths}")
        for path in paths:
            Logger.debug(f"Describing SSM secrets: path={path}")
            # result = ssm.describe_parameters(ParameterFilters=[{'Key':'Type','Values':['SecureString']},{'Key':'Name', 'Values':[path]}])
            result = ssm.describe_parameters(ParameterFilters=[{'Key':'Name', 'Values':[path]}])
            if len(result['Parameters']) > 0: return result['Parameters']

###--------------------------------------------------------------------------------------------

    def load_ssm_path(self, secrets, path, decrypt, recurisve=True):
        Logger.debug(f"Loading SSM secrets: path={path}")
        p = ssm.get_paginator('get_parameters_by_path')
        paginator = p.paginate(Path=path, Recursive=recurisve, WithDecryption=decrypt, ParameterFilters=[{'Key': 'Type','Values': ['SecureString']}]).build_full_result()
        for secret in paginator['Parameters']:
            key = secret['Name'][len(path)+1:]
            value = secret['Value']
            if key in secrets:
                Logger.warn("Inherited secret '{0}' overridden.".format(key))
            secrets[key] = {'Value': value, 'Path': path}
        return secrets

###--------------------------------------------------------------------------------------------

    def get_ssm_search_paths(self, project, application, stage, key, uninherited):
        paths = []
        if uninherited:
            paths.append(self.get_secret_prefix(project, application, stage, key))
        else:
            ### check /dso/project/application/stage/env
            paths.append(self.get_secret_prefix(project, application, stage, key))
            if not Stages.is_stage_default_env(stage): ### otherwise already added above
                ### check /dso/project/application/stage/default
                paths.append(self.get_secret_prefix(project, application, Stages.get_stage_default_env(stage), key))
            if not Stages.is_default(stage): ### otherwise already added above
                ### check /dso/project/application/default
                 paths.append(self.get_secret_prefix(project, application, Stages.default_stage(), key))
            if not application == 'default': ### otherwise already added above
                ### check /dso/project/default/stage/env
                paths.append(self.get_secret_prefix(project, 'default', stage, key))
                if not Stages.is_stage_default_env(stage): ### otherwise already added above
                    ### check /dso/project/default/stage/default
                    paths.append(self.get_secret_prefix(project, 'default', Stages.get_stage_default_env(stage), key))
                if not Stages.is_default(stage): ### otherwise already added above
                    ### check /dso/project/default/default
                    paths.append(self.get_secret_prefix(project, 'default', Stages.default_stage(), key))
                if not project == 'default': ### otherwise already added above
                    ### check /dso/default/default/stage/env
                    paths.append(self.get_secret_prefix('default', 'default', stage, key))
                    if not Stages.is_stage_default_env(stage): ### otherwise already added above
                        ### check /dso/default/default/stage/default
                        paths.append(self.get_secret_prefix('default', 'default', Stages.get_stage_default_env(stage), key))
                    if not Stages.is_default(stage): ### otherwise already added above
                        ### check /dso/default/default/default
                        paths.append(self.get_secret_prefix('default', 'default', Stages.default_stage(), key))

        return paths

###--------------------------------------------------------------------------------------------

    def list(self, project, application, stage, uninherited, decrypt):
        ### construct search path in hierachy with no key specified in reverse order
        paths = list(reversed(self.get_ssm_search_paths(project, application, stage, None, uninherited)))
        # Logger.debug(f"SSM paths to search in order: {paths}")
        secrets = {}
        for path in paths:
            self.load_ssm_path(secrets, path, decrypt)

        result = {'Secrets': []}
        for item in secrets.items():
            result['Secrets'].append({'Key': item[0], 'Value': item[1]['Value'], 'Path': item[1]['Path']})

        return result

###--------------------------------------------------------------------------------------------

    def add(self, project, application, stage, key, value):
        self.assert_no_scope_overwrites(project, application, stage, key)
        found = self.locate_secret(project, application, stage, key, True)
        if found and len(found) > 0 and not found[0]['Type'] in ['SecureString']:
            raise DSOException(f"Failed to add secret '{key}' becasue there is already a SSM parameter with the same key in the given context: project={project}, application={application}, stage={Stages.shorten(stage)}")
        path = self.get_secret_prefix(project, application, stage=stage, key=key)
        Logger.info(f"Adding SSM secret: path={path}")
        ssm.put_parameter(Name=path, Value=value, Type='SecureString', Overwrite=True)

###--------------------------------------------------------------------------------------------

    def get(self, project, application, stage, key):
        found = self.locate_secret(project, application, stage, key)
        if not found or len(found) == 0:
                raise DSOException(f"Secret '{key}' not found: project={project}, application={application}, stage={Stages.shorten(stage)}")
        else:
            # if len(found) > 1:
            #     Logger.warn(f"More than one secret found at '{found[0]['Name']}'. The first one taken, and the rest were discarded.")
            if not found[0]['Type'] in ['SecureString']:
                raise DSOException(f"Secret '{key}' not found: project={project}, application={application}, stage={Stages.shorten(stage)}")
        Logger.info(f"Getting SSM secret: path={found[0]['Name']}")
        result = ssm.get_parameter(Name=found[0]['Name'], WithDecryption=True)
        return result['Parameter']['Value']

###--------------------------------------------------------------------------------------------

    def delete(self, project, application, stage, key):
        ### only secrets owned by the stage can be deleted, hence uninherited=True
        found = self.locate_secret(project, application, stage, key, uninherited=True)
        if not found or len(found) == 0:
                raise DSOException(f"Secret '{key}' not found: project={project}, application={application}, stage={Stages.shorten(stage)}")
        else:
            # if len(found) > 1:
            #     Logger.warn(f"More than one secret found at '{found[0]['Name']}'. The first one taken, and the rest were discarded.")
            if not found[0]['Type'] in ['SecureString']:
                raise DSOException(f"Secret '{key}' not found in the given context: project={project}, application={application}, stage={Stages.shorten(stage)}")
        Logger.info(f"Deleting SSM secret: path={found[0]['Name']}")
        ssm.delete_parameter(Name=found[0]['Name'])

###--------------------------------------------------------------------------------------------
###--------------------------------------------------------------------------------------------
###--------------------------------------------------------------------------------------------

ProviderManager.register(AwsSsmSecretProvider())
