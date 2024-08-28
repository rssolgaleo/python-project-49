from brain_games.cli import hi, number_count, check, win, lose, reply
from brain_games.calc import calculator
from brain_games.prime import is_prime
from brain_games.gcd import gcd
from brain_games.even import is_even
from brain_games.progression import hide_number


def games(game_mode):
    if game_mode == 'calculator':
        answer = calculator()
    elif game_mode == 'even':
        answer = is_even()
    elif game_mode == 'prime':
        answer = is_prime()
    elif game_mode == 'gcd':
        answer = gcd()
    elif game_mode == 'progression':
        answer = hide_number()
    return answer


def find(game_mode):
    if game_mode == 'calculator':
        text = 'What is the result of the expression?'
    elif game_mode == 'even':
        text = 'Answer "yes" if the number is even, otherwise answer "no".'
    elif game_mode == 'prime':
        text = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    elif game_mode == 'gcd':
        text = 'Find the greatest common divisor of given numbers.'
    elif game_mode == 'progression':
        text = 'What number is missing in the progression?'
    return text


def progress_game(game_mode):
    name = hi()
    cycle = number_count()
    count = 0

    text = find(game_mode)
    print(text)

    for _ in range(cycle):

        answer = games(game_mode)

        user_answer = str(reply())
        if check(user_answer, answer):
            count += 1
            if count == cycle:
                win(name)
                return
        else:
            lose(name, user_answer, answer)
            return
