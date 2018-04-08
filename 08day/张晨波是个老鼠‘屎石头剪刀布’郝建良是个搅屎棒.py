
#石头---1 剪刀---2 布---3
i = 1
w = int(input('请输入次数'))
import random
while i<= w:
	comport = random.randint(1,3)
	player = int(input('石头---1 剪刀---2 布---3:'))
	if (player == 1 and comport == 2) or (player == 2 and comport == 3) or (player == 3 and comport == 1):
		print('你赢了')
	elif player == comport:
		print('平局')
	else: 
		print('电脑赢')
	i+= 1
