# Puissance d’un nombre

import sys

# Checks
if len(sys.argv) != 3:
    print("Erreur: Vous devez fournir exactement deux arguments de type nombre : base et exposant.")
    sys.exit(1)
try:
    base = int(sys.argv[1])
    exposant = int(sys.argv[2])
    if exposant < 0:
        print("Erreur: L’exposant ne peut pas être négatif.")
        sys.exit(1)
except ValueError:
    print("Erreur: Les arguments doivent être des nombres entiers.")
    sys.exit(1)

# Fonction
def cestlapuissancecestlapuissance(base, exposant):
    resultat = 1
    for _ in range(exposant): #osef de i
        resultat *= base # multiplication + = 
    return resultat

# Affichage du résultat
print(cestlapuissancecestlapuissance(base, exposant))
