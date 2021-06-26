# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['dovado_rtl',
 'dovado_rtl.antlr',
 'dovado_rtl.antlr.generated',
 'dovado_rtl.antlr.generated.SysVerilogHDL',
 'dovado_rtl.antlr.generated.Verilog2001',
 'dovado_rtl.antlr.generated.vhdl',
 'tcl',
 'verilog',
 'vhdl',
 'xdc']

package_data = \
{'': ['*'], 'dovado_rtl.antlr': ['grammars/*', 'grammars/.antlr/*']}

install_requires = \
['BeautifulSoup4>=4.9.1,<5.0.0',
 'antlr4-python3-runtime>=4.8.0,<4.9.0',
 'lxml>=4.5.2,<5.0.0',
 'movado>=0.4.0,<0.5.0',
 'pathvalidate>=2.3.0,<3.0.0',
 'pexpect>=4.8.0,<5.0.0',
 'pymoo==0.4.1',
 'pyyaml>=5.3.1,<6.0.0',
 'typer>=0.3.2,<0.4.0']

extras_require = \
{':python_version >= "3.6" and python_version < "3.7"': ['dataclasses>=0.8,<0.9']}

entry_points = \
{'console_scripts': ['dovado = dovado_rtl.main:main']}

setup_kwargs = {
    'name': 'dovado-rtl',
    'version': '0.7.5',
    'description': 'CLI tool for RTL Design Space Exploration on top of Vivado',
    'long_description': '\n# Table of Contents\n\n1.  [Installation](#orgc020a3e)\n2.  [Usage](#org4f8647b)\n    1.  [Examples](#org12b2aea)\n        1.  [neorv32 (VHDL)](#orgd8de369)\n        2.  [corundum (VERILOG)](#org43556a3)\n        3.  [cv32e40p (SYSTEM-VERILOG)](#org6e54816)\n\nDoVado is a RTL design automation and exploration CLI tool.\n\n\n<a id="orgc020a3e"></a>\n\n# Installation\n\nDoVado needs python 3.6 or higher. Install it through pip, on many Linux systems use pip3 to force python 3 installation.\n\n    pip3 install --user --no-cache dovado-rtl\n\n\n<a id="org4f8647b"></a>\n\n# Usage\n\nDovado has two modes:\n\n-   points: design automation mode in which a file containing parameter values must be given and a file containing all the evaluations is returned for some given metrics,\n-   space: design exploration mode in which parameters and their ranges must be given together with some target metrics and the pareto set of design points with respect to the given metrics is returned.\n\n<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">\n<caption class="t-above"><span class="table-number">Table 1:</span> dovado general parameters</caption>\n\n<colgroup>\n<col  class="org-left" />\n\n<col  class="org-left" />\n\n<col  class="org-left" />\n</colgroup>\n<thead>\n<tr>\n<th scope="col" class="org-left">parameter</th>\n<th scope="col" class="org-left">description</th>\n<th scope="col" class="org-left">mandatory</th>\n</tr>\n</thead>\n\n<tbody>\n<tr>\n<td class="org-left">&#x2013;file-path</td>\n<td class="org-left">path to the target file</td>\n<td class="org-left">yes</td>\n</tr>\n\n\n<tr>\n<td class="org-left">&#x2013;board</td>\n<td class="org-left">vivado descriptor of a board</td>\n<td class="org-left">yes</td>\n</tr>\n\n\n<tr>\n<td class="org-left">&#x2013;parameters</td>\n<td class="org-left">parameters to use either for points/space</td>\n<td class="org-left">yes</td>\n</tr>\n\n\n<tr>\n<td class="org-left">&#x2013;clock-port</td>\n<td class="org-left">RTL identifier of the clock port</td>\n<td class="org-left">yes</td>\n</tr>\n\n\n<tr>\n<td class="org-left">&#x2013;implementation</td>\n<td class="org-left">switch to evaluate designs after implementation (default is after synthesis)</td>\n<td class="org-left">no</td>\n</tr>\n\n\n<tr>\n<td class="org-left">&#x2013;incremental</td>\n<td class="org-left">switch to use incremental synthesis/implementation</td>\n<td class="org-left">no</td>\n</tr>\n\n\n<tr>\n<td class="org-left">&#x2013;directives</td>\n<td class="org-left">list of directives to pass to synthesis, place and route (default is RuntimeOptimized for all three)</td>\n<td class="org-left">no</td>\n</tr>\n\n\n<tr>\n<td class="org-left">&#x2013;target-clock</td>\n<td class="org-left">clock (Mhz) to give as a constraint to Vivado (default=1000)</td>\n<td class="org-left">no</td>\n</tr>\n\n\n<tr>\n<td class="org-left">&#x2013;metrics</td>\n<td class="org-left">list of metrics to target using their integer identifier (default mode is interactive, you will be asked after first synthesis/implementation)</td>\n<td class="org-left">no</td>\n</tr>\n</tbody>\n</table>\n\nAfter those parameters specify points/space both these modes take an argument:\n\n-   points argument: specify the path to the csv file containing the design points to be analyzed. The csv file must contain on each line the value for each of the parameters stated through &#x2013;parameters in the same order,\n-   space argument: a list of ranges stated as 1 2 3 4 where this way we would be defining two ranges (1, 2) for the first parameter and (3, 4) for the second parameter\n\nNo further parameters can be passed to points\n\n<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">\n<caption class="t-above"><span class="table-number">Table 2:</span> dovado space parameters</caption>\n\n<colgroup>\n<col  class="org-left" />\n\n<col  class="org-left" />\n\n<col  class="org-left" />\n</colgroup>\n<thead>\n<tr>\n<th scope="col" class="org-left">parameter</th>\n<th scope="col" class="org-left">description</th>\n<th scope="col" class="org-left">mandatory</th>\n</tr>\n</thead>\n\n<tbody>\n<tr>\n<td class="org-left">&#x2013;power-of-2</td>\n<td class="org-left">list of &rsquo;y&rsquo; or &rsquo;n&rsquo; where each corresponding parameter, in the same order, is specified as a power of 2 (default is &ldquo;n&rdquo; for all parameters)</td>\n<td class="org-left">no</td>\n</tr>\n\n\n<tr>\n<td class="org-left">&#x2013;param-initial-values</td>\n<td class="org-left">state parameters which are guaranteed to synthesize/implement in order to retrieve the usage metrics after first synthesis</td>\n<td class="org-left">no</td>\n</tr>\n\n\n<tr>\n<td class="org-left">&#x2013;optimization-runtime</td>\n<td class="org-left">set as a termination condition a timeout (which will be taken as a hint and not strictly respected) as hh:mm:ss (default is a tolerance based termination criterion)</td>\n<td class="org-left">no</td>\n</tr>\n\n\n<tr>\n<td class="org-left">&#x2013;record-design-values</td>\n<td class="org-left">record all design values in a csv file</td>\n<td class="org-left">no</td>\n</tr>\n\n\n<tr>\n<td class="org-left">&#x2013;read-design-values</td>\n<td class="org-left">read design values from a csv file</td>\n<td class="org-left">no</td>\n</tr>\n</tbody>\n</table>\n\nDirectory structure is vital for the functioning of the tool:\n\n-   VHDL: if a package is used the corresponding folder must be named exactly as the package; if one wants to analyse a module in a project with multiple packages each file belonging to a given package must reside in a subfolder with the same name as the package it belongs to:\n    -   package-name (top folder must have the name of the top package if it exists or any name if it does not exist)\n        -   file-1 (belonging to package-name)\n        -   file-2 (belonging to package-name)\n        -   subpackage1-name\n            -   file-1 (belonging to subpackage-name)\n            -   file-2 (belonging to subpackage-name)\n            -   &#x2026;\n        -   subpackage2-name\n            -   &#x2026;\n        -   &#x2026;\n-   VERILOG/SYSTEM-VERILOG: include directives are not supported all files must be in the same folder, no subfolders allowed.\n\n\n<a id="org12b2aea"></a>\n\n## Examples\n\n\n<a id="orgd8de369"></a>\n\n### neorv32 (VHDL)\n\n    git clone https://github.com/stnolting/neorv32\n    cd neorv32/rtl\n    mv core neorv32\n\nChanging the name of the core folder, which contains all vhdl files, to the name of the package which is used along the files is mandatory to make dovado get &rsquo;use&rsquo; directives right.\nExploring the parameter space of the top module:\n\n    dovado --file-path <path to "neorv32/rtl/neorv32/neorv32_top.vhd"> --board xc7k70tfbv676-1 --parameters MEM_INT_IMEM_SIZE --parameters MEM_INT_DMEM_SIZE --clock-port clk_i --metrics 0 --metrics 1 --metrics 4 --metrics 9 space 16384 131072 8129 65536 --power-of-2 y --power-of-2 y\n\nAbove we are optimizing two memory parameters (MEM<sub>INT</sub><sub>IMEM</sub><sub>SIZE</sub>, MEM<sub>INT</sub><sub>DMEM</sub><sub>SIZE</sub>) with clk<sub>i</sub> as the clock port with metrics chosen:\n\n-   frequency (0)\n-   LUT occupation (1)\n-   REGISTER occupation (4)\n-   BRAM occupation (9)\n\nRanges are specified after space and we also specify that we want to search only among power of 2&rsquo;s solutions.\n\n\n<a id="org43556a3"></a>\n\n### corundum (VERILOG)\n\n    git clone https://github.com/corundum/corundum\n    cd corundum/\n\nExploring the parameter space of the top module:\n\n    dovado --file-path <path to "corundum/fpga/common/rtl/cpl_queue_manager.v"> --board xc7k70tfbv676-1 --target-clock 100000 --parameters OP_TABLE_SIZE --parameters QUEUE_INDEX_WIDTH --parameters PIPELINE --clock-port clk --metrics 0 --metrics 1 --metrics 4 --metrics 9 space 8 64 4 11 2 32 --record-design-values\n\n\n<a id="org6e54816"></a>\n\n### cv32e40p (SYSTEM-VERILOG)\n\n    git clone https://github.com/openhwgroup/cv32e40p\n    cd rtl\n    mkdir testing\n    cp cv32e40p_fifo.sv testing/\n\nIn this project an include directory is used but dovado does not currently support it thus we create a subfolder, name may be whatever, where to isolate the module we are interested in studying. This workaround is only possible if the module one wants to study works standalone without include directives.\n\n    dovado --file-path ../../test_projects/cv32e40p/rtl/testing/cv32e40p_fifo.sv --board xc7k70tfbv676-1 --target-clock 100000 --parameters DEPTH --parameters DATA_WIDTH --clock-port clk_i --metrics 0 --metrics 1 --metrics 4 --metrics 9 space 2 4294967296 2 64 --power-of-2 y --power-of-2 y\n\n',
    'author': 'Daniele Paletti',
    'author_email': 'danielepaletti98@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/DPaletti/dovado',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.6.1,<4.0.0',
}


setup(**setup_kwargs)
