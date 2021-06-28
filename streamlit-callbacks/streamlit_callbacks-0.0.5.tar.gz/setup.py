import setuptools

setuptools.setup(
    name="streamlit_callbacks",
    version="0.0.5",
    author="",
    author_email="",
    description="",
    long_description="Disclaimer: I'm not the owner of this package. For more information, see the homepage: https://github.com/FloWide/streamlit_callbacks. To remove this package from pypi or transfer ownership, please submit an issue on my fork repository",
    long_description_content_type="text/plain",
    url="https://github.com/FloWide/streamlit_callbacks",
    packages=setuptools.find_namespace_packages(include=['streamlit.*']),
    include_package_data=True,
    setup_requires=['wheel'],
    classifiers=[],
    python_requires=">=3.6",
    install_requires=[
        "streamlit >= 0.76.0",
    ],
)

