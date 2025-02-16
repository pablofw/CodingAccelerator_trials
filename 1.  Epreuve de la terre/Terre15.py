# Trié ou pas

import sys

# Checking
if len(sys.argv) < 2:
    print("erreur: y a pas assez d'arguments pour faire une liste")
    sys.exit(1)
try:
    nombres = [int(arg) for arg in sys.argv[1:]]
except ValueError:
    print("erreur: veuillez donner des nb entiers dans la liste")
    sys.exit(1)

# Traitement
def est_triee(liste):
    for i in range(len(liste) - 1):
        if liste[i] > liste[i + 1]:
            return False
    return True

if est_triee(nombres):
    print("Triée !")
else:
    print("Pas triée !")


# --------------- Utilities --------------- #

# --------------- Error handling --------------- #

# --------------- Parsing & Data Retrieval  --------------- #

# --------------- Resolution --------------- #

# --------------- Result Display / Execution --------------- #
