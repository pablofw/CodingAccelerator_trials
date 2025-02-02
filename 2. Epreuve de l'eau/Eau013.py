### Tri à bulle
# Fonctions
def my_bubble_sort(array):
    n = len(array)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array



# Gestion des erreurs
def check_arguments(args):
    if len(args) < 2:
        print("error")
        exit(1)
    try:
        return [int(arg) for arg in args]
    except ValueError:
        print("error")
        exit(1)

# Parsing
import sys
arguments = sys.argv[1:]
array = check_arguments(arguments)

# Résolution
new_array = my_bubble_sort(array)

# Affichage de résultat
print(" ".join(map(str, new_array)))
