# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aleksis_meta']

package_data = \
{'': ['*']}

install_requires = \
['aleksis-app-alsijil==2.0rc1',
 'aleksis-app-chronos==2.0rc1',
 'aleksis-app-dashboardfeeds==2.0rc1',
 'aleksis-app-hjelp==2.0rc1',
 'aleksis-core==2.0rc2']

extras_require = \
{'csvimport': ['aleksis-app-csvimport==2.0rc1'],
 'ldap': ['aleksis-app-ldap==2.0rc1'],
 'untis': ['aleksis-app-untis==2.0rc1']}

setup_kwargs = {
    'name': 'aleksis',
    'version': '2021.6rc1',
    'description': 'Free School Information System Distribution',
    'long_description': 'AlekSIS — All-libre extensible kit for school information systems\n=================================================================\n\nWhat AlekSIS is\n----------------\n\n`AlekSIS`_ is a web-based school information system (SIS) which can be used to\nmanage and/or publish organisational subjects of educational institutions.\n\nFormerly two separate projects (BiscuIT and SchoolApps), developed by\n`Teckids e.V.`_ and a team of students at `Katharineum zu Lübeck`_, they\nwere merged into the AlekSIS project in 2020.\n\nAlekSIS is a platform based on Django, that provides central funstions\nand data structures that can be used by apps that are developed and provided\nseperately. The AlekSIS team also maintains a set of official apps which\nmake AlekSIS a fully-featured software solutions for the information\nmanagement needs of schools.\n\nBy design, the platform can be used by schools to write their own apps for\nspecific needs they face, also in coding classes. Students are empowered to\ncreate real-world applications that bring direct value to their environment.\n\nAlekSIS is part of the `schul-frei`_ project as a component in sustainable\neducational networks.\n\nOfficial apps\n-------------\n\n+--------------------------------------+---------------------------------------------------------------------------------------------+\n| App name                             | Purpose                                                                                     |\n+======================================+=============================================================================================+\n| `AlekSIS-App-Chronos`_               | The Chronos app provides functionality for digital timetables.                              |\n+--------------------------------------+---------------------------------------------------------------------------------------------+\n| `AlekSIS-App-DashboardFeeds`_        | The DashboardFeeds app provides functionality to add RSS or Atom feeds to dashboard         |\n+--------------------------------------+---------------------------------------------------------------------------------------------+\n| `AlekSIS-App-Hjelp`_                 | The Hjelp app provides functionality for aiding users.                                      |\n+--------------------------------------+---------------------------------------------------------------------------------------------+\n| `AlekSIS-App-LDAP`_                  | The LDAP app provides functionality to import users and groups from LDAP                    |\n+--------------------------------------+---------------------------------------------------------------------------------------------+\n| `AlekSIS-App-Untis`_                 | This app provides import and export functions to interact with Untis, a timetable software. |\n+--------------------------------------+---------------------------------------------------------------------------------------------+\n| `AlekSIS-App-Alsijil`_               | This app provides an online class register.                                                 |\n+--------------------------------------+---------------------------------------------------------------------------------------------+\n| `AlekSIS-App-CSVImport`_             | This app provides import functions to import data from CSV files.                           |\n+--------------------------------------+---------------------------------------------------------------------------------------------+\n\n\nLicence\n-------\n\n::\n\n  Copyright © 2017, 2018, 2019, 2020, 2021 Jonathan Weth <wethjo@katharineum.de>\n  Copyright © 2017, 2018, 2019, 2020 Frank Poetzsch-Heffter <p-h@katharineum.de>\n  Copyright © 2018, 2019, 2020, 2021 Julian Leucker <leuckeju@katharineum.de>\n  Copyright © 2018, 2019, 2020, 2021 Hangzhi Yu <yuha@katharineum.de>\n  Copyright © 2019, 2020, 2021 Dominik George <dominik.george@teckids.org>\n  Copyright © 2019, 2020, 2021 Tom Teichler <tom.teichler@teckids.org>\n  Copyright © 2019 mirabilos <thorsten.glaser@teckids.org>\n  Copyright © 2021 Lloyd Meins <meinsll@katharineum.de>\n  Copyright © 2021 magicfelix <felix@felix-zauberer.de>\n  \n  Licenced under the EUPL, version 1.2 or later, by Teckids e.V. (Bonn, Germany).\n\nPlease see the LICENCE.rst file accompanying this distribution for the\nfull licence text or on the `European Union Public Licence`_ website\nhttps://joinup.ec.europa.eu/collection/eupl/guidelines-users-and-developers\n(including all other official language versions).\n\n.. _AlekSIS: https://aleksis.org/\n.. _Teckids e.V.: https://www.teckids.org/\n.. _Katharineum zu Lübeck: https://www.katharineum.de/\n.. _European Union Public Licence: https://eupl.eu/\n.. _schul-frei: https://schul-frei.org/\n.. _AlekSIS-Core: https://edugit.org/AlekSIS/official/AlekSIS-App-Core\n.. _AlekSIS-App-Chronos: https://edugit.org/AlekSIS/official/AlekSIS-App-Chronos\n.. _AlekSIS-App-DashboardFeeds: https://edugit.org/AlekSIS/official/AlekSIS-App-DashboardFeeds\n.. _AlekSIS-App-Hjelp: https://edugit.org/AlekSIS/official/AlekSIS-App-Hjelp\n.. _AlekSIS-App-LDAP: https://edugit.org/AlekSIS/official/AlekSIS-App-LDAP\n.. _AlekSIS-App-Untis: https://edugit.org/AlekSIS/official/AlekSIS-App-Untis\n.. _AlekSIS-App-Alsijil: https://edugit.org/AlekSIS/official/AlekSIS-App-Alsijil\n.. _AlekSIS-App-CSVImport: https://edugit.org/AlekSIS/official/AlekSIS-App-CSVImport\n',
    'author': 'Dominik George',
    'author_email': 'dominik.george@teckids.org',
    'maintainer': 'Jonathan Weth',
    'maintainer_email': 'wethjo@katharineum.de',
    'url': 'https://aleksis.org/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
}


setup(**setup_kwargs)
