acc = '12345'
pwd = '123'
i = 1
while i <= 3:
	w_acc = input('请输入账号')
	w_pwd = input('请输入密码')
	if w_acc == acc and w_pwd == pwd:
		hero = print(input('0---ADC 1---肉 3---法师'))
		if hero == '0':
			print('鲁班')
		elif hero == '1':
			print('程咬金')
		elif hero == '3':
			print('王昭君')
		break
	else: 
		print('登陆错误，请重新输入')
		w_acc = print('请输入账号')
		w_pwd = print('请输入密码')
	if w_acc != acc and w_pwd != pwd:
		i+=1
	
	
