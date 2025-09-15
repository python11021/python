# 기본 클래스 생성
class Review:
    # 클래스 변수 생성
    count = 0
    # 생성자 메소드 - 자동 호출. 콜백 함수, 이벤트 함수라고도 함.
    def __init__ (self, name=""):
        self.name = name

# 인스턴스 생성
r1 = Review(100)
r2 = Review(10)
# 인스턴스 변수 변경
r1.name = "첫번째 리뷰"
print(f'r1인스턴스 변수 : {r1.name}')
print(f'클래스 변수     : {Review.count}')   
print(f'클래스 변수     : {r1.tostring()}')      

