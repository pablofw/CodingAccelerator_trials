# Afficheur d'arguments
# --------------- Utilities --------------- #
import sys

# --------------- Error handling --------------- #
def has_input_arguments(arguments):
    return len(arguments) > 0 

# --------------- Parsing & Data Retrieval --------------- #
def get_input_arguments():
    return sys.argv[1:]

# --------------- Resolution --------------- #
def retrieve_input_sys_arguments():
    sys_arguments = get_input_arguments()
    if has_input_arguments(sys_arguments) == False:
        print("Error: No arguments provided.")
        sys.exit(1)
    else: return arguments

# --------------- Result Display --------------- #
def display_result():
    arguments = retrieve_input_sys_arguments()
    for argument in arguments:
        print(argument)

display_result()
