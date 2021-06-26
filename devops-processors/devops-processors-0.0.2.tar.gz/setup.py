from setuptools import setup

setup(
    author="David Navarro Alvarez",
    author_email="me@davengeo.com",
    description="devops event processors library dist",
    url="https://github.com/davengeo/devops-processors",
    name="devops-processors",
    version='0.0.2',
    packages=[
        'devopsprocessors',
        'devopsprocessors.history',
        'devopsprocessors.fluentd'
    ],
    install_requires=[
                    "cloudevents",
                    "dependency-injector>=4.0,<5.0",
                    "fluent-logger"
                    "prometheus-client"
    ],
    package_data={
        'ini': ['app.ini']
    },
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: European Union Public Licence 1.2 (EUPL 1.2)',
        'Programming Language :: Python :: 3.8',
        'Topic :: System :: Systems Administration',
    ]
)
