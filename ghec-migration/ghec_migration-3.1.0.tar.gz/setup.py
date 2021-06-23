from setuptools import setup
import sys

from pathlib import Path  # noqa E402

CURRENT_DIR = Path(__file__).parent


def get_long_description() -> str:
    readme_md = CURRENT_DIR / "README.md"
    with open(readme_md, encoding="utf8") as ld_file:
        return ld_file.read()


version = "1.0.0"

setup(
    name="ghec_migration",
    version = "3.1.0",
    description="A Python script for bulk migrating repos from one org to other org "
                "GitHub repositories using the API",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Vamsi Maringanti",
    author_email="vamsikrishna.maringanti@nike.com",
    url="https://github.nike.com/mp-commerce-fulfillment/githubmigration",
    license="MIT",
    py_modules=["jenkins_migration", "github_migration", "ghec_migration", "make_private", "find_new_git_url", "update_topics_for_team"],
    python_requires=">=3.6",
    zip_safe=False,
    install_requires=["requests",
                      "regex",
                      "PyInquirer",
                      "python-jenkins","pbr", "multi-key-dict", "xmltodict"],

    entry_points={
        "console_scripts": [
            "ghec-migration=ghec_migration:main"
        ]
    },
)
