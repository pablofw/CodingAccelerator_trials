# Inverser une chaîne

import sys
# Vérification des arguments
if len(sys.argv) != 2:
    print("Erreur : veuillez fournir une seule chaîne de caractère, et si elle comprend des espaces faut la donner entre guillemets.")
    sys.exit(1)

def inverser_chaine(chaine):
    newchaine = ""  
    for caractere in chaine:
        newchaine = caractere + newchaine  # Ajoute chaque caractère au début
    return newchaine

# Récupération de l'argument et applic de la foncttion
chaine_input = sys.argv[1]
chaine_output = inverser_chaine(chaine_input)

print(chaine_output)

# --------------- Utilities --------------- #

# --------------- Error handling --------------- #

# --------------- Parsing & Data Retrieval  --------------- #

# --------------- Resolution --------------- #

# --------------- Result Display / Execution --------------- #
