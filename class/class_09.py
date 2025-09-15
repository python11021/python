# 가위 바위 보 게임을 클래스로 구현한다.
#  가위는 1, 바위는 2, 보는 3으로 표현합니다.
# 게임이 끝나면 계속할지 물어본다.

import random

class RpgGame:
    choices = {1:"가위", 2:"바위", 3:"보"}

    def __init__(self):
        self