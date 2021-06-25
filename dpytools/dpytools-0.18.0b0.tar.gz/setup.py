# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dpytools']

package_data = \
{'': ['*']}

install_requires = \
['discord.py']

extras_require = \
{'docs': ['sphinxcontrib-trio==1.1.2',
          'sphinx==4.0.2',
          'sphinx-rtd-theme==0.5.2']}

setup_kwargs = {
    'name': 'dpytools',
    'version': '0.18.0b0',
    'description': 'Easy to use, beginner friendly but powerful tools to speed up discord bots development (discord.py)',
    'long_description': '[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)\n\n[![PyPI status](https://img.shields.io/pypi/status/dpytools.svg)](https://pypi.python.org/pypi/dpytools/)\n[![PyPI version fury.io](https://badge.fury.io/py/dpytools.svg)](https://pypi.python.org/pypi/dpytools/)\n[![Downloads](https://pepy.tech/badge/dpytools)](https://pepy.tech/project/dpytools)\n[![Documentation Status](https://readthedocs.org/projects/dpytools/badge/?version=master)](https://dpytools.readthedocs.io/en/latest/?badge=master)\n[![PyPI license](https://img.shields.io/pypi/l/dpytools.svg)](https://pypi.python.org/pypi/dpytools/)\n\n\n\n# dpytools\nCollection of easy to use, beginner friendly but powerful, orthogonal tools to speed up discord bots development (discord.py)\n\n# Features\n- The batteries of discord.py\n- Easy to read type-hinted code\n- Active development\n- Minimal dependencies\n\n# Instalation\nInstall the latest version of the library with pip.\n```\npip install -U dpytools\n```\n\n# Useful links:\n- [Documentation](https://dpytools.readthedocs.io/en/master/)\n- [List](https://github.com/chrisdewa/dpytools/blob/master/docs/All.md) of all the tools.\n- [F. A. Q.](https://github.com/chrisdewa/dpytools/blob/master/docs/FAQ.md) and examples\n- [Changelog](https://github.com/chrisdewa/dpytools/blob/master/CHANGELOG.md)\n- [Project Home](https://github.com/chrisdewa/dpytools) on github\n\n# Use Examples:\nThe library has a couple of reaction menus that are really easy to use.\n`dpytools.menus.arrows` takes a list of embeds and displays it using a reaction menu.\n```python\n@bot.command()\nasync def arrow_menu(ctx):\n    """\n    This command sends a list of embeds in a reaction menu with emojis aid in navigation\n    """\n    from dpytools.menus import arrows\n    long_list_of_embeds = [discord.Embed(...), ...]\n    await arrows(ctx, long_list_of_embeds)\n```\nThere are multiple checks you can use directly on your commands\n`dpytools.checks.admin_or_roles` takes any number of strings (Role names) and ints  (role ID) \nand checks if the person using the command has those roles or has administrator permissions. \n```python\nfrom dpytools.checks import admin_or_roles\n@bot.command()\n@admin_or_roles(\'Moderator\', 123456789)\nasync def moderation(ctx):\n    ctx.send(\'Only admins and people with a a role named "Moderator" \' \n             \'or with a role with id 123456789 can use this command\')\n```\n\n```python\nfrom dpytools.checks import any_checks\n\n@commands.guild_only()       # This command must be called inside a server\n@any_checks                  # Place the decorator above the checks you with to compare using "OR"\n@commands.is_owner()         # The command will run if ctx.author is the owner of the bot\n@commands.has_role(\'Admin\')  # __OR__ if ctx.author has the role "Admin"\n@bot.command()               # this decorator transforms this function in a command any_checks must be above it\nasync def test(ct):\n    await ctx.send(\'The command works\')\n```\n\nThere are also multiple argument parsers. Functions that convert a user\'s input to something more useful.\n`dpytools.parsers.to_timedelta` takes a string in the format `<number>[s|m|h|d|w]` and returns a timedelta object\n```python\nfrom dpytools.parsers import to_timedelta\n@bot.command()\n@commands.guild_only()\nasync def mute(ctx, member: discord.Member, time: to_timedelta):\n    await ctx.send(f"{member.mention} muted for {time.total_seconds()} seconds")\n    mute_role = ctx.guild.get_role(1234567890)\n    await member.add_roles(mute_role)\n    await asyncio.sleep(time.total_seconds())\n    await member.remove_roles(mute_role)\n    await ctx.send(f"{member.mention} unmuted")\n```\nThis argument parsers can also be used outside the context of `discord.ext.commands`\nIn the end most of them only take a string and return the appropriate object.\nOnly converter classes that inherit from `discord.ext.commands.Converter` require a command context to work.\n\nThere are many other tools available in the library, check them in [docs/All.md](https://github.com/chrisdewa/dpytools/blob/master/docs/All.md)\n\n# Todos:\n1. Add interactions\n\n# Status of the project\nBeta.\nAll functions have been tested but new tools are frequently added.\nBreaking changes may come depending on changes on API or discord.\nUse in production only after extensive testing.\n\n# Contributing\nFeel free to make a pull request or rise any issues.\n\n# Contact\nMessage me on discord at **ChrisDewa#4552** if you have any questions, ideas or suggestions.\n',
    'author': 'chrisdewa',
    'author_email': 'alexdewa@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/chrisdewa/dpytools',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
