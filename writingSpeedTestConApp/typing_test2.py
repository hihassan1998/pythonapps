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

# def count_letters(word_per_line):
#     """Counts the total occurrences of letters in the list of words."""
#     total_letter_count = sum(len(word) for word in word_per_line)
#     return total_letter_count

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

# def total_letters(lines):
#     """ Counts the letters in all the words in the lines
#     """
#     letters_per_lines = []
#     words_per_line = count_words(lines)
#     for word in words_per_line:
#         for letter in word:
#             letters_per_lines.append(letter)
#     return letters_per_lines

def total_letters(words_per_line):
    """ Counts the letters in all the words in the lines
    """
    letters = []
    for word in words_per_line:
        for letter in word:
            letters.append(letter)
    return letters

# def compare_user_input(user_input, lines):
#     """
#     Compares user input with the letters from count_letters.
#     Returns a list of mistakes and the number of occurrences.
#     """
#     # Convert user input to a list of letters
#     user_letters = [char for char in user_input]
    
#     # Get the list of letters from count_letters
#     target_letters = total_letters(lines)
    
#     # Initialize the list for mistakes and a dictionary to count occurrences
#     user_letter_mistakes = []
#     mistake_counts = {}

#     # Loop through the range of user_letters
#     for i in range(len(user_letters)):
#         if i < len(target_letters):  # Ensure we stay within bounds
#             if user_letters[i] != target_letters[i]:  # Compare each letter
#                 # Store the mistake letter
#                 user_letter_mistakes.append(user_letters[i])
                
#                 # Count occurrences of the mistake letter
#                 if user_letters[i] in mistake_counts:
#                     mistake_counts[user_letters[i]] += 1
#                 else:
#                     mistake_counts[user_letters[i]] = 1

#     return user_letter_mistakes, mistake_counts


def start_game(lines,tot_letters, tot_words):
    """Function starts the typing game and calculates word and character precision."""
    
    # Get total words and letters before starting the game
    tot_letters, tot_words = words_letters_returned(lines)
    
    result = []  # List to store individual line results
    total_correct_words = 0  # Total number of correctly typed words
    total_words_needed = 0  # Total number of expected words across lines
    
    misspelled_chars = {}
    # total_correct_characters = 0  # Correct characters typed
    total_characters_needed = 0  # Total characters expected across lines
    # total_words_in_file = count_words(lines)
    
    total_mistakes = 0
    mistake_count = 0
    
    for line in lines:
        
        # print(f"Words-precision för denna rad: {word_pres_till_now:.2f}%")
        # print(f"Chars-precision för denna rad: {this_char_precision:.2f}%")
        # print("Felstavade Tecken:")
        # print("THE VAR THAT STORES THE MISTAKEN LETTERS WITH THEIR COUNTS")
        # print(misspelled_chars)
        # print(f"You must type correctly a total of {tot_letters} letters and {tot_words} words to get 100% precision")
        print("----------------------------------")
        
        print("\nSkriv följande rad:")
        print(line.strip())  # Display the expected line
        user_input = input("--> ").strip()  # Get the user's input
        
        # Split into words and count the necessary/typed words
        correct_words = line.strip().split()
        user_words = user_input.split()
        
        total_words_needed += len(correct_words)

        # Initialize correct and incorrect counts
        correct_word_count = 0
        wrong_letters_count = 0

        # Check words for correctness
                # correct_word_count = sum(1 for i in range(len(correct_words)) 
        #                           if i < len(user_words) and user_words[i] == correct_words[i])
        
        for i in range(len(correct_words)):
            if i < len(user_words) and user_words[i] == correct_words[i]:
                correct_word_count += 1
            else:
                if i < len(user_words):
                    # If the word exists but is incorrect
                    wrong_letters_count += len(user_words[i])
                # If the word does not exist, count all letters as mistakes
                if i >= len(user_words) or len(user_words[i]) != len(correct_words[i]):
                    wrong_letters_count += len(correct_words[i])  # All letters of this word are wrong

        total_correct_words += correct_word_count
        
        # add a count for wrong number of words incearing under the loop
        mistaken_word_this_line = len(correct_words) - correct_word_count
        
        # Debugging prints
        # print(f"Results:  {tot_words - mistaken_word_this_line}/{tot_words}")
        # print(f"Total words in file: {tot_words}")
        # print(f"Correct words in this line: {correct_word_count}")
        # print(f"Mistaken words in this line: {mistaken_word_this_line}")
        
        print(f"Total correct words so far: {total_correct_words}")
        
        word_pres_till_now = ((tot_words - mistaken_word_this_line) / tot_words) * 100
        print(f"Total words presi so far: {word_pres_till_now:2f}")
        
        # check against letters and stoe in a list        
        user_letters = total_letters(user_input)  # Converts user input to a list of letters
        target_letters = ''.join(line).replace(' ', '').replace("\n", "")

        # Initialize lists and dictionaries to store correct and incorrect letters
        correct_letters = []
        wrong_letters_count = {}  # Dictionary to count how many times each expected letter was mistyped
        correct_letter_count = 0  # Count correctly typed letters

        # Count mistakes and track specific mistyped letters
        for i in range(len(target_letters)):
            if i < len(user_letters):  # Ensure index is within user input range
                if user_letters[i] == target_letters[i]:  # Correct letter
                    correct_letters.append(user_letters[i])  # Add to correct letters
                    correct_letter_count += 1  # Count correctly typed letters
                else:  # Incorrect letter
                    total_mistakes += 1
                    
                    # Count the expected letter as mistyped
                    wrong_letter = target_letters[i]
                    wrong_letters_count[wrong_letter] = wrong_letters_count.get(wrong_letter, 0) + 1
                    
                    # If user typed a letter that wasn't expected (ignore spaces)
                    if user_letters[i] != ' ':
                        # Increment the wrong letter count for user input (optional based on your logic)
                        misspelled_chars[user_letters[i]] = misspelled_chars.get(user_letters[i], 0) + 1
            else:
                # User input is missing letters at the end
                total_mistakes += 1  # Count missing letters as mistakes
                # Increment wrong letter count for missing expected letters
                wrong_letter = target_letters[i]
                wrong_letters_count[wrong_letter] = wrong_letters_count.get(wrong_letter, 0) + 1

        # Total characters without spaces
        total_characters_needed += len(target_letters)  # Total expected characters without spaces

        # Print results for tracking
        print(f"Total mistakes so far: {total_mistakes}")
        print(f"Wrong letter count: {wrong_letters_count}")
        print(f"Correctly typed letters count: {correct_letter_count}")

        # Calculate precision
        char_precision = (correct_letter_count / tot_letters) * 100 if tot_letters > 0 else 0

        # Output wrong letters sorted by frequency
        sorted_wrong_letters = sorted(wrong_letters_count.items(), key=lambda item: (-item[1], item[0]))

        print("Felstavade tecken:")
        for letter, count in sorted_wrong_letters:
            print(f"   {letter}: {count}")

        print(f"Teckenprecision: {char_precision:.2f}%")

        
        

        # Precision calculations
        # word_pres_till_now = ((tot_words - mistaken_word_this_line) / tot_words) * 100
        # char_pres_till_now = (total_correct_characters / total_characters_needed) * 100 if total_characters_needed > 0 else 0

        print(f"Words-precision för föregående rad: {word_pres_till_now:.2f}%")
        # print(f"Chars-precision för föregående rad: {char_pres_till_now:.2f}%")

    # Calculate cumulative precision values
    name = input("Ange ditt namn: ")
    total_word_precision = (total_correct_words / tot_words) * 100 if tot_words > 0 else 0
    
    # Maybe hint here under ¨¨
    # total_char_precision = (mistake_count / total_characters_needed) * 100 if total_characters_needed > 0 else 0
    total_char_precision = (correct_letter_count / tot_letters) * 100 if tot_letters > 0 else 0
    
    print(f"\nTotal ordprecision: {total_word_precision:.2f}%")
    print(f"Total teckenprecision: {total_char_precision:.2f}% \n")

    sorted_wrong_letters = sorted(wrong_letters_count.items(), key=lambda item: (-item[1], item[0]))

    print("Felstavade tecken:")
    for letter, count in sorted_wrong_letters:
        print(f"   {letter}: {count}")

    print(f"Teckenprecision: {char_precision:.2f}%")

    # Save results to file
    result.append((name, total_word_precision, total_char_precision))
    # result.append((name, total_word_precision))
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