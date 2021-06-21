"""
VCP generator module.
"""

import argparse

from rpgt.src.setup.vcp.github_setup import GithubSetup
from rpgt.src.setup.vcp.gitlab_setup import GitlabSetup
from rpgt.src.setup.vcp.vcp_setup import VCPSetup


def get_vcp(name: str, args: argparse.Namespace, cwd: str) -> VCPSetup:
    """
    Get VCP setup.
    :return: the VCP setup.
    """
    vcp_setup: VCPSetup
    # Version Control
    if name == "gitlab":
        vcp_setup = GitlabSetup(args, cwd)
    elif name == "github":
        print("WARNING: github is not fully supported yet!")
        vcp_setup = GithubSetup(args, cwd)
    else:
        raise Exception(f"'{name}' is not supported as a version control provider")

    return vcp_setup
