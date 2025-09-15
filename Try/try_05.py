# 사용자 입력 처리 함수
# 이름은 get_data()
# 파라메터
    # start : 시작값
    # end : 종료값
    # input_str 
# 사용자 입력은 input
# return 정수로 변환된 입력값

def get_data(start,end,input_str='입력'):
    while True:
        try:
            input_data = int(input(f'{input_str}({start}~{end})'))
            if not start <= input_data <= end:
                raise ValueError(f'{start}~{end} 범위 초과')
        except Exception as e:
            print(f'{e.__class__.__name__} 에러발생 : {e}' )        
            # print(f'{start}와 {end} 사이의 정수를 입력해주세요.')
            # return int(input(input_str))    
        else:
            return input_data
    

print(get_data(1,1000,"정수를 입력해주세요 "))

