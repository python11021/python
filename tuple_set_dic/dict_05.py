# 선거시스템
# 유권자들은 기호로 투표 진행
# ex 1,2,3
# 투표는 순환문을 이용해서 유권자가 10이라면 10번 순환하면서 후보자(1~5) 선택
# [1,1,2,3,4,1,5,1]
# 리스트에 있는 각 번호의 횟수를 구해서 당선자를 출력
import random

candidate = ['홍길동','이순신','강감찬','율곡','신사임당']
vote = [] # [1, 2, 3, 4, 1, 2, 3, 4, 5, 1]
counts = 10

for i in range(counts):
    vote_result = int(input('투표를 하세요(1~5) : '))
#   validation 체크
    # if not vote_result.is
    # random_vote = random.randint(1,5) # 1~5 중 랜덤하게 뽑기

    vote.append(vote_result)    # 투표 결과 담기

vote_count = tuple(vote)

# print(vote_count.count(1))

candidate = dict( [ ['홍길동',vote_count.count(1)],['이순신',vote_count.count(2)],['강감찬',vote_count.count(3)],['율곡',vote_count.count(4)],  ['신사임당',vote_count.count(4)]     ] )

print(f'candidate == {candidate}')
# for i in vote:

# 키의 값을 가져올 때.. 딕셔너리 변수['키값']
# 딕셔너리변수.get('키값') 없으면 None

print(max(candidate,key=candidate.get))

# print(candidate.get(20,1))  #20의 값이 없으면 1을 가져온다.
# max(candidate,key=lambda)
