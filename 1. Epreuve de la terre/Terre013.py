# 12 to 24

import sys

def convert_to_24h(time_12h):
    # Séparer l'heure et l'indicateur AM/PM + gestion erreurs arguments
    if time_12h[-2:].upper() not in ["AM", "PM"]:
        print("Format invalide. Veuillez utiliser des arguments au format HH:mmAM ou HH:mmPM.")
        return
    time, period = time_12h[:-2], time_12h[-2:].upper()
    try:
        hours, minutes = map(int, time.split(":"))
        # Check si heure donnée correcte
        if not (0 <= hours < 24 and 0 <= minutes < 60):
            raise ValueError
    except ValueError:
        print("Format invalide. Utilisez HH:mmAM ou HH:mmPM.")
        return

    # Conversion de l'heure
    if period == "AM":
        if hours == 12:
            hours = 0  # Exception minuit
    else:  # Gestion période PM
        if hours != 12:
            hours += 12  # Conversion en format 24h

    # Affichage du résultat
    print(f"{hours:02}:{minutes:02}")

# Vérification des arguments
if len(sys.argv) != 2:
    print("Utilisation : python3 monexo.py HH:MMAM/PM")
else:
    convert_to_24h(sys.argv[1])
