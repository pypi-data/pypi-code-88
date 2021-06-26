import setuptools


with open("README.md", encoding="utf8") as f:
    readme = f.read()


setuptools.setup(
    name="jupyter-www-proxy",
    version="0.1",
    author="Chung Chan",
    license="MIT",
    description="HTTP server for Jupyter",
    long_description=readme,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    keywords=["Jupyter", "http", "server"],
    classifiers=["Framework :: Jupyter"],
    install_requires=[
        'jupyter-server-proxy'
    ],
    entry_points={
        "jupyter_serverproxy_servers": ["www = jupyter_www_proxy:setup_www",]
    },
    package_data={"jupyter_www_proxy": ["icons/*"]}
)
