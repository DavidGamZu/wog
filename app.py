import time
from games import guess_game, memory_game, currency_roulette_game
from utils import gett_int, clear_screen, show_result


def welcome():
    name = input("Welcome to GOW! Please enter your name: ")
    clear_screen()
    print(f"Hello, {str(name)}")


def start_play():
    print("Please choose a game to play: \n 1. Memory Game - a sequence of numbers will appear for 1 second and you "
          "have to guess it back. \n 2. Guess Game - guess a number and see if you chose like the computer. \n 3. "
          "Currency Roulette - try and guess the value of a random amount of USD in ILS\nSelect your choose then "
          "press enter: ", end='')
    game_type = gett_int(limit_b=3)
    print('Please enter difficulty level between 1-5: ', end='')
    difficulty = gett_int(limit_b=5)
    print(f"Difficulty level chosen: {difficulty}")
    time.sleep(2)
    clear_screen()
    if game_type == 1:
        show_result(memory_game.play(difficulty), difficulty)
    elif game_type == 2:
        show_result(guess_game.play(difficulty), difficulty)
    elif game_type == 3:
        show_result(currency_roulette_game.play(difficulty), difficulty)
