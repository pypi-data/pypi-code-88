from setuptools import setup, find_packages

setup(
    name='echo_lv',
    version='0.1.2',
    author='Zyuzin Vasily',
    author_email='zvvzuzin@gmail.com',
    description='Library for Echocardiographic images',
    packages=['echo_lv'],#find_packages('./src'),
    package_dir = {'echo_lv': ''},
    url='https://github.com/zvvzuzin/us_left_ventricle',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['numpy >= 1.11.1',
                      'scipy',
                      'pandas',
                      'torch',
                      'scikit-image',
                      'opencv-python',
                      'SimpleITK',
                      'matplotlib >= 1.5.1'],
)
