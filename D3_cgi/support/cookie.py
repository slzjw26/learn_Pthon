#!/usr/bin/python3

import os
import pytz
from datetime import datetime, timedelta


def calc_expire(tz='Asia/Chongqing', **kargs):
    now = datetime.now()
    tz = pytz.timezone(tz)
    now = tz.localize(now)
    delta = timedelta(**kargs)
    now = now + delta
    return now.strftime('%a, %d %b %Y %H:%M:%S %z')


print('Content-Type: text/plain')
# print('Set-Cookie: name=alice; expires=%s; domain=.example.com' % calc_expire(seconds=10))
# print('Set-Cookie: age=18; expires=%s' % calc_expire(seconds=30))
print('Set-Cookie: name=alice; path=/cgi-bin/')
print('Set-Cookie: age=18; path=/cgi-bin/cookie.py')
print('Set-Cookie: gender=male; httponly;')
print()
print('hello cookie')
