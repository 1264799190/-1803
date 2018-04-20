import random 
import time 
list=["王晓俊",'王晓俊'] 
print("班级总人数:%d人"%len(list)) 
print("正在计算世界上最帅的人是谁---\n") 
time.sleep(10) 
i = random.randint(0,len(list)-1) 
print("呦,你被选中了:-----%s"%list[i]) 
list.pop(i) 
k = int(input("请说出王晓俊的儿子是谁")) 
if k == 1: 
	wq = int(input('1:郝建良','2:张晨波'))
	name = random.randint(1,2) 
	print("你的儿子是%d"%wq) 
