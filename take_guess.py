def take_guess():
    print("숫자 3개를 하나씩 차례대로 입력하세요.")
    new_guess = []
    while len(new_guess) < 3:
        your_guess = int(input("{}번째 숫자를 입력하세요: ".format(len(new_guess) + 1)))
        if your_guess in new_guess:
            print("중복되는 숫자입니다. 다시 입력하세요.")
        elif your_guess not in new_guess:
            if your_guess < 46 and your_guess > 0:
                new_guess.append(your_guess)
            else:
                print("범위를 벗어나는 숫자입니다. 다시 입력하세요.")
    return new_guess
print(take_guess())