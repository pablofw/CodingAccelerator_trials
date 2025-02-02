### Eau : ok
# Fonctions
def celebrer_victoire(adjectif):
    return f"J’ai terminé l’Épreuve de l’Eau et c’était {adjectif}."

# Gestion des erreurs
def verifier_arguments(args):
    if len(args) != 1:
        print("Erreur : Veuillez donner un seul adjectif.")
        exit(1)

# Parsing
import sys
args = sys.argv[1:]
verifier_arguments(args)
adjectif = args[0]

# Résolution
message = celebrer_victoire(adjectif)

# Affichage de résultat
print(message)
