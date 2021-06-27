import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="simple-gpg",
    version="8.2",
    author="Anish M",
    author_email="aneesh25861@gmail.com",
    description="A simple program to make use of GNU Privacy Guard for Cryptographical use.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT License",
    keywords = ['gnupg','openpgp','pgp','gpg','encryption', 'cryptography','student project'],
    url="https://github.com/Anish-M-code/simple-gpg",
    packages=["simple_gpg"],
    classifiers=(
        'Development Status :: 5 - Production/Stable',      
        'Intended Audience :: Developers',      
        'Topic :: Software Development',
        'License :: OSI Approved :: MIT License',   
        'Programming Language :: Python :: 3',      
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: End Users/Desktop',
        'Topic :: Security :: Cryptography',
  
    ),
    entry_points={"console_scripts": ["simple-gpg = simple_gpg:main",],},
)
