from functools import reduce
import math
import sys


def toSeconds(t):
    h, m = t.split(':')
    negative = True if '-' in h else False
    h, m = map(int, (h, m))
    if negative:
        return h*3600 - m*60
    return h*3600 + m*60


def toHoursMinutes(seconds):
    seconds = int(seconds)
    negative = False
    if seconds < 0:
        # Avoid floor errors with negative amounts
        negative = True
        seconds = -seconds
    # Rounding up seems safer than performing a simple integer division
    m = math.ceil(seconds / 60)
    h, m = m // 60, m % 60
    if negative:
        return '-%0d:%02d' % (h, m)
    return '%0d:%02d' % (h, m)


def planning(hours, minutes, days):
    '''
    Return the average time per day required to achieve hours and minutes in
    days.
    '''
    hours, minutes, days = int(hours), int(minutes), int(days)
    seconds = (hours*3600 + minutes*60) / days
    return toHoursMinutes(seconds)


def timebank(times):
    '''times: array of strings in HH:mm format'''

    seconds = [toSeconds(t) for t in times]
    return reduce(lambda x, y: x + y, seconds)


def worktime(times, lunch_discount=False, lunch='1:00'):
    '''
    Goal and luch (amounts) are just an idea. Maybe make an optional parameter
    such as use_lunch (bool) that verifies if we need to discount the lunch
    time from total. Also, in this case, make sure we have both use_lunch and
    lunch
    '''

    assert len(times) % 2 == 0, f'Need an even amount of timestamps, got' \
        ' {len(times)}'

    if lunch_discount:
        assert lunch is not None, 'Lunch must be a time string in the format' \
            'HH:mm'

    signals = [-1, 1] * len(times)
    total = 0

    for s, t in zip(signals, map(toSeconds, times)):
        total += s * t

    if lunch_discount:
        lunch_seconds = toSeconds(lunch)
        if lunch_seconds > 0:
            total -= lunch_seconds
        else:
            total += lunch_seconds

    return toHoursMinutes(total)


if __name__ == '__main__':
    print(planning(sys.argv[1], sys.argv[2], sys.argv[3]))
