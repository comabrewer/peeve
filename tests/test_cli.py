"""Test command line interface."""
import subprocess

import pytest


@pytest.mark.parametrize("commands", [
    pytest.param(["python", "peeve.py"], id="script"),
    pytest.param(["python", "-m", "peeve"], id="module"),
    pytest.param(["peeve"], id="cli"),
    pytest.param(["pv"], id="short_cli"),
])
def test_invocation(commands, script_path):
    """Different invocation modes work."""
    commands += [str(script_path)]
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
def test_module_execution(script_path):
    """Modules or packages can be executed."""
    commands = ["peeve", "-m", script_path.name]
    subprocess.run(commands, check=True, cwd=script.parent)
