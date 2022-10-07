#!/usr/bin/env python3
# Created by: Carolyn Webster Pless
# Created on: 2022/10/06
# Asks the user to guess a number between 0 and 9
# and randomizes the correct number

# to be able to create random numbers
import random


def main():

    # title of the program
    print("Guess the Randomized Number")

    # to randomize the number
    correct_number = random.randint(0, 9)  # a

    # input for the guessed number
    guess = int(input("Guess the number between 0 and 9: "))

    # if statement if the user guesses it correctly
    if guess == correct_number:
        print("You guessed the number correctly! Great job!")

    # else statement if you guess the number wrong
    else:
        print(
            "You guessed the number incorrectly. The correct number was {}".format(
                correct_number
            )
        )


if __name__ == "__main__":
    main()
