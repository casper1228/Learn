# 完成2022/04/12
height = input('請輸入身高: ')
weight = input('請輸入體重: ')
bmi = float(weight)/(float(height)/100) ** 2
if bmi < 18.5:
    print('你身高: ', height)
    print('你體重: ', weight)
    print('你體重過輕BMI只有: ', bmi)
elif bmi >= 18.5 and bmi < 24:
    print('你身高: ', height)
    print('你體重: ', weight)
    print('你體重正常BMI: ', bmi)
elif bmi >= 24 and bmi < 27:
    print('你身高: ', height)
    print('你體重: ', weight)
    print('你體重過重BMI: ', bmi)
elif bmi >= 27 and bmi < 30:
    print('你身高: ', height)
    print('你體重: ', weight)
    print('你已經輕度肥胖BMI: ', bmi)
elif bmi >= 30 and bmi < 35:
    print('你身高: ', height)
    print('你體重: ', weight)
    print('你已經中度肥胖BMI: ', bmi)
elif bmi >= 35:
    print('你身高: ', height)
    print('你體重: ', weight)
    print('你重度肥胖死肥仔BMI: ', bmi)
