from setuptools import setup, find_packages

setup(
    name = "upn2sepa",
    version = "1.0.0",
    description = "UPN QR to SEPA QR converter.",
    author = "Jan Zmazek",
    license = "MIT license",
    packages = find_packages(exclude=['*test']),
    entry_points = {
        'console_scripts': [
            'upn2sepa = upn2sepa.run:run',
        ]
    },
    install_requires = ['Pillow', 'pyzbar', 'segno']
)
