#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
main.py file for main funtion to run the the 82-Game chatbot
"""
from pathlib import Path
import typing_test2


def main():
    """
    A funtion to run the 82-Game chatbot that takes in 3 text files
    and runs a typing test on them.
    """

    cwd = Path.cwd()
    easy_file = cwd / "easy22.txt"
    medium_file = cwd / "medium.txt"
    hard_file = cwd / "hard.txt"
    score_file = cwd / "score.txt"

    game_img = r"""
     ___    _____ _
    ( _ )  |  ___(_)_ __   __ _  ___ _ __ ___
    / _ \  | |_  | | '_ \ / _` |/ _ \ '__/ __|
   | (_) | |  _| | | | | | (_| |  __/ |  \__ \  _
    \___/  |_|___|_|_| |_|\__, |\___|_| _|___/ (_)
    |___ \  |_   _| |__  _ |___/ __ ___ | |__  ___
      __) |   | | | '_ \| | | | '_ ` _ \| '_ \/ __|
     / __/    | | | | | | |_| | | | | | | |_) \__ \
    |_____|   |_| |_| |_|\__,_|_| |_| |_|_.__/|___/

    """
    while True:
        print(game_img)
        print(chr(27) + "[2J" + chr(27) + "[;H")
        print("Welcome to 8 fingers and 2 thumbs game, "
              "where you get to compete with yourself and learn to type faster.")
        print("| Menu: ty_t2|")
        print("1.Start typing test. (Easy Level)")
        print("2. Start typing test. (Medium Level)")
        print("3.Start typing test. (Hard Level)")
        print("4. Show saved test results.")
        print("Press 'q' to quit.")

        choice = input("Choose an option; 1-4: \n -->")

        try:

            if choice == "1":
                lines = typing_test2.read_file(easy_file)
                tot_letters, tot_words = typing_test2.words_letters_returned(lines)
                typing_test2.start_game(lines, tot_letters, tot_words)


            elif choice == "2":
                print("You selected option 2.")
                print(f"Trying to read from: {medium_file}")

                lines = typing_test2.read_file(medium_file)
                print("File read successfully.")
                tot_letters, tot_words = typing_test2.words_letters_returned(lines)

                if tot_words == 0:
                    print("Error: No words found in the file.")
                    continue  # Go back to the menu

                typing_test2.start_game(lines, tot_letters, tot_words)


            elif choice == "3":
                lines = typing_test2.read_file(hard_file)
                print("File read successfully.")
                tot_letters, tot_words = typing_test2.words_letters_returned(lines)

                if tot_words == 0:
                    print("Error: No words found in the file.")
                    continue  # Go back to the menu

                typing_test2.start_game(lines, tot_letters, tot_words)


            elif choice == "4":
                if score_file.exists():
                    typing_test2.show_results(score_file)
                else:
                    print("No files found.")

            elif choice == "q":
                    print("Thank you for playing 82. Have a nice day\n")
                    break
            else:
                print("Wrong choice, choose from the options!")
        
        except ValueError as e:
            print(f"Error: {e}. Please ensure the file is correctly formatted.")
        except FileNotFoundError as e:
                print(f"Error: {e}. File not found.")




if __name__ == "__main__":
    main()
