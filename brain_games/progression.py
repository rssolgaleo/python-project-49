import random


def hide_number():
    start = random.randint(1, 10)
    step = random.randint(1, 7)
    progression = [start + i * step for i in range(10)]

    index = random.randint(1, len(progression) - 1)
    hidden_number = progression[index]
    progression[index] = '..'
    print(f"Question: {' '.join(map(str, progression))}")
    return str(hidden_number)
