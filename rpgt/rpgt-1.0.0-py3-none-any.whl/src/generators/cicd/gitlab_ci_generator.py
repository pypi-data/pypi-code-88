"""
Gitlab CI generator module.
"""

from typing import Any

from rpgt.src.generators.cicd.cicd_generator import CICDGenerator


class GitlabCICDGenerator(CICDGenerator):
    """
    Gitlab CI generator class.
    """

    def add_job(self, job: str, data: Any) -> None:
        """
        Add job to CI
        """
        self.jobs[job] = data

        if data["stage"] not in self.stages:
            self.stages.append(data["stage"])

    def generate(self, cwd: str) -> None:
        """
        Generate CI
        """
        texts = ["image: python:3.8\n"]

        texts.append("variables:")
        texts.append("  WORKON_HOME: .pipenv/venvs")
        texts.append("  PIP_CACHE_DIR: .pipenv/pipcache\n")

        texts.append("cache:")
        texts.append("  paths:")
        texts.append("    - .cache/pip")
        texts.append("    - venv/")
        texts.append("    - .pipenv")
        texts.append("    - .venv/\n")

        texts.append("before_script:")
        texts.append("  - pip install pipenv\n")

        texts.append("stages:")
        for stage in self.stages:
            texts.append(f"  - {stage}")

        texts.append("")

        for job, data in self.jobs.items():
            texts.append(self.generate_job(job, data))

        final_text = "\n".join(texts)

        with open(f"{cwd}/.gitlab-ci.yml", "w") as file:
            file.write(final_text)

    def generate_job(self, job: str, data: Any) -> str:
        """
        Generate job
        """
        texts = [f"{job}:"]

        texts.append(f'  stage: {data["stage"]}')
        texts.append("  script:")

        for script_line in data["script"]:
            texts.append(f"    - {script_line}")

        if "artifacts" in data:
            texts.append("  artifacts:")
            for artifact in data["artifacts"]:
                texts.append("    paths:")
                for path in artifact["paths"]:
                    texts.append(f"      - {path}")
                texts.append(f'    expire_in: {artifact["expire_in"]}')

                if "reports" in artifact:
                    texts.append("    reports:")
                    texts.append("      junit:")
                    for report in artifact["reports"]["junit"]:
                        texts.append(f"        - {report}")

        if "only" in data:
            texts.append("  only:")
            for branch in data["only"]:
                texts.append(f"    - {branch}")

        texts.append("\n")
        return "\n".join(texts)
