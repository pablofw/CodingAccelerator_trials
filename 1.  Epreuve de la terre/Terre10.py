# Racine carrée d’un nombre

import sys

# Checking
if len(sys.argv) != 2:
    print("Erreur : Veuillez entrer un seul entier positif en argument.")
    sys.exit(1)
try:
    nombre_input = int(sys.argv[1])
    if nombre_input < 0:
        print("Erreur : Entrez un entier positif.")
        sys.exit(1)
except ValueError:
    print("Erreur : L'argument doit être un entier positif.")
    sys.exit(1)

# Traitements
def racine_carree(n):
    if n == 0 or n == 1:
        return n
    r = 1
    while r * r <= n:
        r += 1
    
    return r - 1, (n - (r - 1) * (r - 1))
racine, reste = racine_carree(nombre_input)

print(f"Racine entière : {racine}, Reste : {reste}")

# --------------- Utilities --------------- #

# --------------- Error handling --------------- #

# --------------- Parsing & Data Retrieval  --------------- #

# --------------- Resolution --------------- #

# --------------- Result Display / Execution --------------- #
