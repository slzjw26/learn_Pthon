import os
import re
import subprocess as sub
from wsgiref.simple_server import make_server


# 显示本机的CPU 使用状况
def cpu():
    text = sub.getoutput('uptime')
    data = text.replace(',', '').split()[-3:]
    header = ['1min', '5min', '15min']
    matrix = [header, data]
    return html(matrix)


# 显示本机的RAM 使用状况
def ram():
    text = sub.getoutput('free')
    lines = text.splitlines()
    total, used, free, shared, buffers, cached = lines[1].split()[1:7]
    used_real, free_real = lines[2].split()[-2:]
    header = ['total', 'used', 'used(real)', 'free', 'free(real)',
              'shared', 'buffers', 'cached']
    data = [total, used, used_real, free, free_real, shared, buffers, cached]
    return html([header, data])


# 显示本机的文件系统使用状况
def hd():
    text = sub.getoutput('df | tail -n +2')
    data = [line.split() for line in text.splitlines()]
    header = ['Device', '1K-blocks', 'Used', 'Available', 'Use%', 'Directory']
    data.insert(0, header)
    return html(data)


# html output
def html(matrix):
    texts = []
    texts.append('<table>')
    for line in matrix:
        texts.append('<tr>')
        for col in line:
            texts.append('<td>%s</td>' % col)
        texts.append('</tr>')
    texts.append('</table>')
    return ''.join(texts)


def application(env, start_response):
    headers = [('Content-Type', 'text/html')]
    status = '200 OK'
    body = []

    if re.match('/monitor/cpu/?', env['PATH_INFO']):
        body.append(cpu().encode())
    elif re.match('/monitor/ram/?', env['PATH_INFO']):
        body.append(ram().encode())
    elif re.match('/monitor/hd/?', env['PATH_INFO']):
        body.append(hd().encode())
    elif re.match('/monitor/?$', env['PATH_INFO']):
        body.append(b'<h3>==&gt; CPU</h3>')
        body.append(cpu().encode())
        body.append(b'<h3>==&gt; RAM</h3>')
        body.append(ram().encode())
        body.append(b'<h3>==&gt; HD</h3>')
        body.append(hd().encode())
    else:
        status = '404 NOT FOUND'

    content_length = sum(len(x) for x in body)
    headers.append(('Content-Length', str(content_length)))
    start_response(status, headers)
    return body


if __name__ == '__main__':
    host = 'localhost'
    port = 8000
    server = make_server(host, port, application)
    print('serving on http://%s:%s (pid %s)' % (host, port, os.getpid()))
    server.serve_forever()
