# import random

# print(random.randint(1,5))

# 함수정의 def 키워드 사용
# 매개변수(parameter)   : 함수가 전달받는 값
# 인자(Argument)        : 함수를 호출할 때 전달하는 값
# 반환값(Return Value)  : 함수가 작업을 마치고 호출한 곳으로 돌려주는 값 
# return 키워드를 사용.

# 함수의 구성요소
def myCalc(num1,num2):
    '''
    #두 개의 값을 받아서 더하는 기능
        -num1은 숫자
        -num2는 숫자
    '''
    result = num1+num2
    return result

#1. 매개변수와 반환값이 없는 함수
def say_hello():
    print('안녕하세요...')

#2. 매개변수가 있고 반환값이 없는 함수
def say_hello_name(name):
    print(f'{name}님 안녕하세요.')

#3. 매개변수 없고 반환값 있는 함수
import datetime
def get_current_time():
    return datetime.datetime.now()

print('-'*30)
# 위에서 만든 4개의 함수 사용해보기

param_name = '홍길동'

say_hello_name(param_name)

curTime = get_current_time()
print(f'현재 시간은 {curTime}')

say_hello()

plus_num = myCalc(3,5)
print(f'두 수의 합은 {plus_num}')

