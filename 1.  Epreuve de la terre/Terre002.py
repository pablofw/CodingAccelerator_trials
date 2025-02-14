# Nom du prog
'''
print(__file__.split('/')[-1].split('\\')[-1])
'''
# --------------- Utilities --------------- #
import sys
def get_filename():
    full_path = sys.argv[0]
    filename = ""
    
    for char in full_path:
        if char in ("/", "\\"):
            filename = ""
        else:
            filename += char
            
    return filename
    
# --------------- Error handling --------------- #
def is_valid_filename(filename):
    return isinstance(filename, str) and "." in filename and len(filename) > 0

# --------------- Parsing & Data Retrieval--------------- #
# --------------- Resolution --------------- #
def retrieve_filename(): 
    filename = get_filename()
    return filename if is_valid_filename(filename) else None

# --------------- Result Display --------------- #
def display_filename():
    result = retrieve_filename()
    if result:
        print(result)
    else:
        print("Error")

display_filename()
