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

def total_letters(words_per_line):
    """Gets the letters in all the words in the lines
    """
    letters = []
    for word in words_per_line:
        for letter in word:
            letters.append(letter)
    return letters
def words_letters_returned(lines):
    """Counts total words and letters, printing the results."""
    combined_string = ''.join(lines).replace(' ', '').replace("\n", "")

    total_words_count = count_words(lines)
    tot_words = sum(len(inner_list) for inner_list in total_words_count)

    tot_letters =  len(combined_string)

    return tot_letters, tot_words

def calculate_word_precision(line, user_input):
    """Calculates word precision and counts correct and incorrect words."""
    correct_words = line.strip().split()
    user_words = user_input.split()
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
                wrong_words_count += len(user_words[i])
                wrong_words_in_line.append(user_words[i])
            if i >= len(user_words) or len(user_words[i]) != len(correct_word):
                wrong_words_count += len(correct_word)

    mistaken_word_this_line = len(correct_words) - correct_word_count
    return correct_word_count, mistaken_word_this_line, correct_words_in_line

def convert_str_to_list(string):
    """Converts a string into a list of characters."""
    char_list = []
    for char in string:
        char_list.append(char)
    return char_list


def calculate_letter_precision(line, user_input, correct_words_in_line):
    """Calculates letter precision and tracks correct and incorrect letters."""
    correct_words_string = ' '.join(correct_words_in_line)
    user_input_after_removal = user_input.replace(correct_words_string, "").replace(" ", "")
    user_letters = convert_str_to_list(user_input_after_removal)
    
    modified_line = line.strip().replace(correct_words_string, "").replace(" ", "")
    target_letters = convert_str_to_list(modified_line)

    correct_count = 0
    mistake_count_for_line = {}

    for i, target_letter in enumerate(target_letters):
        if i < len(user_letters):
            if user_letters[i] == target_letter:
                correct_count += 1
            else:
                if target_letter not in mistake_count_for_line:
                    mistake_count_for_line[target_letter] = 0
                mistake_count_for_line[target_letter] += 1
        else:
            if target_letter not in mistake_count_for_line:
                mistake_count_for_line[target_letter] = 0
            mistake_count_for_line[target_letter] += 1

    return mistake_count_for_line


def update_misspelled_letters(mistake_count_for_line, misspelled_letters_dict):
    """Updates the dictionary of misspelled letters based on current line's mistakes."""
    for letter, count in mistake_count_for_line.items():
        if letter not in misspelled_letters_dict:
            misspelled_letters_dict[letter] = 0
        misspelled_letters_dict[letter] += count

def sort_list_of_tuples(data_list, index):
    """Sorts a list of tuples in descending order based on the specified index."""
    for current_index, _ in enumerate(data_list):  # Loop through the list with index
        max_index = current_index  # Assume the first unsorted element is the largest
        for unsorted_index in range(current_index + 1, len(data_list)):
            if data_list[unsorted_index][index] > data_list[max_index][index]:  # Compare based on the specified index
                max_index = unsorted_index  # Update max_index if a larger value is found
        # Swap the found maximum element with the first unsorted element
        data_list[current_index], data_list[max_index] = data_list[max_index], data_list[current_index]


def sort_dictionary(misspelled_letters_dict):
    """Sorts and displays the misspelled letters in descending order of frequency."""
    # Convert the dictionary to a list of (letter, count) pairs
    misspelled_letters_list = []
    for letter in misspelled_letters_dict:  # Loop through each letter in the dictionary
        count = misspelled_letters_dict[letter]  # Get the count for the current letter
        misspelled_letters_list.append((letter, count))  # Add the pair to the list

    sort_list_of_tuples(misspelled_letters_list, 1)

    # Print the sorted list
    print("\nMisspelled Characters:")
    for letter, count in misspelled_letters_list:
        print(f"{letter}: {count}")


def start_game(lines, tot_letters, tot_words):
    """Function starts the typing game and calculates word and character precision."""
    result = []
    total_correct_words = 0
    total_wrong_words = 0
    total_mistakes = 0
    misspelled_letters_dict = {}

    word_pres_till_now = 100.0  # Assume 100% word precision initially
    letter_pres_till_now = 100.0

    print(f"Words-precision till now: {word_pres_till_now:.2f}%")
    print(f"Chars-precision till now: {letter_pres_till_now:.2f}%")
    print(f"Misspelled Characters: {misspelled_letters_dict}")

    for line in lines:
        print("----------------------------------")
        print("\nSkriv följande rad:")
        print(line.strip())
        user_input = input("--> ").strip()

        tot_letters, tot_words = words_letters_returned(lines)

        # Calculate word precision for the current line
        correct_word_count, mistaken_word_this_line, correct_words_in_line = calculate_word_precision(line, user_input)
        total_correct_words += correct_word_count
        total_wrong_words += mistaken_word_this_line

        word_pres_till_now = ((tot_words - total_wrong_words) / tot_words) * 100

        # Calculate letter precision for the current line
        mistake_count_for_line = calculate_letter_precision(line, user_input, correct_words_in_line)
        update_misspelled_letters(mistake_count_for_line, misspelled_letters_dict)

        mistake_count = sum(mistake_count_for_line.values())
        total_mistakes += mistake_count
        letter_pres_till_now = ((tot_letters - total_mistakes) / tot_letters) * 100 if tot_letters > 0 else 0

        # Sort the dictionary

        # Display current precision
        print(f"Words-precision till now: {word_pres_till_now:.2f}%")
        print(f"Chars-precision till now: {letter_pres_till_now:.2f}%")
        # print(f"Misspelled Characters: {sorted_dictionary}")
        sort_dictionary(misspelled_letters_dict)

    name = input("DONE! Kindly, enter your name to save your score: ")
    total_word_precision = ((tot_words - total_wrong_words) / tot_words) * 100
    total_letter_precision = ((tot_letters - total_mistakes) / tot_letters) * 100 if tot_letters > 0 else 0

    result.append((name, total_word_precision, total_letter_precision))
    save_result(result)


def save_result(result):
    """Function saves the results in 'score.txt' file"""
    with open("score.txt", 'a', encoding='utf-8') as filehandle:
        for name, total_word_precision, total_letter_precision in result:
            filehandle.write(f"{name}: Ordprecision: {total_word_precision:.2f}%, Teckenprecision: {total_letter_precision:.2f}%\n")

def show_results(filename:Path):
    """Function reads the results from 'score.txt' file and displays them sorted by word precision."""
    print("\nResults:")
    scores = []  # Initialize a list to hold the scores

    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()  # Strip whitespace from the line

            # Split the line into components
            name, precision_info = line.split(": ", 1)  # Split into name and the rest of the string
            total_word_precision = precision_info.split(", ")[0]  # Get the word precision part
            total_letter_precision = precision_info.split(", ")[1]  # Get the letter precision part

            # Extract and convert precision to float
            word_precision = float(total_word_precision.split(": ")[1][:-1])
            letter_precision = float(total_letter_precision.split(": ")[1][:-1])

            scores.append((name, word_precision, letter_precision))  # Append to the scores list

    # Sort the scores based on total word precision (index 1)
    sort_list_of_tuples(scores, 1)  # Sort by total word precision

    # Display sorted results
    for name, word_precision, letter_precision in scores:
        print(f"{name}: Ordprecision: {word_precision:.2f}%, Teckenprecision: {letter_precision:.2f}%")
