from setuptools import setup

setup(
	name = "deezloader",
	version = "2021.06.23",
	description = "Downloads songs, albums or playlists from deezer",
	license = "CC BY-NC-SA 4.0",
	author = "An0nimia",
	author_email = "An0nimia@protonmail.com",
	url = "https://github.com/An0nimia/deezloader",
	packages = ["deezloader", "deezloader_lite"],

	install_requires = [
		"mutagen", "pycryptodome", "requests",
		"spotipy", "tqdm", "fastapi", "uvicorn[standard]"
	],

	scripts = ["deezloader/bin/deez-dw.py", "deezloader/bin/deez-web.py"]
)