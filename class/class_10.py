# 숫자 맞추기 게임
# 규칙
# 1.컴퓨터가 1~100 사이의 숫자를 랜덤으로 선택합니다.
# 2.사용자는 숫자를 입력하여 컴퓨터가 선택한 숫자를 맞춥니다.
# 3.사용자가 입력한 숫자가 컴퓨터가 선택한 숫자보다 크면 "너무 큽니다"라고 출력합니다.
# 4.사용자가 입력한 숫자가 컴퓨터가 선택한 숫자보다 작으면 "너무 작습니다."라고 출력합니다.
# 5.사용자가 입력한 숫자가 컴퓨터가 선택한 숫자와 같으면 "정답입니다."라고 출력하고 게임을 종료합니다.
# 6.사용자가 숫자를 맞출 때까지 계속 입력을 받습니다.

import random

class NumberGuessGame:
    def __init__(self):
        self.answer = random.randint(1, 100)
        self.finished = False
    @classmethod
    def guess(self, user_input):
        if self.finished:
            return "게임이 이미 종료되었습니다."
        if user_input > self.answer:
            return "너무 큽니다."
        elif user_input < self.answer:
            return "너무 작습니다."
        else:
            self.finished = True
            return "정답입니다."

# 외부 입력 및 게임 진행 예시
if __name__ == "__main__":  # 이 파일을 직접 실행할 때만
    game = NumberGuessGame()
    while not game.finished:
        try:
            user_input = int(input("1부터 100 사이의 숫자를 입력하세요: "))
            result = game.guess(user_input)
            print(result)
        except ValueError:
            print("숫자를 입력해 주세요.")
