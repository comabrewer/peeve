"""Test virtual environment management."""
import pytest
import subprocess
import sys

import peeve


def test_create_venv(venv_path):
    """Venv exists after creation."""
    assert not venv_path.exists()
    peeve.create_venv(venv_path)
    assert venv_path.exists()


def test_update_venv(venv_path, requirements_path):
    """Dependencies exist after venv update."""
    peeve.create_venv(venv_path)
    peeve.update_venv(venv_path, requirements_path)
    site_packages = venv_path / peeve.get_lib_dir_name() / "site-packages"
    assert "abomination.py" in site_packages.iterdir()


def test_is_active(venv_path):
    """Venv is not active by default."""
    assert not peeve.is_active(venv_path)


def test_activation(venv_path, tmp_path):
    """Venv is active after activation."""
    script = tmp_path / "activate.py"
    lines = [
        "import peeve",
        "from pathlib import Path",
        "venv_dir = Path(r'{venv_path}')",
        "peeve.activate(venv_dir)",
        "assert peeve.is_active(venv_dir)",
    ]
    script.write_text("\n".join(lines))
    subprocess.run([sys.executable, str(script)], check=True)
