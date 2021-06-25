
APPLICATION_NAME = "DevSecOps utilty"
REGEX_PATTERNS = {
    'stage' : r"^([a-zA-Z][a-zA-Z0-9]+)/?([0-9])?$",
    'parameter_key' : r"^([a-zA-Z][a-zA-Z0-9]*/)?([a-zA-Z][a-zA-Z0-9_.-]*)$",
    'parameter_key_value' : r"^([a-zA-Z][a-zA-Z0-9_.-/]*)=(.*)$",
}

CLI_COMMANDS_HELP = {
    'parameter': {
        'add': """Add a parameter to a context, or update a parameter If it is already existing in the context.\n
                ** Tips: 1) If the parameter is inherited from the parent contexts, it will be overriden in the context. 2) Multiple parameters may be added at once using the '--input' option.\n
                KEY: The identifier of the parameter to be added. It may also be provided using the '--key' option.\n
                VALUE: The value for the parameter. If the parameter is already existing in the context, the value will be updated to the new one. It may also be provided using the '--value' option.\n
                """,
        'list': """Return the list of owned/inherited parameters in a context.\n
                ** Tips: 1) To limit the list to the owned/overriden parameters only, use the '--uninherited' option. This will return only the context specific parameters.
                """,
        'get': """Return the current value of a parameter in a context.\n
                ** Tips: 1) The parameter may be inherited from the parent contexts or owned by the given context.\n
                KEY: The identifier of the parameter. It may also be provided using the '--key' option.\n
                """,
        'delete': """Delete a parameter from a context.\n
                ** Tips: 1) The inherited parameters cannot be deleted. In other words, the context must be the owner of the parameter or a not found error will be returned. 2) Multiple parameters may be deleted at once using the '--input' option.\n         
                KEY: The identifier of the parameter to be deleted. It may also be provided using the '--key' option.\n
                """,                
    },
    'secret': {
        'add': """Add a secret to a context, or update a secret If it is already existing in the context.\n
                ** Tips: 1) If the secret is inherited from the parent contexts, it will be overriden in the context. 2) Multiple secrets may be added at once using the '--input' option.\n
                KEY: The identifier of the secret to be added. It may also be provided using the '--key' option.\n
                VALUE: The value for the secret. If the secret is already existing in the context, the value will be updated to the new one. It may also be provided using the '--value' option.\n
                """,
        'list': """Return the list of owned/inherited secrets in a context.\n
                ** Tips: 1) To limit the list to the owned/overriden secrets only, use the '--uninherited' option. This will return only the context specific secrets.
                """,
        'get': """Return the current value of a secret in a context.\n
                ** Tips: 1) The secret may be inherited from the parent contexts or owned by the given context.\n
                KEY: The identifier of the secret. It may also be provided using the '--key' option.\n
                """,
        'delete': """Delete a secret from a context.\n
                ** Tips: 1) The inherited secrets cannot be deleted. In other words, the context must be the owner of the secret or a not found error will be returned. 2) Multiple secrets may be deleted at once using the '--input' option.\n         
                KEY: The identifier of the secret to be deleted. It may also be provided using the '--key' option.\n
                """,                
    },
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
        'working_dir': "Path to a (local) directory where the DSO application configuration resides. By default, the current working directory will be used if the option is not provided.",
        'verbosity' : "Specify the logging verbosity, where 0 is for logging critical fatal errors only, 1 also logs error messages, 2 also logs warnings, 3 also logs information messages, 4 also logs debug messages, and finally 5 logs everything.",
        'stage' : "Target a specific stage using the stage identifier, which is combination of a name and an optional number, where name must conform to ^([a-zA-Z][a-zA-Z0-9]+)$ regex expression. If no /<number> is specified, the default environment (/0) in the given stage will be targeted.",
        'input' : "Path to a (local) file defining the input data. Use '-' to read from the shell pipe or stdin. Use '--format' to specify the format if needed.",
        'format': "Specify the format of the output or the input if mixed with the '--input' option.",
        'config': "Comma separated list of key/value pairs to temporarily override the current DSO application configurations. It takes effect only while executing the command and does not have any lasting effect on the DSO application configuration or subsequent command executions.",
        'query': "Customize output using JMESPath query language.",
        'query_all': "Include all the available fields in the ouput.",
    },
    'parameter': {
        'key': "The key of the parameter. See KEY argument for more details.",
        'value': "The value for the parameter. See VALUE argument for more details.",
        'query_values': "Include parameter values in the output.",
        'uninherited': "Select only parameters which are specific to the gievn context, i.e. not inherited from the parent contexts.",

    },
    'secret': {
        'key': "The key of the secret",
        'value': "The value for the secret",
        'query_values': "Include secret values in the output.",
        'uninherited': "Select only secrets which are specific to the gievn context, i.e. not inherited from the parent contexts."
    },
    'template': {
        'type': "Type of the template. Use 'resource' for templates needed at the provision time when provisioning resources required by the application to run such as SQS queus, SNS topics, and CI/CD piplines.\nUse 'package' for templates needed at the build time when generating a package.\nUse 'release' for templates needed at the deploy time when generating a release." ,
        'key': "The key of the template",
        'limit': "Limit templates to be rendered.",
        'render_path': "Path (relative to the root of the DSO application) where rendered template will be placed at.",
        'query_render_path': "Include the template render paths in the output.",
        'input' : "Path to a local file containing the template content.",
        'recursive' : "Add files recursively.",
    },
    'config': {
        'key': "The key of the configuration",
        'value': 'Value for the configuration key',
        'input' : "Path to a local (yaml) file inputing the configuration. Use '-' to read from the shell pipe or stdin.",
        'local': "Select only the local DSO configurations, i.e. existing in the working directory.",
        'global': "Select only the global DSO configurations, i.e. user-wide configuration.",
        'init_local': "Explicitly override inherited configurations locally. If mixed with '-i' / '--input' option, it will casue the local configuration to be merged with the provided input configuration.",
        'setup': "Run a setup wizard to assist configuring the DSO application.",

    }


}


CLI_MESSAGES = {
    'InvalidKey': "'{0}' is an invalid key. Must conform to '{1}'",
    'ParameterNotFound': "Parameter '{0}' not found in the given context.",
    'SecretNotFound': "Secret '{0}' not found in the given context.",
    'InvalidStage': "'{0}' is not a valid stage name. Valid form is <string>[/number], where it must conform to '{1}'.",
    'ContextNotFound': "Context '{0}' not found.",
    'PatternNotMatched': "'{0}' is invalid. Must conform to '{1}'",
    'InvalidParameterKeyValuePair': "'{0}' is an invalid parameter key/value pair. Must conform to '^([a-zA-Z][a-zA-Z0-9_.-/]*)=(.*)$'",
    'InvalidParameterKey': "'{0}' is an invalid parameter key. Must conform to '{1}'",
    'AtleastOneofTwoNeeded': "At least one of {0} or {1} must be provided.",
    'MissingOption': "Missing option {0}.",
    'MissingArgument': "Missing argument {0}.",
    'ArgumentsMutualExclusive': "Either {0} or {1} must be provided, but not both.",
    'ArgumentsMutualInclusive': "{0} is needed when {1} is provided.",
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
    'ProviderNotSet': "{0} provider has not been set.",
    'InvalidDSOConfigOverrides': "Invalid DSO configuration overrides. Must conform to '<key>=<value>, ...'",
    'DSOConfigutrationOverriden': "DSO configuration '{0}' overriden to '{1}'.",
    'DSOConfigNewer': "Application is configured to use a newer version of dso, expected '{0}', got '{1}'.",
    'DSOConfigOlder': "Application is configured to use an older version of dso, expected '{0}', got '{1}'.",
    'DSOConfigurationNotFound': 'DSO configuration not found.',
    'NoDSOConfigFound': "No DSO configuration found in the working directory.",
    'EnteredSecretValuesNotMatched': "Entered values for the secret did not macth.",
    'InvalidRenderPath': "'{0}' is not a valid render path.",
    'InvalidRenderPathExistingDir': "'{0}' is not a valid render path because it is an existing directory.",
    'InvalidRenderPathAbs': "'{0}' is not a valid render path becasue render path must be relative to the root of the DSO application.",
    'QueryOptionCompatibleFormats': "Option '-q' / '--query' can be used only with 'json'/'yaml' output formats.",
    'QueryAllOptionNonCompatibleFormats': "Option '-a'/ '--query-all' cannot be used with 'shell' output format.",    
}