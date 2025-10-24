import random
import game_logic

WORDS = ["python", "git", "github", "snowman", "meltdown"]


def main():
    while True:
        play_game()
        if not play_again():
            sys.exit()

if __name__ == "__main__":
    main()