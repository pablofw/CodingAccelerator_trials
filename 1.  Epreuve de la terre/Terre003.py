# Afficheur d'arguments
'''
import sys

for argument in sys.argv[1:]: # On prend tout les arguments sauf le 1 (le nom du fichier)
    print(argument)
'''
# Utilities 
import sys

def get_arguments():
    return sys.argv[1:]

# Error handling 
def is_valid_arguments(arguments):
    return len(arguments) > 0 

# Parsing & Data Retrieval
def find_arguments():
    arguments = get_arguments()
    return arguments if is_valid_arguments(arguments) else None

# Resolution X 

# Result Display

# Entry point
if __name__ == "__main__":
    display_result()
