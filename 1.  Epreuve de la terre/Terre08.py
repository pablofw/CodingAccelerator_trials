# Taille d’une chaîne
# --------------- Utilities --------------- #
import sys

def count_characters(input_string: str) -> int:
    count = 0
    for char in input_string:
        count += 1
    return count

# --------------- Error handling --------------- #
def is_valid_string_chain(arguments) -> bool:
    return len(arguments) == 2 and isinstance(arguments[1], str) and arguments[1].strip() != ""
    
# --------------- Parsing & Data Retrieval  --------------- #
def get_arguments():
    return sys.argv
    
# --------------- Resolution --------------- #
def process_count_characters():
arguments = get_arguments()
if not is_valid_string_chain(arguments):
    print("Error")
    sys.exit(1)
return count_characters(arguments[1])

# --------------- Result Display / Execution --------------- #
def display_nb_characters():
    result = process_count_characters()
    print(result)
    
display_nb_characters()
