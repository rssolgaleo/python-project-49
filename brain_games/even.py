import random
from brain_games.cli import hi, number_count, check, win, lose, reply


def text():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    return


def is_even(a):
    print(f'Question: {a}')
    return 'yes' if a % 2 == 0 else 'no'


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
        answer = is_even(a)
        user_answer = reply()
        if check(user_answer, answer):
            count += 1
            if count == cycle:
                win(name)
                return
        else:
            lose(name, user_answer, answer)
            return
