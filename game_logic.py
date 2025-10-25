"""
game_logic.py
-------------
Contains the main logic for the Snowman Meltdown game, including:
- Input handling
- Game flow control
- Display of ASCII art and game state
"""

import random
from ascii_art import STAGES

WORDS = ["python", "git", "github", "snowman", "meltdown"]


# -------------------- Input & Helpers --------------------

def get_valid_input():
    """
    Prompt the player to guess a single letter.

    Returns:
        str: A single alphabetical character in lowercase.
    """

    while True:
        guess = input("Guess a letter: ").strip().lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetical character.")
        else:
            return guess


def play_again():
    """
    Ask the player if they want to play again.

    Returns:
        bool: True if the player chooses 'y', False if 'n'.
    """

    while True:
        choice = input("Would you like to play again? (y/n): ").strip().lower()
        if choice == "y":
            return True
        elif choice == "n":
            return False
        else:
            print("Please enter y or n.")


def get_random_word():
    """
    Select a random word from the word list.

    Returns:
        str: A randomly chosen word from WORDS.
    """
    return random.choice(WORDS)


def print_centered(stage: str, width: int = 40):
    """
    Print each line of a multi-line string centered in a fixed width.

    Args:
        stage (str): The ASCII art or text block to center.
        width (int): Total width of the line. Default is 40.
    """

    for line in stage.splitlines():
        print(f"{line:^{width}}")


# -------------------- Display --------------------

def display_game_state(mistakes, secret_word, guessed_letters, wrong_letters):
    """
    Display the current game state, including:
    - Snowman ASCII art for the current number of mistakes
    - The secret word with underscores for unguessed letters
    - Wrong guesses
    - Tries left

    Args:
        mistakes (int): Number of incorrect guesses so far.
        secret_word (str): The word the player is trying to guess.
        guessed_letters (list): Letters the player has correctly guessed.
        wrong_letters (list): Letters the player has guessed incorrectly.
    """

    print("=" * 40)
    print(f"{'SNOWMAN MELTDOWN':^40}")
    print("=" * 40)
    print_centered(STAGES[mistakes])

    display_word = " ".join([c if c in guessed_letters else "_" for c in secret_word])
    print(f"{'Word:':<10} {display_word}")

    if wrong_letters:
        print(f"{'Wrong:':<10} {' '.join(sorted(wrong_letters))}")

    max_mistakes = len(STAGES) - 1
    tries_left = max_mistakes - mistakes
    print(f"{'Tries left:':<10} {tries_left}")
    print("-" * 40, "\n")


# -------------------- Main Game --------------------

def play_game():
    """
    Run a single round of the Snowman Meltdown game.

    The function:
    - Selects a random secret word
    - Repeatedly prompts the player to guess letters
    - Updates and displays the game state
    - Ends when the word is fully guessed or the snowman melts.
    """

    secret_word = get_random_word()
    guessed_letters = []
    wrong_letters = []
    mistakes = 0
    max_mistakes = len(STAGES) - 1

    print(f"{'Welcome to Snowman Meltdown!':^40}")
    display_game_state(mistakes, secret_word, guessed_letters, wrong_letters)

    while mistakes < max_mistakes:
        guess = get_valid_input()

        if guess in guessed_letters or guess in wrong_letters:
            print("You already tried that letter.")
            continue

        if guess in secret_word:
            print(f"Good guess: {guess}")
            guessed_letters.append(guess)
            display_game_state(mistakes, secret_word, guessed_letters, wrong_letters)

            # Win when all unique letters are found
            if set(secret_word) <= set(guessed_letters):
                print("\n❄️ The snowman survived another day! ❄️\n")
                return
        else:
            mistakes += 1
            wrong_letters.append(guess)
            print(f"Oops! '{guess}' is not in the word.")
            display_game_state(mistakes, secret_word, guessed_letters, wrong_letters)

    print(f"The word was: {secret_word}")
    print("\n💧 The snowman has melted... better luck next time. 💧\n")

