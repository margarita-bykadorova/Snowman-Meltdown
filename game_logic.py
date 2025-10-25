import random
from ascii_art import STAGES

WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_valid_input():
    """Gets a single alphabetical character"""

    while True:
        guess = input("Guess a letter: ").strip().lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetical character.")
        else:
            return guess


def play_again():
    """Let's the user choose to play again or quit the game."""

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
    return random.choice(WORDS)


def print_centered(stage: str, width: int = 40):
    """Print each line of the ASCII art centered in a fixed width."""
    for line in stage.splitlines():
        print(f"{line:^{width}}")


def display_game_state(mistakes, secret_word, guessed_letters, wrong_letters):
    """Show the ASCII stage, the current word, wrong letters, and tries left."""
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


def play_game():
    """The game flow."""
    secret_word = get_random_word()
    guessed_letters = []
    wrong_letters = []
    mistakes = 0
    max_mistakes = len(STAGES) - 1

    print("Welcome to Snowman Meltdown!")
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
                print("🎉 You saved the snowman!")
                return
        else:
            mistakes += 1
            wrong_letters.append(guess)
            print(f"Oops! '{guess}' is not in the word.")
            display_game_state(mistakes, secret_word, guessed_letters, wrong_letters)

    print("💧 You didn't save the snowman!")

