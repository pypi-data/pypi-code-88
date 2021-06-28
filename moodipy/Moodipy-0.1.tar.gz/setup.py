from setuptools import setup

setup(
    name="Moodipy",
    version="0.1",
    packages=["Moodipy"],
    url="https://github.com/dianas11xx/MoodipyTest",
    author="Noteworthy",
    license = "GPL 3",
    package_data = {"Moodipy":['imgs/*jpeg', 'imgs/*png']},
    description="use sentiment analysis to create a playlist that matches someone's mood and also predict songs to rise in popularity.",
    install_requires=["python3.8", "spotipy==2.18.0", "nltk==3.6.2", "PyQt5==5.12", "PyQt5-sip==4.19.19", "screeninfo"],
    entry_points={"console_scripts": ["start_Moodipy=GUI:main"]}
)
