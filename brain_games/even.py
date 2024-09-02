import random
from brain_games.progress_game import progress_game


def is_even() -> str:
    a: int = random.randint(1, 100)
    print(f'Question: {a}')
    return 'yes' if a % 2 == 0 else 'no'


def play():
    text = 'Answer "yes" if the number is even, otherwise answer "no".'
    progress_game(is_even, text)
