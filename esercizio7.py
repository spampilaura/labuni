# punto 1 
num = int(input("inserici un numero: "))
''' generatore infinito di multipli di un numero'''
def generatore(num):
    n = 0
    while True : #loop infinito 
        yield n*num
        n += 1
g = generatore(num)
print(f'giocheremo con il numero {num}')
num_tabellina = next(g)
c = True
while c : 
    guess = input(f'il numero attuale è {num_tabellina}. Quale è il prossimo numero? ')
    if guess == 'FINE' : # controllo se fermare il gioco
        c = False 
    num_tabellina = next(g)
    if num_tabellina == int(guess) : 
        print('hai indovinato')
    else : 
        print('riprova')
print('Esco dal gioco')