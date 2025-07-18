# Sikai Sellers CIS261 GuessingGame

import random

def display_heading():
    print(" Welcome to the Number Game! \n")

def play_game(limit):
    number_to_guess = random.randint(1, limit)
    print(f"I'm thinking of a number between 1 and {limit}. Can you guess it?\n")

    while True:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Invalid number.")
            continue

        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print("Correct! You guessed the number!\n")
            break

def main():
    display_heading()
    while True:
        try:
            limit = int(input("Enter the upper limit for the guessing range: "))
            if limit < 1:
                print("Please enter a number greater than 0.")
                continue
        except ValueError:
            print("Please enter a valid integer.")
            continue

        play_game(limit)

        play_again = input("Do you want to play again? (y/n): ").strip().lower()
        if play_again != 'y':
            print("Thanks for playing! Goodbye!")
            break
main()

