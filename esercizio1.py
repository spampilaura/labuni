""" punto 1) ritorna vero se "n" è pari, falso se è "n" dispari"""
def is_pari(n) :
    if(n%2 == 0) : # se n è pari restituisce il valore true 
        return True
    else : # se n è dispari restituisce il valore false 
        return False
""" punto 2) ritorna un numero positivo che li da l'utente se non va bene richiederlo """
def positive_value(n) : 
    if (n >= 1) : # se il n è maggiore o uguale a 1 restituisce n 
        return n
    else : # se n è minore di 1, ciclo while fin quando n non è valido
        while (n < 1) :
            return int(input("numero non valido, inserisci un numero valido DEVE ESSERE POSITIVO: "))
""" punto 3) num. pari // 2, num. diversi *3+1, la lista finisce quando arriva a 1 oppure a 100 elementi """
def generate_list(n) :
    list = [n] # creo la lista 
    while (n != 1 and len(list) <= 100) : # "len" è la lunghezza della lista, "!=" è diverso
        if(n%2 == 0) : # se n è pari, n viene diviso per due 
            n = n//2 
        else : # se n è dispari, n viene moltiplicato per tre 
            n = n*3+1
        list.append(n) # "append" aggiunge il numero alla lista 
    return list
    
def main(): 
    result = int((input("scrivi un numero: ")))
    print(is_pari(result))
    print(positive_value(result))
    print(generate_list(result))

main()

