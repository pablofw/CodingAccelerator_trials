### Prochain nombre premier
# Fonctions
def est_premier(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):  
        if n % i == 0:
            return False
    return True

def premier_suivant(n):
    candidat = n + 1
    while not est_premier(candidat):
        candidat += 1
    return candidat

# Gestion des erreurs
import sys

if len(sys.argv) != 2:
    print("Erreur: Pas le bon nombre d'argument")
    sys.exit(1)
try:
    nombre = int(sys.argv[1])
except ValueError:
    print("Erreur: Pas le bon type de données en input")
    sys.exit(1)

if nombre < 0:
    print("Erreur: le nombre est négatif ^^")
    sys.exit(1)

# Parsing 

# Résolution
resultat = premier_suivant(nombre)

# Affichage de résultat
print(resultat)
