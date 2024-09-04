import random
from brain_games.progress_game import progress_game


def gcd() -> str:
    a: int = random.randint(1, 100)
    b: int = random.randint(1, 100)
    print(f'Question: {a} {b}')
    while a != 0 and b != 0:
        if (a > b):
            a = a % b
        else:
            b = b % a
    return str(a + b)


def play():
    text = 'Find the greatest common divisor of given numbers.'
    progress_game(gcd, text)
