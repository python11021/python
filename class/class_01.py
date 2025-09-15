# 클래스 변수 VS 인스턴스 변수

class StudentMsg:
    name = '홍길동' # 클래스 변수

class StudentMsg():
    name = '홍길동'
    
s1 = StudentMsg()
s2 = StudentMsg()
s3 = StudentMsg()

s1.name ='이순신'

s2.name='가나다'
StudentMsg.name='강감찬'
s1.age  =20
StudentMsg.name='TEST'
s2.name='라마바'
print(s1.name, s2.name, s3.name)

# 클래스 변수는 모든 객체가 참조하는 변수
# but 객체가 변수를 재 할당받으면 해당 객체는 더 이상 참조하지 않는다.

# print(s1.age)

# print(s1.name)