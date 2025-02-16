# The alphabet from _
# --------------- Utilities --------------- #
def get_alphabet_from_letter(start_letter: str) -> str:
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    start_index = alphabet.index(start_letter)
    return alphabet[start_index:]

# --------------- Error handling --------------- #
def is_valid_lowercase_letter(argument: str) -> bool:
    is_single_character = len(argument) == 1  
    is_lowercase_letter = 'a' <= argument <= 'z'  
    return is_single_character and is_lowercase_letter

# --------------- Parsing & Data Retrieval --------------- #
def retrieve_start_letter_from_args():
    import sys
    if len(sys.argv) == 2:
        return sys.argv[1] 
    else:
        return None

# --------------- Resolution --------------- #
def process_alphabet_generator_from_letter():
    start_letter = retrieve_start_letter_from_args()

    if not is_valid_lowercase_letter(start_letter):
        return "Error: Please provide a single lowercase letter."

    alphabet_extract = get_alphabet_from_letter(start_letter)
    
    return alphabet_extract

# --------------- Result Display / Execution --------------- #
def display_alphabet_from_letter():
    result = process_alphabet_generator_from_letter()
    print(result)

display_alphabet_from_letter()