def qq():
	print('名片系统'.center(30,'_'))
	print('1:新增名片'.center(30,' '))
	print('2:查看名片'.center(30,' '))
	print('3:修改名片'.center(30,' '))
	print('4:删除名片'.center(30,' '))
	print('5:打印名片'.center(30,' '))
	print('6:退出系统'.center(30,' '))
def pp():
	cards = []
	while True:
		fun_num = int(input('请输入功能'))
		if fun_num == 1:
			add_card()
		elif fun_num == 2:
			find_card()
		elif fun_num == 3:
			xiu_card()
		elif fun_num == 4:
			del_card()
		elif fun_num == 5:
			print_card()
		elif fun_num == 6:
def oo():
	name = input('请输入名字')	
	job = input('请输入职位')
	phone = int(input('请输入手机号'))
	address = input('请输入地址')
	card['name'] = name
	card['job'] = job
	card['phone'] = phone
	card['address'] = address
	cards.append(card)
	print('添加成功')

