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
# Utilities 
def generate_alphabet():
    first_ascii = ord("a")
    last_ascii = ord("z")
    alphabet = ""
    for ascii_code in range(first_ascii, last_ascii + 1):
        alphabet += chr(ascii_code)
    return alphabet

# Error handling 
def is_valid_alphabet(alphabet):
    reference_alphabet_FR = "abcdefghijklmnopqrstuvwxyz"
    return alphabet == reference_alphabet_FR

# Parsing & Data Retrieval 
def get_alphabet():
    alphabet = generate_alphabet()
    return alphabet if is_valid_alphabet(alphabet) else None 

# Resolution
def display_alphabet():
    result = get_alphabet()
    if result:
        print(result)
    else:
        print("Error")

# Result Display
display_alphabet()