import random
from brain_games.cli import hi, number_count, check, win, lose, reply
from brain_games.prime import prime_game


def progress_game():
    name = hi()
    cycle = number_count()
    count = 0

    text()

    for _ in range(cycle):
        answer = prime()
        user_answer = reply()
        if check(user_answer, answer):
            count += 1
            if count == cycle:
                win(name)
                return
        else:
            lose(name, user_answer, answer)
            return
