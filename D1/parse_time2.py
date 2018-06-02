import sys
import time
from datetime import datetime, timedelta

# 命令行参数必须等于1个
if len(sys.argv) != 3:
    print('usage: time_parse.py <date time string> <time delta>')
    exit(1)

time_str = sys.argv[1]
delta_str = sys.argv[2]
time_fmt = '%Y-%m-%d %H:%M:%S'

if delta_str.startswith('-'):
    tmp_str = delta_str[1:]
else:
    tmp_str = delta_str
if not tmp_str.isdigit():
    print('invalid time delta: %s' % delta_str)
    exit(1)
delta = int(delta_str)

# 用户输入的时间字符串很可能是不符合规范的,如果遇到这样的不规范时间字符串,
# time.strptime 函数将会抛出ValueErro 异常
try:
    t = time.strptime(time_str, time_fmt)
except ValueError:
    print('invalid time string: %s' % time_str)
    exit(1)

# t是一个时间结构体,其前面6个字段就是年/月/日/时/分/秒
t2 = t[:6]

# 通过 *t2 这样的传参方式把t2里面的6个元素打散,按顺序传递给datetime类的构造函数
dt = datetime(*t2)

# add time delta
dt = dt + timedelta(days=delta)

# 格式化并输出结果
result = dt.strftime('%a, %Y-%m-%d %H:%M:%S')
print(result)
