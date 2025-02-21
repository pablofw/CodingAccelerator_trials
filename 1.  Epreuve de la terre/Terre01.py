# alphabet
'''
Goals :
- Applying clean code concepts (STP, DRY, lisibility...)
- Training algorithmic skills
- Discovering ASCII range, chr() & ord()
- Using coherent loops 
'''

# --------------- Utilities --------------- #
def generate_alphabet() -> str:
    """
    Generate a string containing the lowercase English alphabet.
    """
    ascii_a = ord("a")
    ascii_z = ord("z")
    alphabet = ""
    for ascii_code in range(ascii_a, ascii_z + 1):
        alphabet += chr(ascii_code) 
    return alphabet

# --------------- Error handling --------------- #
# --------------- Parsing & Data Retrieval  --------------- #
# --------------- Resolution --------------- #
def display_alphabet():
    print(generate_alphabet(), end="\n")

# --------------- Result Display / Execution --------------- #
display_alphabet()
