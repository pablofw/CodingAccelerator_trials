### Paramètres à l’envers aka Yoda translator
# Fonctions
def yoda_translator(arguments):
    return arguments[::-1]

# Gestion des erreurs
def check_errors(arguments):
    if len(arguments) == 0:
        print("erreur: il n'y a aucun argument à inverser !")
        exit(1)

# Parsing
import sys
arguments = sys.argv[1:]

# Résolution
check_errors(arguments)
yoda_translated = yoda_translator(arguments)

# Affichage de résultat
for arg in yoda_translated:
    print(arg)
