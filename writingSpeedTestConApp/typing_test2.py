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
    if lines:
        combined_string = ''.join(lines).replace(' ', '').replace("\n", "")

        total_words_count = count_words(lines)
        tot_words = sum(len(inner_list) for inner_list in total_words_count)

        tot_letters =  len(combined_string)

        print(f"Total words count: {tot_words}")
        print(f"Total letters count: {tot_letters}")
    return tot_letters, tot_words


def total_letters(words_per_line):
    """Gets the letters in all the words in the lines
    """
    letters = []
    for word in words_per_line:
        for letter in word:
            letters.append(letter)
    return letters

# def compare_user_input( lines, total_letters_in_file):
#     """
#     Compares user input with the letters from count_letters.
#     Returns lists of correctly spelled letters, mistakes, count of correct vs. incorrect letters,
#     precision as a percentage of correctly spelled letters, and user accuracy.
#     """
#     for line in lines:
#         # Convert user input to a list of letters
#         print("\nSkriv följande rad:")
#         print(line.strip())  # Display the expected line
#         user_input = input("--> ").strip()  # Get the user's input

#         user_letters = [char for char in user_input]

#         # Get the list of letters from count_letters
#         target_letters = total_letters(line)

#         # Initialize lists and counters
#         correct_letters = []
#         user_letter_mistakes = []
#         correct_count = 0
#         mistake_count = 0
#         total_characters_needed = len(target_letters)

#         # Loop through the full range of target_letters
#         for i in range(total_characters_needed):
#             if i < len(user_letters):  # Ensure index is within user input range
#                 if user_letters[i] == target_letters[i]:  # Correct letter
#                     correct_letters.append(user_letters[i])
#                     correct_count += 1
#                 else:  # Incorrect letter
#                     user_letter_mistakes.append((user_letters[i], target_letters[i]))
#                     mistake_count += 1
#             else:
#                 # User input is missing letters at the end
#                 user_letter_mistakes.append(('_', target_letters[i]))  # "_" represents missing letter
#                 mistake_count += 1

#         # Calculate precision of correct letters
#         total_char_precision = (correct_count / total_characters_needed) * 100 if total_characters_needed > 0 else 0

#         # Calculate accuracy based on total_letters_in_file
#         accuracy = ((total_letters_in_file - mistake_count) / total_letters_in_file) * 100 if total_letters_in_file > 0 else 0

#         print(f"Total correct letters: {correct_count}")
#         print(f"Total incorrect letters: {mistake_count}")
#         print(f"Total characters needed: {total_characters_needed}")
#         print(f"Total characters in file: {total_letters_in_file}")
#         print(f"Correct letters: {correct_letters}")
#         print(f"Mistakes: {user_letter_mistakes}")

#     return correct_letters, user_letter_mistakes, correct_count, mistake_count, total_char_precision, accuracy


def start_game(lines,tot_letters, tot_words):
    """Function starts the typing game and calculates word and character precision."""

    # Get total words and letters before starting the game
    (tot_letters, tot_words) = words_letters_returned(lines)
    
    result = []  # List to store individual line results
    total_correct_words = 0  # Total number of correctly typed words
    total_words_needed = 0  # Total number of expected words across lines
    # mistake_count = 0
    total_wrong_words = 0
    # total_correct_letters = 0
    total_mistakes = 0
    for line in lines:
        print("----------------------------------")
        print("\nSkriv följande rad:")
        print(line.strip())  # Display the expected line
        user_input = input("--> ").strip()  # Get the user's input

        # Split into words and count the necessary/typed words
        correct_words = line.strip().split()
        user_words = user_input.split()
        total_words_needed += len(correct_words)

        # print(f"user_words: {user_words}")
        # print(f"correct_words: {correct_words}")
        # print(f"correct_words2: {correct_words2}")
        # Initialize correct and incorrect counts
        correct_word_count = 0
        wrong_letters_count = 0
        correct_words_in_line = []
        wrong_words_in_line = []
        
        for i in range(len(correct_words)):
            if i < len(user_words) and user_words[i] == correct_words[i]:
                correct_word_count += 1
                correct_words_in_line += [user_words[i]]
            else:
                if i < len(user_words):
                    # If the word exists but is incorrect
                    wrong_letters_count += len(user_words[i])
                    wrong_words_in_line += [user_words[i]]
                # If the word does not exist, count all letters as mistakes
                if i >= len(user_words) or len(user_words[i]) != len(correct_words[i]):
                    wrong_letters_count += len(correct_words[i])
                    # wrong_words_in_line.append(correct_words[i])

        total_correct_words += correct_word_count
        mistaken_word_this_line = len(correct_words) - correct_word_count
        total_wrong_words += mistaken_word_this_line
        word_pres_till_now = ((tot_words - total_wrong_words) / tot_words) * 100
        print(f"Total words presi so far: {word_pres_till_now:2f}\n")
        print(f"Total correct words so far: {total_correct_words}")
        print(f"Total correct stored words so far: {correct_words_in_line}")
        print(f"Total wrong words so far: {total_wrong_words}\n")
        print(f"Correct words in this line: {correct_word_count}")
        print(f"Mistaken words in this line: {mistaken_word_this_line}") # remove mayybe
        print("--------------------------------------------------")
        # Debugging prints
        # print(f"Results:  {tot_words - mistaken_word_this_line}/{tot_words}")
        # print(f"Total words in file: {tot_words}")
        
        # check against letters and stoe in a list        
        # user_letters = total_letters(user_input)
        # target_letters = ''.join(line).replace(' ', '').replace("\n", "")

        # total_letters_in_file = 44
        ## Leetters calculations start here under
        # Convert user input to a list of letters
        # user_letters = [char for char in user_input]
        # user_letters = []
        # for char in user_input:
        #     user_letters.append(char)
        correct_words_string = ' '.join(correct_words_in_line)

        # Now use the string in the replace method
        user_input_after_removal = user_input.replace(correct_words_string, "").replace(" ", "")

        # Create a list of letters from the modified user input
        user_letters = list(user_input_after_removal)

        # user_letters = list(user_input.replace(" ", ""))

        # target_letters = total_letters(correct_words)
        # target_letters = list(line.strip().replace(" ", ""))
        modified_line = line.strip().replace(correct_words_string, "").replace(" ", "")
        target_letters = list(modified_line)


        # Initialize lists and counters
        # correct_letters = []
        # user_letter_mistakes = []

        # mistake_count = 0
        # correct_count = 0
        # # total_characters_needed = len(target_letters)

        # # Loop through the full range of target_letters
        # for i in range(len(target_letters)):
        #     if i < len(user_letters):
        #         if user_letters[i] == target_letters[i]:
        #             correct_count += 1
        #         else:
        #             mistake_count += 1
        #     else:
        #         # If the user input is missing letters at the end
        #         mistake_count += 1

        # if len(user_letters) < len(target_letters):
        #     mistake_count += len(target_letters) - len(user_letters)
        # Initialize counts
        mistake_count = 0
        correct_count = 0

        # Initialize lists to store correct letters and mistakes
        correct_count_letters = []  # List to store correct letters
        mistake_count_letters = []  # List to store mistaken letters

        # Loop through the full range of target_letters
        for i in range(len(target_letters)):
            if i < len(user_letters):
                if user_letters[i] == target_letters[i] and user_letters[i] == target_letters[i]:
                    correct_count += 1
                    correct_count_letters.append(user_letters[i])  # Add to correct letters list
                else:
                    mistake_count += 1
                    mistake_count_letters.append(user_letters[i])  # Add to mistakes list
            else:
                # If the user input is missing letters at the end
                mistake_count += 1
                # Consider the missing letters as mistakes; you can choose how to represent them
                mistake_count_letters.append('_')  # Represent missing letters with an underscore or any placeholder
        total_mistakes += mistake_count
        # Add extra mistakes for missing letters if user_letters is shorter than target_letters
        # if len(user_letters) < len(target_letters):
        #     additional_mistakes = len(target_letters) - len(user_letters)
        #     mistake_count += additional_mistakes
        #     mistake_count_letters.extend(['_'] * additional_mistakes)  # Add placeholders for missing letters

        # Debugging outputs
        print(f"user_letters: {user_letters}")
        print(f"target_letters: {target_letters}")

        print(f"Correct letters: {correct_count_letters}")
        print(f"Mistake letters: {mistake_count_letters}")
        print(f"Total mistakes: {total_mistakes}")
        print(f"Correct letters: {correct_count}")

        # Total precision calculations
        if mistake_count > 0:
            total_char_precision = ((tot_letters - total_mistakes) / tot_letters) * 100 if tot_letters > 0 else 0
            accuracy = ((tot_letters - total_mistakes) / tot_letters) * 100 if tot_letters > 0 else 0
            # print(f"Correct Letter precision so far: {total_char_precision:.2f}%")


        print(f"Correct Letter precision so far: {total_char_precision:.2f}%")
        print(f"Correct letters so far: {correct_count}")
        print(f"Mistakes in this line: {mistake_count}")
        print(f"User accuracy so far: {accuracy:.2f}%")

        # Print results for tracking
        # print(f"Total mistakes so far: {total_mistakes}")
        # print(f"Wrong letter count: {wrong_letters_count}")
        # print(f"Correctly typed letters count: {correct_letter_count}")

        # Calculate precision
        # char_pres_till_now =

        # Output wrong letters sorted by frequency
        # sorted_wrong_letters = sorted(wrong_letters_count.items(), key=lambda item: (-item[1], item[0]))

        # print("Felstavade tecken:")
        # for letter, count in sorted_wrong_letters:
        #     print(f"   {letter}: {count}")

        # print(f"Teckenprecision: {char_pres_till_now:.2f}%")

        
        

        # Precision calculations
        print(f"Words-precision för föregående rad: {word_pres_till_now:.2f}%")
        print(f"Chars-precision för föregående rad: {accuracy:.2f}%")

    # Calculate cumulative precision values
    name = input("Ange ditt namn: ")
    total_word_precision = (total_correct_words / tot_words) * 100 if tot_words > 0 else 0
    
    # Maybe hint here under ¨¨
    accuracy = ((tot_letters - mistake_count) / tot_letters) * 100 if tot_letters > 0 else 0

    # total_char_precision = (correct_letter_count / tot_letters) * 100 if tot_letters > 0 else 0
    
    # print(f"\nTotal ordprecision: {total_word_precision:.2f}%")
    # print(f"Total teckenprecision: {total_char_precision:.2f}% \n")

    # sorted_wrong_letters = sorted(wrong_letters_count.items(), key=lambda item: (-item[1], item[0]))

    # print("Felstavade tecken:")
    # for letter, count in sorted_wrong_letters:
    #     print(f"   {letter}: {count}")

    # print(f"Teckenprecision: {char_pres_till_now:.2f}%")

    # Save results to file
    # result.append((name, total_word_precision, char_pres_till_now))
    # result.append((name, total_word_precision, total_char_precision))
    result.append((name, total_word_precision, accuracy))
    save_result(result)




def save_result(result):
    """Function saves the results in 'score.txt' file"""
    with open("score.txt", 'a', encoding='utf-8') as filehandle:
        for name, word_precision, char_precision in result:
            filehandle.write(f"{name}: Ordprecision: {word_precision:.2f}%, Teckenprecision: {char_precision:.2f}%\n")

def show_results():
    """Function reads the results from 'score.txt' file"""
    print("\nResultat:")
    with open('score.txt', 'r', encoding='utf-8') as file:
        scores = file.readlines()
        for score in scores:
            print(score.strip())