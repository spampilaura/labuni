""" punto 1) ritorna vero se "n" è pari, falso se è "n" dispari"""
def is_pari(n) :
    if(n%2 == 0) : # se n è pari restituisce il valore true 
        return True
    else : # se n è dispari restituisce il valore false 
        return False

""" punto 2) ritorna un numero positivo che li da l'utente se non va bene richiederlo """
def positive_value() : 
        n = int(input("Inserisci un numero intero positivo: "))
        while (n < 1) : #quando il numero è minore di 1, imposto un ciclo che va avanti fin quando non viene dato un valore corretto
            n = int(input("numero non valido, inserisci un numero valido DEVE ESSERE POSITIVO: "))
        return n

""" punto 3) num. pari // 2, num. diversi *3+1, la lista finisce quando arriva a 1 oppure a 100 elementi """
def generate_list(n) :
    nstart = n 
    l = [n] # creo la lista 
    while (n != 1 and len(l) < 100) : # "len" è la lunghezza della lista, "!=" è diverso
        if(is_pari(n)) : # se n è pari, n viene diviso per due 
            n = n//2 
        else : # se n è dispari, n viene moltiplicato per tre 
            n = n*3+1
        l.append(n) # "append" aggiunge il numero alla lista 
    print("La lista per il numero", nstart, "è: ", l) # la lista per il numero che ha dato l'utente è: 
    return l

""" punto 4) somma, lunghezza e numero più grande della lista """
def analizza_sequenza(l) : 
    s = sum(l) #la somma della lista
    lenght = len(l) # la lunghezza della lista
    m = max(l) # il numero più grande
    return m, lenght, s

""" punto 5) se la lista contiene un numero divisibile per 5 restituisce il numero, senno print frase di spiegazione """
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
        print() #soltanto per mettere un a capo, cosi che i numeri o "nessuno" sia attacato a "inserisci un numero intero positivo: "

def main(): 
    print("In questo programma vengono fatti vari test sui numeri interi per trovare quale numero generi la sequenza più lunga")
    test = int((input("Inserisci un numero, corrispondente al numero di test che vuoi eseguire: ")))
    max_lenght = 0 # lunghezza più grand trovata
    num_max = 0 # numero inziale che ha prodotto la sequenza 
    for i in range(test) : 
        n = positive_value()
        l = generate_list(n) 
        m, lenght, s = analizza_sequenza(l)
        print("Somma:", s)
        print("Lunghezza:", lenght)
        print("Massimo:", m)
        div5(l)
        
        if (lenght > max_lenght) :
            max_lenght = lenght
            num_max = n
    print("Il numero con la sequenza più lunga è: ", num_max)
main()

