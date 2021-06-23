import setuptools

#https://stackoverflow.com/questions/1471994/what-is-setup-py#:~:text=setup.py%20is%20a%20python,to%20easily%20install%20Python%20packages.
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="googlewrapper",
    version="0.1.9",
    author="Jace Iverson",
    author_email="iverson.jace@gmail.com",
    description="Simple API wrapper for Google Products",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jaceiverson/google-wrapper",
    project_urls = {
        "Bug Tracker":"https://github.com/jaceiverson/google-wrapper/issues"
    },
    packages = ["googlewrapper"],
    install_requires=[
            "google-api-python-client==2.4.0",
            "oauth2client==4.1.3",
            "pandas==1.2.4",
            "pygsheets==2.0.5",
            "google-cloud-bigquery==2.16.1",
            "pandas-gbq==0.15.0"
                ],
    keywords = "google, api, wrapper, search console, analytics, "\
                "big query, sheets, pagespeed, gmail, calendar, "\
                "gsc, ga, gbq"
)
