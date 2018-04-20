stus = [{"name":"zhangsan", "age":18},{"name":"lisi", "age":19},{"name":"wangwu", "age":17}]


stus.sort(key = lambda a:a['name'])
print(stus)
stus.sort(key = lambda a:a['age'])
print(stus)
#stus.sort(key = lambda x:x['name:age'])
#print(stus)
