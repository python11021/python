# 매개변수 O, 반환값 O
# 매개변수 O, 반환값 X
# 매개변수 X, 반환값 O
# 매개변수 X, 반환값 X

# 만들고 사용해보기

# 매개변수 O, 반환값 O
def car_sel(color1, kind1):
    return f'{color1}의 {kind1}이 지나갑니다'

print(car_sel('red','트럭'))

# 매개변수 O, 반환값 X
import random
def car_color(color1):
    print(f'{color1}의 차가 지나갑니다.')

car_color('Green')

# 매개변수 X, 반환값 O
from datetime import datetime

def cur_day():
 return datetime.today().day 
current_day = cur_day()
print(f'현재 일자는 {current_day}')
# 매개변수 X, 반환값 X
