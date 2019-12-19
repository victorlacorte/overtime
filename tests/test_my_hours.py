import pytest
from collections import namedtuple

from hours import timebank, toHoursMinutes, worktime

Hours = namedtuple('Hours', [
    'Acc',
    'Extra',
    'Delay',
    'Miss'
])


@pytest.mark.parametrize('times, expected', [
    (('7:15', '11:48', '12:46', '17:40'), '9:27'),  # 12/17/2019
    (('9:07', '12:04', '14:19', '18:21'), '6:59'),  # 12/18/2019
    (('8:10', '11:40', '13:00', '18:00'), '8:30'),  # 12/19/2019
])
def test_myworktime(times, expected):
    assert worktime(times) == expected


@pytest.mark.parametrize('times, expected', [
    # December
    (('0:00',), '0:00'),

    (Hours(
        Acc='0:00',
        Extra='0:00',
        Delay='-0:00',
        Miss='-0:00',
    ), '0:00')
])
def test_myTimebank(times, expected):
    assert toHoursMinutes(timebank(tuple(times))) == expected
