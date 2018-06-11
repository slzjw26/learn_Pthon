#!/usr/bin/python3
#
# User management application
#

"""
六、用python写一个cgi程序，功能如下：

    1. 查询用户 (get)
    2. 创建用户 (post)
    3. 修改用户 (post)
    4. 删除用户 (post)

要点：

    1. 通过变量 REQUEST_METHOD 来判断是get还是post
    2. 通过变量 QUERY_STRING 来判断是创建还是修改还是删除
    3. 通过subprocess.getoutput, 或者os.system 来运行shell命令
    4. 相关命令如下：
        查用户：grep ^root /etc/passwd
        加用户：useradd user-name
        改用户：usermod user-name
        删用户：userdel user-name
"""
import os
import sys
import subprocess as sub


def response(headers, body):
    for h in headers:
        print(h)
    print()
    for b in body:
        sys.stdout.write(b)


def get_user_info(params_str, headers):
    if params_str:
        params = dict(p.split('=') for p in params_str.split('&'))
    else:
        params = {}
    name = params.get('name')
    if not name:
        headers.append('Status: 400 BAD_REQUEST')
        return response(headers, ['name is required'])

    info = read_user_info(name)
    if not info:
        headers.append('Status: 200 OK')
        return response(headers, ['name %s not exists' % name])

    body = []
    body.append('name: %s\n' % info['name'])
    body.append('uid: %s\n' % info['uid'])
    body.append('gid: %s\n' % info['gid'])
    body.append('comment: %s\n' % info['comment'])
    body.append('home: %s\n' % info['home'])
    body.append('shell: %s\n' % info['shell'])
    return response(headers, body)


def read_user_info(name):
    """从系统的用户数据库 /etc/passwd 中读取指定用户的基本信息，返回字典"""
    db = '/etc/passwd'
    info = [line.split(':') for line in open(db).read().splitlines()]
    user_info = [i for i in info if i[0] == name]
    if not user_info:   # 找不到用户
        return
    user_info = user_info[0]
    colnames = ('name', 'password', 'uid', 'gid', 'comment', 'home', 'shell')
    return dict(zip(colnames, user_info))


def alter_user(headers):
    data = sys.stdin.read().strip()
    if data:
        params = dict(p.split('=') for p in data.split('&'))
    else:
        headers.append('Status: 400 BAD_REQUEST')
        return response(headers, ['invalid parameters'])

    kind = params['kind']   # add? delete? modify?
    if kind == 'add':
        cmd = ['useradd', params['name']]
    elif kind == 'delete':
        cmd = ['userdel', '-r', params['name']]
    elif kind == 'mod':
        # 目前只支持修改用户的comment字段，后续可以扩展
        name = params['name']
        comment = params['comment']
        cmd = ['usermod', '-c', comment, name]
    else:
        headers.append('Status: 400 BAD_REQUEST')
        return response(headers, ['operation %s not supported' % kind])

    # 运行外部的用户管理命令
    # 临时修改，用sudo 执行命令
    cmd.insert(0, 'sudo')
    cmd = ' '.join(cmd)
    code, out = sub.getstatusoutput(cmd)
    if code == 0:
        headers.append('Status: 200 OK')
        return response(headers, ['operation success'])
    else:
        headers.append('Status: 200 OK')
        return response(headers, ['failed: %s' % out])


if __name__ == '__main__':
    headers = []
    headers.append('Content-Type: text/plain')

    if os.getenv('REQUEST_METHOD') == 'GET':
        params = os.getenv('QUERY_STRING', '')
        get_user_info(params, headers)
    elif os.getenv('REQUEST_METHOD') == 'POST':
        alter_user(headers)
    else:
        headers.append('Status: 405 METHOD_NOT_ALLOWED')
        response(headers, [])
