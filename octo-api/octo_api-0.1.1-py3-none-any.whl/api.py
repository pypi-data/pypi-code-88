#!/usr/bin/env python3
#
#  api.py
"""
The primary interface to the Octopus Energy API.

.. note::

	The Octopus Energy API uses the term "Grid Supply Point" (GSP) to refer to what are actually
	the 14 former Public Electricity Suppliers. The GSP terminology has been used here to better
	reflect the REST API.

"""
#
#  Copyright © 2020 Dominic Davis-Foster <dominic@davis-foster.co.uk>
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
#  EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
#  MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
#  IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
#  DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
#  OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE
#  OR OTHER DEALINGS IN THE SOFTWARE.
#

# stdlib
from datetime import datetime
from typing import Any, Dict, MutableMapping, Optional, Union

# 3rd party
from apeye.slumber_url import SlumberURL
from domdf_python_tools.secrets import Secret
from typing_extensions import Literal

# this package
from octo_api.consumption import Consumption
from octo_api.pagination import PaginatedResponse
from octo_api.products import DetailedProduct, Product, RateInfo
from octo_api.utils import MeterPointDetails, RateType, Region

__all__ = ["OctoAPI"]


class OctoAPI:
	"""
	The primary interface to the Octopus Energy API.

	:param api_key: API key to access the Octopus Energy API.

	If you are an Octopus Energy customer, you can generate an API key from your
	`online dashboard <https://octopus.energy/dashboard/developer/>`_.
	"""

	def __init__(self, api_key: str):

		#: The API key to access the Octopus Energy API.
		self.API_KEY: Secret = Secret(api_key)

		#: The base URL of the Octopus Energy API.
		self.API_BASE: SlumberURL = SlumberURL("https://api.octopus.energy/v1", auth=(self.API_KEY.value, ''))

	def get_products(
			self,
			is_variable: bool = None,
			is_green: bool = None,
			is_tracker: bool = None,
			is_prepay: bool = None,
			is_business: bool = False,
			available_at: Optional[datetime] = None,
			) -> PaginatedResponse[Product]:
		"""
		Returns a list of energy products.

		By default, the results only include public energy products.
		Authenticated organisations will also see products available to their organisation.

		:param is_variable: Show only variable products.
		:param is_green: Show only green products.
		:param is_tracker: Show only tracker products.
		:param is_prepay: Show only pre-pay products.
		:param is_business: Show only business products.
		:param available_at: Show products available for new agreements on the given datetime.
			Defaults to the current datetime, effectively showing products that are currently available.
		:no-default available_at:

		.. https://developer.octopus.energy/docs/api/#list-products

		**Example**

		.. code-block:: python

			>>> api.get_products()[0]
			octo_api.products.Product(
				available_from='2016-01-01T:00:00:00+00:00',
				available_to=None,
				brand='AFFECT_ENERGY',
				code='1201',
				description='Affect Standard Tariff',
				display_name='Affect Standard Tariff',
				full_name='Affect Standard Tariff',
				is_business=False,
				is_green=False,
				is_prepay=False,
				is_restricted=False,
				is_tracker=False,
				is_variable=True,
				links=[
					{
						'href': 'https://api.octopus.energy/v1/products/1201/',
						'method': 'GET',
						'rel': 'self'
					}
				],
				term=None,
				direction='IMPORT',
			)

		"""

		parameters: Dict[str, Any] = {}

		if is_variable is not None:
			parameters["is_variable"] = is_variable
		if is_green is not None:
			parameters["is_green"] = is_green
		if is_tracker is not None:
			parameters["is_tracker"] = is_tracker
		if is_prepay is not None:
			parameters["is_prepay"] = is_prepay
		parameters["is_business"] = is_business
		if available_at is not None:
			parameters["available_at"] = available_at.isoformat()

		query_url = self.API_BASE / "products"
		return PaginatedResponse(query_url, parameters, obj_type=Product)

	def get_product_info(
			self,
			product_code: str,
			tariffs_active_at: Optional[datetime] = None,
			) -> DetailedProduct:
		"""
		Retrieve the details of a product (including all its tariffs) for a particular point in time.

		:param product_code: The code of the product to be retrieved, for example ``VAR-17-01-11``.
		:param tariffs_active_at: The point in time in which to show the active charges. Defaults to current datetime.
		:no-default available_at:

		.. https://developer.octopus.energy/docs/api/#retrieve-a-product


		**Example**

		.. code-block:: python

			>>> api.get_product_info(product_code='VAR-17-01-11')
			octo_api.products.DetailedProduct(
				available_from='2017-01-11T10:00:00+00:00',
				available_to='2018-02-15T00:00:00+00:00',
				brand='S_ENERGY',
				code='7-01-11',
				description='This variable tariff always offers great value - driven by our'
							'belief that prices should be fair for the long term, not just a'
							'fixed term. We aim for 50% renewable electricity on this tariff.',
				display_name='pus',
				full_name='ctopus January 2017 v1',
				is_business=False,
				is_green=False,
				is_prepay=False,
				is_restricted=False,
				is_tracker=False,
				is_variable=True,
				links=[
					{
						'href': 'https://api.octopus.energy/v1/products/VAR-17-01-11/',
						'method': 'GET',
						'rel': 'self'
					}
				],
				term=None,
				tariffs_active_at='2020-10-26T11:15:17.208285+00:00',
				single_register_electricity_tariffs=RegionalTariffs(['direct_debit_monthly']),
				dual_register_electricity_tariffs=RegionalTariffs(['direct_debit_monthly']),
				single_register_gas_tariffs=RegionalTariffs(['direct_debit_monthly']),
				sample_quotes=RegionalQuotes([dual_fuel_dual_rate, dual_fuel_single_rate, electricity_dual_rate, electricity_single_rate]),
				sample_consumption={
					'electricity_single_rate': {'electricity_standard': 2900},
					'electricity_dual_rate': {
						'electricity_day': 2436,
						'electricity_night': 1764
					},
					'dual_fuel_single_rate': {
						'electricity_standard': 2900,
						'gas_standard': 12000
					},
					'dual_fuel_dual_rate': {
						'electricity_day': 2436,
						'electricity_night': 1764,
						'gas_standard': 12000
					}
				},
			)
		"""

		parameters = {}

		if tariffs_active_at is not None:
			parameters["tariffs_active_at"] = tariffs_active_at.isoformat()

		query_url = self.API_BASE / "products" / product_code
		return DetailedProduct(**query_url.get(**parameters))

	def get_tariff_charges(
			self,
			product_code: str,
			tariff_code: str,
			fuel: Literal["electricity", "gas"],
			rate_type: RateType,
			period_from: Optional[datetime] = None,
			period_to: Optional[datetime] = None,
			page_size: int = 100,
			) -> PaginatedResponse[RateInfo]:
		"""
		Returns a list of time periods and their associated unit rates charges.

		If the tariff has a fixed unit rate the list will only contain one element.

		:param product_code: The code of the product to be retrieved, for example ``VAR-17-01-11``.
		:param tariff_code: The code of the tariff to be retrieved, for example ``E-1R-VAR-17-01-11-A``.
			From what I can tell the format is::

				<E for electricity><optional hyphen><1R for single rate?><the product code>-<the grid supply point>

		:param fuel:
		:param rate_type:
		:param period_from: Show charges active from the given datetime (inclusive).
			This parameter can be provided on its own.
		:param period_to: Show charges active up to the given datetime (exclusive).
			You must also provide the ``period_from`` parameter in order to create a range.
		:param page_size: Page size of returned results.
			Default is ``100``, maximum is ``1,500`` to give up to a month of half-hourly prices.
		:no-default page_size:

		.. https://developer.octopus.energy/docs/api/#list-tariff-charges

		.. note::

			If you're using this API to query future unit-rates of the Agile Octopus product,
			note that day-ahead prices are normally created by 4pm in the Europe/London timezone.
			Further, the market index used to calculate unit rates is based in the CET timezone (UTC+1)
			and so its "day" corresponds to 11pm to 11pm in UK time.
			Hence, if you query today's unit rates before 4pm, you'll get 46 results back rather than 48.
		"""

		parameters: MutableMapping[str, Union[str, int]] = {}

		if period_from is not None:
			parameters["period_from"] = period_from.isoformat()
		if period_to is not None:
			parameters["period_to"] = period_to.isoformat()

		if page_size > 1500:
			raise ValueError("'page_size' may not be greater than 1,500")

		parameters["page_size"] = int(page_size)

		query_url = self.API_BASE / "products" / product_code / f"{fuel}-tariffs" / tariff_code / str(rate_type)
		return PaginatedResponse(query_url, query_params=parameters, obj_type=RateInfo)

	def get_meter_point_details(self, mpan: str) -> MeterPointDetails:
		"""
		Retrieve the details of a meter-point.

		This can be used to get the GSP of a given meter-point.

		:param mpan: The electricity meter-point's MPAN.

		:return:
		"""

		return MeterPointDetails._from_dict((self.API_BASE / "electricity-meter-points" / mpan).get())

	def get_grid_supply_point(self, postcode: str) -> Region:
		"""
		Returns the grid supply point for the given postcode.

		:param postcode:

		:raises: :exc:`ValueError` if the postcode cannot be mapped to a GSP.
		"""

		query_url = self.API_BASE / "industry" / "grid-supply-points"

		results = query_url.get(postcode=postcode)["results"]
		if results:
			return Region(results[0]["group_id"])
		else:
			raise ValueError(f"Cannot map the postcode {postcode!r} to a GSP.")

	def get_consumption(
			self,
			mpan: str,
			serial_number: str,
			fuel: Literal["electricity", "gas"],
			period_from: Optional[datetime] = None,
			period_to: Optional[datetime] = None,
			page_size: int = 100,
			reverse: bool = False,
			group_by: Optional[str] = None,
			) -> PaginatedResponse[Consumption]:
		r"""
		Return a list of consumption values for half-hour periods for a given meter-point and meter.

		Unit of measurement:

		* Electricity meters: kWh
		* SMETS1 Secure gas meters: kWh
		* SMETS2 gas meters: m\ :superscript:`3`

		.. attention::

			Half-hourly consumption data is only available for smart meters.
			Requests for consumption data for non-smart meters will return an empty response payload.

		:param mpan: The electricity meter-point's MPAN or gas meter-point's MPRN.
		:param serial_number: The meter's serial number.
		:param fuel:
		:param period_from: Show consumption for periods which start at or after the given datetime.
			This parameter can be provided on its own.
		:param period_to: Show consumption for periods which start at or before the given datetime.
			This parameter also requires providing the ``period_from`` parameter to create a range.
		:param page_size: Page size of returned results.
			Default is ``100``, maximum is ``25,000`` to give a full year of half-hourly consumption details.
		:no-default page_size:
		:param reverse: Returns the results ordered from most oldest to newest. By default the results are from most recent backwards.
		:no-default reverse:
		:param group_by: The grouping of the consumption data.
			By default the consumption is returned in half-hour periods.

			Possible alternatives are:

			* ``'hour'``
			* ``'day'``
			* ``'week'``
			* ``'month'``
			* ``'quarter'``
		:no-default group_by:
		"""

		parameters: MutableMapping[str, Union[str, int]] = {}

		if period_from is not None:
			parameters["period_from"] = period_from.isoformat()
		if period_to is not None:
			parameters["period_to"] = period_to.isoformat()

		if page_size > 25000:
			raise ValueError("'page_size' may not be greater than 25,000")

		parameters["page_size"] = int(page_size)

		if reverse:
			parameters["order_by"] = "period"
		if group_by is not None:
			parameters["group_by"] = str(group_by)

		query_url = self.API_BASE / f"{fuel}-meter-points" / mpan / "meters" / serial_number / "consumption"
		return PaginatedResponse(query_url, query_params=parameters, obj_type=Consumption)
