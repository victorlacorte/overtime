from functools import reduce
import datetime
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

def worktime(times, goal='8:00', lunch='1:00'):
    '''Goal and luch (amounts) are just an idea'''

    assert len(times) % 2 == 0,
    f'Need an even amount of timestamps, got {len(times)}'

    signals = [-1, 1] * len(times)
    total = 0
    for s, t in zip(signals, map(toSeconds, times)):
        total += s * t
    return toHoursMinutes(total)


if __name__ == '__main__':
    print(planning(sys.argv[1], sys.argv[2], sys.argv[3]))
