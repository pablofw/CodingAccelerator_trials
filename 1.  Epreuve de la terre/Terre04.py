# The alphabet from _
'''
Goals:
- String manipulation
- Using coherent loops 
- Applying clean code concepts
'''

# --------------- Utilities --------------- #
import sys

def get_arguments():
    """
    Extract arguments from command line input, without path.
    """
    return sys.argv[1:]

def generate_alphabet() -> str:
    """
    Generate a string containing the lowercase English alphabet.
    """
    ascii_a = ord("a")
    ascii_z = ord("z")
    alphabet = ""
    for ascii_code in range(ascii_a, ascii_z + 1):
        alphabet += chr(ascii_code) 
    return alphabet

def get_alphabet_from_letter(start_letter: str) -> str:
    """
    Generate the alphabet starting from a specific letter
    """
    alphabet = generate_alphabet()
    start_letter_found = False
    subset_alphabet = ""
    for letter in alphabet:
        if letter == start_letter:
            start_letter_found = True
        if start_letter_found:
            subset_alphabet += letter

    return subset_alphabet

# --------------- Error handling --------------- #
def is_valid_lowercase_letter_argument(arguments: list) -> bool:
    if len(arguments) != 1:
        print("Error: Please provide only one entry.")
        return None
    start_letter = arguments[0]
    is_single_character = len(start_letter) == 1  
    is_lowercase_letter = 'a' <= start_letter <= 'z'  
    if is_single_character and is_lowercase_letter:
        return True
    else:
        print("Error: Please provide a single lowercase letter.")
        return False 

# --------------- Parsing & Data Retrieval --------------- #

# --------------- Resolution --------------- #
def process_alphabet_generator_from_letter():
    start_letter = get_arguments()
    if not start_letter or not is_valid_lowercase_letter_argument(start_letter):
        return None
    alphabet_extract = get_alphabet_from_letter(start_letter)
    return alphabet_extract

# --------------- Result Display / Execution --------------- #
print(process_alphabet_generator_from_letter())