class People():
    def __init__(self): #생성자
        self.name = None
        self.age  = None
        self.addr = None
        print('생성자 호출')

print('h1 객체 생성전')
h1 = People()
# print(h1.addr)
print('h1 객체 생성후')
h2 = People()
print(h2.addr)
