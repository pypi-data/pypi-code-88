import json
import os
from functools import lru_cache

_API_TOKEN = 'RALLY_API_TOKEN'
_API_URL = 'RALLY_URL'
_CONTEXT = 'RALLY_USER_CONTEXT'

ASSET_ID = 'assetId'
ASSET_NAME = 'assetName'
BASE_ASSET_ID = 'baseAssetId'
DYNAMIC_PRESET_DATA = 'dynamicPresetData'
JOB_UUID = 'jobUuid'
ORG_ID = 'orgId'
PRIORITY = 'priority'
USER_ID = 'userId'
WORKFLOW_BASE_ID = 'workflowBaseId'
WORKFLOW_ID = 'workflowId'
WORKFLOW_PARENT_ID = 'workflowParentId'
WORKFLOW_RULE_ID = 'wfRuleId'


@lru_cache(maxsize=1)
def _make_user_context():
    result = {}
    try:
        for (k,v) in json.loads(os.environ[_CONTEXT]).items():
            result[k] = v
    except (KeyError, TypeError, ValueError) as err:
        raise ValueError(f"Context missing or non-JSON in environment variable '{_CONTEXT}'") from err
    return result


@lru_cache(maxsize=1)
def _make_sdk_context():
    result = {k: v for k, v in _make_user_context().items()}
    for k in [_API_TOKEN, _API_URL]:
        if k in os.environ:
            result[k] = os.environ[k]
    return result


def _refresh():
    _make_user_context.cache_clear()
    _make_sdk_context.cache_clear()


def context(key):
    """ Retrieve key from context, or None if not present. """
    return _make_user_context().get(key)


def _sdk_context(key):
    """ Retrieve key from SDK context, a superset of context for internal use. """
    return _make_sdk_context().get(key)


