message = ""#"@"%"$"!"^""

# print("3",2,1,message,sep="\n",end="Let's go!") and ("21")
# print(message)


# user_input = int(input('!!!!'))

# print(user_input&1)



# print(4859 % 100)
# print(59 // 100)


# number = int(input())

answer = 0
# print(f'len -- {len(str(number))/2}')
# for i in range(len(str(number))//2):
#     answer += number % 100
#     # print(answer)
    
#     number //= 100
#     # print(number)
# print(f'answer -- {answer}')

# list_a = [1,2,3,4]
# list_b = ['가','나','다','라','마']

# ziped = dict(zip(list_a,list_b))

# # print(ziped)

# list_a = ['가나다','가나다라','가나다라마바']

# print(max(list_a, key=len)) # 가나다라마바

# fruits = ['banana','apple','cherry']

# # for idx,fruits in enumerate(fruits, start=lambda x:x % 2== 0):
# #     print(idx,fruits)

# even_fruit = [fruit for idx, fruit in enumerate(fruits) if idx % 2 == 0]
# print(even_fruit)
    




def solution(cpr):
    answer = []
    basic_order = ["check", "call", "pressure", "respiration", "repeat"]
    for action in cpr:
        print(f"action -- {action}")
        for i in range(len(basic_order)) :
            if action == basic_order[i]:
                answer.append(i)
    return answer



print(solution(["call", "respiration", "repeat", "check", "pressure"]))