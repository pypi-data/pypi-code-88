import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="df3dbehav",
    version="0.23",
    author="Semih Gunel",
    package_data={
        "": ["*.ckpt"],
    },
    packages=["df3dbehav", "df3dbehav.data"],
    entry_points={"console_scripts": ["df3dbehav = df3dbehav.df3dbehav:main"]},
    description="Behavior Estimation on DeepFly3D annotations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/semihgunel/Df3dBehav",
    install_requires=[
          'numpy',
          'matplotlib',
          'pandas',
          'pytorch-lightning',
          'torch',
          'torchvision',
          'torchaudio',
          'einops',
          'opencv-python',
          'scipy',
          'pickle5',
          'tsaug'
      ],
)
