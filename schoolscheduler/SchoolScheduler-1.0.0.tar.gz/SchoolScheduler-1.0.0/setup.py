import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="SchoolScheduler",
    version="1.0.0",
    author="Michael Berry",
    author_email="michael.berry@ufl.edu",
    description="Python School Scheduler",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jaberrio/SchoolScheduler",
    project_urls={
        "Source": "https://github.com/jaberrio/SchoolScheduler",
        "Bug Tracker": "https://trello.com/b/G1f61mAc/school-scheduler",
    },
    install_requires=["PyQt5", "reportlab"],
    entry_points={"console_scripts":
                    [
                        "play_scheduler = scheduler:main",
                    ]
                  }
)