# Program name
'''
Goals:
- Discovering sys
- Using coherent loops 
- Applying clean code concepts
'''

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
    if bool(filename):
        return True
    else:
        print("Error: no filename detected")
        return False

# --------------- Parsing & Data Retrieval--------------- #
    
# --------------- Resolution --------------- #
def retrieve_filename(): 
    filename = get_filename()   
    if is_valid_filename(filename):
        return filename
    return None

# --------------- Result Display / Execution --------------- #
print(retrieve_filename())