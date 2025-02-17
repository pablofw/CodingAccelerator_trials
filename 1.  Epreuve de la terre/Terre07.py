# Invert a character string
# --------------- Utilities --------------- #
import sys

def reverse_string(text: str):
    reversed_text = []  
    for char in text:
        reversed_text = char + reversed_text
    reversed_chain = "".join(reversed_text)
    return reversed_chain

# --------------- Error handling --------------- #
def is_valid_string_chain(arguments) -> bool:
    return len(arguments) == 2 and isinstance(arguments[1], str) and arguments[1].strip() != ""

# --------------- Parsing & Data Retrieval --------------- #
def get_arguments() -> str:
    return sys.argv

# --------------- Resolution --------------- #
def process_reversing_text() -> str:
    arguments = get_arguments()
    if not is_valid_string_chain(arguments):
        print("Error: Please provide a non-empty string as an argument.")
        sys.exit(1)
        
    text = arguments[1]
    return reverse_string(text)

# --------------- Result Display / Execution --------------- #
def display_reversed_string():
    reversed_string = process_reversing_text()
    print(reversed_string)

display_reversed_string()
