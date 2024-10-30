from pathlib import Path

def read_file(filename:Path):
    """Function reads in the file and returns the lines."""
    with open(filename, 'r', encoding='utf-8') as filehandle:
        lines = filehandle.readlines()
    return lines

def count_words(lines):
    """Function returns a list of words from the file, removing specified symbols."""
    word_per_line = []
    for words in lines:
        word_per_line.append(words.split())
    return word_per_line

def words_letters_returned(lines):
    """Counts total words and letters, printing the results."""
    combined_string = ''.join(lines).replace(' ', '').replace("\n", "")

    total_words_count = count_words(lines)
    tot_words = sum(len(inner_list) for inner_list in total_words_count)

    tot_letters =  len(combined_string)

    return tot_letters, tot_words


def total_letters(words_per_line):
    """Gets the letters in all the words in the lines
    """
    letters = []
    for word in words_per_line:
        for letter in word:
            letters.append(letter)
    return letters

def start_game(lines,tot_letters, tot_words):
    """Function starts the typing game and calculates word and character precision."""
    result = []
    #int the counters for words
    total_correct_words = 0
    total_words_needed = 0
    total_wrong_words = 0

    # Int the dictionary and counters for letters
    misspelled_letters_dict = {}
    total_mistakes = 0

    # initial Display screen
    word_pres_till_now = 100.0  # Assume 100% word precision initially
    letter_pres_till_now = 100.0

    print(f"Words-precision till now: {word_pres_till_now:.2f}%")
    print(f"Chars-precision till now: {letter_pres_till_now:.2f}%")
    print(f"Misspelled Characters: {misspelled_letters_dict}")
    for line in lines:
        print("----------------------------------")
        print("\nSkriv följande rad:")
        print(line.strip())  # Display the expected line
        user_input = input("--> ").strip()  # Get the user's input
        
        # Get total words and letters before starting the game
        (tot_letters, tot_words) = words_letters_returned(lines)

        # Split into words and count the necessary/typed words
        correct_words = line.strip().split()
        user_words = user_input.split()
        total_words_needed += len(correct_words)
        # Initialize correct and incorrect counts
        correct_word_count = 0
        wrong_words_count = 0
        correct_words_in_line = []
        wrong_words_in_line = []
        
        for i, correct_word in enumerate(correct_words):
            if i < len(user_words) and user_words[i] == correct_word:
                correct_word_count += 1
                correct_words_in_line.append(user_words[i])
            else:
                if i < len(user_words):
                    # If the word exists but is incorrect
                    wrong_words_count += len(user_words[i])
                    wrong_words_in_line.append(user_words[i])
                # If the word does not exist, count all letters as mistakes
                if i >= len(user_words) or len(user_words[i]) != len(correct_word):
                    wrong_words_count += len(correct_word)
        total_correct_words += correct_word_count
        mistaken_word_this_line = len(correct_words) - correct_word_count
        total_wrong_words += mistaken_word_this_line
        
        word_pres_till_now = ((tot_words - total_wrong_words) / tot_words) * 100
        # print(f"Total wrong words so far: {total_wrong_words}\n")
        # print(f"Mistaken words in this line: {mistaken_word_this_line}") # remove mayybe
        # print("--------------------------------------------------")
        # Debugging prints
        # print(f"Results:  {tot_words - mistaken_word_this_line}/{tot_words}")
        # print(f"Total words in file: {tot_words}")
        
        # check against letters and stoe in a list        

        correct_words_string = ' '.join(correct_words_in_line)
        user_input_after_removal = user_input.replace(correct_words_string, "").replace(" ", "")
        user_letters = list(user_input_after_removal)
        modified_line = line.strip().replace(correct_words_string, "").replace(" ", "")
        target_letters = list(modified_line)

        # Initialize counters and storage
        correct_count = 0
        mistake_count = 0
        correct_count_letters = []
        # mistake_count_letters = []
        mistake_count_for_line = {}


        # Iterate through each letter
        # for i, target_letter in enumerate(target_letters):
        #     if i < len(user_letters):
        #         if user_letters[i] == target_letter:
        #             correct_count += 1
        #             correct_count_letters.append(user_letters[i])  # Add to correct letters list
        #         else:
        #             mistake_count += 1
        #             mistake_count_for_line[target_letter] = 0
        #             mistake_count_for_line[target_letter] += 1
        #             # Increment the mistake count for the correct target letter
        #             correct_letter_mistakes[target_letter] += 1
        #     else:
        #         # Handle missing letters
        #         mistake_count += 1
        #         if target_letter not in mistake_count_for_line:
        #             mistake_count_for_line[target_letter] = 0
        #         mistake_count_for_line[target_letter] += 1  # Count the missing letter as a mistake
        for i, target_letter in enumerate(target_letters):
            if i < len(user_letters):
                if user_letters[i] == target_letter:
                    correct_count += 1  # Increment correct letter count if correct
                else:
                    # Count the mistake for the correct letter
                    if target_letter not in mistake_count_for_line:
                        mistake_count_for_line[target_letter] = 0
                    mistake_count_for_line[target_letter] += 1  # Increment the mistake count for this letter
                    mistake_count += 1  # Increment total mistake count
            else:
                # If the user input is shorter than the target
                if target_letter not in mistake_count_for_line:
                    mistake_count_for_line[target_letter] = 0
                mistake_count_for_line[target_letter] += 1  # Count the missing letter as a mistake
                mistake_count += 1  # Increment total mistake count

        # Update the global misspelled_letters_dict with mistakes from this line
        for letter, count in mistake_count_for_line.items():
            if letter not in misspelled_letters_dict:
                misspelled_letters_dict[letter] = 0  # Initialize if not present
            misspelled_letters_dict[letter] += count  # Add the count of mistakes for this letter


        # Calculate totals
        total_mistakes += mistake_count
        correct_count += len(correct_count_letters)
        # Debugging outputs
        # print(f"user_letters: {user_letters}")
        # print(f"target_letters: {target_letters}")

        # Total precision calculations

        letter_pres_till_now = ((tot_letters - total_mistakes) / tot_letters) * 100 if tot_letters > 0 else 0
        # Precision calculations
        print(f"Words-precision till now: {word_pres_till_now:.2f}%")
        print(f"Chars-precision till now: {letter_pres_till_now:.2f}%")
        print(f"Misspelled Characters: {misspelled_letters_dict}")

    # Calculate cumulative precision values
    name = input("Ange ditt namn: ")
    total_word_precision = ((tot_words - total_wrong_words) / tot_words) * 100
    total_letter_precision = ((tot_letters - total_mistakes) / tot_letters) * 100 if tot_letters > 0 else 0

    result.append((name, total_word_precision, total_letter_precision))
    save_result(result)


def save_result(result):
    """Function saves the results in 'score.txt' file"""
    with open("score.txt", 'a', encoding='utf-8') as filehandle:
        for name, total_word_precision, total_letter_precision in result:
            filehandle.write(f"{name}: Ordprecision: {total_word_precision:.2f}%, Teckenprecision: {total_letter_precision:.2f}%\n")

def show_results():
    """Function reads the results from 'score.txt' file"""
    print("\nResultat:")
    with open('score.txt', 'r', encoding='utf-8') as file:
        scores = file.readlines()
        for score in scores:
            print(score.strip())