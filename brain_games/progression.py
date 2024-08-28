import random
from brain_games.cli import hi, number_count, check, win, lose, reply


def hide_number() -> str:
    start = random.randint(1, 10)
    step = random.randint(1, 7)
    progression = [start + i * step for i in range(10)]

    index = random.randint(1, len(progression) - 1)
    hidden_number = progression[index]
    progression[index] = '..'
    print(f"Question: {' '.join(map(str, progression))}")
    return hidden_number


def progression_game():
    name = hi()
    cycle = number_count()
    count = 0

    print('What number is missing in the progression?')

    for _ in range(cycle):
        answer = hide_number()
        user_answer = reply()
        if check(user_answer, answer):
            count += 1
            if count == cycle:
                win(name)
                return
        else:
            lose(name, user_answer, answer)
            return
