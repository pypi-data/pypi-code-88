
import os
import ezpip
from setuptools import setup

# key誤公開防止
if os.listdir("./_develop_tskr/key/") != ["debug_group.key"]:
	raise Exception("[key誤公開防止] debug用アカウント以外のkeyが誤って公開されようとしている可能性があります。./_develop_tskr/key/を確認し、debug_group.keyのみであることをensureしてください。")

with ezpip.packager("./_develop_tskr/") as p:
	setup(
		name = "tskr",
		version = "1.0.3",
		description = "task management tool",
		author = "team_tskr",
		author_email = "tskr.tools@gmail.com",
		url = "https://github.co.jp/",
		packages = p.packages,
		install_requires = ["pycryptodome", "fileinit", "relpath", "sout"],
		long_description = p.long_description,
		long_description_content_type = "text/markdown",
		license = "CC0 v1.0",
		classifiers = [
			"Programming Language :: Python :: 3",
			"Topic :: Software Development :: Libraries",
			"License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication"
		],
		entry_points = """
			[console_scripts]
			tskr = tskr:tskr_command
		"""
	)
