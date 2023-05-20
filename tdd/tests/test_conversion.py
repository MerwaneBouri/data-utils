import pytest
from tdd.conversion import project_4326_to_2154


def test_project_4326_to_2154_works():
    assert project_4326_to_2154(lat=46.5, long=3) == (
        pytest.approx(700_000),
        pytest.approx(6_600_000),
    )