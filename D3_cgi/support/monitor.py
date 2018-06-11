#!/usr/bin/python3
#
# 显示本机的CPU/RAM/HD使用状况
#
import os
import subprocess as sub


# 显示本机的CPU 使用状况
def cpu():
    text = sub.getoutput('uptime')
    data = text.replace(',', '').split()[-3:]
    header = ['1min', '5min', '15min']
    matrix = [header, data]
    pretty_output(matrix)


# 显示本机的RAM 使用状况
def ram():
    text = sub.getoutput('free')
    lines = text.splitlines()
    total, used, free, shared, buffers, cached = lines[1].split()[1:7]
    used_real, free_real = lines[2].split()[-2:]
    header = ['total', 'used', 'used(real)', 'free', 'free(real)',
              'shared', 'buffers', 'cached']
    data = [total, used, used_real, free, free_real, shared, buffers, cached]
    pretty_output([header, data])


# 显示本机的文件系统使用状况
def hd():
    text = sub.getoutput('df | tail -n +2')
    data = [line.split() for line in text.splitlines()]
    header = ['Device', '1K-blocks', 'Used', 'Available', 'Use%', 'Directory']
    data.insert(0, header)
    pretty_output(data)


# column output
def column(matrix):
    lens = [max(len(col) for col in cols) for cols in zip(*matrix)]
    margin = 2
    for line in matrix:
        for l, col in zip(lens, line):
            fmt = '%%-%ds' % (l + margin)
            print(fmt % col, end='')
        print()


# html output
def html(matrix):
    print('<table>')
    for line in matrix:
        print('<tr>')
        for col in line:
            print('<td>', col, '</td>', sep='')
        print('</tr>\n')
    print('</table>')


if __name__ == '__main__':
    ct = 'text/html'

    # pretty output
    def pretty_output(matrix, ct=ct):
        if ct == 'text/plain':
            column(matrix)
        elif ct == 'text/html':
            html(matrix)

    print("Content-Type: %s\n\n" % ct, end='')
    qs = os.getenv('QUERY_STRING', '')
    if 'cpu' in qs:
        cpu()
    elif 'ram' in qs:
        ram()
    elif 'hd' in qs:
        hd()
    else:
        print('<h3>===> CPU</h3>')
        cpu()
        print('<h3>\n===> RAM</h3>')
        ram()
        print('<h3>\n===> HD</h3>')
        hd()
