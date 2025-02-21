# Odd or even
'''
Goals:
- String manipulation
- Using coherent loops 
- Discovering index
- Applying clean code concepts
'''

# --------------- Utilities --------------- #
import sys

# --------------- Error handling --------------- #
def is_valid_integer(value: str) -> bool:
    return value.lstrip("-").isdigit() #consider also negative

# --------------- Parsing & Data Retrieval  --------------- #
def get_integer_argument():
    if len(sys.argv) == 2:
        return sys.argv[1]  
    else:
        return None

# --------------- Resolution --------------- #
def is_even_or_odd() -> str:
    sys_arguments = get_integer_argument()
    if sys_arguments is None or not is_valid_integer(sys_arguments):
            return "Tu ne me la mettras pas à l’envers."
    number_tested = int(sys_arguments)
    if number_tested % 2 == 0:
        return "Even"
    else: 
        return "Odd"
    
# --------------- Result Display / Execution --------------- #
def display_even_or_odd():
    result = is_even_or_odd()
    print(result)

display_even_or_odd()

