### Majuscule sur deux
# Fonctions
def alternate_caps(string):
    result = []
    uppercase = True
    for char in string:
        if char.isalpha():
            if uppercase:
                result.append(char.upper())
            else:
                result.append(char.lower())
            uppercase = not uppercase
        else:
            result.append(char)
    
    return "".join(result)

# Gestion des erreurs
import sys
if len(sys.argv) != 2:
    print("erreur de nb d'arguments")
    sys.exit(1)

# Parsing
input_string = sys.argv[1]

# Résolution
output_string = alternate_caps(input_string)

# Affichage de résultat
print(output_string)
