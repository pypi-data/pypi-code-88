# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src',
 'instawow_gui': 'gui-webview/src/instawow_gui',
 'instawow_gui.frontend': 'gui-webview/src/instawow_gui/frontend',
 'instawow_gui.resources': 'gui-webview/src/instawow_gui/resources',
 'instawow_gui.templates': 'gui-webview/src/instawow_gui/templates'}

packages = \
['instawow',
 'instawow.migrations',
 'instawow.migrations.versions',
 'instawow.wa_templates',
 'instawow_gui',
 'instawow_gui.frontend',
 'instawow_gui.resources',
 'instawow_gui.templates']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.7.4,<4.0.0',
 'alembic>=1.4.3,<2.0.0',
 'click>=7.1,<9',
 'jinja2>=2.11,<4',
 'loguru<1',
 'pluggy>=0.13,<0.14',
 'prompt-toolkit>=3.0.15,<4.0.0',
 'pydantic>=1.8.2,<2.0.0',
 'questionary>=1.8,<2.0',
 'rapidfuzz>=1.4.1,<2.0.0',
 'sqlalchemy>=1.3.19,<2.0.0',
 'typing-extensions>=3.10.0.0,<4.0.0.0',
 'yarl>=1.4,<2.0']

extras_require = \
{'gui': ['aiohttp-rpc>=0.6.3', 'toga>=0.3.0.dev27'],
 'gui:platform_system == "Darwin"': ['toga-cocoa>=0.3.0.dev27'],
 'gui:platform_system == "Linux"': ['toga-gtk>=0.3.0.dev27'],
 'gui:platform_system == "Windows"': ['cefpython3==66.1',
                                      'toga-winforms>=0.3.0.dev27'],
 'test': ['aresponses>=2.0,<3.0',
          'coverage[toml]>=5.2,<6.0',
          'pytest>=6.0.1,<7.0.0',
          'pytest-asyncio>=0.14,<0.15',
          'pytest-xdist>=2.2.1,<3.0.0'],
 'types': ['sqlalchemy2-stubs']}

entry_points = \
{'console_scripts': ['instawow = instawow.cli:main']}

setup_kwargs = {
    'name': 'instawow',
    'version': '1.26.0',
    'description': 'CLI for managing World of Warcraft add-ons',
    'long_description': "*instawow*\n==========\n\n.. image:: https://img.shields.io/matrix/wow-addon-management:matrix.org\n   :target: https://matrix.to/#/#wow-addon-management:matrix.org?via=matrix.org\n   :alt: Matrix channel\n\n*instawow* is a package manager for World of Warcraft.\nIt can be used to install, remove and update add-ons from\nWoWInterface, CurseForge, Tukui and GitHub.\n\n*instawow* tries to make installing, updating and removing\nadd-ons quick and painless for those of us who are\n(ever so slightly) proficient with the command line\nand do not revel in using bloatware which infringe on our privacy\nor inhabiting walled gardens.\n\nIndi-co-depedently, an *instawow* GUI is in early development.\nThe GUI does not have feature parity with the CLI and is not particularly,\nrigorously, tested.  However, it does offload add-on management to\nthe *instawow* core.\n\nSome of the features of *instawow* are:\n\n- Interoperable CLI and GUI\n- Fuzzy search with download scoring, backed by a catalogue which\n  combines add-ons from WoWInterface, CurseForge, Tukui and Townlong Yak\n- Ability to interpret add-on URLs and host IDs\n- Add-on reconciliation which works with all three major hosts\n- Rollback – ability to revert problematic updates\n- Multiple update channels – 'stable', 'latest', and alpha and beta\n  for CurseForge add-ons\n- Dependency resolution on installation\n- Version pinning of CurseForge and GitHub add-ons\n- Wago integration – a WeakAuras Companion clone which can be managed like\n  any other add-on\n\n.. figure:: https://asciinema.org/a/8m36ncAoyTmig4MXfQM8YjE6a.svg\n   :alt: Asciicast demonstrating the operation of instawow\n   :target: https://asciinema.org/a/8m36ncAoyTmig4MXfQM8YjE6a?autoplay=1\n   :width: 640\n\n.. figure:: https://raw.githubusercontent.com/layday/instawow/main/gui-webview/screenshots/v0.6.0_640px.png\n   :target: https://github.com/layday/instawow/releases/latest\n   :alt: The instawow GUI's main window\n\nInstallation\n------------\n\nYou can download pre-built binaries of *instawow* from GitHub:\n\n- `Binaries <https://github.com/layday/instawow/releases/latest>`__\n\nIf you'd prefer to install *instawow* from source, you are able to choose from:\n\n- `pipx <https://github.com/pipxproject/pipx>`__:\n  ``pipx install instawow`` or ``pipx install instawow[gui]`` for the GUI\n- The `AUR <https://aur.archlinux.org/packages/instawow/>`__\n  for Arch Linux:\n  ``yay -S instawow``\n- Vanilla pip:\n  ``python -m pip install -U instawow`` or ``python -m pip install -U instawow[gui]`` for the GUI\n\nGetting started\n---------------\n\ntl;dr\n~~~~~\n\nBegin by running ``instawow reconcile``\nto register previously-installed add-ons with *instawow*\n(``instawow reconcile --auto`` to do the same without user input).\nTo install add-ons, you can search for them using the ``search`` command::\n\n    instawow search molinari\n\nIn addition, *instawow* is able to interpret add-on URLs and *instawow*-specific\nURNs of slugs and host IDs.\nAll of the following will install Molinari from CurseForge::\n\n    instawow install https://www.curseforge.com/wow/addons/molinari\n    instawow install curse:molinari\n    instawow install curse:20338\n\nYou can ``update`` add-ons and ``remove`` them just as you'd install them.\nIf ``update`` is invoked without arguments, it will update all of your\ninstalled add-ons.  You can ``list`` add-ons and view detailed information about\nthem using ``list --format detailed``.\nFor ``list`` and similarly non-destructive commands, the source can be omitted\nand the slug can be abbreviated, e.g. ``instawow reveal moli``\nwill open the Molinari add-on folder in your file manager.\n\nReconciling add-ons\n~~~~~~~~~~~~~~~~~~~\n\n*instawow* does not know about add-ons it did not itself install.\nThe Twitch and Minion clients each use their own, proprietary\nfingerprinting algorithm to reconcile add-ons you have installed with add-ons\ntheir respective hosts keep on their servers.  Though the details of their implementation\nelude me, *instawow* tries to accomplish something similar by combining a variety\nof cues (e.g. folders and TOC entries).\nThis is not done automatically for you – *instawow* makes a point of\nnot automatically assuming ownership of your add-ons or your preference\nof add-on host.\nHowever, you can run ``reconcile`` in promptless mode with the ``--auto`` flag,\nand *instawow* will prioritise add-ons from CurseForge because: (a) they\nsee more frequent updates; and (b) the API is of a higher quality.\nReconciled add-ons are reinstalled because it is not possible to reliably\ndetermine the installed version; consequently, it would not be possible to offer\nupdates reliably.\n\nSearching for add-ons\n~~~~~~~~~~~~~~~~~~~~~\n\n*instawow* comes with a rudimentary ``search`` command\nwith results ranked based on edit distance.\nSearch uses a collated add-on catalogue internally which is updated\n`once daily <https://github.com/layday/instawow-data/tree/data>`__.\nYou can install multiple add-ons directly from search.\n\nDealing with pesky updates\n~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n*instawow* keeps a log of all versions of an add-on it has previously\ninstalled.\nAdd-on updates can be undone using the ``instawow rollback`` command.\nAdd-ons which have been rolled back are pinned and will not receive updates.\nRollbacks can themselves be undone with ``instawow rollback --undo``,\nwhich will install the latest version of the specified add-on using\nthe ``default`` strategy.\n\nRollback is not supported for WoWInterface and Tukui.\n\nGitHub as a source\n~~~~~~~~~~~~~~~~~~\n\n*instawow* supports WoW add-ons *released* on GitHub; that is to say,\nthe repository must have had a release\n– tags are not sufficient – and the release *must*\nhave a ZIP file attached to it as an asset.\n*instawow* will not install or build add-ons directly from\nsource, or from tarballs or 'zipballs'.\nFuthermore, *instawow* will not validate the contents of the ZIP file.\nI do not recommend using GitHub as a source unless an add-on cannot\nbe found on one of the supported add-on hosts.\n\nWoW Classic and *instawow* profiles\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n*instawow* supports Classic – it will correctly install Classic versions\nof multi-flavour add-ons provided that the ``game_flavour``\nsetting is set to ``classic``.\nAssuming your default profile is configured for Retail,\nyou can create a pristine profile for Classic by running::\n\n    instawow -p classic configure\n\nYou can create profiles for other versions of the game (e.g. PTR or beta)\nin the same way.\nYou must prefix ``-p <profile>`` to *instawow* commands\nto manage each respective profile.\n\nThe ``any_flavour`` strategy can be used to install add-ons from CurseForge\nwhich do not have Classic releases but are known to work just as well::\n\n    instawow -p classic install -s any_flavour https://www.curseforge.com/wow/addons/colorpickerplus\n\n\nAdditional functionality\n------------------------\n\nWeakAuras aura updater\n~~~~~~~~~~~~~~~~~~~~~~\n\n*instawow* contains a WeakAuras updater modelled on\n`WeakAuras Companion <https://weakauras.wtf/>`__.  To use the updater\nand provided that you have WeakAuras installed::\n\n    instawow weakauras-companion build\n    instawow install instawow:weakauras-companion\n\nYou will have to rebuild the companion add-on prior to updating\nto receive aura updates.  If you would like to check for updates on\nevery invocation of ``instawow update``, install the\n``instawow:weakauras-companion-autoupdate`` variant::\n\n    instawow install instawow:weakauras-companion-autoupdate\n    instawow update\n\nPlug-ins\n~~~~~~~~\n\n*instawow* can be extended using plug-ins.  Plug-ins can be used to add support\nfor arbitrary hosts and add new commands to the CLI.  You will find a sample\nplug-in in ``tests/plugin``.\n\nMetadata sourcing\n-----------------\n\nOriginally, *instawow* relied on the official feeds provided by Curse.\nCurse retired the feeds in June 2018 and – for a period – *instawow* would\nscrape the CurseForge website.  The alternative would have been to use the\nold XML-like API.  Because the API was not built for third-party use, it had not been\nisolated from user accounts (cf. GitHub integrations).\nIf users were to log into the API, *instawow* would acquire full\naccess to their account.  Authentication was also complicated\nby the ongoing Curse account migration to Twitch and is (or should be)\nunnecessary for the simple use case of installing and updating add-ons.\nThankfully, Twitch migrated to an unauthenticated\nAPI interally in the second quarter of the year of the periodic table,\nwhich we have adopted for our own use.\nThis is similar to what Minion, the WoWInterface-branded add-on manager, has been\ndoing for years.  The good people at Tukui provide an API for public use.\n*instawow* might break whenever one of our sources introduces\na change to their website or API (though only temporarily).\n\nRemote hosts\n------------\n\nWeb requests initiated by *instawow* can be identified by its user agent string.\n\nWhen installing, updating or searching for add-ons, *instawow* will retrieve\nadd-on metadata from https://raw.githubusercontent.com,\nhttps://addons-ecs.forgesvc.net, https://api.mmoui.com, https://www.tukui.org,\nhttps://hub.wowup.io, https://api.github.com and https://data.wago.io,\nand will follow download URLs found in metadata.\n\nEvery 24 hours, on launch, *instawow* will query PyPI (https://pypi.org) –\nthe canonical Python package repository – to check for *instawow* updates.\n\nRelated work\n------------\n\nThe author of `strongbox <https://github.com/ogri-la/strongbox>`__ has been cataloguing similar software\n`here <https://ogri-la.github.io/wow-addon-managers/>`__.  If you are unhappy\nwith *instawow*, you might find one of these other add-on managers more\nto your liking.\n\nContributing\n------------\n\nBug reports and fixes are welcome.  Do open an issue before committing to\nmaking any significant changes.\n",
    'author': 'layday',
    'author_email': 'layday@protonmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.7',
}


setup(**setup_kwargs)
