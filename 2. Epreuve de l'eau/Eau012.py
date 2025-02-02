### Différence minimum absolue
import sys

# Fonctions
def find_min_abs_difference(numbers):
    numbers.sort()
    min_diff = float('inf')
    for i in range(len(numbers) - 1):
        diff = abs(numbers[i] - numbers[i + 1])
        if diff < min_diff:
            min_diff = diff
    return min_diff

# Gestion des erreurs
if len(sys.argv) < 3:
    print("error")
    sys.exit(1)
try:
    numbers = [int(arg) for arg in sys.argv[1:]]
except ValueError:
    print("error")
    sys.exit(1)

# Résolution
min_difference = find_min_abs_difference(numbers)

# Affichage de résultat
print(min_difference)