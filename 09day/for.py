while trun
	w = int(input('请输入一个数字:'))
	a = int(input('请输入一个数字:'))
	sum = 0 
	if w < a:
		for i in range(w,a+1):
			print(i)
			sum = sum+1
		print(sum)
		break
	else:
		print('输入有误')
	
	
