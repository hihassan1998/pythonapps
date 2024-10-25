#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
main function to run the 82-Game chatbot
"""


import typing_test


def main():
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
        print("Welcome to 8 fingers and 2 thumbs game, "
              "where you get to compete with yourself and learn to type faster.")
        print("| Menu: |")
        print("1.Start typing test. (Easy Level)")
        print("2. Start typing test. (Medium Level)")
        print("3.Start typing test. (Hard Level)")
        print("4. Show saved test results.")
        print("Press 'q' to quit.")

        choice = input("Choose an option; 1-3")

        if choice == "1":
            typing_test.start_game("easy.txt")
        if choice == "1":
            typing_test.start_game("medium.txt")
        if choice == "1":
            typing_test.start_game("hard.txt")
        if choice == "1":
            typing_test.start_game("score.txt")
        elif choice == "q":
            break
        else:
            print("Wrong choice, choose from the options!")


if __name__ == "__main__":
    main()
