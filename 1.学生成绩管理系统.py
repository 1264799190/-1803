def print_function():
	print('学生成绩管理系统'.center(50,'_'))
	print('1.录入成绩'.center(50,' '))
	print('2.查询成绩'.center(50,' '))
	print('3.修改成绩'.center(50,' '))
	print('4.删除成绩'.center(50,' '))
	print('5.打印全部成绩'.center(52,' '))
	print('6.退出系统'.center(50,' '))
cards = []
def input_fun():
	while True:
		fun_num = int(input('请选择功能'))
		if fun_num == 1:
			add()
		elif fun_num == 2:
			inquire()
		elif fun_num == 3:
			amend()
		elif fun_num == 4:
			del_num()
		elif fun_num == 5:
			all_num()
		else:
			break

#print('录入')
def add():
		name = input('请输入学生姓名:')
		flag = 0
		card = {}
		hao = int(input('请输入学号'))
		for temp in cards:
			if hao == temp['hao']:
				flag = 1
				break
		if flag == 1:
			print('学号重复')
			return
		yufen = float(input('请输入语文分数'))
		shufen = float(input('请输入数学分数'))
		yingfen = float(input('请输入英语分数'))
		card['name'] = name
		card['hao'] = hao
		card['yufen'] = yufen
		card['shufen'] = shufen
		card['yingfen'] = yingfen
		cards.append(card)
		print('录入成绩成功')
		for i in cards:
			print(i)


#print('查询')
def inquire():
	flag = 0
	hao = int(input('请输入你要查询的学号'))
	for temp in cards:
		if hao == temp['hao']:
			flag = 1
			print('姓名%s\n学号%s\n语文分数%0.2f\n数学分数%0.2f\n英语分数%0.2f\n'%(temp['name'],temp['hao'],temp['yufen'],temp['shufen'],temp['yingfen']))
			break
	if flag == 0:
		print('没有此学号') 


#print('修改')
def amend():

		hao = int(input('请输入你要修改的学号'))
		for temp in cards:
			if hao == temp['hao']:
				print('1:修改姓名')
				print('2:修改学号')
				print('3:修改语文分数')
				print('4:修改数学分数')
				print('5:修改英语分数')
				p_num = int(input('请输入序号'))
				if p_num == 1:
					name = input('请输入新的姓名')
					temp['name'] = name
				elif p_num == 2:
					hao = int(input('请输入新的学号'))
					temp['hao'] = hao
				elif p_num == 3:
					yufen = float(input('请输入新的语文分数'))
					temp['yufen'] = yufen
				elif p_num == 4:
					shufen = float(input('请输入新的数学分数'))
					temp['shufen'] = shufen
				elif p_num == 5:
					yingfen = float(input('请输入新的英语分数'))
					temp['yingfen'] = yingfen
					print('修改成功')


#print('删除')
def del_num():
		hao = int(input('请输入要删除的学号'))
		flag = 1
		for temp in cards:
			if hao == temp['hao']:
				flag = 1
				cards.remove(temp)
				print('删除成功')
				break
			else:
				print('没有此学号')


#print('打印')
def all_num():
		print('hao\tname\tyufen\tshufen\tyingfen')
		for temp in cards:
			print('%d\t%s\t%0.2f\t%0.2f\t%0.2f\t'%(temp['hao'],temp['name'],temp['yufen'],temp['shufen'],temp['yingfen']))


print_function()
input_fun()
