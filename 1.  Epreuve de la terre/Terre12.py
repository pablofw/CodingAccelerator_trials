# 24 to 12

import sys

def convert_to_12h(time_24h):
    try:
        # Séparer les heures et minutes
        hours, minutes = map(int, time_24h.split(":"))
        
        # Check si heure donnée correcte
        if not (0 <= hours < 24 and 0 <= minutes < 60):
            raise ValueError
        
        # Conversion au format british 12h
        period = "AM"
        if hours == 0:
            hours = 12  # Exception Minuit = 12:XX AM
        elif hours == 12:
            period = "PM"  # Exception Midi = 12:XX PM
        elif hours > 12:
            hours -= 12
            period = "PM"
        
        # Affichage du résultat
        print(f"{hours}:{minutes:02d}{period}")

    except ValueError:
        print("Format incorrect. Veuillez entrer la commande suivante : python3 Terre012.py HH:mm (24h)")

# Vérifier que l'argument est fourni
if len(sys.argv) != 2:
    print("Erreur : Veuillez fournir une heure au format 24h.")
else:
    convert_to_12h(sys.argv[1])

# --------------- Utilities --------------- #

# --------------- Error handling --------------- #

# --------------- Parsing & Data Retrieval  --------------- #

# --------------- Resolution --------------- #

# --------------- Result Display / Execution --------------- #
