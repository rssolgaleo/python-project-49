import random
from brain_games.progress_game import progress_game


def hide_number() -> str:
    start: int = random.randint(1, 10)
    step: int = random.randint(1, 7)
    progression = [start + i * step for i in range(10)]

    index: int = random.randint(1, len(progression) - 1)
    hidden_number = progression[index]
    progression[index] = '..'
    print(f"Question: {' '.join(map(str, progression))}")
    return str(hidden_number)


def play():
    text = 'What number is missing in the progression?'
    progress_game(hide_number, text)
