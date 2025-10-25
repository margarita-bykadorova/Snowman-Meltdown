import random
import sys
from ascii_art import STAGES


"""
Clearer Display: Improve the output formatting for readability.
"""


def get_valid_input():
    while True:
        guess = input("Guess a letter: ").strip().lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetical character.")
        else:
            return guess


def play_again():
    while True:
        choice = input("Would you like to play again? (y/n): ").strip().lower()
        if choice == "y":
            return True
        elif choice == "n":
            return False
        else:
            print("Please enter a valid choice.")


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    """Display the snowman stage for the current number of mistakes."""

    print(STAGES[mistakes])
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word: ", display_word)
    if len(secret_word) == len(guessed_letters):
        print("You saved the snowman!")
        exit()
    print("\n")


def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0

    print("Welcome to Snowman Meltdown!")
    display_game_state(mistakes, secret_word, guessed_letters)

    while mistakes < (len(STAGES) - 1):
        guess = get_valid_input()
        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in secret_word:
            print("You guessed:", guess)
            guessed_letters.append(guess)
            display_game_state(mistakes, secret_word, guessed_letters)
        else:
            mistakes += 1
            print("That's a wrong letter, snowman melts!")
            display_game_state(mistakes, secret_word, guessed_letters)
    print("You didn't save the snowman!")

