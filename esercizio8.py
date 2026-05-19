#
# File: Esercizio8.py
#
# Author: L. Rossi
#
# Date: 2026/05/19
#
# Version: 1.0
#
# Description: My First Project Program to print "Hello, World!".
#
import random 
def gioco_impiccato():
    # Lista di parole possibili per il gioco
    parole = ["python", "programmazione", "computer", "funzione", "sviluppatore", "tastiera"]
    
    # Scelta casuale della parola segreta
    parola_segreta = random.choice(parole).lower()
    
    # Inizializzazione delle lettere indovinate (es. ['_', '_', '_'])
    lettere_indovinate = ["_"] * len(parola_segreta)
    
    # Insieme per tenere traccia delle lettere già provate
    lettere_tentate = []
    
    # Numero massimo di errori consentiti
    tentativi_rimasti = 6
    
    print("=== BENVENUTO AL GIOCO DELL'IMPICCATO ===")
    
    # Loop principale del gioco
    while tentativi_rimasti > 0 and "_" in lettere_indovinate:
        print(f"\nParola da indovinare: {" ".join(lettere_indovinate)}")
        print(f"Tentativi rimasti: {tentativi_rimasti}")
        print(f"Lettere già provate: {", ".join(sorted(lettere_tentate)) if lettere_tentate else "nessuna"}")
        
        # Input dell'utente con controllo di validità
        tentativo = input("Inserisci una lettera: ").lower().strip()
        
        if len(tentativo) != 1 or not tentativo.isalpha():
            print("Per favore, inserisci una sola lettera valida.")
            continue
        try: 
            parole = lettere_tentate.index(tentativo)  
        except ValueError: 
            pass
        else: 
            print(f"Hai già provato la lettera '{tentativo}'.")
            continue   
            
        # Aggiunge la lettera a quelle tentate
        lettere_tentate.append(tentativo)
        
        # Controllo se la lettera è nella parola
        if tentativo in parola_segreta:
            print(f"Ottimo! La lettera '{tentativo}' è presente.")
            # Aggiorna la visualizzazione della parola
            for i in range(len(parola_segreta)):
                if parola_segreta[i] == tentativo:
                    lettere_indovinate[i] = tentativo
        else:
            print(f"Peccato! La lettera '{tentativo}' non è presente.")
            tentativi_rimasti -= 1
            
    # Fine del gioco: controllo della vittoria o della sconfitta
    print("\n=========================================")
    if "_" not in lettere_indovinate:
        print(f"COMPLIMENTI! Hai vinto! La parola era: {parola_segreta.upper()}")
    else:
        print(f"GAME OVER! Hai esaurito i tentativi. La parola era: {parola_segreta.upper()}")
    print("=========================================")

gioco_impiccato()