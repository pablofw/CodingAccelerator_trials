# alphabet
# --------------- Utilities --------------- #
def generate_alphabet():
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
    print(generate_alphabet())

# --------------- Result Display / Execution --------------- #
display_alphabet()
