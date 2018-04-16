def print_num():
	print('学生成绩管理系统'.center(50,'_'))
	print('1.录入成绩'.center(50,' '))
	print('2.查询成绩'.center(50,' '))
	print('3.修改成绩'.center(50,' '))
	print('4.删除成绩'.center(50,' '))
	print('5.打印全部成绩'.center(52,' '))
	print('6.退出系统'.center(50,' '))

def input_fun():
	cards = []
	while True:
		fun_num = int(input('请选择功能'))
		if fun_num == 1:
			add_card()
		elif fun_num == 2:
			find_num()
		elif fun_num == 3:
			up_date()
		elif fun_num == 4:
			del_num()
		elif fun_num == 5:
			all_num()
		else:
			break





print_num()
input_fun()




#def add_card():





#def find_card():





#def update_card():





#def del_card():



#def all_card():



#print_num()
#input_fun()
			
