# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['portableqda', 'tests']

package_data = \
{'': ['*']}

install_requires = \
['lxml>=4.6.2,<5.0.0', 'nose>=1.3.7,<2.0.0']

setup_kwargs = {
    'name': 'portableqda',
    'version': '0.4.0',
    'description': 'portableQDA facilitates round-trip information exchange using the REFI-QDA standard: codebooks (QDC files) and QDPX projects. This portable information can be used by any Qualitative Data Analysis (CAQDAS) Software conforming to that XML-based standard, as per https://www.qdasoftware.org',
    'long_description': '# portableQDA\n\nportableQDA facilitates round-trip information exchange using the [REFI-QDA](https://www.qdasoftware.org) standard: codebooks (QDC files) and QDPX projects. This portable information can be used by any [Qualitative Data Analysis (CAQDAS) Software](https://en.wikipedia.org/wiki/Computer-assisted_qualitative_data_analysis_software) conforming to that XML-based standard.\n\nImport/Export formats [QDC and QDPX](https://www.qdasoftware.org/wp-content/uploads/2019/09/REFI-QDA-1-5.pdf) are:   \n\n- suitable for structured archiving of any kind of files, including:\n  + personal corpus of information analysis (text coding, cites, comments)\n  + the source documents themselves (any arbitrary format, including office docs, PDF, html, audio, surverys)\n- well-defined and maintained by the [REF-QDA working group](http://qdasoftware.org)\n- supported and developed by a growing number of participants\n\nQDA stands for Qualitative Data Analysis, as known in social sciences. Related Wikipedia article states: “Qualitative research relies on data obtained by the researcher by first-hand observation, interviews, recordings, […]. The data are generally non-numerical. Qualitative methods include ethnography, grounded theory, discourse analysis […]. These methods have been used in sociology, anthropology, and educational research.”\n\n## Installation\n\n```bash\npip install portableqda\n```\n\n## Basic usage\n\n\n### Testing (specially the output format)\n\nchange your current directory to portableQDA\'s root, then\n\n```bash\npoetry shell\npython tests\n```\n\nproduces various codebooks (QDC files) in your home directory, should be suitable for import by your CAQDAS software. \n\n### Testing the input format\n\n- export a codebook from the QDA software of your choise\n- run the following script:\n```python\nimport portableqda\ncodebook = portableqda.codebookCls(output="portableQDA-output-test.qdc")\ncodebook.readQdcFile(input="/path/to/file-from-first-step.qdc")\ncodebook.writeQdcFile()\n```\n- should throw no errors, check the file ```portableQDA-output-test.qdc``` at your home directory for completeness\n- try to import into your CAQDAS software\n\n\n### Developing\n\nYou will find examples for many use cases at the ```examples``` directory. Some of them are:\n\n```python\n# examples/ex1_codesAndSets.py\nimport portableqda\n#look for output in system logging\n\ncodebook = portableqda.codebookCls(output="codebook_example.qdc") #create a codebook\n\n# create 3 codes and group them in two sets\nfor number in range(3):\n    codebook.createElement(elementCls=portableqda.codeCls,\n                                                name=f"code{number}",\n                                                sets=["set1","set2"])\n    # for error checking, see examples/ex2_flowControl.py \n    \ncodebook.writeQdcFile() # export the codebook as a REFI-QDA 1.5 compliant QDC file\n```\n\nLook for the file `codebook_example.qdc` at your home directory. You can see more of what\'s happening (portableQDA is a library thus not intended for direct use), inserting the following code where the comment "look for output in system logging" is, right after the `import portableqda` statement:\n\n```python\nimport logging\nhandler = logging.StreamHandler(sys.stdout)\nhandler.setLevel(logging.DEBUG)\nformatter = logging.Formatter(\'%(name)s - %(levelname)s - %(message)s\')\nhandler.setFormatter(formatter)\nportableqda.log.addHandler(handler)\nportableqda.log.setLevel(logging.DEBUG)\n```\n\nOutput should look like this:\n\n```log\nportableqda.refi_qda - DEBUG - tree created, root node: \'CodeBook\'. see REFI-QDA 1.5\nportableqda.refi_qda - INFO - output is C:\\Users\\X\\codebook_example.qdc\nportableqda.refi_qda - DEBUG - added code code0 to set set1 \nportableqda.refi_qda - DEBUG - added code code2 to set set2 \nportableqda.refi_qda - INFO - exporting as REFI-QDC  codebook to file: C:\\Users\\X\\codebook_example.qdc\n```\n\n\n## Documentation\n\n## Contributing\n\n## Acknowledgents\n\nLMXL: portableQDA relies on the excellent [lxml package](http://lxml.de) for the  underlying tree data structure and  XML handling   \nREFI-QDA: [working group](http://qdasoftware.org) pushing interoperability and open standards   \n\n\n\n\n## License\n\n[GNU Lesser General Public License v3 (LGPLv3)](https://www.gnu.org/licenses/lgpl-3.0.html)\n',
    'author': 'Leandro Batlle',
    'author_email': 'Leandro.Batlle@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://gitlab.com/portableqda/portableQDA',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
