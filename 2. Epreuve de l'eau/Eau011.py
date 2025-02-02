### Index wanted
# Fonctions
def find_index(elements, target):
    for i, elem in enumerate(elements):
        if elem == target:
            return i
    return -1 # Si l'élément est pas trouvé

# Gestion des erreurs
import sys
if len(sys.argv) < 3:
    print("error")
    sys.exit(1)

# Parsing
elements = sys.argv[1:-1]
target = sys.argv[-1]

# Résolution
index = find_index(elements, target)

# Affichage de résultat
print(index)
