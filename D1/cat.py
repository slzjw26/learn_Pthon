import os
import sys

bs = 4096
src = sys.argv[1]
ifile = open(src, 'rb')
ofile = os.fdopen(sys.stdout.fileno(), 'wb')

while True:
    chunk = ifile.read(bs)
    if not chunk:
        break
    ofile.write(chunk)

ifile.close()
ofile.close()

