print('名片系统'.center(20,'*'))
print('1.新增名片'.center(20,' '))
print('2.查看名片'.center(20,' '))
print('3.修改名片'.center(20,' '))
print('4.删除名片'.center(20,' '))
print('5.退出系统'.center(20,' '))
cards = []
while True:
	fun_number = int(input('请输入功能'))
	if fun_number == 1:
		#print('新增')
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
		print('添加成功')
		for w in cards:
			print(w)
		print('*'*40)



	elif fun_number == 2:
		#print('查看')	
		name = input('请输入姓名')
		flag = 0
		count = 0
		for temp in cards:
			count+=1
			if name == temp['name']:
				flag = 1
				break
		if flag == 0:
			print('查无此人')
		else:
			print('姓名%s\n手机号码%s\n地址%s\n职位%s\n'%(cards[count -1]['name'],cards[count -1]['phone'],cards[count -1]['address'],cards[count -1]['jod']))
		print('*'*40)



	elif fun_number == 3:
		#print('修改')
		name = input('请输入修改名字')
		for temp in cards:
			if name == temp['name']:
				print('1.修改名字'.center(30,' '))
				print('2.修改电话号码'.center(32,' '))
				print('3.修改地址'.center(30,' '))
				print('4.修改职位'.center(30,' '))
				ch_num = int(input('请输入修改序号'))
				if ch_num == 1:
					name = input('请输入新的名字')
					temp['name'] = name
				elif ch_num == 2:
					phone = input('请输入新的手机号码')
					temp['phone'] = phone
				elif ch_num == 3:
					address = input('请输入新的地址')
					temp['address'] = address
				elif ch_num == 4:
					jod = input('请输入新的职位')
					temp['jod'] = jod
					print('输入成功')
				else:
					print('输入有误')
				


	elif fun_number == 4:
		#print('删除')
		name = input('请输入删除姓名')		
		flag = 0
		for temp in cards:
			if name == temp['name']:
				flag = 1
				cards.remove(temp)
				print('删除成功')
				break
		else:
			print('没有此人')
		print('*'*40)



	else:
		print('退出系统')
		break
