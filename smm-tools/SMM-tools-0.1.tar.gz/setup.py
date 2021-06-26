import setuptools


def readme():
    with open('README.md') as f:
        return f.read()


setuptools.setup(name='SMM-tools',
      version='0.1',
      description='Usifull SMM tools for authors',
      long_description=readme(),
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
        'Topic :: Multimedia :: Graphics :: Editors',
      ],
      keywords='instagram',
      url='https://github.com/dev-muhammad/smm-tools',
      author='dev-muhammad',
      author_email='iam.markjobs@gmail.com',
      license='MIT',
      package_dir={"": "src"},
      packages=setuptools.find_packages(where="src"),
      include_package_data=True,
      zip_safe=False)
