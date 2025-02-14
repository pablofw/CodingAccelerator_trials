# Nom du prog
'''
print(__file__.split('/')[-1].split('\\')[-1])
'''
# --------------- Utilities --------------- #
import sys
def get_filename():
    full_path = sys.argv[0]
    filename = full_path.split("/")[-1]
    return filename

# --------------- Error handling --------------- #
def is_valid_filename(filename):
    return isinstance(filename, str) and len(filename) > 0

# --------------- Parsing & Data Retrieval--------------- #
'''no needed'''
# --------------- Resolution --------------- #
def find_filename(): 
    filename = get_filename()
    return filename if is_valid_filename(filename) else None

# --------------- Result Display --------------- #
def display_filename():
    result = find_filename()
    if result:
        print(result)
    else:
        print("Error")

display_filename()
