# Trouver la Suisse (lol)

import sys

# Checking
if len(sys.argv) != 4:
    print("Erreur: veuillez donner trois nombres entiers")
    sys.exit(1)
try:
    a, b, c = map(int, sys.argv[1:4])
except ValueError:
    print("Erreur: veuillez donner trois nombres entiers")
    sys.exit(1)
if a == b == c:
    print("erreur.")
else:
    # Traitement
    if (a < b < c) or (c < b < a):
        print(b)
    elif (b < a < c) or (c < a < b):
        print(a)
    else:
        print(c)
