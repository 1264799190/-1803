print('名片系统'.center(20,'*'))
print('1.新增名片'.center(20,' '))
print('2.查看名片'.center(20,' '))
print('3.修改名片'.center(20,' '))
print('4.删除名片'.center(20,' '))
cards = []
while True:
	fun_number = int(input('请输入功能'))
	if fun_number == 1:
		print('新增')
		flag = 0
		card = {}
		name = input('请输入你的姓名')
		for temp in cards:
			if name == temp['name']:
				flag = 1
				break
		if flag == 1:
			print('名字重了')
			continue


		phone = input('请输入你的电话号码')
		address = input('请输入你的地址')
		jod = input('请输入你的职位')

		card['name'] = name
		card['phone'] = phone
		card['address'] = address
		card['jod'] = jod
		cards.append(card)




	elif fun_number == 2:
		print('查看')
	elif fun_number == 3:
		print('修改')
	elif fun_number == 4:
		print('删除')
