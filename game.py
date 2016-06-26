import random


def game_logic(integer):
    for i in range(10):             # The game contains 10 turn
        input_int = 0               # In every new turn we change the value to zero
        rand_num = random.randint(1, integer)     # We generate a random number between 1 and 99\49
        while rand_num != input_int:              # While we don't find the input_int
            input_int = int(input("Enter an integer from 1 to " + str(integer) + ":"))  # Ask a new number from the user
            print("guess is low" if input_int < rand_num else "guess is high" if input_int > rand_num else "you got it")
            # Compare input_int and rand_num, then print the result

game_logic(99)      # First part of the game, random nums between 1 and 99
game_logic(49)      # Second part of the game, random nums between 1 and 49
