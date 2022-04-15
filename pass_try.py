password = 'a123456'
x = 3
while x > 0:
    pa = input('請輸入密碼: ')
    x = x - 1
    if password == pa:
        print('恭喜密碼正確成功登出')
        break
    elif password != pa:
        print('密碼錯誤!還有', x, '次機會')
