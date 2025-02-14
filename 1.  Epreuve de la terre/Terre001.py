# alphabet
'''
# V1 
alphabet = "abcdefghijklmnopqrstuvwxyz"

for lettre in alphabet:
    print(lettre, end='')
print()  
print()
'''
# V2
# --------------- Utilities --------------- #
def generate_alphabet():
    ascii_a = ord("a")
    ascii_z = ord("z")
    alphabet = ""
    for ascii_code in range(first_ascii, last_ascii + 1):
        alphabet += chr(ascii_code)
    return alphabet

# --------------- Error handling --------------- #
# --------------- Parsing & Data Retrieval  --------------- #
# --------------- Resolution --------------- #
def display_alphabet():
    result = generate_alphabet()
    if result == "abcdefghijklmnopqrstuvwxyz":
        print(result)
    else:
        print("Error")

# --------------- Result Display / Execution --------------- #
display_alphabet()