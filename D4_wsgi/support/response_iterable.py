from wsgiref.simple_server import make_server


def application(env, start_response):
    response_body = b'a'
    status = '200 OK'
    response_headers = [
        ('Content-Type', 'text/plain'),
        ('Content-Length', str(len(response_body))),
    ]
    start_response(status, response_headers)
    # return response_body
    return [response_body]


if __name__ == '__main__':
    host = 'localhost'
    port = 8000
    print('serving on %s:%s' % (host, port))
    httpd = make_server(host, port, application)
    httpd.serve_forever()
