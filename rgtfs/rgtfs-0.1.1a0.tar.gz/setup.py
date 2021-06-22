# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['rgtfs', 'rgtfs.helpers']

package_data = \
{'': ['*']}

install_requires = \
['gtfs-kit==5.0.2', 'pandas>=1.1.0,<2.0.0', 'pymove==2.7.2']

setup_kwargs = {
    'name': 'rgtfs',
    'version': '0.1.1a0',
    'description': 'Calculates the retroactive GTFS based on GPS data',
    'long_description': "# rGTFS\n\nTool to compare planned GTFS with real GTFS (rGTFS) extracted from GPS data.\n# Working API\n\n```\nimport rgtfs\n\n# Generage Realized Trips from GTFS\nrgtfs.generate_realized_trips_from_gtfs(gtfs_path)\n\n# Treat Rio de Janeiro BRT realized trips\nrgtfs.helpers.treat_rj_brt_realized_trips(brt_raw_realized_trips_path)\n```\n\n# New Tables Documentation\n\n##### Realized Trips\n\n| Field Name | Type | Required | Description |\n|-|-|-|-|\n| vehicle_id | ID referencing vehicles.vehicle_id | Required | identifies vehicle |\n| departure_datetime | Datetime | Required | Time at which the vehicle departs from the first stop |\n| arrival_datetime | Datetime | Required | Time at which the vehicle departs from the stop |\n| departure_id | ID referencing stops.stop_id or garages.garage.id | Required | Departure unique identifier. Can be a stop_id or a garage_id. |\n| arrival_id | ID referencing stops.stop_id or garages.garage.id | Required | Arrival unique identifier. Can be a stop_id or a garage_id. Can be empty if trajectory_type is garage_to_stop. |\n| distance | Float | Required | Distance travelled in the trajectory in seconds |\n| elapsed_time | Integer | Required | Trajectory duration in seconds |\n| average_speed | Float | Required | Trajectory average speed in km/h |\n| trajectory_type | Enum | Required | One of the followin trajectory types: 1. complete_trip: A complete one-way trip. Departure stop and Arrival stop should map to the first and last stop of the trip respectively. 2. not_complete_trip: An incomplete one-way trip. Departure stop should map to the first stop of the trip, but the trip was sundelly aborted so it has no Arrival. 3. garage_to_stop: A trajectory between a garage and a stop or otherwise. One of the stops should map to a garage_id.  |\n| trip_id | ID referencing trips.trip_id | Optional | Trip unique identier. Only applicable for trajectory_type: complete_trip and not_complete_trip |\n| trip_short_name | Trip name | Optioanl | Public facing text used to identify the trip to riders, for instance, to identify train numbers for commuter rail trips. If riders do not commonly rely on trip names, leave this field empty. A trip_short_name value, if provided, should uniquely identify a trip within a service day; it should not be used for destination names or limited/express designations. It can be used if trip_id is not available. |\n\n\n## How to go about it\n\n##### Set standards of how the GPS data should look like. What are the accepted columns? How should the feed be structured? What is the best fit with GTFS?\n##### What are the expected results?\n\n- Retrospective GTFS, rGTFS, which is a GTFS of what actually happend on date YYYY-MM-DD\n  - Fully dependend on GPS. It'd have to create the shapes, stops, lines, etc\n  - Based on planned GTFS. It'd use the current GTFS shapes, stops and lines to support the algorithm\n\n- Comparisson between GTFS and rGTFS\n  - Difference in bus frequency/waiting times\n  - Difference in the fleet. What are the lines larges fleet difference?\n  - Ponctuality score. \n\n##### How the module should look like?\n\n- io (read and write to GTFS)\n- GTFS object\n- rGTFS builder to GTFS object\n- \n\n\n## Similar Projects\n\nRelated projects by other people:\n* https://github.com/CUTR-at-USF/retro-gtfs/tree/GTFS-Realtime (a fork of this code extending it to GTFS-realtime data sources)\n* https://github.com/WorldBank-Transport/Transitime\n\n",
    'author': 'Joao Carabetta',
    'author_email': 'joao.carabetta@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/RJ-SMTR/rGTFS',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
