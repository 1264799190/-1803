def pp_phone(phone):
	if phone.startswith('1') and len(phone) == 11:
		return True
	else:
		return False
phone = input('请输入手机号')
result = pp_phone(phone)
if result == False:
	#print('手机号错误')

phone2 = input('请输入手机号')
result == pp_phone(phone2)
if result == False:
	#print('手机号错误')


