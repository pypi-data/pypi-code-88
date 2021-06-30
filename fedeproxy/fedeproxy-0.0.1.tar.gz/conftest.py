import pytest
import sh


def pytest_configure(config):
    config.addinivalue_line("markers", "gitlab: mark tests which require live GitLab instances")


@pytest.fixture
def git_repository(tmpdir):
    d = f"{tmpdir}/origin"
    sh.git.init(d)
    open(f"{d}/README.md", "w").write("# testrepo")
    open(f"{d}/info.txt", "w").write("# someinfo")
    sh.git("-C", d, "add", "README.md", "info.txt")
    sh.git("-C", d, "commit", "-m", "initial")
    sh.git("-C", d, "checkout", "-b", "otherbranch")
    return d
