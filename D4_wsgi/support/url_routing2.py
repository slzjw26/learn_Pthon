import re
from datetime import datetime
from wsgiref.simple_server import make_server


def showtime(env, format='iso', zone=''):
    now = datetime.now()
    if format == 'rfc2822':
        fmt = '%a, %d %b %Y %H:%M:%S %z'
    else:
        fmt = '%F %T'

    time_text = now.strftime('current time: ' + fmt)
    time_text = time_text + '\nZone: %s' % zone
    time_text = time_text.encode()

    status = '200 OK'
    headers = [('Content-Type', 'text/plain'),
               ('Content-Length', str(len(time_text)))]
    return status, headers, time_text


def find_worker(path):
    for url in url_patterns:
        m = url.match(path)
        if m:
            args = ()
            kwargs = m.groupdict()
            kwargs = {k: v for k, v in kwargs.items() if v}
            if kwargs:
                kwargs.update(url.kwargs)
            else:
                args = m.groups()
            return url.func, args, kwargs


def application(env, start_response):
    url = env['PATH_INFO']
    worker = find_worker(url)      # 找出响应函数

    if not worker:
        status = '404 NOT FOUND'
        response_headers = [
            ('Content-Type', 'text/plain'),
            ('Content-Length', '0'),
        ]
        response_body = b''
    else:
        func, args, kwargs = worker
        status, response_headers, response_body = func(env, *args, **kwargs)
    start_response(status, response_headers)
    return [response_body]


class url:

    def __init__(self, pattern, func, kwargs={}):
        self.pattern = pattern
        self.func = func
        self.kwargs = kwargs

    def match(self, path):
        return re.match(self.pattern, path)


# url 与响应函数之间的映射关系
url_patterns = [
    url(r'/time/(?P<format>[a-z0-9]+)/$', showtime),
    url(r'/time2/(?P<format>[a-z0-9]+)/$', showtime, kwargs={'format': 'iso'}),
    url(r'/time3/([a-z0-9]+)/(?:(?P<zone>[a-z]+)/)?$', showtime),
]


if __name__ == '__main__':
    host = 'localhost'
    port = 8000
    print('serving on http://%s:%s' % (host, port))
    httpd = make_server(host, port, application)
    httpd.serve_forever()
