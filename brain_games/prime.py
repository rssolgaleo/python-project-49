import random
from brain_games.cli import hi, number_count, check, win, lose, reply


def is_prime():
    a = random.randint(1, 100)
    print(f"Question: {a}")
    for i in range(2, a // 2 + 1):
        if a % i == 0:
            return 'no'
    return 'yes'


def progress_game():
    name = hi()
    cycle = number_count()
    count = 0

    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    for _ in range(cycle):
        answer = is_prime()
        user_answer = reply()
        if check(user_answer, answer):
            count += 1
            if count == cycle:
                win(name)
                return
        else:
            lose(name, user_answer, answer)
            return
