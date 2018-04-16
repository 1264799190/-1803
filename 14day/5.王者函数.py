list = []
def qq():
	i = input('请输入英雄')
	list.append(i)
while True:
	qq()
	if len(list) == 5:
		print(list)
		break
