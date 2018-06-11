#!/usr/bin/python3
#

import sys
import os


def response(headers, body):
    for h in headers:
        print(h)
    print()
    for b in body:
        sys.stdout.write(b)


if __name__ == '__main__':
    ifile = os.fdopen(sys.stdin.fileno(), 'rb')
    ifile.readline()            # 第一行，丢弃
    line = ifile.readline()     # 第二行，用来取出文件名
    ifile.readline()            # 第三行，丢弃

    # 取出文件名，打开文件用来写
    fname = line.split(b'"')[-2].decode()
    ofile = open('/tmp/%s' % fname, 'wb')

    old_chunk = b''
    bs = 4096

    while True:
        chunk = ifile.read(bs)
        if len(chunk) < bs:             # 文件中读取完毕
            chunk = old_chunk + chunk
            if chunk:
                lines = chunk.splitlines(keepends=True)
                del lines[-1]
                if lines:
                    lines[-1] = lines[-1][:-2]
                    ofile.writelines(lines)
            break
        else:                           # 文件中还有未读的内容
            ofile.write(old_chunk)
            old_chunk = chunk

    headers = []
    headers.append('Content-Type: text/plain')
    response(headers, ['ok'])
