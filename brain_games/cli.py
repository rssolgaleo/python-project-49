import prompt


def hi():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    return name


def number_count():
    return 3


def user_answer():
    answer = input("Your answer: ")
    return answer


def check(name, answer, right):
    if answer == right:
        print("Correct!")
        return True
    else:
        bye(name, answer, right)


def bye(name, answ, right):
    print(f"'{answ}' is wrong answer ;(. Correct answer was '{right}'.")
    print(f"Let's try again, {name}!")
    return False


def end(name, count):
    if count == number_count():
        print(f"Congratulations, {name}!")
        return True
    return False
