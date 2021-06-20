from setuptools import setup, find_namespace_packages

setup(name='mindmap',
      description='Command line tool for keeping notes simple way.',
      long_description='Command line tool for keeping notes simple way.',
      version='0.0.65',
      url='https://github.com/ferdielik/mindmap',
      author='Ferdi Elik',
      author_email='elik.ferdi@gmail.com',
      license='MIT',
      classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: System Administrators',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3'
      ],
      scripts=['mindmap/mindmap'],
      packages=find_namespace_packages(include=['mindmap'])
      )
