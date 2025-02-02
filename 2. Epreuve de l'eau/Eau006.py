### String dans string
# Fonctions
def contains_substring(main_string: str, sub_string: str) -> bool:
    return sub_string in main_string

# Gestion des erreurs
def validate_args(args):
    if len(args) != 2:
        print("Erreur: pas le bon nombre d'argument")
        exit(1)

# Parsing
import sys
args = sys.argv[1:]
validate_args(args)
main_string, sub_string = args

# Résolution
res = contains_substring(main_string, sub_string)

# Affichage de résultat
print("true" if res else "false")
