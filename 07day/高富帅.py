shenjia = float(input('请输入你的身价'))
fice = int(input('请输入你的颜值分'))
height = float(input('请输入你的身高'))
if height > 180 and money >100000 and fice > 99:
	print('高富帅')
elif shenjia > 100000 and fice > 99:
	print('富帅')
elif fice > 99:
	print('帅')
elif height < 160 and shenjia <100 and fice < 60:
	print('矮穷矬')
