"""Test requirements hashing."""

# same file: same hashes
# differnt contents: different hashes

# is required:
import pytest

@pytest.fixture
def some_requirements(tmp_path):
    path = tmp_path / "some_requirements.txt"
    path.write_text("requests\n")
    return path


@pytest.fixture
def same_requirements(tmp_path):
    path = tmp_path / "same_requirements.txt"
    path.write_text("requests\n")
    return path


@pytest.fixture
def other_requirements(tmp_path):
    path = tmp_path / "other_requirements.txt"
    path.write_text("httpx\n")
    return path


def test_identical_requirements(some_requirements, same_requirements):
    some_hash = peeve.hash_requirements(some_requirements)
    same_hash = peeve.hash_requirements(same_requirements)
    assert some_hash == same_hash


def test_different_requirements(some_requirements, other_requirements):
    some_hash = peeve.hash_requirements(some_requirements)
    other_hash = peeve.hash_requirements(other_requirements)
    assert some_hash != other_hash


def test_update_not_required(tmp_path):
    hash_file = tmp_path / "peeve.json"
    some_hash = "jabberwocky"
    peeve.update_hash(hash_file, some_hash)
    assert peeve.is_update_required(hash_file, some_hash) is False


def test_update_required(tmp_path):
    hash_file = tmp_path / "peeve.json"
    some_hash = "jabberwocky"
    peeve.update_hash(hash_file, some_hash)
    assert peeve.is_update_required(hash_file, "bandersnatch") is True
