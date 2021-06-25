# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['streamrip']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.0.1,<9.0.0',
 'mutagen>=1.45.1,<2.0.0',
 'pathvalidate>=2.4.1,<3.0.0',
 'requests>=2.25.1,<3.0.0',
 'tomlkit>=0.7.2,<0.8.0',
 'tqdm>=4.61.1,<5.0.0']

extras_require = \
{':sys_platform == "cygwin"': ['pick>=1.0.0,<2.0.0',
                               'windows-curses>=2.2.0,<3.0.0'],
 ':sys_platform == "darwin"': ['simple-term-menu>=1.2.1,<2.0.0']}

entry_points = \
{'console_scripts': ['rip = streamrip.cli:main']}

setup_kwargs = {
    'name': 'streamrip',
    'version': '0.6.4',
    'description': 'A fast, all-in-one music ripper for Qobuz, Deezer, Tidal, and SoundCloud',
    'long_description': "# streamrip\n\n[![Downloads](https://static.pepy.tech/personalized-badge/streamrip?period=total&units=international_system&left_color=black&right_color=green&left_text=Downloads)](https://pepy.tech/project/streamrip)\n\n\nA scriptable stream downloader for Qobuz, Tidal, Deezer and SoundCloud.\n\n\n## Features\n\n- Super fast, as it utilizes concurrent downloads and conversion\n- Downloads tracks, albums, playlists, discographies, and labels from Qobuz, Tidal, Deezer, and SoundCloud\n- Supports downloads of Spotify and Apple Music playlists through [last.fm](https://www.last.fm)\n- Automatically converts files to a preferred format\n- Has a database that stores the downloaded tracks' IDs so that repeats are avoided\n- Easy to customize with the config file\n- Integration with `youtube-dl`\n\n## Installation\n\nFirst, ensure [Python](https://www.python.org/downloads/) and [pip](https://pip.pypa.io/en/stable/installing/) are installed. Then run the following in the command line:\n\n```bash\npip3 install streamrip --upgrade\n```\n\nIf you would like to use `streamrip`'s conversion capabilities, download TIDAL videos, or download music from SoundCloud, install [ffmpeg](https://ffmpeg.org/download.html). To download music from YouTube, install [youtube-dl](https://github.com/ytdl-org/youtube-dl#installation).\n\n\n## Example Usage\n\n**For Tidal and Qobuz, you NEED a premium subscription.**\n\nDownload an album from Qobuz\n\n```bash\nrip -u https://open.qobuz.com/album/0060253780968\n```\n\nDownload multiple albums from Qobuz\n```bash\nrip -u https://www.qobuz.com/us-en/album/back-in-black-ac-dc/0886444889841 -u https://www.qobuz.com/us-en/album/blue-train-john-coltrane/0060253764852\n```\n\n![Streamrip downloading an album](https://github.com/nathom/streamrip/blob/main/demo/download_url.png?raw=true)\n\nDownload the album and convert it to `mp3`\n\n```bash\nrip --convert mp3 -u https://open.qobuz.com/album/0060253780968\n```\n\n\n\nTo set the quality, use the `--quality` option to `0, 1, 2, 3, 4`:\n\n| Quality ID | Audio Quality         | Available Sources                            |\n| ---------- | --------------------- | -------------------------------------------- |\n| 0          | 128 kbps MP3 or AAC   | Deezer, Tidal, SoundCloud (most of the time) |\n| 1          | 320 kbps MP3 or AAC   | Deezer, Tidal, Qobuz, SoundCloud (rarely)    |\n| 2          | 16 bit, 44.1 kHz (CD) | Deezer, Tidal, Qobuz, SoundCloud (rarely)    |\n| 3          | 24 bit, ≤ 96 kHz      | Tidal (MQA), Qobuz, SoundCloud (rarely)      |\n| 4          | 24 bit, ≤ 192 kHz     | Qobuz                                        |\n\n\n\n\n\n```bash\nrip --quality 3 https://tidal.com/browse/album/147569387\n```\n\nSearch for albums matching `lil uzi vert` on SoundCloud\n\n```bash\nrip search -s soundcloud 'lil uzi vert'\n```\n\n![streamrip interactive search](https://github.com/nathom/streamrip/blob/main/demo/interactive_search.png?raw=true)\n\nSearch for *Rumours* on Tidal, download it, convert it to `ALAC`\n\n```bash\nrip -c alac search 'fleetwood mac rumours'\n```\n\nQobuz discographies can be filtered using the `filter` subcommand\n\n```bash\nrip filter --repeats --features 'https://open.qobuz.com/artist/22195'\n```\n\n\n\nWant to find some new music? Use the `discover` command (only on Qobuz)\n\n```bash\nrip discover --list 'best-sellers'\n```\n\n> Avaiable options for `--list`:\n>\n> - most-streamed\n> - recent-releases\n> - best-sellers\n> - press-awards\n> - ideal-discography\n> - editor-picks\n> - most-featured\n> - qobuzissims\n> - new-releases\n> - new-releases-full\n> - harmonia-mundi\n> - universal-classic\n> - universal-jazz\n> - universal-jeunesse\n> - universal-chanson\n\n## Other information\n\nFor more in-depth information about `streamrip`, see the [wiki](https://github.com/nathom/streamrip/wiki/).\n\n\n## Contributions\n\nAll contributions are appreciated! You can help out the project by opening an issue\nor by submitting code.\n\n### Guidelines for opening issues\n\n- Include a general description of the feature request or bug in the title\n- Limit each Issue to a single subject\n- For bug reports, include the traceback, command (including the url) you used,\nand version of `streamrip`\n- If you do not follow the template provided, I will not respond\n\n### Contributing code\n\nIf you're new to Git, follow these steps to open your first Pull Request (PR):\n\n- Fork this repository\n- Clone the new repository\n- Commit your changes\n- Open a pull request to the `dev` branch\n\nPlease document any functions or obscure lines of code.\n\n\n## Acknowledgements\n\nThanks to Vitiko98, Sorrow446, and DashLt for their contributions to this project, and the previous projects that made this one possible.\n\n`streamrip` was inspired by:\n\n- [qobuz-dl](https://github.com/vitiko98/qobuz-dl)\n- [Qo-DL Reborn](https://github.com/badumbass/Qo-DL-Reborn)\n- [Tidal-Media-Downloader](https://github.com/yaronzz/Tidal-Media-Downloader)\n- [scdl](https://github.com/flyingrub/scdl)\n\n\n\n## Disclaimer\n\n\nI will not be responsible for how you use `streamrip`. By using `streamrip`, you agree to the terms and conditions of the Qobuz, Tidal, and Deezer APIs.\n",
    'author': 'nathom',
    'author_email': 'nathanthomas707@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/nathom/streamrip',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
