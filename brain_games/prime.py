import random
from brain_games.cli import hi, number_count, check, win, lose, reply


def text():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    return


def is_prime(a):
    print(f"Question: {a}")
    for i in range(2, a // 2 + 1):
        if a % i == 0:
            return 'no'
    return 'yes'


def function():
    a = random.randint(1, 100)
    return a


def progress_game():
    name = hi()
    cycle = number_count()
    count = 0

    text()

    for _ in range(cycle):
        a = function()
        answer = is_prime(a)
        user_answer = reply()
        if check(user_answer, answer):
            count += 1
            if count == cycle:
                win(name)
                return
        else:
            lose(name, user_answer, answer)
            return
