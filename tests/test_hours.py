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
    (('1:30', '-1:30', '1:30', '-1:30', '1:00','-1:00'), 0),
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

@pytest.mark.parametrize('times, expected', [
    (('3:07', '8:12', '-1:17', '15:03', '-0:27', '-16:00'), '8:38'), # jan
    (('3:07', '8:12', '14:44'), '26:03'),
    (('-1:17', '-0:27', '-16:00'), '-17:44'),
    (('26:03', '-17:44'), '8:19'),
    (('8:38', '2:57', '-0:13'), '11:22'), # fev
])
def test_myTimebank(times, expected):
    assert toHoursMinutes(timebank(times)) == expected

@pytest.mark.parametrize('times, expected', [
    (('8:00', '12:00', '13:00', '17:00'), '8:00'),
    (('8:00', '12:00', '13:00', '16:00'), '7:00'),
    (('8:06', '11:45', '13:36', '17:57'), '8:00'),
])
def test_worktime(times, expected):
    assert worktime(times) == expected
