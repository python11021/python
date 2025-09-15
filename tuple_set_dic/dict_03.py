# 딕셔너리의 생성
# dict_a = {'국어':99,'수학':80,'영어':70}
dict_a = dict([['국어',99],['영어',80],['수학',70],['사회',[100,20]]])
# 딕셔너리에서 값을 출력
print(dict_a)
# 딕셔너리에서 값을 추가
dict_a['과학'] = 77 
print(dict_a)
# 딕셔너리 삭제
del dict_a['영어']
print(dict_a)
# 딕셔너리 특정 키의 데이타를 수정
dict_a['수학'] = 100
print(dict_a)
# enumerate, zip(), .items() .keys() .values()
# map(), 함수의 파라메터 - 키워드 파라메터, 가변 키워드 파라메터

my_bag = {'필통':'파란색','공책':'수학공책','지갑':'분홍색'}
# 출력
print(my_bag)
# 가방에서 필통을 꺼내 출력
print(f"가방 -- {my_bag['필통']}")
# 가방에서 공책을 꺼내서 출력
print(f"가방 -- {my_bag['공책']}")
# 지갑이 오래되서 '가죽지갑' 변경 
my_bag['지갑'] = '가죽지갑'
print(f"my_bag['지갑' --- {my_bag['지갑']}]")
# 물통을 추가 하얀색
my_bag['물통'] = '하얀색'
# 공책을 다써서 버려
del my_bag['공책']

for i in my_bag:
    print(f'i === {my_bag[i]}')