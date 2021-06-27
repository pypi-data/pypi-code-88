from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Panduza Plugin to manage Linux sysfs I/O'
LONG_DESCRIPTION = 'Panduza Plugin to control /sys/class/gpio'

# Setting up
setup(
        name="panduza_plg_devfs_gpio", 
        version=VERSION,
        author="Panduza Team",
        author_email="panduza.team@gmail.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        
            
        keywords=['python', 'first package'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Programming Language :: Python :: 3",
            'Operating System :: POSIX',
        ]
)


