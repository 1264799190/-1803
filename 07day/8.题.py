acc = "123456"
pwd = "1234"
money = 100000
q_acc = input('请输入账号')
q_pwd = input('请输入密码')
if 'q_acc == acc and q_pwd == pwd':
	q_money = float(input('取钱金额'))
	if q_money <= money:
		print('已取金额%f,剩余金额%f'%(money,money-q_money))
	else:
		print('钱')
else:
	print('非法账户')

