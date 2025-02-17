# Number's power
# --------------- Utilities --------------- #
import sys

def compute_power(base: int, exponent: int) -> int:
    power_result = 1
    for i in range(exponent):
        power_result *= base
    return power_result

# --------------- Error handling --------------- #
def is_valid_integer(value: str) -> bool:
    return value.lstrip("-").isdigit()


# --------------- Parsing & Data Retrieval --------------- #
def get_input_arguments():
    return sys.argv[1:]

# --------------- Resolution --------------- #
def process_compute_power():  
    arguments = get_input_arguments()
    if len(arguments) != 2:
        print("Error: Provide exactly two integer arguments.")
        sys.exit(1)
    for arg in arguments:
        if not is_valid_integer(arg):
            print("Error: not a valid integer")
            sys.exit(1)
            
    base = int(arguments[0])
    exponent = int(arguments[1])
    if exponent < 0:
        print("Error: The exponent must be a non-negative integer.")
        sys.exit(1)
        
    power_result = compute_power(base, exponent)
    return power_result   

# --------------- Result Display / Execution --------------- #
def display_power_result():
    power_result = process_compute_power()
    print(power_result)

display_power_result()
