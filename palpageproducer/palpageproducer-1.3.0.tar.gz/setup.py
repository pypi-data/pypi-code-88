from setuptools import setup
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='palpageproducer',
      version='1.3.0',
      description='Palette page producer',
      long_description=long_description,
      long_description_content_type='text/markdown',
      classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python :: 3',
        'Intended Audience :: End Users/Desktop',
        'Topic :: Multimedia :: Graphics',
        'Topic :: Multimedia :: Graphics :: Graphics Conversion',
      ],
      keywords='sass html colors',
      url='https://www.twinkle-night.net/Code/ppp.html',
      author='Garrick',
      author_email='earthisthering@posteo.de',
      license='GPLv3+',
      packages=['palpageproducer'],
      install_requires=[
          'appdirs',
          'python-slugify'
      ],
      entry_points={'console_scripts':['palpageproducer=palpageproducer.__main__:main']},
      include_package_data=True,
      zip_safe=False)
