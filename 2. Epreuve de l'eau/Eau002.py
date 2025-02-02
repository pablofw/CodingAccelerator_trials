### Combinaisons de 2 nombres
# Fonctions
def generer_combi():
    combinaisons = []
    for i in range(100):
        for j in range(i + 1, 100):
            combinaisons.append(f"{i:02d} {j:02d}")
    return combinaisons

# Gestion des erreurs

# Parsing

# Résolution

# Affichage de résultat
print(", ".join(generer_combi()))

