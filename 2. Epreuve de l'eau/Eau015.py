### Par ordre Ascii 
'''
L’ASCII (American Standard Code for Information Interchange) est un système de codage,
qui attribue un numéro unique à chaque caractère (lettres, chiffres, symboles).
'''
# Fonctions
def trier_par_ascii(elements):
    return sorted(elements)

# Gestion des erreurs
def verifier_arguments(arguments):
    if len(arguments) < 2:
        print("error")
        exit(1)

# Parsing
import sys
arguments = sys.argv[1:]
verifier_arguments(arguments)

# Résolution
resultat = trier_par_ascii(arguments)

# Affichage de résultat
print(" ".join(resultat))
