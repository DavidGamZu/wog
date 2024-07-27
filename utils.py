import os
from score import add_score
score_file_name = 'Scores.txt'
bad_return_code = 404


def gett_int(limit_b, limit_a=1):
    while True:
        num = input()
        if str.isdigit(num):
            if limit_a <= int(num) <= limit_b:
                break
            else:
                print('Option Not available, please try again: ', end='')
        else:
            print('Option Not available, please try again: ', end='')
    return int(num)


def is_float(string):
    if string.replace(".", "").isnumeric() and string.count(".") <= 1:
        return True
    else:
        return False


def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def show_result(result, difficulty):
    if result:
        add_score(difficulty, score_file_name)
        clear_screen()
        print('Congratulations, You Win!')
    else:
        clear_screen()
        print('Sorry, unfortunately You lost :( \nTry next time!')
