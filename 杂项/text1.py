#coding=utf-8
for x in range(999999):
	n = x
	z = []
	for i in range(len(str(x))):
		z.append(n%10)
		n = n//10
	s = 0
	for y in z:
		s =s + y**len(str(x))
	if s == x:
		print('%d是水仙花数！' %(x))