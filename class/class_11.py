# isinstance() 함수
# 객체가 특정 클래스의 인스턴스(객체)인지 확인하는데 사용됩니다.
# 사용하는 이유
# 1.타입 확인: 함수나 메서드가 특정 클래스의 인스턴스를 기대할 때, 이를 확인합니다.
# 1.다형성 지원: 상속 관계에 있는 클래스들 간에 공통된 인터페이스를 제공할 
class Student:
    def study(self):
        return "공부 중입니다."

class Teacher:
    def teach(self):
        return "가르치는 중입니다."

# 리스트에 어떤 객체가 있는지 모르는 경우
peoples = [Student(), Teacher(), Student() ]
del peoples[0]
if isinstance(peoples[0], Student):
    print(peoples[0].study())
else:
    print(peoples[0].teach())