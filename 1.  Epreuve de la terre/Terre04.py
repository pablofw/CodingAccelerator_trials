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
def retrieve_start_letter_from_args() -> str:
    import sys
    if len(sys.argv) != 2 or not is_valid_lowercase_letter(sys.argv[1]):
        print("Error: Please provide a single lowercase letter.")
        sys.exit(1)
    return sys.argv[1]

# --------------- Resolution --------------- #
def run_alphabet_generator_from_letter():
    start_letter = retrieve_start_letter_from_args()
    result = get_alphabet_from_letter(start_letter)
    print(result)

# --------------- Result Display / Execution --------------- #
run_alphabet_generator_from_letter()