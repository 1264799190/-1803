i = 1 
oi = 0
ji = 0
while i<= 100:
	if i%2 == 0:
		oi+= i
	else:
		ji+= i
	i+= 1

print('偶数和是%d'%oi)
print('基数和是%d'%ji)	
