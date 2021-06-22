# import subprocess
# import os

# print("[*] Installing requirements.txt...")
# subprocess.Popen("pip3 install -r requirements.txt", shell=True).wait()
# print("[*] Installing ppm to /usr/share/ppm..")
# subprocess.Popen("mkdir /usr/share/ppm/;cp -rf * /usr/share/ppm/",
#                  shell=True).wait()
# print(
#     '[*] Done. Add export PATH="$PATH:/usr/share/ppm/src" in your .bashrc or .zshrc'
# )
# print("[*] Finished. Run 'ppm' to start the Python Package Maneger.")

from setuptools import setup, find_packages

# The text of the README file
README = open("README.md", "r").read()

setup(
    name='pyposer',
    version='0.1.4b3',
    description='Python Packeage Manager',
    long_description=README,
    long_description_content_type="text/markdown",
    packages=find_packages("src"),
    package_dir={"": "src"},
    author='Alisson Santos',
    author_email='dev.alysson@gmail.com',
    install_requires=["click", "virtualenv", "inquirer"],
    url='https://github.com/alysson3dev/pyposer',
    keywords=['PYPOSER', 'PIP', 'PACKAGE', 'KEYWORDS'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.9',
    ],
    entry_points={
        'console_scripts': [
            'pyposer = pyposer.__main__:main',
        ],
    },
)
