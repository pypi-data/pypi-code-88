from setuptools import setup

setup(
    name="Moodipy",
    version="0.115",
    packages=['Moodipy'],
    url="https://github.com/dianas11xx/Moodify",
    author="Noteworthy",
    license = "GPL 3",
    long_description = "Uses sentiment analysis to create a playlist that matches someone's mood and also predict songs to rise in popularity.",
    description="Spotify Playlist Generator based of Mood",
    install_requires=['nltk==3.6.2', 'screeninfo==0.6.7', 'spotipy==2.18.0', 'requests>=2.25.0', 'PyQt5>=5.12','urllib3==1.26.6', 'PyQt5-sip>=4.19.19'],
    entry_points={"console_scripts": ["Moodipy=Moodipy.main:main"]},
    include_package_data=True
)
