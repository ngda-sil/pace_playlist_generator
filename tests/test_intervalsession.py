import pytest

from models import IntervalSession


@pytest.fixture()
def my_interval_session():
    return IntervalSession(500, 4, 30, 60, 8)


def test_effort_duration_ms(my_interval_session):
    assert my_interval_session.effort_duration_ms == 135000


def test_rest_ms(my_interval_session):
    assert my_interval_session.rest_ms == 60000


def test_distance_zero():
    with pytest.raises(ValueError):
        IntervalSession(0, 4, 30, 60, 8)


def test_s_pace_too_big():
    with pytest.raises(ValueError):
        IntervalSession(500, 4, 90, 60, 8)


def test_pace_zero():
    with pytest.raises(ValueError):
        IntervalSession(500, 0, 0, 60, 8)
