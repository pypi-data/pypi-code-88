
APPLICATION_NAME = "DevSecOps utilty"
REGEX_PATTERNS = {
    'stage' : r"^([a-zA-Z][a-zA-Z0-9]+)/?([0-9])?$",
    'parameter_key' : r"^([a-zA-Z][a-zA-Z0-9]*/)?([a-zA-Z][a-zA-Z0-9_.-]*)$",
    'parameter_key_value' : r"^([a-zA-Z][a-zA-Z0-9_.-/]*)=(.*)$",
}

CLI_COMMANDS_SHORT_HELP = {
    'version': "Display versions.",
    'parameter': {
        'list': "List parameters added to the application.",
        'add': "Add one or multiple parameters to the application.",
        'get': "Get the value of a parameter.",
        'delete': "Delete one or multiple parameters from an application.",
    },
    'secret': {
        'list': "List secrets added to the application.",
        'add': "Add one or multiple secrets to the application.",
        'get': "Get the value of a secret.",
        'delete': "Delete one or multiple secrets from an application.",
    },
    'template': {
        'list': "List templates added to the application.",
        'add': "Add a template to the application.",
        'get': "Get the content of a template.",
        'delete': "Delete one or multiple templates from the application.",
        'render': "Render templates using parameters in a context.",
    },
    'package': {
        'list': "List packages built for the application.",
        'create': "Create a build package for the application.",
        'get': "Download an application build package.",
        'delete': "Delete a build package from the application.",
    },
    'release': {
        'list': "List deployment releases for the application.",
        'create': "Create a deployment release for the application.",
        'get': "Download an application deployment release.",
        'delete': "Delete a deployment release from the application.",
    },
    'config': {
        'get': "Get DSO application configuration(s).",
        'set': "Set the DSO application configuration(s).",
        'delete': "Delete a DSO application configuration.",
        'init': "Initialize DSO configuration for the working directory.",
    },
}
CLI_PARAMETERS_HELP = {
    'common': {
        'working_dir': "Path to the directory where the DSO application configuration resides. The current working directory will be used by default.",
        'verbosity' : "Logging verbosity: 0 for criticals, 1 for errors, 2 for warnings, 3 for information, 4 for debug, 5 for everything.",
        'stage' : f"Identifier of the stage, which is combination of a name and an optional number as in <name>[/<number>], and it must conform to '{REGEX_PATTERNS['stage']}'. If no <number> is specefied, the default environment (0) in the given stage will be used.",
        'input' : "Path to a local file inputing the parameters. Use '-' to read from pipe/stdin.",
        'format' : "Data format",
        'config': "Comma separated list of key/value pairs to override DSO configurations.",
        'query': "Select output using JMESPath query language.",
        'show_all': "Show all the available fields in the ouput.",
    },
    'parameter': {
        'key': "The key of the parameter",
        'value': "The value for the parameter",
        'show_values': "Show parameter values in the output.",
        'uninherited': "Select only parameters which are specific to the gievn context, i.e. not inherited from the parent contexts."
    },
    'secret': {
        'key': "The key of the secret",
        'value': "The value for the secret",
        'show_values': "Show secret values in the output.",
        'uninherited': "Select only secrets which are specific to the gievn context, i.e. not inherited from the parent contexts."
    },
    'template': {
        'type': "Type of the template. Use 'resource' for templates needed at the provision time when provisioning resources required by the application to run such as SQS queus, SNS topics, and CI/CD piplines.\nUse 'package' for templates needed at the build time when generating a package.\nUse 'release' for templates needed at the deploy time when generating a release." ,
        'key': "The key of the template",
        'limit': "Limit templates to be rendered.",
        'render_path': "Path (relative to the root of the DSO application) where rendered template will be placed at.",
        'show_render_path': "Show render path",
        'input' : "Path to a local file containing the template content.",
        'recursive' : "Add all files within 'input' recursively.",
    },
    'config': {
        'key': "The key of the configuration",
        'value': 'Value for the configuration key',
        'input' : "Path to a local (yaml) file inputing the configuration. Use '-' to read from pipe/stdin.",
        'local': "Select only the local DSO configurations, i.e. existing in the working directory.",
        'global': "Select only the global DSO configurations, i.e. user-wide configuration.",
        'init_local': "Explicitly override inherited configurations locally. If mixed with '-i' / '--input' option, it will casue the local configuration to be merged with the provided input configuration.",
        'setup': "Run a setup wizard to assist configuring the DSO application.",

    }


}

# CLI_MESSAGES = {
#     'InvalidArgumentValue': "Invalid argument value: '{0}' is invalid for '{1}'. Must conform to '{2}'",
#     'AtleastOneofTwoArgumentsNeeded': "At least one of '{0}' or '{1}' must be provided.",
#     'ArgumentsMutalExclusive': "'{0}' is mutually exclusive with '{1}'.",
# }



MESSAGES = {
    'InvalidKey': "'{0}' is an invalid key. Must conform to '{1}'",
    'ParameterNotFound': "Parameter '{0}' not found in the given context.",
    'SecretNotFound': "Secret '{0}' not found in the given context.",
    # 'ParameterNotFoundScope': "'{0}' not found as a parameter, but found a scope.",
    'InvalidStage': "'{0}' is not a valid stage name. Valid form is <string>[/number], where it must conform to '{1}'.",
    'DSOConfigNotFound': 'DSO application configuration not found.',
    'ContextNotFound': "Context '{0}' not found.",
    'PatternNotMatched': "'{0}' is invalid. Must conform to '{1}'",
    'InvalidParameterKeyValuePair': "'{0}' is an invalid parameter key/value pair. Must conform to '^([a-zA-Z][a-zA-Z0-9_.-/]*)=(.*)$'",
    'InvalidParameterKey': "'{0}' is an invalid parameter key. Must conform to '{1}'",
    'AtleastOneofTwoNeeded': "At least one of {0} or {1} must be provided.",
    'MissingOption': "Missing option {0}.",
    'MissingArgument': "Missing argument {0}.",
    'ArgumentsMutualExclusive': "Either {0} or {1} must be provided, but not both.",
    'TemplateNotFound': "Template '{0}' not found.",
    'InvalidTemplateKey': "'{0}' is an invalid template key. Must conform to '{1}'",
    'ContextNotFoundListingInherited': "Context '{0}' not found, listing inherited parameters if any.",
    'TryHelpWithCommand': "Try '{0} --help' for more details.",
    'TryHelp': "Try the command with '-h' / '--help' option for more details.",
    'InvalidJsonFile': "Invalid json file.",
    'InvalidYamlFile': "Invalid yaml file.",
    'InvalidFileFormat': "Invalid file, not conforming to expected {0} format.",
    'ArgumentsOrOption': "{0} may be provider via either argument {1} or option {2}, but not both.",
    'LoadingParameters': "Loading parameters...",
    'LoadingSecrets': "Loading secrets...",
    'LoadingTemplates': "Loading templates...",
    'MerginParameters': "Consolidating parameters...",
    'RenderingTemplates': "Rendering templates...",
    'RenderingTemplate': "Rendering '{0}'...",
    'OptionMutualInclusive': "Option {0} needed when {1} is provided.",
    'InvalidDSOConfigurationFile': "'{0}' is not a valid DSO configuration file.",
    'DSOConfigNewer': "Application is configured to use a newer version of dso, expected '{0}', got '{1}'.",
    'DSOConfigOlder': "Application is configured to use an older version of dso, expected '{0}', got '{1}'.",
    'ProviderNotSet': "{0} provider has not been set.",
    'InvalidConfigOverrides': "Invalid DSO configuration overrides. Must conform to '<key>=<value>, ...'",
    'DSOConfigutrationOverriden': "DSO configuration '{0}' overriden to '{1}'.",
    'NoDSOConfigFound': "No DSO configuration found in the working directory.",
    'EnteredSecretValuesNotMatched': "Entered values for the secret did not macth.",
    'InvalidRenderPath': "'{0}' is not a valid render path.",
    'InvalidRenderPathExistingDir': "'{0}' is not a valid render path because it is an existing directory.",
    'InvalidRenderPathAbs': "'{0}' is not a valid render path becasue render path must be relative to the root of the DSO application.",
}
