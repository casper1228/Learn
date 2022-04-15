import random
a = input('請輸入第一個值: ')
b = input('請輸入第二個值: ')
x = random.randint(int(a), int(b))
print('請輸入範圍 ', a, '-', b, '之間的數字')
count = 0
while True:
    y = input('請輸入數字: ')
    count = int(count) + 1
    y = int(y)
    if x == y:
        print('恭喜猜對，總共猜了 ', count, '次')
        break
    elif x < y:
        print('猜錯答案比數字小')
    elif x > y:
        print('猜錯答案比數字大')
    print('這是你猜的第 ', count, '次')
