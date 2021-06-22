# Copyright (c) 2014-2021 GeoSpock Ltd.

enterPassword = "Please enter GSDB authentication password:"
helpLogin = "Could not complete configuration. Command should be of the format `gsdb configure --user <value> " \
            "[--password <value>] --endpoint <value>`."
insufficientLoginDetails = "No authentication information found - please use, 'gsdb configure --user <value> " \
                           "--password <value> --endpoint <value>' to save your username and password for your own " \
                           "IdP or `gsdb --user <value> --password <value> --endpoint <value> COMMAND` if not " \
                           "saving your username and password."
invalidConfig = "The geospock configuration file is invalid or empty, and no user and password information given. " \
                "Please ensure that the 'gsdb configure' command has been run correctly, otherwise contact your " \
                "system administrator for assistance."
userButNoPassword = "`--user` specified but no `--password` - please use both or neither of these arguments."
