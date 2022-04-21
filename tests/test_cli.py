"""Test command line interface."""
import subprocess

import pytest


@pytest.fixture(scope="session")
def script(tmp_path):
    requirements = tmp_path / "requirements.txt"
    requirements.write_text("abomination")
    script = tmp_path / "script.py"
    script.write_text("import abomination")
    return str(script)


@pytest.mark.parametrize("commands", [
    pytest.param(["python", "peeve.py"], id="script"),
    pytest.param(["python", "-m", "peeve"], id="module"),
    pytest.param(["peeve"], id="cli"),
    pytest.param(["pv"], id="short_cli"),
    [""],
])
def test_invocation(commands, script):
    """Different invocation modes work."""
    commands += [script]
    subprocess.run(commands, check=True)


def test_missing_argument():
    """A script argument is required."""
    process = subprocess.run(["peeve"], text=True)
    assert process.returncode != 0


def test_non_existing_script():
    """The argument must point to an existing script."""
    process = subprocess.run(["peeve", "doesnt_exist.py"])
    assert process.returncode != 0


@pytest.mark.xfail(reason="Module execution not implemented yet.")
def test_module_execution(script):
    """Modules or packages can be executed."""
    commands = ["peeve", "-m", script.name]
    subprocess.run(commands, check=True, cwd=script.parent)
