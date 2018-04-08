acc = "123456"
pwd = "abc"
q_acc = input('请输入账号')
q_pwd = input('请输入密码')
if q_acc == acc and q_pwd == pwd:
	print('登陆成功')
elif acc != q_acc:
	print('账号错误')
elif pwd != q_pwd:
	print('密码错误')
