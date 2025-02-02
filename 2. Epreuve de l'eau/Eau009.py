### Chiffres only
# Fonctions
def contient_uniquement_chiffres(chaine: str) -> bool:
    return chaine.isdigit()

# Gestion des erreurs
import sys
if len(sys.argv) != 2:
    print("Erreur : mauvais argument en input")
    sys.exit(1)

# Parsing
chaine = sys.argv[1]

# Résolution
resultat = contient_uniquement_chiffres(chaine)

# Affichage de résultat
print("true" if resultat else "false")
