# 다양한 매개변수
#   기본 매개변수 default

def myadd(num1, num2=0):
    return num1+num2

result = myadd(10,20)
print(f'result = {result}')

result = myadd(10)
print(f'result = {result}')