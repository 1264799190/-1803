list = []

def register():
	account = input('请输入账号')
	pwd = input('请输入密码')
	flag = 0
	for i in list:
		if account == i['account']:
			print('账号已存在')
			flag = 1
			break
	if flag == 0:
		dict = {}
		dict['account'] = account
		dict['pwd'] = pwd
		list.append(dict)
		print('成功')

def login():
	account = input('请输入账号')
	pwd = input('请输入密码')
	flag = 0
	for i in list:
		if account == i['account']:
			if i.get('status') == 1:
				print('账号在登录着')
			else:
				if pwd == i[pwd]:
					print('登录成功')
					i['status'] = 1
				else:
					print('登录失败')
			flag = 1
			break
	if flag == 0:
		print('账号不存在，请先注册')


def loginout():	
	account = input('请输入账号')
	pwd = input('请输入密码')
	flag = 0
	for i in list:
		if account == i['account']:
			if i.get('status') == 1:
				print('账号退出成功')
				i.get('status') == 0
			else:
				print('账号根本没登录')
			flag = 1
			break
		if flag == 0:
			print('账号不存在')
while True:
	fun = int(input('请选择功能 1注册 2登录 3登出 4退出'))
	if fun == 1:
		register()
	elif fun == 2:
		login()
	elif fun == 3:
		loginout()
