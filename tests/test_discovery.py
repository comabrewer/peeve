"""Test discovery of requirements file and virtual environment."""
import pytest

import peeve


@pytest.fixture(scope="session")
def other_path(tmp_path_factory):
    """Path to some directory outside of project."""
    path = tmp_path_factory.mktemp("other")
    return path


@pytest.fixture
def nested_script_path(project_path):
    """Path to script in child directory."""
    script_path = project_path / "scripts" / "script.py"
    script_path.parent.mkdir()
    script_path.touch()
    yield script_path
    script_path.unlink()
    script_path.parent.rmdir()


def test_get_script_path_single_argument(script_path):
    """Get path to script to execute."""
    argv = [str(script_path)]
    assert peeve.get_script_path(argv) == script_path


def test_get_script_path_multiple_arguments(script_path):
    """Get path to script to execute when multiple arguments are given."""
    argv = [str(script_path), "--help"]
    assert peeve.get_script_path(argv) == script_path
    # TODO: ensure that additional args are passed to script


def test_get_script_path_missing_arguments():
    """Get path to script to execute when multiple arguments are given."""
    assert peeve.get_script_path(["peeve"]) is None


def test_find_requirements_same_dir(requirements_path, script_path):
    """Find requirements file next to script."""
    assert peeve.find_requirements_file(script_path) == requirements_path


def test_find_requirements_parent_dir(requirements_path, nested_script_path):
    """Find requirements file in some parent directory of script."""
    assert peeve.find_requirements_file(nested_script_path) == requirements_path


def test_find_requirements_missing(other_path):
    """Do nothing if requirements missing."""
    assert peeve.find_requirements_file(other_path) is None
