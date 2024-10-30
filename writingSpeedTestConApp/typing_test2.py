from pathlib import Path

def read_file(filename:Path):
    """
    Function reads in the file.
    And returns the lines.
    """
    with open(filename, 'r', encoding='utf-8') as filehandle:
        lines = filehandle.readlines()
    return lines

def total_words(lines):
    """
    Function returns a list of all words from the file.
    """
    word_per_line = []
    for words in lines:
        word_per_line.append(words.split())
    return word_per_line

def words_letters_returned(lines):
    """Counts total words and letters,
    printing the lengths of the letters and words.
    """
    # if lines:
    combined_string = ''.join(lines).replace(' ', '').replace("\n", "")

    total_words_count = total_words(lines)
    tot_words = sum(len(inner_list) for inner_list in total_words_count)

    tot_letters =  len(combined_string)

        # print(f"Total words count: {tot_words}")
        # print(f"Total letters count: {tot_letters}")
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
    """
    Function starts the typing game and
    calculates word and letter precision.
    """
    
    result = []  # List to store individual line results
    total_correct_words = 0
    total_wrong_words = 0
    total_mistakes = 0

    for line in lines:
        print("----------------------------------")
        print("\nSkriv följande rad:")
        print(line.strip())  # Print expected line
        user_input = input("--> ").strip()  # Get user's input

        # Get total words and letters in the file
        (tot_letters, tot_words) = words_letters_returned(lines)

        # Start calculating the words:
        # Split into words and count the necessary/typed words
        correct_words = line.strip().split()
        user_words = user_input.split()

        # Initialize correct and incorrect counters
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

        # Start calulating the characters

        correct_words_string = ' '.join(correct_words_in_line)
        user_input_after_removal = user_input.replace(correct_words_string, "").replace(" ", "")
        user_letters = list(user_input_after_removal)
        modified_line = line.strip().replace(correct_words_string, "").replace(" ", "")
        target_letters = list(modified_line)

        # Initialize counters for letter check
        mistake_count = 0
        correct_count = 0

        # Initialize lists to store correct letters and mistakes
        correct_count_letters = []
        mistake_count_letters = []

        # Loop through the full range of target_letters
        for i in range(len(target_letters)):
            if i < len(user_letters):
                if user_letters[i] == target_letters[i]:
                    correct_count += 1
                    correct_count_letters.append(user_letters[i])  # Add to correct letters list
                else:
                    mistake_count += 1
                    mistake_count_letters.append(user_letters[i])  # Add to mistakes list
            else:
                # If the user input is missing letters at the end
                mistake_count += 1
                # Consider the missing letters as mistakes; you can choose how to represent them
                mistake_count_letters.append('')  # Represent missing letters with an underscore or any placeholder
        total_mistakes += mistake_count


        # Debugging outputs
        print(f"user_letters: {user_letters}")
        print(f"target_letters: {target_letters}")
        print("-----------------------------------------------")
        print(f"Correct letters: {correct_count_letters}")
        print(f"Correct letters count in this line: {correct_count}")
        print(f"Mistake letters: {mistake_count_letters}")
        print("-----------------------------------------------")
        print(f"Total mistakes (letters) so far: {total_mistakes}")

        # Total letter precision calculations
        accuracy = ((tot_letters - total_mistakes) / tot_letters) * 100 if tot_letters > 0 else 0
            # print(f"Correct Letter precision so far: {total_char_precision:.2f}%")


        # print(f"Correct Letter precision so far: {total_char_precision:.2f}%")
        print(f"Correct letters so far: {correct_count}")
        print(f"Mistakes in this line: {mistake_count}")
        print("-----------------------------------------------")

        # Precision calculations
        print(f"Words-precision till now: {word_pres_till_now:.2f}%")
        print(f"Chars-precision till now: {accuracy:.2f}%")

    # Calculate cumulative precision values
    name = input("Ange ditt namn: ")
    total_word_precision = (total_correct_words / tot_words) * 100 if tot_words > 0 else 0
    accuracy = ((tot_letters - total_mistakes) / tot_letters) * 100 if tot_letters > 0 else 0

    
    print(f"\nTotal ordprecision: {total_word_precision:.2f}%")
    print(f"Total teckenprecision: {accuracy:.2f}% \n")

    # Save results to file
    result.append((name, total_word_precision, accuracy))
    save_result(result)


def save_result(result):
    """Function saves the results in 'score.txt' file"""
    with open("score.txt", 'a', encoding='utf-8') as filehandle:
        for name, total_word_precision, accuracy in result:
            filehandle.write(f"{name}: Ordprecision: {total_word_precision:.2f}%, Teckenprecision: {accuracy:.2f}%\n")

def show_results():
    """Function reads the results from 'score.txt' file"""
    print("\nResultat:")
    with open('score.txt', 'r', encoding='utf-8') as file:
        scores = file.readlines()
        for score in scores:
            print(score.strip())