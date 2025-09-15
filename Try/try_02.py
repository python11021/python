# 오류를 피해가는 행위 --> 예외 처리
# num1 = int(input('숫자를 입력하세요.'))
# num2 = int(input('숫자를 입력하세요.'))

try:
    num1,num2 = map(int, input('공백을 기준으로 두개의 숫자를 입력').split())

    calc_lists = [num1+num2, num1-num2, num1*num2, num1/num2]

    # print(f'{num1} + {num2} = {calc_lists[0]}')
    # print(f'{num1} - {num2} = {calc_lists[1]}')
    # print(f'{num1} * {num2} = {calc_lists[2]}')
    # print(f'{num1} / {num2} = {calc_lists[3]}')

    print('1. 더하기',end='\t')
    print('2. 빼기',end='\t')
    print('3. 곱하기',end='\t')
    print('4. 나누기')
    choice = int(input(' 원하는 결과를 입력하세요. '))
    print(f'결과는 = {calc_lists[choice]}')
except Exception as e:
    print(f'오류 발생 :{e}')

print('프로그램 종료')
