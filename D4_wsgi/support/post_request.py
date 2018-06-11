from wsgiref.simple_server import make_server
from urllib.parse import parse_qs
from html import escape

html = """
<html>
<body>
  <form method="post" action="">
    <p>Age: <input type="text" name="age" value="%(age)s"></p>
    <p>Hobbies:
      <input name="hobbies" type="checkbox" value="software"
        %(checked-software)s> Software
      <input name="hobbies" type="checkbox" value="tunning"
        %(checked-tunning)s> Auto Tunning
    </p>
    <p>
      <input type="submit" value="Submit">
    </p>
  </form>
  <p>
    Age: %(age)s<br>
    Hobbies: %(hobbies)s
  </p>
</body>
</html>
"""

def application(env, start_response):

    # CONTENT_LENGTH 可能为空或者不存在，因此放到try中
    try:
        request_body_size = int(env.get('CONTENT_LENGTH', 0))
    except ValueError:
        request_body_size = 0

    # 当方法为POST时，提交的变量将会通过http的请求体来传输
    # http请求体是一个类似文件的对象，WSGI服务器把对此对象
    # 的引用放到环境字典中，key是wsgi.input
    # 读出来的数据是字节串，需要解码
    request_body = env['wsgi.input'].read(request_body_size)
    d = parse_qs(request_body.decode())

    # 因为一个key对应的值是一个列表，所以默认值使用了一个列表
    age = d.get('age', [''])[0]
    hobbies = d.get('hobbies', [])

    # 应该总是对来自用户的数据做转义，以防止代码注入
    age = escape(age)
    hobbies = [escape(hobby) for hobby in hobbies]

    response_body = html % {
        'checked-software': ('', 'checked')['software' in hobbies],
        'checked-tunning': ('', 'checked')['tunning' in hobbies],
        'age': age or 'Empty',
        'hobbies': ', '.join(hobbies or ['No Hobbies?'])
    }
    response_body = response_body.encode()

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
    print('serving on %s:%s' % (host, port))
    httpd = make_server(host, port, application)
    httpd.serve_forever()
