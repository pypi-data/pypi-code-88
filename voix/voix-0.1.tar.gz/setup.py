from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='voix',
  version='0.1',
  description='A tiny package that can generate voice for you',
  long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.txt').read(),
  long_description_content_type="text/markdown",
  author='Tahmid Ahnaf',
  author_email='tahmidahnafxtra@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords=['voix' , 'voice' ,'sound' ,'speak' , 'speaker' , 'sound generator' , 'voice generator' , 'text to speech' ,'tts' , 'translate'], 
  packages=find_packages(),
  install_requires=['gtts', 'googletrans' , 'playsound'] 
)