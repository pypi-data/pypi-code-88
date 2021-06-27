import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="leakylan",
    version="0.2.3",
    author="Anish M",
    author_email="aneesh25861@gmail.com",
    description="Simple File sharing Service over LAN.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT License",
    keywords = ['File Sharing Service','student project'],
    url="https://github.com/Anish-M-code/Leaky-LAN",
    packages=["leakylan"],
    classifiers=(
        'Development Status :: 5 - Production/Stable',      
        'Intended Audience :: Developers',      
        'Topic :: Software Development',
        'License :: OSI Approved :: MIT License',   
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: End Users/Desktop',
        'Topic :: Communications :: File Sharing',
  
    ),
    entry_points={"console_scripts": ["leakylan = leakylan:main",],},
)
