arr = [n for n in open('inp2')]
dw = h = ai = fw = 0

for i in arr:
	f,s = i.split()
	s = int(s)
	if f == 'forward':
		fw += s
		dw += ai * s
	elif f == 'up':
		#dw -= s
		ai -= s
	else:
		ai += s
		#dw += s
#print(h * dw)
print(fw * dw)