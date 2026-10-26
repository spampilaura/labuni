#
# File: esercizio4.py
#
# Author: L.Rossi
#
# Date: 2026/06/15
#
# Version: 1.0
#
# Description: Creare file testo e JSON
#
import json # per punto 2)
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

''' punto 1) creare un file testo per ogni linea della rubrica'''
file_testo = open('rubrica.txt', 'w') # creo il file testo dove andro ad aggiungere tutti gli elementi della rubrica
print("Il file denominato 'rubrica.txt' è stato creato")
for nome in rubrica : 
    file_testo.write(f"{nome}, {rubrica[nome]['giorno']}, {rubrica[nome]['mese']}, {rubrica[nome]['anno']}, {rubrica[nome]['età']}, {rubrica[nome]['sesso']}, {rubrica[nome]['mail']}\n") # scrive dentro al file per ogni nome tutto quello che c'è
file_testo.close() # chiude il file
print("Al file sono stati aggiunti tutti gli elementi della rubrica")

''' punto 2) creare un file JSON '''
file_json = open('rubrica.json', 'w') # creo il file scrittura
print("Il file denominato 'rubrica.json' è stato creato")
json.dump(rubrica, file_json) # con dump creo il file json 
file_json.close() 

''' punto 3) leggere la rubrica '''
with open('rubrica.json', 'r') as in_file:
    # legge il contenuto del file in un dizionario
    rubrica = json.load(in_file)
print(rubrica)