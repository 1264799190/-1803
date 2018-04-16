def jisuanji(i,w,q):
	if q == '+':
		print(i+w)
	elif q == '-':
		print(i-w)
	elif q == '*':
		print(i*w)
	elif q == '/':
		print(i/w)
i = float(input('请输入一个数字'))
w = float(input('请输入一个数字'))
q = input('请输入+—×/')
jisuanji(i,w,q)
