id_card = {'name':'王晓俊','age':18,'sex':'男','group':'汉'}
print(id_card)
print('*'*80)

id_card['address'] = '北京市'
id_card['merry'] = '单身'
print(id_card)
print('*'*80)

id_card.pop('merry')
print(id_card)
print('*'*80)

id_card['name'] = '张晨波'
print(id_card)
print('*'*80)

print(id_card['name'])
print(id_card)
print('*'*80)

id_card2 = {'name','group'}
id_card.update(id_card)
print(id_card2)
print('*'*80)

print(id_card.keys())
print('*'*80)

print(id_card.values())
print('*'*80)

print(id_card.items())
print('*'*80)
