# Nom du prog
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
def is_valid_filename(filename: str) -> bool:
    return bool(filename and "." in filename and not filename.startswith("."))

# --------------- Parsing & Data Retrieval--------------- #
# --------------- Resolution --------------- #
def retrieve_filename(): 
    filename = get_filename()

    if not is_valid_filename(filename):
        print("Error")
        sys.exit(1)
    
    return filename

# --------------- Result Display --------------- #
def display_filename():
    filename = retrieve_filename()
    print(filename)

display_filename()
