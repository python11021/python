import time

def display_second(count):
    count += 1
    print(f'{count}초')
    time.sleep(1)   #1초간 지연

    return count

def is_user_continue(count):
   if count % 5 == 0:
        user_input = str(input("To be continue(Y/y) :")).upper()
        if not user_input == 'Y':
            return False
   return True

        
count = 0
is_continue = True
while is_continue:
   count = display_second(count)    #1초 간격으로 출력
#    print(f'!! {count}초')
   is_continue = is_user_continue(count) # 5초 단위로 진행여부 판단
#    print(is_continue)
  
    # 5초 단위로 사용자한테 계속 할건지 몰어본다.. "To be continue(x/y)"
    
    
         
