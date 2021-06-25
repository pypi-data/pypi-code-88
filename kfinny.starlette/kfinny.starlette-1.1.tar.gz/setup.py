from setuptools import setup, find_packages

setup(name='kfinny.starlette',
      version='1.1',
      description='A pip-installable of starlette-example',
      url='https://github.com/kfinny/starlette-pip-example',
      author='Kevin Finnigin',
      author_email='kevin@finnigin.net',
      license='MIT',
      packages=find_packages(),
        install_requires=[
          'aiofiles',
          'jinja2',
          'starlette',
          'uvicorn'
      ],
      entry_points={
        "console_scripts": [
            "kfstarlette-app = kfinny.starlette.app:main"
        ]
      },
      zip_safe=False,
      include_package_data=True)
