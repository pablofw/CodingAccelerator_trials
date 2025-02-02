### Entre min et max
# Fonctions
def afficher_valeurs(min, max):
    for i in range(min, max):
        print(i, end=" ")
    print()

# Gestion des erreurs
def verifier_arguments(args):
    if len(args) != 3:
        print("erreur: il n'y a pas le bon nb d'arg en entrée")
        exit(1)
    try:
        nombre1 = int(args[1])
        nombre2 = int(args[2])
        return nombre1, nombre2
    except ValueError:
        print("Erreur: les arg ne sont pas des nombres (mauvais format)")
        exit(1)

# Parsing
import sys
nombre1, nombre2 = verifier_arguments(sys.argv)

# Résolution
borne_min, borne_max = min(nombre1, nombre2), max(nombre1, nombre2)

# Affichage de résultat
afficher_valeurs(borne_min, borne_max)