# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['temperature_conversion']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'temperature-conversion',
    'version': '1.0.0',
    'description': 'Paquete de conversión de temperaturas',
    'long_description': "# temperature_conversion\n\nPaquete de conversión de temperaturas\n\nEl módulo del paquete contiene las funciones siguientes:\n\n- Una función llamada F_to_K que convierte temperaturas en Fahrenheit a Kelvin.\n- Una función llamada C_to_R que convierte temperaturas en Celsius a Rankine.\n- Una función llamada C_to_F que convierte temperaturas en Celsius a Fahrenheit.\n\n## Instalación\n```\npip install temperature_conversion\n```\n\n## Forma de uso\n\n```python\nprint('To be edited')\n```",
    'author': 'Danilo Mendoza',
    'author_email': 'odmendoza@utpl.edu.ec',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/odmendoza/temperature_conversion',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
