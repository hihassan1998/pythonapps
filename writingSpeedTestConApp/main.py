#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
main.py file for main funtion to run the the 82-Game chatbot
"""
from pathlib import Path
import typing_test2


def main():

    cwd = Path.cwd()
    easy_file = cwd / "easy2.txt"
    # medium_file = cwd / "medium.txt"
    # hard_file = cwd / "hard.txt"
    # score_file = cwd / "score.txt"

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
        print("| Menu: |")
        print("1.Start typing test. (Easy Level)")
        print("2. Start typing test. (Medium Level)")
        print("3.Start typing test. (Hard Level)")
        print("4. Show saved test results.")
        print("Press 'q' to quit.")

        choice = input("Choose an option; 1-3: \n -->")

        if choice == "1":
            lines = typing_test2.read_file(easy_file)
            tot_letters, tot_words = typing_test2.words_letters_returned(lines)
            typing_test2.start_game(lines,tot_letters, tot_words)  # Pass the path
        elif choice == "2":
            lines = typing_test2.read_file(easy_file)
            typing_test2.total_letters(lines)  # Pass the path
        elif choice == "3":
            lines = typing_test2.read_file(easy_file)
            total_letters_in_file = 44
            typing_test2.compare_user_input(lines, total_letters_in_file)
            # typing_test2.start_game(hard_file)  # Pass the path
        elif choice == "31":
            lines = typing_test2.read_file(easy_file)
            letters = typing_test2.total_letters(lines)
            print("Total letters:", letters)

        elif choice == "4":
            typing_test2.show_results()  # Pass the path
        elif choice == "q":
            break
        else:
            print("Wrong choice, choose from the options!")


if __name__ == "__main__":
    main()
