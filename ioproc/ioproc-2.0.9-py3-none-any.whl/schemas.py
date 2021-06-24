#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = ["Benjamin Fuchs", "Jan Buschmann", "Felix Nitsch"]
__copyright__ = "Copyright 2020, German Aerospace Center (DLR)"
__credits__ = []

__license__ = "MIT"
__version__ = "1.0.4"
__maintainer__ = "Felix Nitsch"
__email__ = "ioProc@dlr.de"
__status__ = "Production"


general_schema = {
    "workflow": {
        "required": True,
        "type": "list",
        "schema": {
            "type": "dict",
            "valuesrules": {
                "type": "dict",
                "schema": {
                    "project": {"type": "string", "required": True,},
                    "call": {"type": "string", "required": True,},
                    "data": {"required": False,},
                    "args": {"required": False,},
                    "tag": {"required": False,},
                },
            },
        },
    },
    "actionFolder": {"type": "string", "required": True,},
    "debug": {
        "type": "dict",
        "required": True,
        "schema": {
            "timeit": {"type": "boolean", "required": True,},
            "enable development mode": {"type": "boolean", "required": True,},
            "log_level": {
                "type": "string",
                "required": False,
                "allowed": ["INFO", "WARNING", "DEBUG", "CRITICAL", "ERROR"],
            },
        },
    },
    "fromCheckPoint": {"type": ["string", "integer"],},
    "global": {
        "type": ["string", "integer", "float", "dict", "list"],
        "required": False,
    },
}


action_schema = {
    "action": {
        "type": "dict",
        "keysrules": {"type": "string",},
        "valuesrules": {
            "type": "dict",
            "schema": {
                "project": {"type": "string", "required": True,},
                "call": {"type": "string", "required": True,},
                "data": {
                    "required": False,
                    "schema": {
                        "read_from_dmgr": {
                            "nullable": True,
                            "type": ["string", "list", "dict"],
                            "required": True,
                            "forbidden": ["None", "none"],
                        },
                        "write_to_dmgr": {
                            "nullable": True,
                            "type": ["string", "list", "dict"],
                            "required": True,
                            "forbidden": ["None", "none"],
                        },
                    },
                },
                "args": {"type": "dict", "required": False,},
            },
        },
    }
}


checkpoint_schema = {
    "action": {
        "type": "dict",
        "keysrules": {"type": "string",},
        "valuesrules": {
            "type": "dict",
            "schema": {
                "project": {"type": "string", "required": True,},
                "call": {"type": "string", "required": True,},
                "tag": {"type": ["string", "integer"], "required": True,},
            },
        },
    }
}
