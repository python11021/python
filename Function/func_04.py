# 다양한 매개변수
#   기본 매개변수 default

def myadd(num1=0, num2=0, num3=0):
    return num1+num2+num3

result = myadd(10,20)
print(f'result = {result}')

result = myadd(10)
print(f'result = {result}')

result1 = myadd()
result2 = myadd(1)
result3 = myadd(1,2)
result4 = myadd(1,2,3)
print(result1,result2,result3,result4)
