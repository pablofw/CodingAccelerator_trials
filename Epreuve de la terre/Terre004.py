# L’alphabet à partir de
import sys

alphabet = "abcdefghijklmnopqrstuvwxyz"

if len(sys.argv) != 2 or sys.argv[1] not in alphabet:  # Vérifie qu'une seule lettre minuscule est entrée
    print("L'entrée n'est pas une lettre minuscule valide, dsl le couz")
    sys.exit(1)  # altF4

lettre = sys.argv[1]

index = alphabet.index(lettre)
print(alphabet[index:])
