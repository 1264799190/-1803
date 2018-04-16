def big_year(year):
	if (year%4 == 0 and year%100 != 0) or (year%400 == 0):
		print('yes')
	else:
		print('no')
year = int(input('请输入年份'))
big_year(year)
