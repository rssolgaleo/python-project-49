import random
from brain_games.cli import hi, number_count, check, win, lose, reply


def gcd():
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    print(f'Question: {a} {b}')
    while a != 0 and b != 0:
        if (a > b):
            a = a % b
        else:
            b = b % a
    return str(a + b)


def progress_game():
    name = hi()
    cycle = number_count()
    count = 0

    print('Find the greatest common divisor of given numbers.')

    for _ in range(cycle):
        answer = gcd()
        user_answer = reply()
        if check(user_answer, answer):
            count += 1
            if count == cycle:
                win(name)
                return
        else:
            lose(name, user_answer, answer)
            return
