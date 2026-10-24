#
# File: esercizio3.py
#
# Author: L.Rossi
#
# Date: 2026/05/23
#
# Version: 1.0
#
# Description: Manipolazione del dizionario
#
import sys # importo sys per il punto 5)
import argparse # importo argparse per il punto 6) 

''' punto 7) opzioni per eseguire i punti 1, 2, 3, 4, 5 '''
parser = argparse.ArgumentParser()
parser.add_argument("punto", type = int) # leggo il nome scritto nel terminale 
parser.add_argument("chiave", nargs="?", type=str) # nargs per poter leggere il secondo argomento
parser.add_argument("--nome", type = str) # leggo stringa
args = parser.parse_args()

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

''' punto1) visualizzare la rubrica cin ke chisvi e i valori '''
if args.punto == 1: 
  print("Punto 1: visualizzare il contenuto del dizionario")
  print()
  for el in rubrica.keys() : 
    print(el, end=" ") # end permette di non mandare a capo il print 
    for el2 in rubrica[el].keys() : 
      print(el2, ":", rubrica[el][el2], end=" ") 
    print() # manda a capo quando inizia un altra key della rubrica 

''' punto 2) creare lista dell'età in ordine crescente e visualizzare i nomi in base alla lista '''
if args.punto == 2: 
  lista_eta = []
  print("Punto 2: visualizzare i nomi in base all'ordine dell'età crescente")
  print()
  for eta in rubrica.keys() : 
    lista_eta.append(rubrica[eta]["età"]) #aggiunge alla lista gli elementi della rubrica dove trova scritto età
    lista_eta.sort() #per mettere la lista in ordine crescente 
  for v in lista_eta : 
    for nome in rubrica.keys() : 
      if rubrica[nome]["età"] == v : 
        print(nome, end =" ")
  print()

''' punto 3) invertire l'ordine della lista e visulizzarla '''
if args.punto == 3: 
  lista_eta = []
  for nome in rubrica:
    lista_eta.append(rubrica[nome]["età"])
  lista_eta.sort()
  print("Punto 3: visualizzare la lista creata in ordine crescente dell'età, in ordine decrescente: ")
  print()
  print("Lista crescente: ", lista_eta)
  lista_eta.reverse() #cambia l'ordine degli elementi nella lista 
  print("Lista decrescente: ", lista_eta)

''' punto 4) per ogni membro della rubrica definire un messaggio '''
if args.punto == 4: 
  print("Punto 4: visualizzare un messaggio per ogni membro")
  print()
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

''' punto 5) passare una chiave in input e visualizzare tutto il contenuto della rubrica che corrisponnde alla chiave - con argv'''
if args.punto == 5: # se l'argomento  scritto non inzia con "--" esegui 
  chiave = sys.argv[2] # 1 perchè prende quello che viene scritto dall'utente dopo "python esericizio3.py" e dopo il numero che deve essere giorno, mese, anno, età, sesso o mail
  print(f"Punto 5: visualizzare tutto il contenuto per {chiave}")
  print()
  for nome in rubrica: # scorre i nomi della rubrica 
    print(nome, rubrica[nome][chiave]) # prende il valore della chiave scelto per il nome

''' punto 6) la stringa del punto 4) solo per il nome fornito come opzione - con argparse'''
if args.punto == 6 : # se l'argomento scritto è --nome esegui 
  nome = args.nome # salva il nome inserito 
  print(f"Punto 6: visualizzare il messaggio per {nome}")
  print()
  if nome in rubrica : # visualizza soltanto per quella persona
    print(f"Cara {nome}, sei nata il {rubrica[nome]['giorno']} di {rubrica[nome]['mese']} del {rubrica[nome]['anno']} e quindi a breve compirai {rubrica[nome]['età']} anni. Ti manderemo gli auguri a {rubrica[nome]['mail']}")
  else:
      print("Nome non presente nella rubrica")

# riga 76 e riga 83, servono cosi che posso sia eseguire il punto 5) che il punto 6) senza dover commentare uno o l'altro 
