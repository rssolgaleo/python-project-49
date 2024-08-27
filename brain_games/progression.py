import random
from brain_games.cli import hi, number_count, check, win, lose, reply


def generate_progression():
    start = random.randint(1, 10)
    step = random.randint(2, 7)
    progression = [start + i * step for i in range(10)]
    return progression


def hide_number(progression):
    index = random.randint(0, len(progression) - 1)
    hidden_number = progression[index]
    progression[index] = '..'
    print(f"Question: {' '.join(map(str, progression))}")
    return int(hidden_number)


def progress_game():
    name = hi()
    cycle = number_count()
    count = 0

    print('What number is missing in the progression?')

    for _ in range(cycle):
        progression = generate_progression()
        answer = hide_number(progression)
        user_answer = int(reply())
        if check(user_answer, answer):
            count += 1
            if count == cycle:
                win(name)
                return
        else:
            lose(name, user_answer, answer)
            return
