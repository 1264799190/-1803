def qq(i,q):
	for i in range(1,10):
		for q in range(1,i+1):
			print('%d*%d=%d'%(q,i,i*q),end = '\t')
		print('')
qq(i,q)
