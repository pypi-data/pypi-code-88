
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
  name = 'telegram-logger-x',         # How you named your package folder (MyLib)
  packages = ['telegram_logger'],
  entry_points = {
        'console_scripts': ['telegram-logger = telegram_logger:main'],
    },
  version = '0.12a',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Logs Telegram events to your console, file(s) or both simultanously.',   # Give a short description about your library
  long_description = long_description,
  author = '21st Century Code Bros',                   # Type in your name
  author_email = 'noreply-use-github-project-page-for-contact@fakemail.com',      # Type in your E-Mail
  url = 'https://github.com/nyuszika7h/telegram-logger',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/nyuszika7h/telegram-logger/archive/refs/heads/main.tar.gz',    # I explain this later on
  keywords = ['Telegram','Logs','logging'],   # Keywords that define your package best
  install_requires=['telethon', 'toml'],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)