"""Test virtual environment management."""

import pytest

import peeve

@pytest.fixture
def existing_venv(tmp_path):
    venv_dir = tmp_path / "my_venv"
    create_venv_dir()
    return venv_dir


def test_create_venv(venv_dir):
    assert not venv_dir.exists()
    create_venv(venv_dir)
    assert venv_dir.exists()


def test_update_venv(venv_dir):
    create_venv()
    # TODO


def test_is_active(venv_dir):
    assert not peeve.is_active(venv_dir)
    # TODO: check that tox venv is active


def test_activation(venv_dir, tmp_path):
    # Test in process activation
    script = tmp_path / "activate.py"
    script.write_text(f"import peeve; peeve.activate({venv_dir})")
    subprocess.run([sys.executable, str(script)], check=True)
    # TODO: check that packages in venv are visible
    # TODO: check that packages outside are not visible
