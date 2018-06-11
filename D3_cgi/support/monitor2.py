#!/usr/bin/python3
#
# 如果用户已经登录，就显示本机的CPU/RAM/HD使用状况，和在线用户信息;
# 否则，就仅仅显示CPU/RAM/HD使用状况信息。
#

import os
import json
import subprocess as sub
import time
from datetime import datetime, timedelta
import pytz


# 显示本机的CPU 使用状况
def cpu():
    text = sub.getoutput('uptime')
    data = text.replace(',', '').split()[-3:]
    header = ['1min', '5min', '15min']
    matrix = [header, data]
    pretty_output(matrix)


# 显示本机的RAM 使用状况
def ram():
    text = sub.getoutput('free')
    lines = text.splitlines()
    total, used, free, shared, buffers, cached = lines[1].split()[1:7]
    used_real, free_real = lines[2].split()[-2:]
    header = ['total', 'used', 'used(real)', 'free', 'free(real)',
              'shared', 'buffers', 'cached']
    data = [total, used, used_real, free, free_real, shared, buffers, cached]
    pretty_output([header, data])


# 显示本机的文件系统使用状况
def hd():
    text = sub.getoutput('df | tail -n +2')
    data = [line.split() for line in text.splitlines()]
    header = ['Device', '1K-blocks', 'Used', 'Available', 'Use%', 'Directory']
    data.insert(0, header)
    pretty_output(data)


# 显示本机的在线用户
def online_user():
    text = sub.getoutput('who')
    data = [line.split() for line in text.splitlines()]
    pretty_output(data)


# column output
def column(matrix):
    lens = [max(len(col) for col in cols) for cols in zip(*matrix)]
    margin = 2
    for line in matrix:
        for l, col in zip(lens, line):
            fmt = '%%-%ds' % (l + margin)
            print(fmt % col, end='')
        print()


# html output
def html(matrix):
    print('<table>')
    for line in matrix:
        print('<tr>')
        for col in line:
            print('<td>', col, '</td>', sep='')
        print('</tr>\n')
    print('</table>')


def parse_cookie():
    cookie_str = os.getenv('HTTP_COOKIE')
    if cookie_str:
        return dict(k.split('=') for k in cookie_str.split('; '))
    else:
        return {}


def get_sessionid():
    cookies = parse_cookie()
    return cookies.get('sessionid')


def is_login(sessionid):
    if not sessionid:
        return False

    session_file_path = os.path.join(session_data_dir, sessionid)

    # 如果session数据不存在，算为没登录
    if not os.path.exists(session_file_path):
        return False

    # 取出session数据，检查是否过期
    session_str = open(session_file_path).read()
    session_data = json.loads(session_str)
    expires = session_data['expires']
    expires = rfc2822_to_datetime(expires)
    if expires < datetime.now():
        os.remove(session_file_path)
        return False
    else:
        return True


def rfc2822_to_datetime(timestr):
    """按照rfc2822标准来解析时间字符串，返回datetime对象"""
    return datetime(*time.strptime(timestr, '%a, %d %b %Y %H:%M:%S %z')[:6])


def update_session_time(sessionid):
    session_file_path = os.path.join(session_data_dir, sessionid)
    session_str = open(session_file_path).read()
    session_data = json.loads(session_str)
    session_data['expires'] = rfc2822_time(calc_time(days=1))
    data_str = json.dumps(session_data)
    open(session_file_path, 'w').write(data_str)


def rfc2822_time(dt):
    """把datetime数据按照rfc2822标准来格式化"""
    return dt.strftime('%a, %d %b %Y %H:%M:%S %z')


def calc_time(tz='Asia/Chongqing', **kargs):
    """计算一个未来的时间点，包含时区信息，返回datetime对象"""
    dt = datetime.now()
    tz = pytz.timezone(tz)
    dt = tz.localize(dt)
    delta = timedelta(**kargs)
    dt = dt + delta
    return dt


session_data_dir = '/tmp/sessions'


if __name__ == '__main__':
    ct = 'text/html'

    # pretty output
    def pretty_output(matrix, ct=ct):
        if ct == 'text/plain':
            column(matrix)
        elif ct == 'text/html':
            html(matrix)

    print("Content-Type: %s\n\n" % ct, end='')
    qs = os.getenv('QUERY_STRING', '')
    if 'cpu' in qs:
        cpu()
    elif 'ram' in qs:
        ram()
    elif 'hd' in qs:
        hd()
    else:
        print('<h3>===> CPU</h3>')
        cpu()
        print('<h3>\n===> RAM</h3>')
        ram()
        print('<h3>\n===> HD</h3>')
        hd()
        # 判断用户是否登录
        sessionid = get_sessionid()
        if is_login(sessionid):
            update_session_time(sessionid)
            print('<h3>\n===> ONLINE USER</h3>')
            online_user()
