# Pair ou impair
import sys

def pair_ou_impair(argument):
    try:
        nombre = int(argument)
        if nombre % 2 == 0: # reste de la division
            print("pair")
        else:
            print("impair")
    except ValueError:
        print("Erreur")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Merci de rentrer un seul nombre")
    else:
        pair_ou_impair(sys.argv[1])
