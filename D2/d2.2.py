import time
import sys
from datetime import datetime, timedelta


if len(sys.argv) != 3:
    print('usage: d2.2.py<date time string><time delta>')
    exit(1)

time_str = sys.argv[1]
add_days = sys.argv[2]
time_format = '%Y-%m-%d %H:%M:%S'

if add_days.startswith('-'):
    tmp_add = add_days[1:]
else:
    tmp_add = add_days
if not tmp_add.isdigit():
    print('invalid time delta: %s' % add_days)
    exit(1)

add_days = int(add_days)
delta = timedelta(add_days)

try:
    t = time.strptime(time_str, time_format)
except ValueError:
    print('invalid time string: %s' % time_str)
    exit(1)

t2 = t[:6]
dt = datetime(*t2) + delta
result = dt.strftime(time_format)
print(result)