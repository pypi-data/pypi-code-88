"""
Type annotations for migrationhub-config service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migrationhub_config/type_defs.html)

Usage::

    ```python
    from mypy_boto3_migrationhub_config.type_defs import CreateHomeRegionControlResultTypeDef

    data: CreateHomeRegionControlResultTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CreateHomeRegionControlResultTypeDef",
    "DescribeHomeRegionControlsResultTypeDef",
    "GetHomeRegionResultTypeDef",
    "HomeRegionControlTypeDef",
    "TargetTypeDef",
)

CreateHomeRegionControlResultTypeDef = TypedDict(
    "CreateHomeRegionControlResultTypeDef",
    {
        "HomeRegionControl": "HomeRegionControlTypeDef",
    },
    total=False,
)

DescribeHomeRegionControlsResultTypeDef = TypedDict(
    "DescribeHomeRegionControlsResultTypeDef",
    {
        "HomeRegionControls": List["HomeRegionControlTypeDef"],
        "NextToken": str,
    },
    total=False,
)

GetHomeRegionResultTypeDef = TypedDict(
    "GetHomeRegionResultTypeDef",
    {
        "HomeRegion": str,
    },
    total=False,
)

HomeRegionControlTypeDef = TypedDict(
    "HomeRegionControlTypeDef",
    {
        "ControlId": str,
        "HomeRegion": str,
        "Target": "TargetTypeDef",
        "RequestedTime": datetime,
    },
    total=False,
)

_RequiredTargetTypeDef = TypedDict(
    "_RequiredTargetTypeDef",
    {
        "Type": Literal["ACCOUNT"],
    },
)
_OptionalTargetTypeDef = TypedDict(
    "_OptionalTargetTypeDef",
    {
        "Id": str,
    },
    total=False,
)


class TargetTypeDef(_RequiredTargetTypeDef, _OptionalTargetTypeDef):
    pass
