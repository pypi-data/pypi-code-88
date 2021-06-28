import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="SchoolSchedulerTest",
    version="0.0.1",
    author="Several Authors",
    author_email="michael.berry@ufl.edu",
    description="A schoolscheduler app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jaberrio/SchoolScheduler",
    project_urls={
        "Source": "https://github.com/jaberrio/SchoolScheduler",
        "Bug Tracker": "https://trello.com/b/G1f61mAc/school-scheduler",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    install_requires=['PyQt5'],
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)