# Divisions

import sys

# Check qu'on a bien juste 2 arguments
if len(sys.argv) != 3:
    print("erreur.")
    sys.exit(1)

try:
    # Récup des deux nb, et check si cest bien des nb
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
    # Check division interdite
    if num2 == 0:
        print("Division par 0 interdite, retourne en 6ème chef")
    else:
        # Calcul et affichage du résultat et du reste
        print(f"résultat: {num1 // num2}")
        print(f"reste: {num1 % num2}")

except ValueError:
    print("erreur.")  # Gère le cas où les arguments ne sont pas des nombres





# --------------- Utilities --------------- #
import sys

def is_integer(value: str) -> bool:
    """Check if a string is a valid integer."""
    return value.lstrip('-').isdigit()

# --------------- Error handling --------------- #
def validate_inputs(arguments: list[str]) -> tuple[int, int] | str:
    """Validate and parse inputs, returning integers if valid, else an error message."""
    if len(arguments) != 2:
        return "erreur."
    
    dividend, divisor = arguments

    if not is_integer(dividend) or not is_integer(divisor):
        return "erreur."

    dividend, divisor = int(dividend), int(divisor)

    if divisor == 0 or dividend < divisor:
        return "erreur."

    return dividend, divisor

# --------------- Resolution --------------- #
def compute_division(dividend: int, divisor: int) -> tuple[int, int]:
    """Compute quotient and remainder of an integer division."""
    quotient = dividend // divisor
    remainder = dividend % divisor
    return quotient, remainder

# --------------- Result Display / Execution --------------- #
def main():
    result = validate_inputs(sys.argv[1:])
    
    if isinstance(result, str):  # Error case
        print(result)
        return

    dividend, divisor = result
    quotient, remainder = compute_division(dividend, divisor)

    print(f"résultat: {quotient}")
    print(f"reste: {remainder}")

if __name__ == "__main__":
    main()
