import random
from utils import clear_screen, gett_int
import time


def generate_sequence(difficulty):
    rand_list = []
    for i in range(0, difficulty):
        n = random.randint(1, 101)
        rand_list.append(n)
    for i in reversed(range(0, 3)):
        u = i + 1
        print(f'Beginning in {u}')
        time.sleep(1)
        clear_screen()
    print(*rand_list)
    time.sleep(0.7)
    clear_screen()
    return rand_list


def get_list_from_user(difficulty):
    user_list = []
    list_number = ['fist', 'second', 'third', 'fourth', 'fifth']
    for i in range(0, difficulty):
        if difficulty > 1:
            print(f'Please enter the {list_number[i]} number: ', end='')
        else:
            print(f'Please enter the number: ', end='')
        n = gett_int(limit_a=0, limit_b=102)
        user_list.append(n)
    return user_list


def is_list_equal(rand_list, user_list):
    if rand_list == user_list:
        return True
    else:
        return False


def play(difficulty):
    rand_list = generate_sequence(difficulty)
    user_list = get_list_from_user(difficulty)
    return is_list_equal(rand_list, user_list)
