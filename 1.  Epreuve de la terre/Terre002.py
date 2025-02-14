# Nom du prog
# --------------- Utilities --------------- #
import sys
    
# --------------- Error handling --------------- #
def is_valid_filename(filename: str) -> bool:
    return bool(filename and "." in filename and not filename.startswith("."))

# --------------- Parsing & Data Retrieval--------------- #
def get_filename():
    full_path = sys.argv[0]
    filename = ""
    
    for char in full_path:
        if char in ("/", "\\"):
            filename = ""
        else:
            filename += char
            
    return filename
    
# --------------- Resolution --------------- #
def display_filename(): 
    filename = get_filename()

    if is_valid_filename(filename):
        print(filename)
    else: 
        print("Error")
        sys.exit(1)
        
    return filename

# --------------- Result Display / Execution --------------- #
display_filename()
