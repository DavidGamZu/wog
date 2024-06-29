import random
from utilities.utils import gett_int


def generate_number(difficulty):
    ran_num = random.randint(0, difficulty)
    return difficulty, ran_num


def get_guess_from_user(difficulty, ran_num):
    print(f'Please guess a number between 0 - {difficulty}: ', end="")
    guessed_num = gett_int(limit_a=0, limit_b=difficulty)
    return guessed_num, ran_num


def compare_results(guessed_num, ran_num):
    if guessed_num == ran_num:
        return True
    else:
        return False


def play(difficulty):
    difficulty, ran_num = generate_number(difficulty)
    guessed_num, ran_num = get_guess_from_user(difficulty, ran_num)
    return compare_results(guessed_num, ran_num)
