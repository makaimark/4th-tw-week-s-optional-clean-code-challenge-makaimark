import random


def print_logic(input_int, rand_num):
    if input_int < rand_num:
        print("guess is low")
    elif input_int > rand_num:
        print("guess is high")
    else:
        print("you guessed it!")


def game_logic(integer):
    for i in range(10):             # The game contains 10 turn
        input_int = 0               # In every new turn we change the value to zero
        rand_num = random.randint(1, integer)     # We generate a random number between 1 and 99\49
        while rand_num != input_int:              # While we don't find the rand_num
            input_int = int(input("Enter an integer from 1 to " + str(integer) + ":"))  # Ask a new number from the user
            print_logic(input_int, rand_num)
            # Compare input_int and rand_num, then print the result

game_logic(99)      # First part of the game, random nums between 1 and 99
game_logic(49)      # Second part of the game, random nums between 1 and 49

