# Taille d’une chaîne

import sys

# Check nb argu
if len(sys.argv) != 2:
    print("Erreur : veuillez fournir une seule chaîne de caractère, et si elle comprend des espaces faut la donner entre guillemets.")
    exit()
# Check bon format
argument = sys.argv[1]
if argument.isdigit():
    print("Erreur, donne une chaine de caractère.")
    exit()

# Fonction
def nb_caracteres(chaine):
    nb = 0
    for _ in chaine:
        nb += 1
    return nb

print(nb_caracteres(argument))

# --------------- Utilities --------------- #

# --------------- Error handling --------------- #

# --------------- Parsing & Data Retrieval  --------------- #

# --------------- Resolution --------------- #

# --------------- Result Display / Execution --------------- #
