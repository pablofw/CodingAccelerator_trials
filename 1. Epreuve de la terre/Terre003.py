# Afficheur d'arguments
import sys

for argument in sys.argv[1:]: # On prend tout les arguments sauf le 1 (le nom du fichier)
    print(argument)