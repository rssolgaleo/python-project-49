import random
from brain_games.cli import hi, number_count, check, win, lose, reply


def is_even():
    a = random.randint(1, 100)
    print(f'Question: {a}')
    return 'yes' if a % 2 == 0 else 'no'


def progress_game():
    name = hi()
    cycle = number_count()
    count = 0

    print('Answer "yes" if the number is even, otherwise answer "no".')

    for _ in range(cycle):
        answer = is_even()
        user_answer = reply()
        if check(user_answer, answer):
            count += 1
            if count == cycle:
                win(name)
                return
        else:
            lose(name, user_answer, answer)
            return
