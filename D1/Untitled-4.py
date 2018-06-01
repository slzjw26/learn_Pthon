#!/urs/bin/env python
import subprocess as sub
import time

p = sub.Popen(['Python', 'cat.py', '1.goals'], stdout = sub.PIPE)
stdout, stderr = p.communicate()

stdout = stdout.decode()
print(stdout)

time.sleep(10)
