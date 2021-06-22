"""
Sites are physical locations where flexibility assets are deployed.
"""

from bambooapi_client.api.sites_api import SitesApi as _SitesApi
from bambooapi_client.exceptions import NotFoundException
from bambooapi_client.model.site import Site

import pandas as pd


class SitesApi(object):
    """Implementation for '/v1/sites' endpoints."""

    def __init__(self, bambooapi_client):
        """Initialize defaults."""
        self._bambooapi_client = bambooapi_client
        self._api_instance = _SitesApi(bambooapi_client.api_client)

    def list_sites(self):
        """List sites."""
        return self._api_instance.list_sites(_check_return_type=False)

    def get_site(self, site_id):
        """Get site by id."""
        try:
            return self._api_instance.read_site(site_id, _check_return_type=False)
        except NotFoundException:
            return None

    def get_site_id(self, site_name):
        """Get site id by name."""
        try:
            return self._api_instance.get_site_id_by_name(site_name)
        except NotFoundException:
            return None

    def list_devices(self, site_id, device_type='hvac'):
        """List devices for a given site."""
        return self._api_instance.list_devices(site_id, device_type=device_type)

    def get_device(self, site_id, device_name):
        """Get single device by name for a given site."""
        try:
            return self._api_instance.read_device(site_id, device_name)
        except NotFoundException:
            return None

    def list_zones(self, site_id):
        """List zones for a given site."""
        return self._api_instance.list_zones(site_id)

    def get_zone(self, site_id, zone_name):
        """Get single zone by name for a given site."""
        try:
            return self._api_instance.read_zone(site_id, zone_name)
        except NotFoundException:
            return None

    def read_baseline_model(self, site_id, asset_name, horizon='day-ahead'):
        """Read baseline model for a given site and asset."""
        try:
            return self._api_instance.read_baseline_model(site_id, asset_name,
                                                          horizon=horizon,
                                                          _check_return_type=False)
        except NotFoundException:
            return None

    def update_baseline_model(self, site_id, asset_name, baseline_model,
                              horizon='day-ahead'):
        """Update baseline model for a given site and asset."""
        return self._api_instance.update_baseline_model(site_id, asset_name,
                                                        baseline_model,
                                                        horizon=horizon)

    def read_measurements(self, site_id, asset_name, start=None, stop=None):
        """Read site asset measurements."""
        if start and stop:
            _meas = self._api_instance.read_asset_measurements(site_id, asset_name,
                                                               period='CustomRange',
                                                               period_start=start,
                                                               period_stop=stop,
                                                               _check_return_type=False)
        else:
            _meas = self._api_instance.read_asset_measurements(site_id, asset_name)
        # Convert DataPoint objects to dict before converting to DF
        if _meas:
            _meas = [m.to_dict() for m in _meas]
            # Convert to DF
            return pd.DataFrame.from_records(_meas, index='time')
        else:
            return pd.DataFrame()
    
    def update_measurements(self, site_id, asset_name, data_frame):
        """Update site asset measurements."""
        _DPs = data_frame.reset_index().to_dict(orient='records')
        return self._api_instance.insert_asset_measurements(site_id,
                                                            asset_name,
                                                            _DPs)

    def read_forecasts(self, site_id, asset_name, horizon='day-ahead',
                       start=None, stop=None):
        """Read site asset forecasts."""
        if start and stop:
            _meas = self._api_instance.read_asset_forecasts(site_id, asset_name,
                                                            horizon=horizon,
                                                            period='CustomRange',
                                                            period_start=start,
                                                            period_stop=stop,
                                                            _check_return_type=False)
        else:
            _meas = self._api_instance.read_asset_forecasts(site_id, asset_name)
        # Convert DataPoint objects to dict before converting to DF
        if _meas:
            _meas = [m.to_dict() for m in _meas]
            # Convert to DF
            return pd.DataFrame.from_records(_meas, index='time')
        else:
            return pd.DataFrame()

    def update_forecasts(self, site_id, asset_name, data_frame, horizon):
        """Update site asset forecasts."""
        _DPs = data_frame.reset_index().to_dict(orient='records')
        return self._api_instance.insert_asset_forecasts(site_id,
                                                         asset_name,
                                                         _DPs,
                                                         horizon=horizon)

    def read_activations(self, site_id, asset_name):
        """Read site asset activations."""
        try:
            return self._api_instance.read_asset_activations(site_id, asset_name,
                                                             _check_return_type=False)
        except NotFoundException:
            return None
