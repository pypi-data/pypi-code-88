"""
Contributing generator module.
"""
import argparse

from rpgt.src.generators.generator import Generator
from rpgt.src.generators.structure_generator import StructureGenerator


class ContributingGenerator(Generator):
    """
    Contributing generator class.
    """

    def __init__(self, args: argparse.Namespace, struct_gen: StructureGenerator):
        """
        Initialize Changelog generator with proper parameters.
        """

        super().__init__(args)
        self.struct_gen = struct_gen

    def generate(self, cwd: str) -> None:
        """
        Writes the CONTRIBUTING.md to file.
        """
        self.struct_gen.add_file("CONTRIBUTING.md", self.generate_contributing())

    @staticmethod
    def generate_contributing() -> str:
        """
        Generates the CONTRIBUTING.md file.
        :return: a stringual representation of the contributing file.
        """
        return """# Contributing Guide
We are excited that you are interested in contributing to this project. Before submitting your contribution, please make sure to take a moment and read through the following guidelines:

- [Code of conduct](#code-of-conduct)
- [Issue Reporting Guidelines](#issue-reporting-guidelines)
- [Pull Request Guidelines](#pull-request-guidelines)
- [Semantic Versioning](#semantic-versioning)
- [Style Guide](#style-guide)

## Code of Conduct
As contributors and maintainers of this project, we pledge to respect all people who contribute through reporting issues, posting feature requests, updating documentation, submitting pull requests or patches, and other activities.

We are committed to making participation in this project a harassment-free experience for everyone, regardless of the level of experience, gender, gender identity and expression, sexual orientation, disability, personal appearance, body size, race, age, or religion.

Examples of unacceptable behavior by participants include the use of sexual language or imagery, derogatory comments or personal attacks, trolling, public or private harassment, insults, or other unprofessional conduct.

Project maintainers have the right and responsibility to remove, edit, or reject comments, commits, code, wiki edits, issues, and other contributions that are not aligned to this Code of Conduct. Project maintainers who do not follow the Code of Conduct may be removed from the project team.

Instances of abusive, harassing, or otherwise unacceptable behavior may be reported by opening an issue or contacting one or more of the project maintainers.

This Code of Conduct is adapted from the [Contributor Covenant](http://contributor-covenant.org), version 1.0.0, available at [http://contributor-covenant.org/version/1/0/0/](http://contributor-covenant.org/version/1/0/0/).


## Issue Reporting Guidelines
Please use our `Bug.md` template to report bugs, and our `Feature.md` template to request a new feature.

## Pull Request Guidelines
Please see use our merge request template to open up a new pull or merge request.

## Semantic Versioning
This project follows semantic versioning. We release patch versions for critical bugfixes, minor versions for new features or non-essential changes, and major versions for any breaking changes.

Every significant change is documented in the `CHANGELOG.md` file.

To release a new version, please mind the following:
- Change the version number in the `setup.py` file
- Use `git push --tags`

## Branch Organization
Submit all changes directly to the master branch. We don't use separate branches for development or for upcoming releases. We do our best to keep master in good shape, with all tests passing.

Code that lands in master must be compatible with the latest stable release. It may contain additional features, but no breaking changes. We should be able to release a new minor version from the tip of master at any time.

## Style Guide
This project uses [mllint](https://github.com/bvobart/mllint) to evaluate its technical quality. You can check the status of your code styling by simply running `mllint`.
"""
