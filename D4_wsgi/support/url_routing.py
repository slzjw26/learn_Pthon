"""
'/say/(?P<name>[a-z]+)/(?P<id>[0-9]+)/'
'/mur/(?P<name>[a-z]+)/(?P<id>[0-9]+)/', {'id': 1234}
'/cry/(?P<name>[a-z]+)/(?P<id>[0-9]+)/', {'gender': 'female'}
'/old/'
'/new/'
'/time/'
"""

import http
from datetime import datetime
from wsgiref.simple_server import make_server

from url import route


class HttpResponse:

    def __init__(self, body, status_code=None, content_type=None):
        self.body = body.encode()
        if status_code:
            status = [x for x in http.HTTPStatus if x.value == status_code][0]
        else:
            status = http.HTTPStatus.OK
        self.status = '%s %s' % (status.value, status.name)
        self.headers = [
            ('Content-Type', content_type or 'text/plain'),
            ('Content-Length', str(len(self.body))),
        ]


class HttpResponseRedirect:

    def __init__(self, to, status=302):
        self.body = b''
        if status == 302:
            self.status = '302 FOUND'
        elif status == 301:
            self.status = '301 MOVED PERMANENTLY'
        else:
            raise ValueError('invalid redirect code %s' % status)
        self.headers = [('Location', to)]


@route('/say/(?P<name>[a-z]+)/(?P<id>[0-9]+)/')
@route('/mur/(?P<name>[a-z]+)/(?P<id>[0-9]+)/', {'id': 1234})
@route('/cry/(?P<name>[a-z]+)/(?P<id>[0-9]+)/', {'gender': 'female'})
def hello(env, name, id, gender='male'):
    msg = '<%s: id=%s, gender=%s>' % (name, id, gender)
    return HttpResponse(msg)


@route('/old/')
def old_func(env):
    http_host = env['HTTP_HOST']
    to = 'http://%s/new/' % http_host
    return HttpResponseRedirect(to, status=301)


@route('/new/')
def new_func(env):
    msg = 'This is the new page'
    return HttpResponse(msg)


@route('/time/')
def showtime(env):
    now = datetime.now().strftime('current time: %F %T')
    return HttpResponse(now)


def application(env, start_response):
    url = env['PATH_INFO']
    res = route.search(url)
    if not res:
        status = '404 NOT FOUND'
        response_headers = [
            ('Content-Type', 'text/plain'),
            ('Content-Length', '0'),
        ]
        response_body = b''
    else:
        func, args, kargs = res
        response = func(env, *args, **kargs)
        status = response.status
        response_headers = response.headers
        response_body = response.body
    start_response(status, response_headers)
    return [response_body]


if __name__ == '__main__':
    host = 'localhost'
    port = 8000
    print('serving on %s:%s' % (host, port))
    httpd = make_server(host, port, application)
    httpd.serve_forever()
