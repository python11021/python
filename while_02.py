import time

count = 0

while True:
    count += 1
    print(count)
    time.sleep(1)   #1초간 지연
    
    # 5초 단위로 사용자한테 계속 할건지 몰어본다.. "To be continue(x/y)"
    
    if count % 5 == 0:
        contnue_yn = str(input("To be continue(Y/y) :"))
        if contnue_yn.upper() != 'Y':
            break
            break
