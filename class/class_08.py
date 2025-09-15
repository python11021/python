# 학생 클래스 생성
# 인스턴스 변수 : 이름, 국 영 수
# 인스턴스 메서드 : 총점, 평균, 학점, __str__
class Student:
    def __init__(self,name, kor, eng, math):
        self.name = name 
        self.kor  = kor
        self.eng  = eng
        self.math = math
    
    # 총점
    def total(self):
        return self.kor + self.eng + self.math
    
    def average(self):
        return self.total() / 3
    
    def grade(self):
        avg = self.average()


    def __str__(self):
        return f'이름 : {self.name}, 총점 : {self.total()} 평균 : {self.average()}'    
    


s1 = Student("홍길동", 10,20,30)
s2 = Student("이순신", 50,60,90)

print(s1)
print(s2)
# print(s1.__str__())