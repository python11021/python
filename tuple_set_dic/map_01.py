# map 자료구조의 각 요소에 특정 함수를 적용
str_numbers = ['1','10','100']

print(str_numbers)
print(list(map(int,str_numbers)))

int_numbers = [1, 10, 100]
print(list(map(str,int_numbers)))

scores = input('국어 영어 수학 점수를 공백을 기준으로 입력하세요.')
scores = scores.split()
kor,eng,math =  map(int,scores)

print(kor,eng,math)

list_2 = [10,20,30]

# 각 원소에 x2

print(list(map(lambda x:x*2,list_2))) 