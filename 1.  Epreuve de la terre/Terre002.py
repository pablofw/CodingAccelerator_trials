# Nom du prog
# --------------- Utilities --------------- #
import sys
    
# --------------- Error handling --------------- #
def is_valid_filename(filename: str) -> bool:
    return bool(filename) and filename.count(".") >= 1 and not filename.startswith(".")

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
def retrieve_validated_filename(): 
    filename = get_filename()   
    return filename if is_valid_filename(filename) else None

# --------------- Result Display / Execution --------------- #
def display_filename(): 
    filename = retrieve_validated_filename()
    if filename:
        print(filename)
    else: 
        print("Error")
        sys.exit(1)

display_filename()
