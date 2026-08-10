#
# File: progettopersonale.py
#
# Author: L.Rossi
#
# Date: 2026/07/24
#
# Version: 1.0
#
# Description: Test sui numeri interi positivi
#
import random
''' progetto personale '''

# mi stampa la griglia sia all'inizio, sia modificata quando avviena una mossa 
def stampa_griglia(griglia) : 
    print(f" {griglia[0]} | {griglia[1]} | {griglia[2]} ")
    print("────────────")
    print(f" {griglia[3]} | {griglia[4]} | {griglia[5]} ")
    print("────────────")
    print(f" {griglia[6]} | {griglia[7]} | {griglia[8]} ")

# determina la mossa del giocatore 
def mossa_giocatore(griglia, simbolo) : 
    mossa = input("Digita il numero che vuoi utilizzare: ")
    while not mossa.isdigit() or int(mossa) < 1 or int(mossa) > 9 : 
        mossa = input("Hai scelto un valore non proposto tra la scelta. RICORDA SOLO NUMERI DA 1 A 9. Riprova: ") 
    while griglia[int(mossa) - 1] == "x" or griglia[int(mossa) - 1] == "o":  # serve per determinare un casella non utilizzata, così non può essere sovrascritta
        mossa = input("Questa casella è già occupata. Riprova: ")
    griglia[int(mossa) - 1] = simbolo

# controllo della vittoria
def controllo_vittoria(griglia, simbolo) : 
    # controlla le righe 
    if(griglia[0] == simbolo and griglia[1] == simbolo and griglia[2] == simbolo) : 
        return True 
    if(griglia[3] == simbolo and griglia[4] == simbolo and griglia[5] == simbolo) :
        return True 
    if(griglia[6] == simbolo and griglia[7] == simbolo and griglia[8] == simbolo) :
        return True
    # controlla le colonne
    if(griglia[0] == simbolo and griglia[3] == simbolo and griglia[6] == simbolo) : 
        return True
    if(griglia[1] == simbolo and griglia[4] == simbolo and griglia[7] == simbolo) :
        return True 
    if(griglia[2] == simbolo and griglia[5] == simbolo and griglia[8] == simbolo) :
        return True
    # controlla le diagonali
    if(griglia[0] == simbolo and griglia[4] == simbolo and griglia[8] == simbolo) :
        return True
    if(griglia[2] == simbolo and griglia[4] == simbolo and griglia[6] == simbolo) :
        return True
    return False

# modalità singola
def modalita_singola() :
    simbolo = input("Vuoi utilizzare x oppure o (scriva x oppure o): ")
    while simbolo != "x" and simbolo != "o" : 
        simbolo = input("Hai scelto un simbolo non proposto tra la scelta. Riprova: ") 
    if simbolo == "x" :
        simbolo_pc = "o"
    else :
        simbolo_pc = "x"
    print(f"Il simbolo del pc è: {simbolo_pc}")

    turno = 1
    while turno <= 5 : # 5 turni perchè vengono eseguite due messe alla volta
        # mossa del utente
        mossa_giocatore(griglia, simbolo)
        stampa_griglia(griglia)
        if controllo_vittoria(griglia, simbolo): 
            print("Hai vinto")
            break # se avviene una combinazione tra quelle presenti nel def "controllo_vittoria" il programma si interrompe
        if turno == 5  : 
            print("Pareggio, nessuno ha vinto")
            break
        # mossa del pc 
        mossa_pc = random.randint(1,9)
        while griglia[mossa_pc - 1] == "x" or griglia[mossa_pc - 1] == "o":
            mossa_pc = random.randint(1,9) # restituisce un intero randomico tra il minimo 1 e il massimo 9 
        print(f"la mossa del pc è: {mossa_pc}")
        griglia[mossa_pc - 1] = simbolo_pc
        stampa_griglia(griglia)
        if controllo_vittoria(griglia, simbolo_pc): 
            print("Ha vinto il pc")
            break
        turno += 1

# modalità doppia 
def modalita_doppia() : 
    simbolo = input("Giocatore 1, vuoi utilizzare x oppure o (scriva x oppure o): ")
    while simbolo != "x" and simbolo != "o" : 
        simbolo = input("Hai scelto un simbolo non proposto tra la scelta. Riprova: ") 
    if simbolo == "x" :
        simbolo_giocatore2 = "o"
    else :
        simbolo_giocatore2 = "x"
    print(f"Il simbolo del Giocatore 2 è: {simbolo_giocatore2}")

    turno = 1
    while turno <= 5 : # 5 turni perchè vengono eseguite due messe alla volta
        # mossa del Giocatore 1
        print("Tocca al Giocatore 1")
        mossa_giocatore(griglia, simbolo)
        stampa_griglia(griglia)
        if controllo_vittoria(griglia, simbolo): 
            print("Ha vinto il Giocatore 1")
            break # se avviene una combinazione tra quelle presenti nel def "controllo_vittoria" il programma si interrompe
        if turno == 5  : 
            print("Pareggio, nessuno ha vinto")
            break
        # mossa Giocatore 2
        print("Tocca al Giocatore 2")
        mossa_giocatore(griglia, simbolo_giocatore2)
        stampa_griglia(griglia)
        if controllo_vittoria(griglia, simbolo_giocatore2): 
            print("Ha vinto il Giocatore 2")
            break
        turno += 1

print("Questo programma permette di eseguire il gioco del tris")
print("Per giocare bisogna inserire un numero tra quelli presenti nella griglia di gioco")
while True : # un ciclo while sempre vero così da permettere al/ai giocatore/i di poter rigiocare se vuole/vogliono 
    griglia = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    stampa_griglia(griglia)
    print("Puoi scegliere se giocare in modalità singola oppure doppia.")
    print("Singola: un solo giocatore vs il computer; Doppia: due giocatori che si sfidono.")
    mg = input("Inserisci la modalità di gioco a cui vuoi partecipare (scriva singola oppure doppia): ")
    while mg != "singola" and mg != "doppia" : 
        mg = input("Hai inserito un valore non proposto tra la scelta. Riprova: ")
    if mg == "singola" : # se sceglie singola, richiama la def "modalita_singola()"
        print("Hai scelto modalità di gioco: Singola")
        modalita_singola()
    if mg == "doppia" : # se sceglie doppia, richiama la def "modalita_doppia()"
        print("Hai scelto modalità di gioco: Doppia")
        modalita_doppia()
    rigioca = input("Vuole rigiocare, scriva si oppure no: ")
    while rigioca != "si" and rigioca != "no" : 
        rigioca = input("Hai inserito un valore non proposto tra la scelta. Riprova: ")
    if rigioca == "no" : # se si inserisce no, il gioco viene interrotto 
        break