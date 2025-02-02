### Combinaisons de 3 chiffres
# Fonctions
def generer_combi():
    combinaisons = []
    for i in range(10):
        for j in range(i + 1, 10):
            for k in range(j + 1, 10):
                combinaisons.append(f"{i}{j}{k}")
    return combinaisons

# Gestion des erreurs

# Parsing

# Résolution

# Affichage de résultat
print(", ".join(generer_combi()))
