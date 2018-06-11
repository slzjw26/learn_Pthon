import os
from wsgiref.simple_server import make_server
from cgi import FieldStorage


def application(env, start_response):
    l = int(env['CONTENT_LENGTH'])
    ifile = env['wsgi.input']
    ofile = open('/tmp/uploaded', 'wb')
    ofile.write(ifile.read(l))

    response_body = b''
    status = '200 OK'
    response_headers = [
        ('Content-Type', 'text/html'),
        ('Content-Length', str(len(response_body)))
    ]

    start_response(status, response_headers)
    return [response_body]


if __name__ == '__main__':
    host = 'localhost'
    port = 8000
    print('<pid: %s> serving on %s:%s' % (os.getpid(), host, port))
    httpd = make_server(host, port, application)
    httpd.serve_forever()
