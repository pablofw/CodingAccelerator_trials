### Majuscule
# Fonctions
def capitalize_words(sentence: str) -> str:
    return " ".join(word.capitalize() for word in sentence.split())

# Gestion des erreurs
def validate_args(args):
    if len(args) != 2:
        print("Erreur: mauvais argument en input")
        exit(1)
    if not isinstance(args[1], str) or args[1].isdigit():
        print("Erreur: mauvais argument en input")
        exit(1)

# Parsing
import sys
args = sys.argv
validate_args(args)
input_string = args[1]

# Résolution
res = capitalize_words(input_string)

# Affichage de résultat
print(res)
