import setuptools

setuptools.setup(
    name="rl_bot_model",
    version="0.0.1",
    author="Nabi Ozberkman",
    author_email="n.ozberkman@gmail.com",
    description="Package for various reinforcement models",
    url="https://github.com/micronoz/rl-bot-common",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'torch'
    ]
)
