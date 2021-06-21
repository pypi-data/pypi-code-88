"""
Readme generator module.
"""
import argparse

from rpgt.src.generators.environment.environment_generator import EnvironmentGenerator
from rpgt.src.generators.generator import Generator


def generate_main_information(project: str) -> str:
    """
    Generates the main project information.
    :return: a stringual representation of the main project information.
    """
    return f"""# {project}

"""


def generate_next_steps() -> str:
    """
    Generates the next steps information.
    :return: a stringual representation of the next steps information.
    """
    return """## Getting Started
To get started with your generated repository, please first check the next steps available on [the wiki](https://gitlab.com/tweet.dimitri/rpgt/-/wikis/Next%20steps) of RPGT.

"""


def generate_reproducibility() -> str:
    """
    Generates the reproducibility information.
    :return: a stringual representation of the reproducibility information.
    """
    return """## Reproducibility
Because this package uses [DVC](https://dvc.org/), reproducing results becomes an easy task.
To run all the required scripts in the right order, you only need to run `pipenv run dvc repro` (provided that you have already run `pipenv install`).
This will execute the pipeline defined in `dvc.yaml` and run the correct scripts in the right order.
Afterwards, you'll be able to see the results in the `results` directory.

"""


def generate_license(license_type: str) -> str:
    """
    Generates the license information.
    :return: a stringual representation of the license information.
    """
    return f"""## License
    
This project is {license_type.upper()} licensed. Please see the [LICENSE](LICENSE.md) file for more information.

"""


def generate_authors() -> str:
    """
    Generates the author information.
    :return: a stringual representation of the author information.
    """
    return """## Authors

- [Author 1]
- [Author 2]

Please see the [CONTRIBUTING](CONTRIBUTING.md) file for more information on how to contribute to this project.
"""


class ReadmeGenerator(Generator):
    """
    Readme generator class.
    """

    def __init__(self, args: argparse.Namespace, env_gen: EnvironmentGenerator):
        """
        Abstract initialize function definition.
        """
        super().__init__(args)
        self.env_gen = env_gen

    def generate(self, cwd: str) -> None:
        """
        Writes the README.md to file.
        """
        project = self.args.name
        license_type = self.args.license.lower()

        with open(f"{cwd}/README.md", "w") as file:
            file.write(generate_main_information(project))
            file.write(generate_next_steps())
            file.write(self.generate_requirements())
            file.write(generate_reproducibility())
            file.write(generate_license(license_type))
            file.write(generate_authors())

    def generate_requirements(self) -> str:
        """
        Generates the requirements information.
        :return: a stringual representation of the requirements information.
        """
        reqs = []

        for requirement, _ in self.env_gen.requirements.items():
            reqs.append(f"- {requirement}")

        reqs_str = "\n".join(reqs)

        return f"""## Requirements
In order to contribute to this package, you will need to have the following components installed on your system:
{reqs_str}

You can easily install them using `pipenv install`.

"""
