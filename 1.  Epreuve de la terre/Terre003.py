# Afficheur d'arguments
# --------------- Utilities --------------- #

# --------------- Error handling --------------- #
def has_input_arguments(arguments):
    return len(arguments) > 0 

# --------------- Parsing & Data Retrieval --------------- #
def get_input_arguments():
    import sys
    return sys.argv[1:]

# --------------- Resolution --------------- #
def get_validated_input_arguments():
    import sys
    sys_arguments = get_input_arguments()
    if not has_input_arguments(sys_arguments):
        print("Error: No arguments provided.")
        sys.exit(1)
    else: return sys_arguments

# --------------- Result Display / Execution --------------- #
def display_inputs_arguments():
    arguments = get_validated_input_arguments()
    for argument in arguments:
        print(argument)

display_inputs_arguments()
