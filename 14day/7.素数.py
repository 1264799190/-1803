def sushu():
	for i in range(100,201):
		foag = 0
		for q in range(2,i):
			if i % q == 0:
				foag = 1
				break
		if foag == 0:
			print(i)
sushu()
