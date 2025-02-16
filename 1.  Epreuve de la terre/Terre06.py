# Division
# --------------- Utilities --------------- #
import sys

# --------------- Error Handling --------------- #
def is_valid_division_arguments(list_sys_arguments) -> bool:

    if len(list_sys_arguments) != 2:
        return False

    numerator, denominator = list_sys_arguments

    if not numerator.lstrip("-").isdigit() or not denominator.lstrip("-").isdigit():
        return False

    if int(denominator) == 0:
        return False

    return True

# --------------- Parsing & Data Retrieval --------------- #
def get_input_arguments():
    return sys.argv[1:]

# --------------- Resolution --------------- #
def compute_division_result():
    arguments = get_input_arguments()

    if not is_valid_division_arguments(arguments):
        return "Error."

    numerator, denominator = map(int, arguments)
    quotient = numerator // denominator
    remainder = numerator % denominator

    return quotient, remainder

# --------------- Result Display / Execution --------------- #
def display_division_results():

    results = compute_division_result()

    if isinstance(results, str):  # Error case
            print(results)
    else:
        quotient, remainder = results
        print(f"quotient: {quotient}")
        print(f"remainder: {remainder}")

display_division_results()
