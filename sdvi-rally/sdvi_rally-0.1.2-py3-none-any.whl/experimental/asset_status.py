""" Support for Asset Status Indicator feature

These functions will be merged into the `rally.asset` submodule after Alpha is complete

Importing the experimental module:

>>> from rally import experimental
"""

__all__ = [
    'get_asset_status_indicators',
    'add_asset_status_indicator',
    'clear_asset_status_indicator',
    'clear_all_asset_status_indicators',
]

import json

from rally.context import context, ASSET_ID, JOB_UUID
from rally._session import _getSession, _getAssetByName
from rally._utils import _toDatetime
from rally.exceptions import NotFound, RallyApiError


def get_asset_status_indicators(group=None, asset_name=None):
    """ Return a `generator iterator <https://docs.python.org/3/glossary.html#term-generator-iterator>`_ of dicts
    containing attributes of asset status indicators. The dict has the following keys:

        :id: (int) the id of the indicator
        :message: (str) the message associated with the indicator
        :group: (str) the group in which the indicator is included
        :icon: (str) the name of the `Font Awesome <https://fontawesome.com/icons?d=gallery>`_ icon class
        :color: (str) a hex value or color name for the icon
        :createdAt: (datetime) when the indicator was created
        :cleared: (bool) current cleared status
        :clearedAt:  (datetime, or None) when the indicator was cleared, if applicable

    :param group: The name of the group to filter on
    :type group: str, optional
    :param asset_name: The name of an asset to filter on, defaults to current asset
    :type asset_name: str, optional

    .. warning::

        :func:`rally.experimental.asset.get_asset_status_indicators` is in Alpha Preview and is not considered suitable
        for Production use.  Experimentation in lower environments is encouraged.

    """
    indicatorAttributes = ('message', 'group', 'icon', 'color', 'createdAt', 'cleared')

    paramFilter = {}

    assetId = _getAssetByName(asset_name) if asset_name else context(ASSET_ID)

    if not assetId:
        raise NotFound(f'asset {asset_name}')
    else:
        paramFilter['assetId'] = assetId

    if group:
        if not isinstance(group, str):
            raise TypeError('group must be a string')
        paramFilter['group'] = group

    marker = None

    while True:
        if marker:
            path = marker
            params = None
        else:
            path = 'v2/assetStatusIndicators'
            params = {'page': '1p100', 'filter': json.dumps(paramFilter)}

        page = _getSession().get(path, params=params).json()
        marker = page['links']['next']

        for i in page['data']:
            indicator = {'id': i.get('id')}
            attributes = i.get('attributes', {})
            for attr in indicatorAttributes:
                if attr == 'createdAt':
                    indicator[attr] = _toDatetime(attributes.get(attr))
                else:
                    indicator[attr] = attributes.get(attr)
            yield indicator

        if not marker:
            return


# TODO asset_name as a parameter makes no sense: Indicators require a job and an asset that is related to that job.
#  We either need to take a jobUUID (and work out the asset ourselves), or dis-allow other-asset indicators
def add_asset_status_indicator(message, group, icon, color, asset_name=None, curate_message=False, curate_group=False):
    """ Create a status indicator, optionally adding the group and/or message to the curated lists

    :param message: The message to be displayed with the indicator icon
    :type message: str
    :param group: The group in which the indicator should be included
    :type group: str
    :param icon: The name of the `Font Awesome <https://fontawesome.com/icons?d=gallery>`_ icon class
    :type icon: str
    :param color: A hex value or `Color keyword <https://developer.mozilla.org/en-US/docs/Web/CSS/color_value>`_
    :type color: str
    :param asset_name: The asset to which to add the indicator, defaults to the current asset
    :type asset_name: str, optional
    :param curate_message: Whether to save the message as a curated Asset Status Message, defaults to False
    :type curate_message: bool, optional
    :param curate_group: Whether to save the group as a curated Asset Status Group, defaults to False
    :type curate_group: bool, optional

    .. warning::

        :func:`rally.experimental.asset.add_asset_status_indicator` is in Alpha Preview and is not considered suitable
        for Production use.  Experimentation in lower environments is encouraged.

    """
    assert isinstance(message, str), 'message must be a string'
    assert isinstance(group, str), 'group must be a string'
    assert isinstance(icon, str), 'icon must be a string'
    assert isinstance(color, str), 'color must be a string'

    assetId = _getAssetByName(asset_name) if asset_name else context(ASSET_ID)
    if not assetId:
        raise NotFound()

    if curate_group:
        payload = {'type': 'assetStatusGroups', 'attributes': {'name': group}}
        try:
            _getSession().post('v2/assetStatusGroups', json={'data': payload})
        except RallyApiError as err:
            # check for Already Exists code, since it should not blow up the function
            if err.code == 409:
                pass
            else:
                raise

    if curate_message:
        payload = {'type': 'assetStatusMessages', 'attributes': {'name': message}}
        try:
            _getSession().post('v2/assetStatusMessages', json={'data': payload})
        except RallyApiError as err:
            # check for Already Exists code, since it should not blow up the function
            if err.code == 409:
                # do nothing, it is alright that the curation already exists
                pass
            else:
                raise

    indicator_payload = {'data': {
        'type': 'assetStatusIndicators',
        'attributes': {
            'group': group,
            'icon': icon,
            'message': message,
            'color': color
        },
        'relationships': {
            'asset': {'data': {'id': assetId, 'type': 'assets'}},
            'job': {'data': {'id': context(JOB_UUID), 'type': 'jobs'}}
        }
    }}

    path = f'v2/assetStatusIndicators'
    _getSession().post(path, data=json.dumps(indicator_payload))


def clear_asset_status_indicator(indicator_id):
    """ Sets the `cleared` flag on the given Asset Status Indicator

    :param indicator_id: The id of the indicator to clear
    :type indicator_id: int

    .. warning::

        :func:`rally.experimental.asset.clear_asset_status_indicator` is in Alpha Preview and is not considered suitable
        for Production use.  Experimentation in lower environments is encouraged.

    """
    indicator_id = int(indicator_id)
    payload = {
        'data': {
            'type': 'assetStatusIndicators',
            'attributes': {'cleared': True}
        }
    }
    _getSession().patch(f'v2/assetStatusIndicators/{indicator_id}', data=json.dumps(payload))


def clear_all_asset_status_indicators(group=None, asset_name=None):
    """ Sets the `cleared` flag on: all indicators or all indicators in the named group associated with an asset.

    :param group: The name of the group from which to clear all indicators, defaults to clearing all of the asset's indicators
    :type group: str, optional
    :param asset_name: The name of a different asset from which to clear all indicators, defaults to the current asset
    :type asset_name: str, optional

    .. warning::

        :func:`rally.experimental.asset.clear_all_asset_status_indicators` is in Alpha Preview and is not considered
        suitable for Production use.  Experimentation in lower environments is encouraged.

    """
    indicatorIds = [indicator['id'] for indicator in get_asset_status_indicators(group=group, asset_name=asset_name)]
    for indicator_id in indicatorIds:
        clear_asset_status_indicator(indicator_id)
