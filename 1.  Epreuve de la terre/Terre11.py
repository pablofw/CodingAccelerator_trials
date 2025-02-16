# Nombre premier

import sys

# Checking
if len(sys.argv) != 2:
    print("Erreur : Veuillez fournir un seul argument (un nombre entier).")
    sys.exit(1)
try:
    nombre = int(sys.argv[1])
except ValueError:
    print("Erreur : L'argument doit être un nombre entier.")
    sys.exit(1)

# Traitement 
if nombre < 2:
    print(f"Non, {nombre} n’est pas un nombre premier.")
    sys.exit(0)

def est_premier(n):
    for i in range(2, int(n**0.5) + 1): # évite d'importer math sqrt
        if n % i == 0:
            return False
    return True
if est_premier(nombre):
    print(f"Oui, {nombre} est un nombre premier.")
else:
    print(f"Non, {nombre} n’est pas un nombre premier.")

# --------------- Utilities --------------- #

# --------------- Error handling --------------- #

# --------------- Parsing & Data Retrieval  --------------- #

# --------------- Resolution --------------- #

# --------------- Result Display / Execution --------------- #
