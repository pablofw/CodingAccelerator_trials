# Divisions

import sys

# Check qu'on a bien juste 2 arguments
if len(sys.argv) != 3:
    print("erreur.")
    sys.exit(1)

try:
    # Récup des deux nb, et check si cest bien des nb
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
    # Check division interdite
    if num2 == 0:
        print("Division par 0 interdite, retourne en 6ème chef")
    else:
        # Calcul et affichage du résultat et du reste
        print(f"résultat: {num1 // num2}")
        print(f"reste: {num1 % num2}")

except ValueError:
    print("erreur.")  # Gère le cas où les arguments ne sont pas des nombres
