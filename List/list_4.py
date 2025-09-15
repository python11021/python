# 랜덤 라이브러리 가져오기
import random

# 랜덤 라이브러리 중에서 sample 함수를 호출
# range(100) 0~99 범위에서 중복되지 않은 랜덤한 5개 출력
random_numbers = random.sample(range(100),5)
print(random_numbers)

# 0에서 10사이의 숫자 중 랜덤하게 한개 생성
random_int = random.randint(0,10)

random_numbers.append(random_int)

# 50이 있는지
print(50 in random_numbers)
print(random_numbers)

print('-'*50)

# 삭제
del random_numbers[0] # 삭제한 값을 알 수 없음.
print(random_numbers)

pop_num = random_numbers.pop(0) # 삭제한 값을 알려줌

print(pop_num)



# del list_a[1]

# print(list_a)

# list_a.pop(2)
