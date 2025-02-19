# Program name
# --------------- Utilities --------------- #
import sys

def get_filename() -> str:
    """
    Extract the script's filename from the path manually
    """
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
    return bool(filename)

# --------------- Parsing & Data Retrieval--------------- #
    
# --------------- Resolution --------------- #
def retrieve_filename(): 
    filename = get_filename()   
    if is_valid_filename(filename):
        return filename
    return "Error: no filename detected"

# --------------- Result Display / Execution --------------- #
print(retrieve_filename())
