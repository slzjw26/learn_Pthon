import re
from subprocess import getstatusoutput

from wsgiref.simple_server import make_server


class url:

    mapping = []

    def __init__(self, path_info):
        self.path_info = path_info

    def __call__(self, func):
        url.mapping.append((self.path_info, func))
        return func


@url('/cpu')
@url('/cpu/')
def cpu(env):
    msg = '0.95 0.80 0.67'
    return msg


@url('/ram')
def ram(env):
    msg = 'Mem: 7847 3677 4169 75 392 1613'
    return msg


@url('/hd/([^/]+)/([^/]+)/?')
def hd(env, dir, fmt):
    if fmt == 'byte':
        cmd = 'df -B1 /%s' % dir
    else:
        cmd = 'df -h /%s' % dir
    msg = getstatusoutput(cmd)[-1]
    msg = msg.splitlines()[-1]
    return msg


@url('/.*')
def w(env):
    msg = 'online users: 3'
    return msg


def find_view(real_path):
    for path_pattern, func in url.mapping:
        m = re.match(path_pattern, real_path)
        if m:
            args = m.groups()
            kargs = m.groupdict()
            return func, args, kargs


def application(env, start_response):
    path_info = env['PATH_INFO']
    func, args, kargs = find_view(path_info)
    msg = func(env, *args, **kargs)

    lines = [msg.encode() + b'\n\n']
    for k, v in env.items():
        line = '%s: %s\n' % (k, v)
        lines.append(line.encode())

    length = sum(len(x) for x in lines)
    status = '200 OK'
    response_headers = [
        ('Content-Type', 'text/plain'),
        ('Content-Length', str(length)),
    ]
    start_response(status, response_headers)
    return lines


if __name__ == '__main__':
    host = 'localhost'
    port = 8000
    print('serving on %s:%s' % (host, port))
    httpd = make_server(host, port, application)
    httpd.serve_forever()
