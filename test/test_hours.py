import pytest

from hours import timebank, toHoursMinutes


@pytest.mark.parametrize('times, expected', [
    (('1:00', '0:00'), 3600),
    (('1:30', '0:00'), 5400),
    (('1:30', '-1:30'), 0),
    (('1:30', '-1:30', '1:00'), 3600),
    (('1:30', '-1:30', '-1:00'), -3600),
    (('1:30', '-1:30', '-1:00', '1:00'), 0),
    (('1:30', '-1:30', '1:30', '-1:30', '1:00'), 3600),
    (('1:30', '-1:30', '1:30', '-1:30', '1:00','-1:00'), 0),
])
def test_timebank(times, expected):
    assert timebank(times) == expected

@pytest.mark.parametrize('time, expected', [
    (0, '0:00'),
    (-3600, '-1:00'),
    (3600, '1:00'),
    (5400, '1:30'),
])
def test_toHoursMinutes(time, expected):
    assert toHoursMinutes(time) == expected

@pytest.mark.parametrize('times, expected', [
    (('3:07', '8:12', '-1:17', '14:44', '-0:27', '-16:00'), '8:19'),
    (('3:07', '8:12', '14:44'), '26:03'),
    (('-1:17', '-0:27', '-16:00'), '-18:44'),
    (('26:03', '-17:10'), '8:53'),
])
def test_myTimebank(times, expected):
    assert toHoursMinutes(timebank(times)) == expected
