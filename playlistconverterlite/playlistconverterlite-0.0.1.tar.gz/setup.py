from setuptools import setup

setup(
	name='playlistconverterlite',
	version='0.0.1',
	description='Apple Music to Spotify playlist converter',
	author='Andrew King',
	author_email='andrewking1597@gmail.com',
	url='https://github.com/andrewking1597/playlist-converter-lite',
	packages=['playlistconverterlite'],
	install_requires=['apple-music-python', 'spotipy']
)