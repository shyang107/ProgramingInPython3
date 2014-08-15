# coding=UTF-8

import calendar, time
import datetime


def main():
    moon_datetime_a = datetime.datetime(1969, 7, 20, 20, 17, 40, 0, None)
    moon_time = calendar.timegm(moon_datetime_a.utctimetuple())
    moon_datetime_b = datetime.datetime.utcfromtimestamp(moon_time)
    print(moon_datetime_a.isoformat())
    print(moon_datetime_b.isoformat())
    print(time.strftime("%Y-%m-%dT%H:%M:%S", time.gmtime(moon_time)))


main()
