list = []
while True:
	
	#输入

	dict = {}
	name = input('请输入你的名字')
	age = int(input('请输入你的年龄'))
	sex = input('请输入你的性别')
	qq = int(input('请输入你的qq'))
	weight = float(input('请输入你的体重'))
	
	#字典赋值

	dict['name'] = name
	dict['age'] = age
	dict['sex'] = sex
	dict['qq'] = qq
	dict['weight'] = weight
	
	#list = [{}]
	#int float str bool list tuple dictionary

	list.append(dict)
	print(list)

#遍历

for i in list:
	print(i)
