testo = '''
bello 
ciao 

9 . 
a
fiocco 
day

s
jnd
'''
# in maiuscolo bello, 9 . , fiocco 

count1 = 0 # count righe 
count2 = 0 # count parole
count3 = 0
count4 = 0
a = testo.split('\n') # divide il testo quando trova un a capo 
testo_originale = testo

# punto 1), 2), 3) 
for line in a : 
    if len(line) > 0 : # se la lunghezza di "line" è maggiore di 0 fai: 
        count1 += 1 # aggiungi 1 
        words = line.split() # divide la linea quando trova uno spazio (per restituire una lista con parole)
        count2 +=len(words) # len(words) conta elementi che ci sono in "words"
        for c in line :
            if ("a" <= c <= "z") or ("A" <= c <= "Z") or ("0" <= c <= "9") :
                count3 +=1
print("Il numero delle righe è: ", count1)
print("Il numero delle parole è: ", count2)
print("Il numero di caratteri é: ", count3)

# punto 4) 
character = input("Inserisci una lettera che vuoi che sia contata nel testo: ")
for line in a : 
    for c in line : 
        if c == character : 
            count4 += 1 
print("La lettera ", character, " è presente nel testo ", count4, " volte")

# punto 5)
for i in range(len(a)): # range(len()) per avere gli indic della lista e poter modificare gli elementi
    if a[i] == "day" or a[i] == "water" or a[i] == "about": 
        a[i] = "PYTHON" 
testo = "\n".join(a) # join() per unire gli elementi modificati e il testo 
print("Il testo con le parole 'day', 'water' e 'about sostituite con PHYTON : \n", testo)

# punto 6) 
testo = testo_originale # resetto il testo così la nuova modifica verrà fatta sul testo di base
a = testo.split('\n')
for i in range(len(a)):
    if i % 2 != 0 :  # se il resto è 1 fai .upper() 
        a[i] = a[i].upper()
testo = "\n".join(a)
print ("Il testo con le parole in posizione dispari scritte in maiuscolo: \n", testo)

# punto 7) 
testo = testo_originale
a = testo.split('\n')
a.reverse() # cambia l'ordine delle frasi
testo = "\n".join(a)
print("Il testo riscritto invertendo l'ordine delle frasi: \n", testo)

# punto 8) 
testo = testo_originale
a = testo.split('\n')
for i in range(len(a)) :
    if a[i] == "" :
        verso = 0
    else : 
        verso += 1

        if verso == 2 :  
            t = list(a[i])
            t.reverse()
            a[i] = "".join(t)
testo = "\n".join(a)
print("Il testo riscritto con il secondo verso di ogni strofa scritto a specchio: \n", testo)