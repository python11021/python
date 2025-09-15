for i in range(5):
    print(i)

def say_hello(name):
    return f'{name}님 반가워요'

name = '홍길동'
result = say_hello(name)
print(result)

print(__file__)
print(__name__)