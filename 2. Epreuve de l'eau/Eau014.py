### Tri par sélection
# Fonctions
def my_select_sort(array):
    n = len(array)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
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
new_array = my_select_sort(array)

# Affichage de résultat
print(" ".join(map(str, new_array)))