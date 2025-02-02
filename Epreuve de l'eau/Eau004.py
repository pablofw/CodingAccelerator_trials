### Suite de Fibonacci aka el classico
# Fonctions
def fibonacci(n):
    a, b = 0, 1
    if n < 0:
        return -1
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b

# Gestion des erreurs
import sys
if len(sys.argv) != 2:
    print("erreur: mauvais nombre d'arguments :/")
    sys.exit(1)
try:
    n = int(sys.argv[1])
except ValueError:
    print("Erreur, mauvais format d'input")
    sys.exit(1)

# Parsing

# Résolution
res = fibonacci(n)

# Affichage de résultat
print(res)
