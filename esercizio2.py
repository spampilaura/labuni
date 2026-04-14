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


count1 = 0 # count righe 
count2 = 0 # count parole

a = testo.split('\n') # divide il testo quando trova un a capo 
print(len(a))
for line in a : 
    if len(line) > 0 : # se la lunghezza di "line" è maggiore di 0 fai: 
        count1 += 1 # aggiungi 1 
        words = line.split() # divide la linea quando trova uno spazio (per restituire una lista con parole)
        count2 +=len(words) # len(words) conta elementi che ci sono in "words"
print("il numero delle righe è: ", count1)
print("il numero delle parole è: ", count2)
    #count +=1
#print( "il numero di parole è: ", count)