import setuptools

# read in required packages from requirements.txt
with open("requirements.txt", "r") as fh:
    requirements = fh.read().splitlines()

setuptools.setup(
    name="slotpy",
    version="0.0.8",
    author='Laura Ketzer, Christine Ackerl, George Paraschos',
    author_email='lketzer@aip.de, christine.ackerl@univie.ac.at, gfparaschos@mpifr.de',
    description='Sliders and Plots',
    long_description='''This package was developed during the Code/Astro workshop and is a 
    preliminary version of something cool! =)''',
    url="https://github.com/Chia-vie/slotpy",
    license='BSD',
    keywords='astronomy,plotting,...',
    packages=setuptools.find_packages(),
    classifiers=[
        # Indicate who your project is intended for
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Astronomy',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: BSD License',],
    install_requires=requirements
)
