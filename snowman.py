"""
snowman.py
----------
Main entry point for the Snowman Meltdown game.
Starts and manages the main game loop.
"""

import sys
import game_logic


def main():
    """
    Runs the main game loop:
    - Starts a new game round.
    - Prompts the player to play again after each round.
    - Exits the program if the player chooses not to continue.
    """

    while True:
        game_logic.play_game()
        if not game_logic.play_again():
            sys.exit()


if __name__ == "__main__":
    main()
