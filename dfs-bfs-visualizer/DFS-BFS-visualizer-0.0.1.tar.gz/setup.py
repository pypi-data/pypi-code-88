from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='DFS-BFS-visualizer',
  version='0.0.1',
  description='DFS and BFS visualizer using a drawing tool',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Fars Bein',
  author_email='fars.bein@ryerson.ca',
  license='MIT', 
  classifiers=classifiers,
  keywords=['visualizer', 'DFS', 'BFS'], 
  packages=find_packages(),
  install_requires=['pygame','time','queue'] 
)