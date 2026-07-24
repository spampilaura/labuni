#
# File: esercizio2.py
#
# Author: L.Rossi
#
# Date: 2026/05/04
#
# Version: 1.0
#
# Description: Test sui numeri interi positivi
#
testo = '''
Day after day, day after day,
We stuck, nor breath nor motion;
As idle as a painted ship
Upon a painted ocean.

Water, water, every where,
And all the boards did shrink;
Water, water, every where,
Nor any drop to drink.

The very deep did rot: O Christ!
That ever this should be!
Yea, slimy things did crawl with legs
Upon the slimy sea.

About, about, in reel and rout
The death-fires danced at night;
The water, like a witch's oils,
Burnt green, and blue and white.
''' 

count1 = 0 # counta num righe 
count2 = 0 # counta num parole
count3 = 0 # counta num caratteri
count4 = 0 # counta quante volte il carattere compare nel testo
a = testo.split('\n') # divide il testo quando trova un a capo (in righe)
testo_originale = testo # salva copia del testo originale

''' punto 1) contare le righe non vuote, 2) contare le parole, 3) contare i caratteri alfanumerici''' 
for line in a : 
    if len(line) > 0 : # se la lunghezza di "line" è maggiore di 0 fai: 
        count1 += 1 # aggiungi 1 
        words = line.split() # divide la linea quando trova uno spazio (per restituire una lista con parole)
        count2 +=len(words) # count parola inctementato di len(words) conta elementi che ci sono in "words"
        for c in line :
            if ("a" <= c <= "z") or ("A" <= c <= "Z") or ("0" <= c <= "9") : # se c è da 'a' a 'z' oppure da 'A' a 'Z' oppure da 0 a 9
                count3 +=1 
print("Il numero delle righe è: ", count1)
print("Il numero delle parole è: ", count2)
print("Il numero di caratteri é: ", count3)

''' punto 4) chiedere una lettera e contare quante volte è presente '''
character = input("Inserisci una lettera che vuoi che sia contata nel testo: ")
for line in a : 
    for c in line : 
        if c.lower() == character.lower() : # confronta ignorando minuscole e maiuscole
            count4 += 1 
print("La lettera ", character, " è presente nel testo ", count4, " volte")

''' punto 5) sostituire 'day', 'water', 'about' con 'PHYTON' '''
for i in range(len(a)): # range(len()) viene usato per avere gli indici della lista e poter modificare gli elementi
    parole = a[i].split() # divide la riga in parole 
    for j in range(len(parole)):
        if parole[j] == "day" or parole[j] == "water" or parole[j] == "about":
            parole[j] = "PYTHON" # sostiusce la parola day, water o about con PHYTON 
    a[i] = " ".join(parole) # join() per unire gli elementi modificati
testo = "\n".join(a) # unisce di nuovo le parole della riga 
print("Il testo con le parole 'day', 'water' e 'about' sostituite con PYTON : \n", testo)

''' punto 6) le parole in posizione dispari vengono scritte in maiuscolo '''
testo = testo_originale # resetto il testo così la nuova modifica verrà fatta sul testo di base
a = testo.split()
for i in range(len(a)):
    if i % 2 != 0 :  # se il resto è 1 fai .upper() 
        a[i] = a[i].upper() # trasforma la parola in maiuscolo 
testo = " ".join(a)
print ("Il testo con le parole in posizione dispari scritte in maiuscolo: \n", testo)

''' punto 7) inverte l'ordine delle frasi '''
testo = testo_originale
a = testo.split('\n')
a.reverse() # cambia l'ordine delle frasi
testo = "\n".join(a)
print("Il testo riscritto invertendo l'ordine delle frasi: \n", testo)

''' punto 8) il secondo verso di ogni strofa viene scritto a specchio '''
testo = testo_originale
a = testo.split('\n')
verso = 0 
for i in range(len(a)) :
    if a[i].strip() == "" : # quando trova un a capo 
        verso = 0 
    else : 
        verso += 1

        if verso == 2 :  # se il verso è il seocondo si fa il calcolo per scrivere a specchio 
            t = list(a[i]) 
            t.reverse() # inverte l'ordine delle righe 
            a[i] = "".join(t)
testo = "\n".join(a)
print("Il testo riscritto con il secondo verso di ogni strofa scritto a specchio: \n", testo)

''' punto 9) trova le parole che campaiono in tutte le strofe '''
testo = testo_originale
strofe = testo.split('\n\n') # divide il testo ogni volta che trova uno spazio (in parole)
 
for parola in prima : 
    p = True 
    for i in range(1, len(strofe)) : 
        if parola not in strofe[i].split(): 
            p = False 
    if p == True :
        print("La parola o le parole presenti in tutte le strofe sono : ", parola)

# punto 10)
testo = testo_originale
a = testo.split()
l = []
for parola in a : 
    if parola not in l : 
        l.append(parola) # se "parola" non è già presente nella lista l'aggiunge 
l.sort(key=len) # ordina per la lunghezza di parole la lista
print("La lista univoca ordina per lunghezza è: ", l) 

# punto 11) 
testo = testo_originale
dizionario = {} # dizionario vuoto 
for c in testo :  
    if c in dizionario : # se c'è già nel dizionario aumenta il conteggio 
        dizionario[c] += 1 
    else : # senno, lo inserisce per la prima volta (per questo il valore dato è 1)
        dizionario[c] = 1 
print("Il dizionario per ogni carattere è: ", dizionario)

# punto 12)  
testo = testo_originale 
dizionario2 = {} 
for c in testo :  
    if ("a" <= c <= "z" ) or ("A" <= c <= "Z" ) or ("0" <= c <= "9") : 
        c = c.lower()
        if c in dizionario2 : 
            dizionario2[c] += 1 
        else : 
            dizionario2[c] = 1 
print("Il dizionario per solo i caratteri alfanumerici è: ", dizionario2)