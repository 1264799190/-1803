dict = {'name':'小明','age':20,'sex':'男'}

for i in dict:
	print(i)
	print(dict.get(i))
print('*'*30)

for i in dict.keys():
	print(i)
	print(dict.get(i))
print('*'*30)

for i in dict.values():
	print(i)
print('*'*30)

for k,v in dict.items():
	print('%s的值是%s'%(k,v))
