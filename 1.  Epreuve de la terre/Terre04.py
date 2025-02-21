# The alphabet from _
'''
Goals:
- String manipulation
- Using coherent loops 
- Discovering index
- Applying clean code concepts
'''

# --------------- Utilities --------------- #
import sys

def generate_lowercase_alphabet() -> str:
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
    alphabet = generate_lowercase_alphabet()
    start_index = alphabet.index(start_letter)

    subset_alphabet = ""
    for i in range (start_index, len(alphabet)):
        subset_alphabet += alphabet[i]
    
    return subset_alphabet

# --------------- Error handling --------------- #
def is_valid_lowercase_letter_argument(arguments: list) -> bool:
    """
    Validate that the input is a single lowercase letter.
    """
    if len(arguments) != 1:
        return False
    start_letter = arguments[0]
    is_single_character = len(start_letter) == 1  
    is_lowercase_letter = ('a' <= start_letter <= 'z')
    return is_single_character and is_lowercase_letter

# --------------- Parsing & Data Retrieval --------------- #
def get_arguments():
    """
    Extract arguments from command line input, without path.
    """
    return sys.argv[1:]
    
# --------------- Resolution --------------- #
def process_alphabet_generator_from_letter():
    arguments = get_arguments()
    if not is_valid_lowercase_letter_argument(arguments):
        return None
    start_letter = arguments[0]
    alphabet_extract = get_alphabet_from_letter(start_letter)
    return alphabet_extract

# --------------- Result Display / Execution --------------- #
print(process_alphabet_generator_from_letter())
