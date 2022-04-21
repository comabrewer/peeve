"""



"""

# root directory discovery:
# discover requirements next to script
# discover requriements in some parent directoy
# fail if there are no requirements - or do nothing?

# venv:
# detect if venv exists
# detect if venv is already active
# detect if venv needs update
# detect right python version
# detect platform

# activate:
# venv is active
# packets are installed
# other packets are not visible

# execute

# different execution modes:
# as script; as import; as module; as cli


import pytest

import peeve



@pytest.fixture(scope="session")
def project_path(tmp_path_factory):
	path = tmp_path_factory() / "project"
	path.mkdir()
	return path


@pytest.fixture(scope="session")
def other_path(tmp_path_factory):
	path = tmp_path_factory() / "other"
	path.mkdir()
	return path


@pytest.fixture(scope="session")
def requirements_path(project_path):
	path = project_path / "requirements.txt"
	path.write_text()
	return path


@pytest.fixture(scope="session")
def script_path(project_path):
	path = project_path / "script.py"
	path.write_text("print('hello')")
	return path


@pytest.fixture(scope="session")
def venv_path(project_path):
	path = project_path / ".venv"
	path.mkdir()
	return path


def test_get_script_path_single_argument():
	"""Get path to script to execute."""
	assert peeve.get_script_path(["peeve script.py"]) == "script.py"


def test_get_script_path_multiple_arguments():
	"""Get path to script to execute when multiple arguments are given."""
	assert peeve.get_script_path(["peeve script.py --help"]) == "script.py"


def test_get_script_path_missing_arguments():
	"""Get path to script to execute when multiple arguments are given."""
	assert peeve.get_script_path(["peeve"]) is None


def test_find_requirements_same_dir(requirements_path, script_path):
	"""Find requirements file next to script."""
	assert peeve.find_requirements_file(script_path) == requirements_path


def test_find_requirements_parent_dir(requirements_path):
	"""Find requirements file in some parent directory of script."""
	script_path = requirements_path.parent / "scripts" / "script.py"
	script_path.parent.mkdir()
	script_path.write_text("print('hola')")
	assert peeve.find_requirements_file(script_path) == requirements_path


def test_find_requirements_missing(other_path):
	"""Do nothing if requirements missing."""
	assert peeve.find_requirements_file(other_path) is None


def test_venv_does_exist(project_path, venv_path):
	"""Existing virtual environment is found."""
	assert peeve.find_venv(project_path) == venv_path


def test_venv_doesnt_exist(other_path):
	"""Missing venv is detected as such."""
	assert peeve.find_venv(other_path) is None



