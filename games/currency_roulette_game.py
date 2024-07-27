import random
from utils import is_float
from currency_converter import CurrencyConverter


def get_money_interval(difficulty):
    ils_currency = CurrencyConverter().convert(1, 'USD', 'ILS')
    random_dollar = round(random.uniform(0, 100), 2)
    highest_num = round(random_dollar * ils_currency + 10 - difficulty, 2)
    lowest_num = round(random_dollar * ils_currency - 10 + difficulty, 2)
    return random_dollar, highest_num, lowest_num


def get_guess_from_user(random_dollar):
    print(f"Please enter the your guess for the converted value of {random_dollar}USD:\nyour Answer: ", end='')
    while True:
        user_float = input()
        if is_float(user_float):
            return float(user_float)
        else:
            print('Wrong value!\nPlease enter a valid value: ', end='')


def compare_results(highest_num, lowest_num, user_float):
    if highest_num > user_float > lowest_num:
        return True
    else:
        return False


def play(difficulty):
    random_dollar, highest_num, lowest_num = get_money_interval(difficulty)
    user_float = get_guess_from_user(random_dollar)
    return compare_results(highest_num, lowest_num, user_float)
