list = [13,6,10,21,30,50,4,89,2]
for i in range(len(list)):
	for w in range(i+1,len(list)):
		if list[i] > list[w]:
			list[i],list[w] = list[w],list[i]
print(list)
key = 4
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
