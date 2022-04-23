"""Test requirements hashing."""

import pytest

import peeve


@pytest.fixture
def some_requirements(tmp_path):
    """Path to a requirements file."""
    path = tmp_path / "some_requirements.txt"
    path.write_text("requests\n")
    return path


@pytest.fixture
def same_requirements(tmp_path):
    """Path to other requirements file with same contents."""
    path = tmp_path / "same_requirements.txt"
    path.write_text("requests\n")
    return path


@pytest.fixture
def other_requirements(tmp_path):
    """Path to other requziurements file with other contents."""
    path = tmp_path / "other_requirements.txt"
    path.write_text("httpx\n")
    return path


def test_identical_requirements(some_requirements, same_requirements):
    """Same contents yield same hash."""
    some_hash = peeve.hash_requirements(some_requirements)
    same_hash = peeve.hash_requirements(same_requirements)
    assert some_hash == same_hash


def test_different_requirements(some_requirements, other_requirements):
    """Other contents yield different hash."""
    some_hash = peeve.hash_requirements(some_requirements)
    other_hash = peeve.hash_requirements(other_requirements)
    assert some_hash != other_hash


def test_update_not_required(tmp_path):
    """Update not required if hash is the same."""
    hash_file = tmp_path / "peeve.json"
    some_hash = "jabberwocky"
    peeve.update_hash(hash_file, some_hash)
    assert peeve.is_update_required(hash_file, some_hash) is False


def test_update_required(tmp_path):
    """Update required if hash is different."""
    hash_file = tmp_path / "peeve.json"
    some_hash = "jabberwocky"
    peeve.update_hash(hash_file, some_hash)
    assert peeve.is_update_required(hash_file, "bandersnatch") is True
