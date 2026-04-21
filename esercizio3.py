rubrica = {
  'Paolino Paperino': {'giorno': 9,
                      'mese': 'giugno',
                      'anno': 1934,
                      'età': 93,
                      'sesso': 'M',
                      'mail': 'paolino.paperin0@disney.org'},
'Ron Weasley': {'giorno': 1, 
                'mese': 'marzo', 
                'anno': 1980, 
                'età': 46, 
                'sesso': 'M', 
                'mail': 'ron_weasley80@hogwards.uk'},
'Ramona Flowers': {'giorno': 19, 'mese': 'ottobre', 'anno': 2004, 'età': 22, 'sesso': 'F', 'mail': 'ramona.fls@gmail.com'},
'Madoka Ayukawa': {'giorno': 25, 'mese': 'maggio', 'anno': 1969, 'età': 57, 'sesso': 'F', 'mail': 'madoka_sax@asahi_net.jp'}
}

# punto1) visualizzare la rubrica cin ke chisvi e i valori 
print("Punto 1: visualizzare il contenuto del dizionario")
for el in rubrica.keys() : 
  print(el, end=" ") # end permette di non mandare a capo il print 
  for el2 in rubrica[el].keys() : 
    print(el2, ":", rubrica[el][el2], end=" ") 
  print() # manda a capo quando inizia un altra key della rubrica 

# punto 2) creare lista dell'età in ordine crescente e visualizzare i nomi in base alla lista 
lista_eta = []
print()
print("Punto2: visualizzare i nomi in base all'ordine dell'età crescente")
for eta in rubrica.keys() : 
  lista_eta.append(rubrica[eta]["età"]) #aggiunge alla lista gli elementi della rubrica dove trova scritto età
  lista_eta.sort() #per mettere la lista in ordine crescente 
for v in lista_eta : 
  for nome in rubrica.keys() : 
    if rubrica[nome]["età"] == v : 
      print(nome, end =" ")
print()

# punto 3) invertire l'ordine della lista e visulizzarla 
print()
print("Punto 3: visualizzare la lista creata in ordine crescente dell'età, in ordine decrescente: ")
print("Lista crescente: ", lista_eta)
lista_eta.reverse() #cambia l'ordine degli elementi nella lista 
print("Lista decrescente: ", lista_eta)

# punto 4) per ogni membro della rubrica definire un messaggio 
print() 
print("Punto 4: visualizzare un messaggio per ogni membro")
c = " " 
count = 0 
for nome in rubrica.keys() : 
    count += 1 
    if rubrica[nome]["sesso"] == "M" : 
      c = "o"
    else :
      c = "a"
    print(f"{count}° :")
    print(f"Car{c} {nome},")
    print(f"sei nat{c} il {rubrica[nome]["giorno"]} di {rubrica[nome]["mese"]} del {rubrica[nome]["anno"]} e quindi a breve compirai {rubrica[nome]["età"]} anni.")
    print(f"Ti manderemo gli auguri a {rubrica[nome]["mail"]}")