def jisuanji(i,w,q):
	if q == '+':
		#return i+w
	elif q == '-':
		#return i-w
	elif q == '*':
		#return i*w
	elif q == '/':
		return (i+w,i-w,i*w,i/w)
i = float(input('请输入一个数字:'))
w = float(input('请输入一个数字:'))
q = input('请输入+—×/:]')
ji = jisuanji(i,w,q)
print(ji)
