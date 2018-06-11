from wsgiref.simple_server import make_server
from urllib.parse import parse_qs
from html import escape

html = """
<html>
<body>
  <form method="get" action="">
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

    # parse_qs 返回一个字典，其中的值是列表
    d = parse_qs(env['QUERY_STRING'])

    # 因为一个key对应的值是一个列表，所以默认值使用了一个列表
    age = d.get('age', [''])[0]
    hobbies = d.get('hobbies', ['No Hobbies?'])

    # 应该总是对来自用户的数据做转义，以防止代码注入
    age = escape(age)
    hobbies = [escape(hobby) for hobby in hobbies]

    # 把内容填充到上面的模板字符串中
    pairs = {}
    if 'software' in hobbies:
        pairs['checked-software'] = 'checked'
    else:
        pairs['checked-software'] = ''
    if 'tunning' in hobbies:
        pairs['checked-tunning'] = 'checked'
    else:
        pairs['checked-tunning'] = ''
    pairs['age'] = age or 'Empty'
    pairs['hobbies'] = ', '.join(hobbies)

    response_data = html % pairs
    response_data = response_data.encode()

    status = '200 OK'
    response_headers = [
        ('Content-Type', 'text/html'),
        ('Content-Length', str(len(response_data)))
    ]

    start_response(status, response_headers)
    return [response_data]


if __name__ == '__main__':
    host = 'localhost'
    port = 8000
    print('serving on %s:%s' % (host, port))
    httpd = make_server(host, port, application)
    httpd.serve_forever()
