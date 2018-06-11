#!/usr/bin/python3

"""
八、承接练习三，按以下要求写一个程序

1. 实现用户登录功能，登录有效期为24小时
2. 用户登录后可以查看系统在线用户，没登录用户可以看CPU/RAM/HD使用状况
3. 登录成功后应该自动重定向到查看系统信息的页面 (Status 302, Location)
4. 用户每次查看系统信息时更新session的时间戳，重新计算有效时间

要点：
    1. 把成功登录的用户的相关信息存放到服务器的文件系统中
    2. 服务器创建一个有效期是24小时的cookie，存放session id
    3. 服务端在session数据中存放时间戳信息，防止客户端篡改cookie的时间
    4. 登录成功后设置状态码302，并通过Location提供一个新的URL做重定向

参考：

    echo "Set-Cookie: gender=female; domain=.centosc.com; httponly"
    echo "Status: 302 Found"
    echo "Location: /cgi-bin/monitor"
"""
import os
import sys
import json
import hashlib
import random
import pytz
from datetime import datetime, timedelta


def response(headers, body):
    for h in headers:
        print(h)
    print()
    for b in body:
        sys.stdout.write(b)


def read_params():
    params = sys.stdin.read()
    return dict(p.split('=') for p in params.split('&'))


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


def generate_login_form(error_message=''):
    html = """
    <html>
    <head>
      <title>Log in</title>
    </head>
    <body>
      <form method="post">
        <table>
          <tr><td colspan=2 style="color: red">%s</td></tr>
          <tr>
            <td><label for="username">Name: </label></td>
            <td><input name="username" id="username"></td>
          </tr>
          <tr>
            <td><label for="password">Password: </label></td>
            <td><input name="password" id="password" type="password"></td>
          </tr>
          <tr><td colspan=2><input type="submit" value="Log in"></td></tr>
        <table>
      </form>
    </body>
    </html>
    """ % error_message
    return response(['Content-Type: text/html'], [html])


def generate_session_id(value):
    value += str(random.random())
    h = hashlib.md5(value.encode())
    return h.hexdigest()


def login_ok(params):
    username = params['username']
    password = params['password']
    for info in user_data:
        if (info.get('username') == username
                and info.get('password') == password):
            return True
    return False


session_data_dir = '/tmp/sessions'
user_data = [{'username': 'alice', 'password': 'alice'},
             {'username': 'bob', 'password': 'bob'},
             {'username': 'charlie', 'password': 'charlie'}]


if __name__ == '__main__':
    method = os.getenv('REQUEST_METHOD')
    if method == 'GET':
        # 提供登录表单
        generate_login_form()
    elif method == 'POST':
        params = read_params()
        # 做登录验证
        # 1. 把成功登录的用户的相关信息存放到服务器的文件系统中
        # 2. 服务器创建一个有效期是24小时的cookie，存放session id
        # 3. 服务端在session数据中存放时间戳信息，防止客户端篡改cookie的时间
        # 4. 登录成功后设置状态码302，并通过Location提供一个新的URL做重定向
        if login_ok(params):
            # 制作session
            username = params['username']
            expires = rfc2822_time(calc_time(days=1))
            data_str = json.dumps(dict(username=username, expires=expires))

            sessionid = generate_session_id(username+expires)
            os.makedirs(session_data_dir, 0o755, exist_ok=True)
            session_file_path = os.path.join(session_data_dir, sessionid)
            open(session_file_path, 'w').write(data_str)
            cookie_str = 'sessionid=%s; expires=%s;' % (sessionid, expires)
            headers = ['Content-Type: text/plain',
                       'Set-Cookie: %s' % cookie_str,
                       'Status: 302 FOUND',
                       'Location: /cgi-bin/monitor2.py']
            response(headers, ['unsupported method %s' % method])
        else:
            # 登录失败，返回登录表单，提供用户重试
            generate_login_form(error_message='login failed')
    else:
        headers = ['Content-Type: text/plain',
                   'Status: 400 BAD_REQUEST']
        response(headers, ['unsupported method %s' % method])
