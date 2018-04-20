list = [1,5,9,11,15,19,23]
key = 15
center = int(len(list)/2)
if key in list:
	while True:
		if list[center] > key:
			center = center - 1
		elif list[center] < key:
			center = center + 1
		elif list[center] == key:
			print('数字是%d,索引是%d'%(key,center))
			break

