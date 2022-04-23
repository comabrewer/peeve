"""pytest fixtures and hooks."""
import shutil

import pytest


@pytest.fixture(scope="session", autouse=True)
def project_path(tmp_path_factory):
    """Path to project root directory."""
    path = tmp_path_factory.mktemp("project")
    return path


@pytest.fixture(scope="session", autouse=True)
def requirements_path(project_path):
    """Path to requirements.txt file."""
    path = project_path / "requirements.txt"
    path.write_text("abomination\n")
    return path


@pytest.fixture(scope="session", autouse=True)
def script_path(project_path):
    """Path to Python script."""
    path = project_path / "script.py"
    path.write_text("import abomination\n")
    return path


@pytest.fixture(autouse=True)
def venv_path(project_path):
    """Path to virtual environment.

    Is guaranteed not to exist.
    """
    path = project_path / ".venv"
    if path.exists():
        shutil.rmtree(path)
    yield path
    if path.exists():
        shutil.rmtree(path)
