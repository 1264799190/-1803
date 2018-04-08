number = int(input('请输入年份'))
if number%4 == 0 and number%100 != 0:
	print('闰年')
elif number%400 == 0: 
	print('闰年')
else:
	print('平年')
