from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: OS Independent',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='pyloading',
  version='1.0.0',
  description="Loading made easy" ,
  long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.md').read(),
  long_description_content_type="text/markdown",
  url='https://github.com/DevER-M/pyloading',  
  author='Dever',
  author_email='',
  license='MIT', 
  classifiers=classifiers,
  keywords='Loading (console based)', 
  packages=find_packages(),
  install_requires=['random-dice-roller','rand-password-generator','coord-generator','pyautoclicker']
) 