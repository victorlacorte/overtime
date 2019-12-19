import pytest

from hours import timebank, toHoursMinutes, worktime


@pytest.mark.parametrize('times, expected', [
    (('0:00', '0:00'), 0),
    (('0:01', '0:00'), 60),
    (('0:01', '0:01'), 120),
    (('0:01', '0:10'), 660),
    (('0:01', '-0:01'), 0),
    (('-0:01', '-0:01', '-0:01'), -180),
    (('1:00', '0:00'), 3600),
    (('1:30', '0:00'), 5400),
    (('1:30', '-1:30'), 0),
    (('1:30', '-1:30', '1:00'), 3600),
    (('1:30', '-1:30', '-1:00'), -3600),
    (('1:30', '-1:30', '-1:00', '1:00'), 0),
    (('1:30', '-1:30', '1:30', '-1:30', '1:00'), 3600),
    (('1:30', '-1:30', '1:30', '-1:30', '1:00', '-1:00'), 0),
])
def test_timebank(times, expected):
    assert timebank(times) == expected


@pytest.mark.parametrize('time, expected', [
    (0, '0:00'),
    (-3600, '-1:00'),
    (3600, '1:00'),
    (5400, '1:30'),
    (-4620, '-1:17'),
    (-1620, '-0:27'),
])
def test_toHoursMinutes(time, expected):
    assert toHoursMinutes(time) == expected


@pytest.mark.parametrize('times, lunch_discount, lunch, expected', [
    (('7:15', '11:48', '12:46', '17:40'), False, None, '9:27'),
    (('8:00', '17:00'), True, '1:00', '8:00'),
    (('8:00', '18:00'), True, '2:00', '8:00'),
])
def test_worktime(times, lunch_discount, lunch, expected):
    assert worktime(times, lunch_discount=lunch_discount, lunch=lunch) \
        == expected
