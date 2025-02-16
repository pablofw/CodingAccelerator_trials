# Odd or even
# --------------- Utilities --------------- #
import sys

# --------------- Error handling --------------- #
def is_valid_integer(value: str) -> bool:
    return value.lstrip("-").isdigit() #consider also negative

# --------------- Parsing & Data Retrieval  --------------- #
def get_integer_argument() -> int:
    if len(sys.argv) != 2:
        print("Tu ne me la mettras pas à l’envers.")
        sys.exit(1)
    
    sys_argument = sys.argv[1]
    if not is_valid_integer(sys_argument):
        print("Tu ne me la mettras pas à l’envers.")
        sys.exit(1)
    
    return int(sys_argument)

# --------------- Resolution --------------- #
def is_even_or_odd() -> bool:
    number_tested = get_integer_argument()
    if number_tested % 2 == 0:
        print("Even")
    else: print("Odd")
    
# --------------- Result Display / Execution --------------- #
is_even_or_odd()