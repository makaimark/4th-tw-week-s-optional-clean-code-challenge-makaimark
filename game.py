import random


def print_logic(input_int, rand_num):
    if input_int < rand_num:
        return "guess is low"
    elif input_int > rand_num:
        return "guess is high"
    else:
        return "you guessed it!"


def game_logic(integer):
    for i in range(10):
        input_int = 0
        random_num = random.randint(1, integer)
        while random_num != input_int:
            input_int = int(input("Enter an integer from 1 to " + str(integer) + ":"))
            print(print_logic(input_int, random_num))

game_logic(99)
game_logic(49)
