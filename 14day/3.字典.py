list = [{"beijing":{"mianji":1290,"renkou":123123},"shanghai":{"mianji":12331,"renkou":123123}}]
def pp():
	for i in list:
	#print(i)
		for k,v in i.items():
		#print(k)
		#print(v)
			for q,e in v.items():
				print(k,q,e)
for i in range(5):
	pp()
