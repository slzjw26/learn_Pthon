#!/usr/bin/python3


import os
from wsgiref.simple_server import make_server


def up(env, response):
    status = '200 OK'
    headers = [('Content-Type', 'text/plain')]

    len1 = int(env['CONTENT_LENGTH'])
    ifile = env['wsgi.input']
    ofile = open('/tmp/uploaded', 'wb')
    ofile.write(ifile.read(len1))

    response_body = b''
    headers.append(('Content-Type', str(len(response_body))))

    response(status, headers)
    return [response_body]


if __name__ == '__main__':
    host = 'localhost'
    port = 8000
    print('<pid: %s> serving on http://%s:%s' % (os.getpid(), host, port))
    httpd = make_server(host, port, up)
    httpd.serve_forever()
