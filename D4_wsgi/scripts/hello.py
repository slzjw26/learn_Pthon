import re
from wsgiref.simple_server import make_server


def app(env, callback):
    callback('200 OK', [('Content-Type', 'text/plain')])
    return [b'Hello wsgi world.']


def showenv(env, start_response):
    headers = [('Content-Type', 'text/plain'),
               ('Set-Cookie', 'name=charlie;'),
               ('Set-Cookie', 'age=18;')]
    start_response('200 OK', headers)
    body = []
    for k, v in env.items():
        line = '%s: %s\n' % (k, v)
        body.append(line.encode())

    return body


def monitor(env, start_response):
    headers = [('Content-Type', 'text/plain')]
    status = '200 OK'
    body = []

    #if env['PATH_INFO'].startswith('/cpu'):
    if re.match('/cpu/?', env['PATH_INFO']):
        body.append(b'cpu')
    elif env['PATH_INFO'].startswith('/ram'):
        body.append(b'ram')
    elif env['PATH_INFO'].startswith('/hd'):
        body.append(b'hd')
    else:
        status = '404 NOT FOUND'

    start_response(status, headers)
    return body


if __name__ == '__main__':
    host = 'localhost'
    port = 8000
    server = make_server(host, port, showenv)
    server.serve_forever()
