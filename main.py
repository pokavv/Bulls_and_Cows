import random

answer = []


def generate_numbers():
    for i in range(3):
        num = random.randint(0, 9)
        while num in answer:
            num = random.randint(0, 9)
        answer.append(num)
    return answer


def take_guess():
    print("숫자 3개를 하나씩 차례대로 입력하세요.")
    new_guess = []
    while len(new_guess) < 3:
        your_guess = int(input("{}번째 숫자를 입력하세요: ".format(len(new_guess) + 1)))
        if your_guess in new_guess:
            print("중복되는 숫자입니다. 다시 입력하세요.")
        elif your_guess not in new_guess:
            if your_guess < 10 and your_guess >= 0:
                new_guess.append(your_guess)
            else:
                print("범위를 벗어나는 숫자입니다. 다시 입력하세요.")
    return new_guess


def get_score(guesses, solution):
    strike_count = 0
    ball_count = 0

    for i in range(len(guesses)):
        for j in range(len(solution)):
            if guesses[i] == solution[j]:
                if i == j:
                    strike_count += 1
                else:
                    ball_count += 1

    return strike_count, ball_count


# 여기서부터 게임 시작!
ANSWER = generate_numbers()
tries = 0
while True:
    strike, ball = get_score(take_guess(), ANSWER)
    tries += 1
    print("{}S {}B\n".format(strike, ball))
    if strike == 3:
        break
print("축하합니다. {}번 만에 숫자 3개의 값과 위치를 모두 맞추셨습니다.".format(tries))