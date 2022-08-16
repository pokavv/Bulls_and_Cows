import random
answer = []

def generate_answer():
    for i in range(3):
        num = random.randint(1, 45)
        while num in answer:
            num = random.randint(1, 45)
        answer.append(num)
    return answer