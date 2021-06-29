import os
import setuptools

base_dir = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(base_dir, "README.md"), "r") as f:
    long_description = f.read()

setuptools.setup(
    name="EncryptEnv",
    version="0.0.3",
    author="Thinktron",
    author_email="jeremywang@thinktronltd.com",
    description="Encrypt the passwords in the environment variables.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="http://rd.thinktronltd.com/jeremywang/EncryptEnv",
    packages=setuptools.find_packages(),
    # package_data={'TronGisPy': ['data/*', 'data/*/*']},
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
      install_requires=[
          'cryptography==2.8',
      ]
)

# 0.0.2 Excrypt key as string type
# 0.0.3 change cryptography to cryptography==2.8 in setup.py



# python setup.py sdist bdist_wheel
# twine upload dist/EncryptEnv-0.0.2*
# scp Z:\R014_Jeremy\Projects\EncryptEnv\dist\EncryptEnv-0.0.2-py3-none-any.whl  jeremy@rd.thinktronltd.com:/home/ttl/pypi/EncryptEnv-0.0.2-py3-none-any.whl
