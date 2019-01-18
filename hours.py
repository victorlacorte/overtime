from functools import reduce
import datetime
import sys


def toHoursMinutes(seconds):
    seconds = int(seconds)
    m, _ = divmod(seconds, 60)
    h, m = divmod(m, 60)
    return '%0d:%02d' % (h, m)

def planning(hours, minutes, days):
    '''
    Return the average time per day required to achieve hours and minutes in
    days.
    '''
    hours, minutes, days = int(hours), int(minutes), int(days)
    seconds = (hours*3600 + minutes*60) / days
    return datetime.timedelta(seconds=seconds)

def timebank(times):
    '''times: array of strings in the HH:mm format'''
    def toSeconds(t):
        h, m = t.split(':')
        if '-' in h:
            h, m = map(int, (h, m))
            if h == 0:
                return -m*60
            return h*3600 - m*60
        h, m = map(int, (h, m))
        return h*3600 + m*60

    seconds = [toSeconds(t) for t in times]
    return reduce(lambda x, y: x + y, seconds)


if __name__ == '__main__':
    print(planning(sys.argv[1], sys.argv[2], sys.argv[3]))
