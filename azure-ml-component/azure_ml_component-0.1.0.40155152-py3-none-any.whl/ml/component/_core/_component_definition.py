# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
import os
import re
import logging
import shutil
import inspect
from enum import Enum
from pathlib import Path
from typing import Sequence, Union, Mapping
from collections import OrderedDict
from tempfile import mkdtemp

from azureml.exceptions import UserErrorException
from azureml.core import Workspace

from azure.ml.component._util._utils import _is_empty_dir, _sanitize_python_variable_name, _extract_zip
from azure.ml.component._util._yaml_utils import YAML, YamlFlowList, YamlMultiLineStr, YamlFlowDict
from azure.ml.component._api._api import ModuleAPI, ComponentAPI
from azure.ml.component._core._component_contexts import CreationContext, RegistrationContext
from ._core import Component
from ._launcher_definition import LauncherDefinition
from ._io_definition import _remove_empty_values, ParameterDefinition, InputDefinition, OutputDefinition
from ._environment import Environment
from ._run_settings_definition import RunSettingsDefinition
from .._restclients.designer.models.designer_service_client_enums import SuccessfulCommandReturnCode


# TODO: We should have a shared logger for component package
logger = logging.getLogger(__name__)
logger.propagate = False
logger.setLevel(logging.INFO)


def _to_camel(s, first_lower=False):
    result = s.title().replace('_', '')
    if first_lower and len(result) > 1:
        result = result[0].lower() + result[1:]
    return result


def _to_ordered_dict(data: dict) -> OrderedDict:
    for key, value in data.items():
        if isinstance(value, dict):
            data[key] = _to_ordered_dict(value)
    return OrderedDict(data)


class ComponentType(Enum):
    """Represents all types of components."""

    Component = 'Component'
    CommandComponent = 'CommandComponent'
    PipelineComponent = 'PipelineComponent'
    DistributedComponent = 'DistributedComponent'
    ParallelComponent = 'ParallelComponent'
    HDInsightComponent = 'HDInsightComponent'
    ScopeComponent = 'ScopeComponent'
    DataTransferComponent = 'DataTransferComponent'
    SweepComponent = 'SweepComponent'

    @classmethod
    def get_component_type_by_str(cls, type_str):
        if type_str is None:
            return cls.CommandComponent
        for t in cls:
            # Support CommandComponent@2 => CommandComponent
            if type_str.lower().startswith(t.value.lower()):
                return t

        # The legacy mapping is to get the correct type from the job type in old style yaml.
        legacy_mapping = {
            'basic': cls.CommandComponent,
            'mpi': cls.DistributedComponent,
            'parallel': cls.ParallelComponent,
            'hdinsight': cls.HDInsightComponent,
            'mpicomponent': cls.DistributedComponent,  # It used to be MPIComponent.
        }
        return legacy_mapping.get(type_str.lower(), cls.CommandComponent)

    def get_definition_class(self):
        mapping = {
            self.CommandComponent: CommandComponentDefinition,
            self.DistributedComponent: DistributedComponentDefinition,
            self.ParallelComponent: ParallelComponentDefinition,
            self.HDInsightComponent: HDInsightComponentDefinition,
            self.ScopeComponent: ScopeComponentDefinition,
            self.DataTransferComponent: DataTransferComponentDefinition,
            self.SweepComponent: SweepComponentDefinition,
            self.PipelineComponent: PipelineComponentDefinition
        }
        # For unknown types, we simply use ComponentDefinition in default which includes interface to be used.
        return mapping.get(self, ComponentDefinition)


class ComponentDefinition(Component):
    r"""Represents a Component asset version.

    ComponentDefinition is immutable class.
    """
    SCHEMA_KEY = '$schema'
    SCHEMA = 'http://azureml/sdk-2-0/CommandComponent.json'
    HELP_DOC_KEY = 'helpDocument'
    CONTACT_KEY = 'contact'
    CODE_GEN_BY_KEY = 'codegenBy'
    TYPE = ComponentType.Component
    TYPE_VERSION_PATTERN = re.compile(r"(\S+)@.*$")

    def __init__(
        self, name, version=None, display_name=None,
        description=None, tags=None, is_deterministic=None,
        inputs=None, parameters=None, outputs=None,
        runsettings: RunSettingsDefinition = None,
        workspace=None,
        creation_context=None,
        registration_context=None,
        namespace=None,  # add namespace to be compatible with legacy usage
        snapshot_id=None,
    ):
        """Initialize the component."""
        self._name = name
        self._namespace = namespace
        self._type = self.TYPE
        self._version = version
        self._display_name = display_name
        self._description = description
        self._tags = tags
        self._is_deterministic = is_deterministic
        inputs = inputs or {}
        parameters = parameters or {}
        outputs = outputs or {}
        # Here we accept two kinds of input/parameters/outputs.
        # 1. A Python dict, in this case, we use the dict to initialize definitions;
        # 2. A types defined in dsl.types or a definition,
        # which has correct interface and could be converted to component specification,
        # TODO: Use one centralized class from dsl.types instead of keeping both.
        # Currently we don't do that because it will introduce complicated imports.
        # We need to carefully redesign the whole package to avoid this.
        self._inputs = {
            name: data if not isinstance(data, dict) else InputDefinition.load({'name': name, **data})
            for name, data in inputs.items()
        }
        self._parameters = {
            name: data if not isinstance(data, dict) else ParameterDefinition.load({'name': name, **data})
            for name, data in parameters.items()
        }
        self._outputs = {
            name: data if not isinstance(data, dict) else OutputDefinition.load({'name': name, **data})
            for name, data in outputs.items()
        }
        self._runsettings = runsettings
        self._workspace = workspace
        self._creation_context = creation_context
        self._registration_context = registration_context
        self._snapshot_id = snapshot_id

    @property
    def name(self) -> str:
        """Return the name of the component."""
        if self._namespace is not None:
            # If self._namespace is not None, it's a legacy module, we combine namespace and name as it's name
            return '{}://{}'.format(self._namespace, self._name)
        return self._name

    @property
    def display_name(self) -> str:
        """
        Return the display_name of the component.
        If display_name is None, return name without namespace instead.
        """
        if self._display_name is not None:
            return self._display_name
        elif "://" in self.name:
            # if the name contains '://', componet.run will fail with environment.register return 404
            return self.name.split("://")[-1]
        else:
            return self.name

    @property
    def version(self) -> str:
        """Return the version of the component."""
        return self._version

    @property
    def type(self) -> ComponentType:
        """Return the type of the component."""
        return self._type

    @property
    def inputs(self) -> Mapping[str, InputDefinition]:
        """Return the inputs of the component."""
        return self._inputs

    @property
    def parameters(self) -> Mapping[str, ParameterDefinition]:
        """Return the parameters of the component."""
        return self._parameters

    @property
    def outputs(self) -> Mapping[str, OutputDefinition]:
        """Return the outputs of the component."""
        return self._outputs

    @property
    def description(self):
        """Return the description of the component."""
        return self._description

    @property
    def tags(self):
        """Return the tags of the component."""
        return self._tags or {}

    @property
    def contact(self):
        """Return the contact of the component."""
        return self.tags.get(self.CONTACT_KEY)

    @property
    def help_document(self):
        """Return the help document of the component."""
        return self.tags.get(self.HELP_DOC_KEY)

    @property
    def is_deterministic(self) -> bool:
        """Return whether the component is deterministic."""
        return self._is_deterministic

    @property
    def workspace(self) -> Workspace:
        """Return the workspace of the component."""
        return self._workspace

    @property
    def creation_context(self):
        # If component is not initialized from module dto, create an empty CreationContext.
        if self._creation_context is None:
            self._creation_context = CreationContext({})
        return self._creation_context

    @creation_context.setter
    def creation_context(self, val):
        """Set creation context for ComponentDefinition."""
        self._creation_context = val

    @property
    def registration_context(self):
        # If component is not initialized from module dto, create an empty RegistrationContext.
        if self._registration_context is None:
            self._registration_context = RegistrationContext({})
        return self._registration_context

    @registration_context.setter
    def registration_context(self, val):
        """Set registration context for ComponentDefinition."""
        self._registration_context = val

    @property
    def identifier(self):
        """Return the identifier of the component(unique in one workspace)."""
        return self.registration_context.id

    @property
    def runsettings(self) -> RunSettingsDefinition:
        """Return the run settings definition of the component."""
        return self._runsettings

    @property
    def snapshot_id(self) -> str:
        """Return the snapshot if of the component."""
        return self._snapshot_id

    @staticmethod
    def list(workspace, include_disabled=False) -> Sequence['ComponentDefinition']:
        """Return a list of components in the workspace.

        :param workspace: The workspace from which to list component definitions.
        :type workspace: azureml.core.workspace.Workspace
        :param include_disabled: Include disabled modules in list result
        :type include_disabled: bool
        :return: A list of module objects.
        :rtype: builtin.list['ComponentDefinition']
        """
        raise NotImplementedError

    @staticmethod
    def get(workspace, name, namespace=None, version=None):
        """Get the component definition object from the workspace.

        :param workspace: The workspace that contains the component.
        :type workspace: azureml.core.workspace.Workspace
        :param name: The name of the component to return.
        :type name: str
        :param namespace: The namespace of the component to return.
        :type namespace: str
        :param version: The version of the component to return.
        :type version: str
        :return: The component definition object.
        :rtype: azure.ml.component.core.ComponentDefinition
        """
        raise NotImplementedError

    @staticmethod
    def register(workspace, spec_file, package_zip, anonymous_registration: bool,
                 set_as_default, amlignore_file, version):
        """Register the component to workspace.

        :param workspace: The workspace that contains the component.
        :type workspace: azureml.core.workspace.Workspace
        :param spec_file: The component spec file. Accepts either a local file path, a GitHub url,
                           or a relative path inside the package specified by --package-zip.
        :type spec_file: Union[str, None]
        :param package_zip: The zip package contains the component spec and implementation code.
                           Currently only accepts url to a DevOps build drop.
        :type package_zip: Union[str, None]
        :param anonymous_registration: Whether to register the component as anonymous.
        :type anonymous_registration: bool
        :param set_as_default: Whether to update the default version.
        :type set_as_default: Union[str, None]
        :param amlignore_file: The .amlignore or .gitignore file used to exclude files/directories in the snapshot.
        :type amlignore_file: Union[str, None]
        :param version: If specified, registered component will use specified value as version
                                           instead of the version in the yaml.
        :return: The component definition.
        :rtype: azure.ml.component.core.ComponentDefinition
        """
        raise NotImplementedError

    def validate(self):
        """Validate whether the component is valid."""
        raise NotImplementedError

    def enable(self):
        """Enable a component in the workspace.

        :return: The updated component object.
        :rtype: azure.ml.component.core.ComponentDefinition
        """
        raise NotImplementedError

    def disable(self):
        """Disable a component in the workspace.

        :return: The updated component object.
        :rtype: azure.ml.component.core.ComponentDefinition
        """
        raise NotImplementedError

    @classmethod
    def load(cls, yaml_file):
        """Load a component definition from a component yaml file."""
        with open(yaml_file) as fin:
            data = YAML.safe_load(fin)
            type_str = data.get('type')
            definition_cls = ComponentType.get_component_type_by_str(type_str).get_definition_class()
            return definition_cls._from_dict(data)

    def _dump_to_stream(self, stream):
        """Dump the component definition to stream with specific style."""
        data = _to_ordered_dict(self._to_dict())
        YAML(typ='unsafe', with_additional_representer=True).dump(data, stream)

    def save(self, yaml_file):
        """Dump the component definition to a component yaml file.

        :param yaml_file: The target yaml file path
        :type yaml_file: str
        """
        with open(yaml_file, 'w') as fout:
            self._dump_to_stream(fout)

    @classmethod
    def _from_dict(cls, dct, ignore_unexpected_keywords=True) -> Union[
        'ComponentDefinition', 'CommandComponentDefinition',
        'ParallelComponentDefinition', 'DistributedComponentDefinition',
    ]:
        """Load a component definition from a component yaml dict."""
        # TODO: Load the dict according to the schema version.
        if cls.SCHEMA_KEY in dct:
            dct.pop(cls.SCHEMA_KEY)

        component_type = None if 'type' not in dct else dct.pop('type')
        component_type = cls._extract_type(component_type)

        if cls.TYPE not in {None, ComponentType.Component} and component_type not in {None, cls.TYPE.value}:
            raise TypeError("The type must be %r." % cls.TYPE.value)

        # Distinguish inputs and parameters from original yaml dict if parameters is not specified.
        if not dct.get('parameters'):
            inputs = dct.pop('inputs') if 'inputs' in dct else {}
            types = {k: data['type'] if isinstance(data, dict) else data.type for k, data in inputs.items()}
            dct['inputs'] = {
                k: data for k, data in inputs.items() if not ParameterDefinition.is_valid_type(types[k])
            }
            dct['parameters'] = {
                k: data for k, data in inputs.items() if ParameterDefinition.is_valid_type(types[k])
            }

        valid_parameters = inspect.signature(cls).parameters
        for key in [k for k in dct]:
            if key not in valid_parameters:
                if ignore_unexpected_keywords:
                    dct.pop(key)
                else:
                    raise KeyError("The dict contain an unexpected keyword '%s'." % key)
        return cls(**dct)

    def _to_dict(self):
        """Convert the component definition to a python dict."""
        # Currently we combine inputs/parameters
        inputs = {
            **{key: val._to_dict(remove_name=True) for key, val in self.inputs.items()},
            **{key: val._to_dict(remove_name=True) for key, val in self.parameters.items()}
        }
        outputs = {key: val._to_dict(remove_name=True) for key, val in self.outputs.items()}
        result = {
            self.SCHEMA_KEY: self.SCHEMA,
            'name': self.name,
            'version': self.version,
            'display_name': self.display_name,
            'type': self.type.value,
            'description': self.description,
            'is_deterministic': self.is_deterministic,
            'tags': self.tags,
            'inputs': inputs,
            'outputs': outputs,
        }
        # We don't remove empty values of tags since it may contains the values like {tag: None}
        result = _remove_empty_values(result, ignore_keys={'tags'})
        # code: . is not supported by MT, the replacement is removing it
        if 'code' in result and result['code'] == '.':
            result['code'] = None
        return result

    VALID_NAME_CHARS = set('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789._-')

    @classmethod
    def is_valid_name(cls, name: str):
        """Indicate whether the name is a valid component name."""
        return all(c in cls.VALID_NAME_CHARS for c in name)

    @classmethod
    def _extract_type(cls, component_type):
        # To handle load unregistered component that component type version in component type.
        type_groups = re.match(cls.TYPE_VERSION_PATTERN, component_type) if component_type else None
        if type_groups:
            component_type = type_groups.group(1)
        return component_type


class CommandComponentDefinition(ComponentDefinition):
    r"""represents a Component asset version.

    ComponentDefinition is immutable class.
    """
    SCHEMA = 'http://azureml/sdk-2-0/CommandComponent.json'
    TYPE = ComponentType.CommandComponent

    def __init__(self, name, version=None, display_name=None,
                 description=None, tags=None, is_deterministic=None,
                 inputs=None, parameters=None, outputs=None,
                 runsettings: RunSettingsDefinition = None,
                 command=None, environment=None,
                 code=None,
                 workspace=None,
                 creation_context=None,
                 registration_context=None,
                 namespace=None,  # add namespace to be compatible with legacy usage
                 successful_return_code=SuccessfulCommandReturnCode.zero,
                 is_command=True,
                 snapshot_id=None,
                 ):
        """Initialize a CommandComponentDefinition from the args."""
        super().__init__(
            name=name, namespace=namespace, version=version, display_name=display_name,
            description=description,
            tags=tags,
            is_deterministic=is_deterministic,
            inputs=inputs, parameters=parameters, outputs=outputs,
            runsettings=runsettings,
            workspace=workspace,
            creation_context=creation_context,
            registration_context=registration_context,
            snapshot_id=snapshot_id,
        )
        self._command = command
        if isinstance(environment, dict):
            environment = Environment._from_dict(environment)
        self._environment = environment
        self._code = code
        self._snapshot_local_cache = None
        self._api_caller = None

        # This field is used for telemetry when loading the component from a workspace,
        # a new name may be required since the interface has been changed to `get` instead of `load`
        self._load_source = None

        # This property is a workaround to unblock the implementation of Component,
        # will be removed after all the implementations are ready.
        self._module_dto = None

        # Whether is a command component running a non-python command or python script.
        self._is_command = is_command

        # This property is used to specify how command return code is interpreted.
        self._successful_return_code = successful_return_code

    @property
    def command(self):
        """Return the command of the CommandComponentDefinition."""
        return self._command

    @property
    def environment(self) -> Environment:
        """Return the environment of the CommandComponentDefinition."""
        if self._environment is None:
            self._environment = Environment()
        return self._environment

    @property
    def code(self):
        """Return the source code directory of the CommandComponentDefinition."""
        return self._code or '.'

    @property
    def _registered(self) -> bool:
        """Return whether the CommandComponentDefinition is registered in the workspace."""
        return self.workspace is not None and self.identifier is not None

    @property
    def api_caller(self):
        """CRUD layer to call rest APIs."""
        if self._api_caller is None:
            self._api_caller = ComponentAPI(self.workspace, logger=logger)
        return self._api_caller

    @api_caller.setter
    def api_caller(self, api_caller):
        """Setter for api caller."""
        self._api_caller = api_caller

    @property
    def successful_return_code(self):
        """Return the successful return code that is used to specify how command return code is interpreted."""
        return self._successful_return_code

    @property
    def is_command(self) -> bool:
        """
        Return whether the component command is a non-python command.
        If true, it's a non-python command will directly exeucte command in subprocess,
        else it's python script style command and it will use runpy to invoke.
        """
        return self._is_command

    def _to_dict(self) -> dict:
        """Convert the component definition to a python dict."""
        result = super()._to_dict()
        values_to_update = {
            'command': self._reformat_command(self.command),
            'environment': self.environment._to_dict() if self.environment is not None else None,
            'code': self.code if self.code != '.' else None,
        }
        result.update(_remove_empty_values(values_to_update))
        return result

    def get_snapshot(self, target=None, overwrite=False) -> Path:
        """Get the snapshot in target folder, if target is None, the snapshot folder is returned."""
        if target is not None:
            target = Path(target)
            if target.exists() and not _is_empty_dir(target) and not overwrite:
                raise FileExistsError("Target '%s' can only be an empty folder when overwrite=False." % target)
            if target.exists():
                # Remove the empty folder to store snapshot.
                shutil.rmtree(target)
            # Make sure the parent folder exists.
            target.parent.mkdir(exist_ok=True, parents=True)
        if self._snapshot_local_cache and Path(self._snapshot_local_cache).exists():
            if target is None:
                return self._snapshot_local_cache
            shutil.copytree(str(self._snapshot_local_cache), str(target))
        else:
            # Make sure the snapshot id exists.
            if self.snapshot_id is None:
                raise UserErrorException(
                    "Given component {} does not have a snapshot id, so it doesn't support download.".format(
                        self.name))
            if target is None:
                target = mkdtemp()
            snapshot_path = self.api_caller.download_snapshot_by_id(self.snapshot_id, target)
            _extract_zip(zip_file=snapshot_path, target_dir=target)
            # remove the zip file to align with previous behaviro
            try:
                os.remove(snapshot_path)
            except OSError:
                pass
            self._snapshot_local_cache = target
            return target

    @staticmethod
    def get(
            workspace: Workspace, name: str, version: str = None,
    ) -> 'CommandComponentDefinition':
        """Get the component definition object from the workspace."""
        api_caller = ComponentAPI(workspace=workspace, logger=logger)
        component = api_caller.get(
            name=name,
            version=version,  # If version is None, this will get the default version
        )
        component.api_caller = api_caller
        return component

    @staticmethod
    def get_by_id(workspace: Workspace, _id: str):
        """Get the component definition object by its id from the workspace."""
        api_caller = ComponentAPI(workspace=workspace, logger=logger)
        component = api_caller.get_by_id(_id)
        component.api_caller = api_caller
        return component

    @staticmethod
    def batch_get(workspace: Workspace, module_version_ids, selectors):
        """Batch get component definition objects by their id or identifiers."""
        api_caller = ComponentAPI(workspace=workspace, logger=logger)
        result = api_caller.batch_get(module_version_ids, selectors)
        for d in result:
            d.api_caller = api_caller

        return result

    @staticmethod
    def list(workspace, include_disabled=False) -> Sequence['CommandComponentDefinition']:
        """Return a list of components in the workspace."""
        api_caller = ComponentAPI(workspace=workspace, logger=logger)
        return api_caller.list(include_disabled=include_disabled)

    @staticmethod
    def register(workspace, spec_file, package_zip, anonymous_registration: bool,
                 set_as_default, amlignore_file, version):
        """Register from yaml file or URL"""
        api_caller = ComponentAPI(workspace=workspace, logger=logger)
        return api_caller.register(spec_file=spec_file, package_zip=package_zip,
                                   anonymous_registration=anonymous_registration,
                                   set_as_default=set_as_default,
                                   amlignore_file=amlignore_file, version=version)

    @staticmethod
    def _register_module(workspace, spec_file, package_zip, anonymous_registration: bool,
                         set_as_default, amlignore_file, version):
        """Only used for backward compatibility. Register from yaml file or URL"""
        api_caller = ModuleAPI(workspace=workspace, logger=logger)
        return api_caller.register(spec_file=spec_file, package_zip=package_zip,
                                   anonymous_registration=anonymous_registration,
                                   set_as_default=set_as_default,
                                   amlignore_file=amlignore_file, version=version)

    @classmethod
    def load(cls, yaml_file) -> Union[
        'CommandComponentDefinition', 'ParallelComponentDefinition', 'DistributedComponentDefinition',
        'HDInsightComponentDefinition',
    ]:
        result = super().load(yaml_file=yaml_file)
        result._snapshot_local_cache = Path(Path(yaml_file).parent / result.code)
        return result

    @classmethod
    def _from_dict(cls, dct, ignore_unexpected_keywords=False) -> 'CommandComponentDefinition':
        """Load a component definition from a component yaml dict."""
        return super()._from_dict(dct, ignore_unexpected_keywords=ignore_unexpected_keywords)

    @staticmethod
    def _reformat_command(command):
        """Reformat the command to make the output yaml clear."""
        if isinstance(command, str):
            return YamlMultiLineStr(command)
        if command is None:  # Parallel/HDI doesn't have command.
            return command
        # TODO: Remove the following logic since component yaml doesn't support list command anymore.
        # Here we call YamlFlowList and YamlFlowDict to have better representation when dumping args to yaml.
        result = []
        for arg in command:
            if isinstance(arg, list):
                arg = [YamlFlowDict(item) if isinstance(item, dict) else item for item in arg]
                arg = YamlFlowList(arg)
            result.append(arg)
        return result

    @classmethod
    def _module_yaml_convert_arg_item(cls, arg, inputs, parameters, outputs):
        """Convert one arg item in old style yaml to new style."""
        if isinstance(arg, (str, int, float)):
            return arg
        if isinstance(arg, list):
            return cls._module_yaml_convert_args(arg, inputs, parameters, outputs)
        if not isinstance(arg, dict) or len(arg) != 1:
            raise ValueError("Arg item is not valid: %r" % arg)
        key, value = list(arg.items())[0]
        for value_key in ['inputs', 'outputs', 'parameters']:
            items = locals()[value_key]
            # Parameters are also $inputs.xxx
            if value_key == 'parameters':
                value_key = 'inputs'
            for item in items:
                if item['name'] == value:
                    return '{%s.%s}' % (value_key, item['argumentName'])
        raise ValueError("%r is not in inputs and outputs." % value)

    @classmethod
    def _module_yaml_convert_args(cls, args, inputs, parameters, outputs):
        """Convert the args in old style yaml to new style."""
        return [cls._module_yaml_convert_arg_item(arg, inputs, parameters, outputs) for arg in args] if args else []

    @classmethod
    def _construct_dict_from_module_definition(cls, module):
        """Construct the component dict from an old style ModuleDefinition."""
        inputs, parameters, outputs = module.input_ports, module.params, module.output_ports
        for item in inputs + parameters + outputs:
            if 'argumentName' not in item:
                item['argumentName'] = _sanitize_python_variable_name(item['name'])
            if 'options' in item:
                # This field is different in old module definition and vNext definition.
                item['enum'] = item.pop('options')

        command = module.command or []
        command += cls._module_yaml_convert_args(module.args, inputs, parameters, outputs)
        # Convert the command from list to string
        command = ' '.join(arg if isinstance(arg, str) else '[%s %s]' % (arg[0], arg[1]) for arg in command)

        input_pairs = [(item.pop('argumentName'), item) for item in inputs]
        parameter_pairs = [(item.pop('argumentName'), item) for item in parameters]
        output_pairs = [(item.pop('argumentName'), item) for item in outputs]

        env = module.aml_environment or {}
        if env and 'python' in env:
            env['conda'] = env.pop('python')
        if module.image:
            env.update({'docker': {'image': module.image}})

        # Get tags according to the old yaml.
        tags = {key: None for key in module.tags} if module.tags else {}
        if module.help_document:
            tags[cls.HELP_DOC_KEY] = module.help_document
        if module.contact:
            tags[cls.CONTACT_KEY] = module.contact
        if cls.CODE_GEN_BY_KEY in module.annotations:
            tags[cls.CODE_GEN_BY_KEY] = module.annotations[cls.CODE_GEN_BY_KEY]

        # Convert the name to make sure only valid characters
        name = '%s://%s' % (module.namespace, module.name) if module.namespace else module.name
        name = name.lower().replace('://', '.').replace('/', '.').replace(' ', '_')
        new_dct = {
            'name': name,
            # This is a hard code rule.
            'version': module.version,
            'display_name': module.name,
            'is_deterministic': module.is_deterministic,
            'description': module.description,
            'tags': tags,
            'type': cls.TYPE.value,
            'inputs': {key: value for key, value in input_pairs},
            'parameters': {key: value for key, value in parameter_pairs},
            'outputs': {key: value for key, value in output_pairs},
            'command': command,
            'environment': env,
            'code': module.source_directory,
        }
        return new_dct

    @staticmethod
    def _from_module_yaml_dict(dct) -> 'CommandComponentDefinition':
        """Load the component from the old style module yaml dict."""
        from ..dsl._module_spec import _YamlModuleDefinition, _YamlParallelModuleDefinition, \
            _YamlHDInsightModuleDefinition
        definition_cls, cls = _YamlModuleDefinition, CommandComponentDefinition
        job_type = dct.get('jobType')
        if job_type is not None:
            if job_type.lower() == 'parallel':
                definition_cls, cls = _YamlParallelModuleDefinition, ParallelComponentDefinition
            elif job_type.lower() == 'hdinsight':
                definition_cls, cls = _YamlHDInsightModuleDefinition, HDInsightComponentDefinition
            elif job_type.lower() == 'mpi':
                definition_cls, cls = _YamlModuleDefinition, DistributedComponentDefinition
        module = definition_cls(dct)
        return cls._from_dict(cls._construct_dict_from_module_definition(module))

    @classmethod
    def _from_module_yaml_file(cls, f):
        """Load the component from the old style module yaml file."""
        with open(f) as fin:
            return cls._from_module_yaml_dict(YAML().load(fin))

    DEFAULT_SPEC_FILE = 'spec.yaml'
    DEFAULT_CONDA_FILE = 'conda.yaml'

    def _save_to_code_folder(self, folder, spec_file=None):
        """Save the module spec to specific folder under the source directory."""
        from ..dsl._module_spec import _Dependencies
        from .._util._utils import _relative_to

        if spec_file is None:
            spec_file = self.DEFAULT_SPEC_FILE
        source_directory = self.code if self.code else \
            Path(folder).resolve().absolute().as_posix()
        spec_file = (Path(folder) / spec_file).resolve()
        spec_dict = _to_ordered_dict(self._to_dict())
        if 'code' in spec_dict:
            spec_dict.pop('code')
        # Check whether the spec path is valid and set sourceDirectory to spec_dict.
        try:
            source_dir_2_spec_folder = _relative_to(spec_file.parent, source_directory, raises_if_impossible=True)
        except ValueError as e:
            raise ValueError("Target spec file '%s' is not under the source directory '%s'." % (
                spec_file.absolute().as_posix(), source_directory
            )) from e
        relative_path = source_dir_2_spec_folder.as_posix()
        if relative_path != '.':
            relative_path = ''.join(['../'] * len(relative_path.split('/')))  # aa/bb => ../../
            spec_dict['code'] = relative_path

        env = self.environment
        # Check whether we need to specify a default conda file in the folder containing the spec file.
        # The scenario is that conda_dependencies is not specified, while the conda is specified in dsl.component.
        if env.conda is not None and env.conda.conda_dependencies is None:
            conda_file = (source_dir_2_spec_folder / self.DEFAULT_CONDA_FILE).as_posix()
            spec_dict['environment']['conda'][env.conda.CONDA_FILE_KEY] = conda_file

            # Dump a default conda dependencies to the folder if the conda file doesn't exist.
            # The scenario that the initialized conda is a file need to be refined
            # because we don't know where is the conda.
            if not (Path(source_directory) / conda_file).exists():
                msg = "Conda file %s doesn't exist in the folder %s, a default one is dumped." % (conda_file, folder)
                logging.info(msg)
                YAML._dump_yaml_file(
                    _Dependencies.create_default().conda_dependency_dict,
                    Path(source_directory) / conda_file
                )

        YAML._dump_yaml_file(spec_dict, spec_file, unsafe=True, header=YAML.YAML_HELP_COMMENTS)


class DistributedComponentDefinition(CommandComponentDefinition):
    """The component definition of a MPI component,
    currently there is no difference with CommandComponentDefinition.
    """

    SCHEMA = 'http://azureml/sdk-1-5/DistributedComponent.json'
    TYPE = ComponentType.DistributedComponent

    def __init__(self, name, version=None, display_name=None,
                 description=None, tags=None, is_deterministic=None,
                 inputs=None, parameters=None, outputs=None,
                 runsettings: RunSettingsDefinition = None,
                 launcher=None, environment=None,
                 code=None,
                 workspace=None,
                 creation_context=None,
                 registration_context=None,
                 successful_return_code=SuccessfulCommandReturnCode.zero,
                 is_command=True,
                 snapshot_id=None
                 ):
        super().__init__(
            name=name, version=version, display_name=display_name, description=description, tags=tags,
            is_deterministic=is_deterministic, inputs=inputs, parameters=parameters, outputs=outputs,
            runsettings=runsettings, environment=environment, code=code, workspace=workspace,
            creation_context=creation_context, registration_context=registration_context,
            successful_return_code=successful_return_code, is_command=is_command, snapshot_id=snapshot_id
        )
        if isinstance(launcher, dict):
            launcher = LauncherDefinition._from_dict(launcher)
        self._launcher = launcher

    @property
    def launcher(self) -> LauncherDefinition:
        return self._launcher

    def _to_dict(self) -> dict:
        dct = super()._to_dict()
        dct['launcher'] = self.launcher._to_dict()
        return dct

    @classmethod
    def _construct_dict_from_module_definition(cls, module):
        dct = super()._construct_dict_from_module_definition(module)
        dct['launcher'] = {
            'type': 'mpi',  # module definition only supports MPI
            'additional_arguments': dct.pop('command'),
        }
        return dct


class ParallelComponentDefinition(CommandComponentDefinition):
    """The component definition of a parallel component."""

    SCHEMA = 'http://azureml/sdk-1-5/ParallelComponent.json'
    TYPE = ComponentType.ParallelComponent

    def __init__(self, name, version=None, display_name=None,
                 description=None, tags=None, is_deterministic=None,
                 inputs=None, parameters=None, outputs=None,
                 input_data=None, output_data=None,
                 entry=None,
                 args=None, environment=None,
                 code=None,
                 workspace=None,
                 creation_context=None,
                 registration_context=None,
                 successful_return_code=SuccessfulCommandReturnCode.zero,
                 is_command=True,
                 snapshot_id=None):
        super().__init__(
            name=name, version=version, display_name=display_name,
            description=description, tags=tags,
            is_deterministic=is_deterministic, inputs=inputs, parameters=parameters, outputs=outputs,
            command=None, environment=environment,
            code=code,
            workspace=workspace, creation_context=creation_context, registration_context=registration_context,
            successful_return_code=successful_return_code, is_command=is_command, snapshot_id=snapshot_id
        )
        input_data_list = input_data if isinstance(input_data, list) else [input_data]
        self._input_data = None if not input_data else [self._extract_input_name(data) for data in input_data_list]
        self._output_data = None if not output_data else self._extract_output_name(output_data)
        self._entry = entry
        self._args = args
        if args is not None and not isinstance(args, str):
            raise TypeError("Args must be type str, got %r" % (type(args)))
        self._job_type = 'parallel'

    @property
    def input_data(self) -> Sequence[str]:
        return self._input_data

    @property
    def output_data(self) -> str:
        return self._output_data

    @property
    def entry(self) -> str:
        return self._entry

    @property
    def args(self) -> str:
        return self._args

    @classmethod
    def _construct_dict_from_module_definition(cls, module):
        dct = super()._construct_dict_from_module_definition(module)
        # Use name mapping to make sure input_data/output_data are correct
        # since the component definition uses argument name as the key
        name_mapping = {}
        for item in module.input_ports + module.output_ports:
            name_mapping[item['name']] = item.get('argumentName', _sanitize_python_variable_name(item['name']))
        input_data = module.input_data if isinstance(module.input_data, list) else [module.input_data]
        dct['parallel'] = {
            'input_data': [name_mapping[i] for i in input_data],
            'output_data': name_mapping[module.output_data],
            'entry': module.entry,
            'args': dct.pop('command'),
        }
        return dct

    @classmethod
    def _from_dict(cls, dct) -> 'ParallelComponentDefinition':
        component_type = dct.pop('type') if 'type' in dct else None
        if component_type != cls.TYPE.value:
            raise ValueError("The type must be %r, got %r." % (cls.TYPE.value, component_type))
        if 'parallel' in dct:
            parallel = dct.pop('parallel')
            dct['input_data'] = parallel['input_data']
            dct['output_data'] = parallel['output_data']
            dct['entry'] = parallel['entry']
            if 'args' in parallel:
                dct['args'] = parallel['args']
        return super()._from_dict(dct)

    def _to_dict(self) -> dict:
        result = super()._to_dict()
        if not self.input_data:
            raise ValueError("Parallel component should have at least one input data, got 0.")
        parallel_section = {
            'parallel': {
                'input_data': YamlFlowList(['inputs.%s' % i for i in self.input_data]),
                'output_data': 'outputs.%s' % self.output_data,
                'entry': self.entry,
                'args': self._reformat_command(self.args),
            }}
        result.update(_remove_empty_values(parallel_section))
        return result

    def _extract_input_name(self, data: str):
        """Extract input name from inputs.xx"""
        format_err = ValueError("Input data %r of the parallel component is not 'inputs.xx' format." % data)
        if not isinstance(data, str) or data == '':
            raise format_err
        items = data.split('.')
        if (len(items) > 1 and (items[0] != 'inputs' or len(items) > 2)) or not data:
            raise format_err
        input_name = items[-1]  # Here we support two cases: 'inputs.xx' or 'xx'
        if input_name not in self._inputs:
            raise KeyError("Input data %r is not one of valid inputs, valid inputs: %r." % (
                input_name, set(self._inputs.keys())))
        return input_name

    def _extract_output_name(self, data: str):
        """Extract output name from outputs.xx"""
        format_err = ValueError("Output data %r of the parallel component is not 'outputs.xx' format." % data)
        if not isinstance(data, str) or data == '':
            raise format_err
        items = data.split('.')
        if len(items) > 1 and (items[0] != 'outputs' or len(items) > 2):
            raise format_err
        output_name = items[-1]  # Here we support two cases: 'outputs.xx' or 'xx'
        if output_name not in self._outputs:
            raise KeyError("Output data %r is not one of valid outputs, valid outputs: %r." % (
                output_name, set(self._outputs.keys())))
        return output_name


class HDInsightComponentDefinition(CommandComponentDefinition):
    """The component definition of a HDInsight component."""

    SCHEMA = 'http://azureml/sdk-1-5/HDInsightComponent.json'
    TYPE = ComponentType.HDInsightComponent

    def __init__(self, name, version=None, display_name=None,
                 description=None, tags=None, is_deterministic=None,
                 inputs=None, parameters=None, outputs=None,
                 command=None, environment=None,
                 file=None, files=None, class_name=None, jars=None,
                 py_files=None, archives=None, args=None,
                 code=None,
                 workspace=None,
                 creation_context=None,
                 registration_context=None,
                 snapshot_id=None):
        super().__init__(
            name=name, version=version, display_name=display_name, description=description, tags=tags,
            is_deterministic=is_deterministic, inputs=inputs, parameters=parameters, outputs=outputs,
            command=None, environment=None,
            code=code,
            workspace=workspace, creation_context=creation_context, registration_context=registration_context,
            snapshot_id=snapshot_id
        )
        self._file = file
        self._files = files
        self._class_name = class_name
        self._jars = jars
        self._py_files = py_files
        self._archives = archives
        self._args = args

    @property
    def file(self) -> str:
        return self._file

    @property
    def files(self) -> Sequence[str]:
        return self._files

    @property
    def class_name(self) -> str:
        return self._class_name

    @property
    def jars(self) -> Sequence[str]:
        return self._jars

    @property
    def py_files(self) -> Sequence[str]:
        return self._py_files

    @property
    def archives(self) -> Sequence[str]:
        return self._archives

    @property
    def args(self) -> str:
        return self._args

    @property
    def environment(self) -> Environment:
        """This section does not work for HDI"""
        return None

    @classmethod
    def _construct_dict_from_module_definition(cls, module):
        dct = super()._construct_dict_from_module_definition(module)
        dct['hdinsight'] = {
            'file': module.file,
            'files': module.files,
            'class_name': module.class_name,
            'jars': module.jars,
            'py_files': module.py_files,
            'archives': module.archives,
            'args': dct.pop('command'),
        }
        return dct

    @classmethod
    def _from_dict(cls, dct) -> 'HDInsightComponentDefinition':
        job_type = None if 'jobType' not in dct else dct.pop('jobType')
        component_type = None if 'type' not in dct else dct.pop('type')
        if component_type is None:
            if job_type is None or job_type.lower() != 'hdinsight':
                raise ValueError("The job type must be hdinsight, got '%s'." % job_type)
        else:
            if component_type != ComponentType.HDInsightComponent.value:
                raise ValueError("The type must be '%s', got '%s'." %
                                 (ComponentType.HDInsightComponent, component_type))
        if 'hdinsight' in dct:
            hdinsight = dct.pop('hdinsight')
            dct['file'] = hdinsight['file']
            dct['files'] = hdinsight.get('files')
            dct['class_name'] = hdinsight.get('class_name')
            dct['jars'] = hdinsight.get('jars')
            dct['py_files'] = hdinsight.get('py_files')
            dct['archives'] = hdinsight.get('archives')
            dct['args'] = hdinsight.get('args')
        return super()._from_dict(dct)

    def _to_dict(self) -> dict:
        result = super()._to_dict()
        hdinsight_section = {
            'hdinsight': {
                'file': self._file,
                'files': self._files,
                'class_name': self._class_name,
                'jars': self._jars,
                'py_files': self._py_files,
                'archives': self._archives,
                'args': self._reformat_command(self.args),
            }}
        result.update(_remove_empty_values(hdinsight_section))
        return result


class ScopeComponentDefinition(ComponentDefinition):
    """The component definition of a Scope component."""

    SCHEMA = 'http://azureml/sdk-1-5/ScopeComponent.json'
    TYPE = ComponentType.ScopeComponent

    def __init__(self, name, version=None, display_name=None,
                 description=None, tags=None, is_deterministic=None,
                 inputs=None, parameters=None, outputs=None,
                 runsettings: RunSettingsDefinition = None,
                 script=None,
                 args=None,
                 code=None,
                 workspace=None,
                 creation_context=None,
                 registration_context=None,
                 snapshot_id=None):
        super().__init__(
            name=name, version=version, display_name=display_name, description=description, tags=tags,
            is_deterministic=is_deterministic, inputs=inputs, parameters=parameters, outputs=outputs,
            runsettings=runsettings,
            workspace=workspace, creation_context=creation_context, registration_context=registration_context,
            snapshot_id=snapshot_id
        )
        self._code = code
        self._script = script
        self._args = args

    @property
    def code(self):
        """Return the source code directory of the ScopeComponentDefinition."""
        return self._code or '.'

    @property
    def script(self) -> str:
        return self._script

    @classmethod
    def _from_dict(cls, dct) -> 'ScopeComponentDefinition':
        component_type = None if 'type' not in dct else dct.pop('type')
        if component_type != cls.TYPE.value:
            raise ValueError("The type must be %r, got %r." % (cls.TYPE.value, component_type))

        if 'scope' in dct:
            scope = dct.pop('scope')
            dct['script'] = scope['script']
            dct['args'] = scope['args']

        return super()._from_dict(dct)

    def _to_dict(self) -> dict:
        result = super()._to_dict()
        scope_section = {
            'scope': {
                'script': self.script,
                'args': self._args
            }}
        result.update(_remove_empty_values(scope_section))
        return result


class DataTransferComponentDefinition(ComponentDefinition):
    """The component definition of a DataTransfer component."""

    SCHEMA = 'http://azureml/sdk-1-5/DataTransferComponent.json'
    TYPE = ComponentType.DataTransferComponent


class SweepComponentDefinition(ComponentDefinition):
    """The component definition of a Sweep component."""

    SCHEMA = 'http://azureml/sdk-1-5/SweepComponent.json'
    TYPE = ComponentType.SweepComponent


class PipelineComponentDefinition(ComponentDefinition):
    r"""represents a Component asset version.

    ComponentDefinition is immutable class.
    """
    SCHEMA = 'http://azureml/sdk-2-0/PipelineComponent.json'
    TYPE = ComponentType.PipelineComponent

    def __init__(self, name, id=None, components: dict=None, components_variable_names=None, description=None,
                 version=None, display_name=None, inputs=None, outputs=None, parameters=None, workspace=None,
                 parent_definition_id=None, from_module_name=None, pipeline_function_name=None,
                 outputs_mapping=None, default_compute_target=None, default_datastore=None,
                 tags=None, components_args_matched_dict_list=None,
                 snapshot_id=None, creation_context=None, registration_context=None):
        """
        :param name: Definition name.
        :type name: str
        :param id: Definition id.
        :type id: str
        :param components: Id to components dict inside pipeline definition.
        :type components: OrderedDict[str, Component]
        :param components_variable_names: The variable names of pipeline's components.
        :type components_variable_names: list[str]
        :param description: Description of definition.
        :type description: str
        :param version: The version of pipeline component.
        :type version: str
        :param display_name: The display name of pipeline component.
        :type display_name: str
        :param inputs: A dict of inputs name to definition.
        :type inputs: dict[str, InputDefinition]
        :param outputs: A dict of outputs name to definition.
        :type outputs: dict[str, OutputDefinition]
        :param parameters: Parameters of function defined by dsl.pipeline.
        :type parameters: dict
        :param workspace: workspace of definition.
        :type workspace: Workspace
        :param parent_definition_id: parent definition id.
        :type parent_definition_id: str
        :param from_module_name: from module name.
        :type from_module_name: str
        :param pipeline_function_name: The pipeline funtion name.
        :type pipeline_function_name: str
        :param outputs_mapping: A dict of outputs name to OutputBuilder on Component.
            Different from outputs, the outputs mapping is the real outputs of a pipeline,
             the _owner of dict value(OutputBuilder) is the component of definition.
            This mapping is used to record dsl.pipeline function's output
             and create a pipeline component instance from definition.
        :type outputs_mapping: dict[str, _OutputBuilder]
        :param default_compute_target: The resolved default compute target.
        :type default_compute_target: tuple(str, str)
        :param default_datastore: The default datastore.
        :type default_datastore: str
        :param tags: The tags of pipeline component.
        :type tags: dict[str, str]
        :param components_args_matched_dict_list: A list of dictionaries used to convert pipeline parameter kwargs to
            nodes with replaced keys. Dict key is the nodes parameter keys, value is parent pipeline
            parameter name(direct assign) or _ParameterAssignment(partial assign).
            e.g.
            @dsl.pipeline()
            def parent(str1, str2):
                component1(string_param=str1)
                component2(str=str2)
            Then the dict_list on pipeline 'parent' is [{'string_param', 'str1'}, {'str':'str2'}]
        :type components_args_matched_dict_list: list(dict[(str, Any)])
        :param snapshot_id: The component snapshot id.
        :type snapshot_id: str
        :param creation_context: The component creation context.
        :type creation_context: CreationContext
        :param registration_context: The component registration context.
        :type registration_context: RegistrationContext
        """
        super().__init__(
            name=name, display_name=display_name, description=description, is_deterministic=None, version=version,
            inputs=inputs, outputs=outputs, parameters=parameters, workspace=workspace,
            tags=tags, snapshot_id=snapshot_id, creation_context=creation_context,
            registration_context=registration_context)
        self._components = components
        self._components_variable_names = components_variable_names
        self._id = id
        self._outputs_mapping = outputs_mapping
        self._default_compute_target = default_compute_target
        self._default_datastore = default_datastore
        self._components_args_matched_dict_list = components_args_matched_dict_list
        self._parent_definition_id = parent_definition_id
        # There are tests of the two field so we shall keep them in definition
        self._from_module_name = from_module_name
        self._pipeline_function_name = pipeline_function_name

    @property
    def components(self):
        """
        Get the components of a pipeline component definition.

        The components are shared by all the pipeline component created by same definition.

        :return: Id to component dict inside pipeline component definition.
        :rtype: dict[str, Component]
        """
        return self._components
