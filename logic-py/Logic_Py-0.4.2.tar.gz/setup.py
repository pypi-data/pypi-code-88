# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['logic_py']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.0,<2.0']

setup_kwargs = {
    'name': 'logic-py',
    'version': '0.4.2',
    'description': 'Python Package to realize combinational logic gates',
    'long_description': '# Logic_Py\n\n[![Made with Python3](https://img.shields.io/badge/Made%20With-Python3-green)](https://www.python.org/)\n[![GitHub license](https://img.shields.io/badge/license-Apache2.0-blue.svg)](https://github.com/vishwesh-vishwesh/Logic_Py/blob/main/LICENSE)\n[![Github version](https://img.shields.io/badge/version-0.4.1-green)](https://github.com/vishwesh-vishwesh/Logic_Py)\n\n### *Update : Logic_Py 0.4.1*\n\n1. If input array contains a non-binary element, A ValueError is returned with the exact location of non-binary element in the input array\n```python\nfrom basic_gates import AND\nA = [1,0,1,3]\nB = [0,0,1,1]\ny = AND(A,B)\n```\n Above code returns `ValueError: input must be binary, 0 or  1 in first input index 3`\n\n2. If all the input array lengths are not same, Again code throws a ValueError\n```python\nfrom basic_gates import OR\nA = [1,0,1]\nB = [0,0,1,1]\ny = OR(A,B)\n```\n Above code returns `ValueError: Length of both inputs must be same`\n\n3. Half subtractor and Full subtractor are added to Arithmatic gates\n```python\nfrom arithmatic_gates import half_subtractor, full_subtractor\nB = [1,1,0,1,1,0,0,1,0,0]\nA = [0,0,0,1,0,1,1,0,1,1]\nDifference, Borrow = half_subtractor(A,B)\nprint("Difference : ", Difference, "Borrow : ", Borrow)\n```\n Above snippet returns Difference :  `Difference :  [1, 1, 0, 0, 1, 1, 1, 1, 1, 1] Borrow :  [0, 0, 0, 0, 0, 1, 1, 0, 1, 1]`\n\n4. Code conversions BCD to Excess3 and vice versa are added to Combinational circuits\n```python\nfrom combinational_gates import BCD2Excess3, Excess32BCD\nA = [1,1,0,1,1,0,0,1,0,0]\nB = [0,0,0,1,0,1,1,0,1,1]\nC = [0,1,0,1,0,1,0,0,0,0]\nD = [1,1,0,1,1,0,0,1,0,0]\nw,x,y,z = BCD2Excess3(A,B,C,D)\n```\n Above code saves 4 coverted Excess3 bits in w,x,y,z\n\n5. Encoders and Decoders are added to Logic circuits\n```python\nfrom Logic_circuits import Decoder2_4,Decoder4_16,Decoder3_8,Encoder2_1,Encoder4_2,Encoder8_3,Priority_Enc4_2\n```\n6. Plots are added for half subtractor and full subtractor\n ```python\nfrom plotting import plot_half_subtractor\nx,y = plot_half_subtractor(B,C)\n```\n Above snippet returns a plot of difference and Borrow and also loads difference and borrow onto the variables x and y.\n![Half Subtractor](https://github.com/vishwesh-vishwesh/Logic_Py/blob/main/Figure%202021-06-24%20073914.png "Half subtractor")\n\n\n# Introduction\nThis Python package enables the user to realise Logic based combinational circuits built on basic logic gates.\nAll the inputs must be binary and of same length for the functions to perform desired operation. \n\n## Installation\n`pip install logic-py`\n```python\nfrom Logic_Py import AND, full_adder, plot_secondary\n```\n\n## Basic Gates\n`basic_gates`\n\nThere are 7 basic gates, all other secondaary and combinational gates are the combinations of these 7 basic gates.\n- AND, OR, NOT, NAND, NOR,XNOR,XOR\n```python\nfrom Logic_Py import AND\n```\n\n## Secondary Gates\n`secondary_gates`\n\nThere are 16 Secondary gates, which take 4 binary inputs and 1 binary output.\n- AND_AND, AND_OR, AND_NAND, AND_NOR, OR_AND, OR_OR, OR_NAND, OR_NOR, NAND_AND, NAND_OR, NAND_NAND, NAND_NOR, NOR_AND, NOR_OR, NOR_NAND, NOR_NOR,\n\n## Combinational Gates\n`combintional_gates`\n\nFew combinational circuits are added as start in this beta version, few more will follow in the coming update.\n- Binary2Gray, Gray2Binary, EParity_gen, EParity_check, OParity_gen, OParity_check, Excess32BCD, BCD2Excess3\n\n## Arithmatic Gates\n`arithmatic_gates`\nTwo arithmatic gates are added for the beta version, more will follow in the coming update.\n*update 0.4.1 added subtractors*\n- Half Adder - `half_adder`\n- Full Adder - `full_adder`\n- Half Subtractor - `half_subtractor`\n- Full Subtractor - `full_subtractor`\n\n## Plots\n`plotting`\n\nPlots for the basic gates, secondary gates and arithmatic gates are available with the current version.\n- plot_full_adder, plot_half_adder, plot_secondary, plot_basic\n- *update 0.4.1 added `plot_half_adder` and `plot_full_adder`\n\n## Citation\n- [Tutorialspoint - digital circuit basics](https://www.tutorialspoint.com/digital_circuits)\n- [Geeksforgeeks digital circuits](https://www.geeksforgeeks.org/)\n\n>Use [Github](https://github.com/vishwesh-vishwesh/Logic_Py/) for further updates. \n>Please kindly cite incase you use the package and fork.\n\n>Use Hellow world example for the syntax\n>or use help function in python console\n```python\nhelp(AND)\n```\n\n',
    'author': 'Vishwesh',
    'author_email': 'vishwesh.arush@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Vishwesh-Vishwesh/Logic_Py',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.0,<4.0',
}


setup(**setup_kwargs)
