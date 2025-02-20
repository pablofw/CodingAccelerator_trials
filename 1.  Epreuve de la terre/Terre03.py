# Arguments display
'''
Goals:
- Handling arguments passed to the script via the command line
- Using coherent loops 
- Applying clean code concepts
'''

# --------------- Utilities --------------- #
import sys

def get_arguments():
    """
    Extract arguments from command line input, without path.
    """
    return sys.argv[1:]
    
# --------------- Error handling --------------- #
def has_arguments(arguments):
    if not arguments:
        print("Error: No arguments provided.")
        return False
    return True

# --------------- Parsing & Data Retrieval --------------- #

# --------------- Resolution --------------- #
def get_valid_arguments():
    arguments = get_arguments()
    if not has_arguments(arguments):
        return None
    else: 
        formatted_text = ""
        for arg in arguments:
            formatted_text += arg + "\n"
        formatted_text = formatted_text.strip() 
        return formatted_text

# --------------- Result Display / Execution --------------- #
print(get_valid_arguments())