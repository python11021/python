# 가변 매개변수
    # 함수 정의할 때, 매개변수의 개수를 지정하지 않습니다.
    #  함수 내부에서는 리스트로 간주합니다.
    # 함수를 호출하는 쪽에서는 편안하게.. 1,2,3,4 or 1,2,3,4,5,1,4,5

def myFunc1(*args): # *: list로 묶어줌(packing)
    for i in args:
        print(i)

myFunc1(10,20,30,50)

def myFunc2(args):
    for i in args:
        print(i)

myFunc2([10,20,30,50])

#  unpacking
a,b = [10,20]
print(f'a = {a}')
print(f'b = {b}')