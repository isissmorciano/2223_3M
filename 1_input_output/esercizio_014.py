#Esercizio 14
#Data una sequenza di 8 bit, dare il corrispendente valore decimale. (Dati 8 varibili, da b0 a b7).

#Scritta a schermo di cosa fa il programma
print ("Data una sequenza di 8 bit, dare il corrispendente valore decimale. \
 (Dati 8 varuibili, da b0 a b7).")

#Inserimento degli 8 bit
print ("Inserisci il valore di 8 bit (destra verso sinistra")
b0 = int(input("Inserisci il valore del bit 0: "))
b1 = int(input("Inserisci il valore del bit 1: "))
b2 = int(input("Inserisci il valore del bit 2: "))
b3 = int(input("Inserisci il valore del bit 3: "))
b4 = int(input("Inserisci il valore del bit 4: "))
b5 = int(input("Inserisci il valore del bit 5: "))
b6 = int(input("Inserisci il valore del bit 6: "))
b7 = int(input("Inserisci il valore del bit 7: "))

#Calcolo del valore decimale
Decimale = b0 * 1 + b1 * 2 + b2 * 4 + b3 * 8 + b4 * 16 + b5 * 32 + b6 * 64 + b7 * 128

#Stampo il valore decimale
print ("Il valore è:", Decimale)
