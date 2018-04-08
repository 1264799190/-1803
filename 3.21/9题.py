account = input('请输入你的账号')
password = input('请输入密码')
nick_name = input('请输入姓名')
money = 2000000#价格
need_money = input('请输入你要提取的金额')
sum = money - int(need_money)
print('账号:%s\n密码\n姓名:%s\n价格%s\n提取金额为%s\n剩余%s'%(account,nick_name,money,need_money,sum))
