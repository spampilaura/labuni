''' punto 1) ritorna vero se "n" è pari, falso se è "n" dispari '''
def is_pari(n) :
    if(n%2 == 0) : # se n è pari restituisce il valore true 
        return True
    else : # se n è dispari restituisce il valore false 
        return False

'''  punto 2) ritorna un numero positivo che li da l'utente se non va bene richiederlo '''
def positive_value() : 
        n = int(input("Inserisci un numero intero positivo: "))
        while (n < 1) : # quando il numero è minore di 1, continua a chiederi il numero fin quando non è positivo
            n = int(input("Numero non valido. Inserisci un numero intero positivo: "))
        return n

''' punto 3) num. pari // 2, num. diversi *3+1, la lista finisce quando arriva a 1 oppure a 100 elementi '''
def generate_list(n) :
    nstart = n 
    l = [n] # creo la lista 
    while (n != 1 and len(l) < 100) : # "len" è la lunghezza della lista, "!=" è diverso
        if(is_pari(n)) : # se n è pari, n viene diviso per due 
            n = n//2 
        else : # se n è dispari, n viene moltiplicato per tre e poi sommato 1 
            n = n*3+1
        l.append(n) # "append" aggiunge il numero alla lista 
    print("La lista per il numero", nstart, "è: ", l) # stampa la lista generata dal numero iniziale 
    return l

''' punto 4) somma, lunghezza e numero più grande della lista '''
def analizza_sequenza(l) : 
    s = sum(l) #la somma della lista
    length = len(l) # la lunghezza della lista
    m = max(l) # il numero più grande
    return m, length, s
''' punto 5) se la lista contiene un numero divisibile per 5 restituisce il numero, senno print frase di spiegazione '''
def div5(l) : 
    t = False 
    print("I numeri divisibili per 5 sono:", end =" ")
    for n in l: 
        if (n%5 == 0) :
            print(n, end = " ")
            t = True 
    if not t : # se non trova un numero divisibie per 5 
        print("nessuno")
    else : 
        print() # va a capo dopo la stampa (messo soltanto per un fattore estetico)

''' punto 6) main '''
def main(): 
    print("In questo programma vengono fatti vari test sui numeri interi per trovare quale numero generi la sequenza più lunga")
    test = int((input("Inserisci un numero, corrispondente al numero di test che vuoi eseguire: ")))
    max_length = 0 # lunghezza più grand trovata
    num_max = 0 # numero inziale che ha prodotto la sequenza 
    for i in range(test) : 
        n = positive_value()
        l = generate_list(n) 
        m, length, s = analizza_sequenza(l)
        print("Somma:", s)
        print("Lunghezza:", length)
        print("Massimo:", m)
        div5(l)
        
        if (length > max_length) :
            max_length = length
            num_max = n
    print("Il numero con la sequenza più lunga è: ", num_max)
    print("La lunghezza della sequenza è: ", max_length)
main()

