import random
from brain_games.progress_game import progress_game
from brain_games.constants import constant


def is_prime() -> str:
    a: int = random.randint(1, 100)
    print(f"Question: {a}")
    for i in range(2, a // 2 + 1):
        if a % i == 0:
            return 'no'
    return 'yes'


def play():
    progress_game(is_prime, constant(is_prime))
