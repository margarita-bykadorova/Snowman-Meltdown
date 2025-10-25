import sys
import game_logic


def main():
    """The main function"""

    while True:
        game_logic.play_game()
        if not game_logic.play_again():
            sys.exit()


if __name__ == "__main__":
    main()