#!/usr/bin/env python3

import random
from brain_games.cli import welcome_user


def generate_progression():
    start = random.randint(1, 10)
    step = random.randint(1, 7)
    progression = [start + i * step for i in range(10)]
    return progression

def hide_number(progression):
    index = random.randint(0, len(progression) - 1)
    hidden_number = progression[index]
    progression[index] = '..'
    return progression, hidden_number

def main():
    name = welcome_user()
    print('What number is missing in the progression?')
    score = 0
    while (score < 3):
        progression = generate_progression()
        progression, hidden_number = hide_number(progression)
        print(hidden_number)
        print("Question:", *progression)
        answer = int(input("Your answer: "))
        if answer == hidden_number:
            print("Correct!")
            score += 1
        else:
            print(f"'{answer}' was wrong answer ;(. Correct answer is '{hidden_number}'")
            print(f"Let's try again, {name}")
            break
    if score == 3:
        print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
