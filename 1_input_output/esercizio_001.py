#Esercizio 1
#Dato un importo calcolare lo sconto del 5% e applicare un IVA dell'8%

#Scritta a schermo di cosa fa il programma
print ("Inserisci un importo per applicargli lo sconto dell'5%, e poi le tasse dell'8%")

#Inserimento dell'importo
importo = int(input("Inserisci l'importo: "))

#Calcolo dello sconto 
importo = importo - (importo * 5 / 100)
#Calcolo dell'iva
importo = importo + (importo * 8 / 100)

#Lettura a schermo del prezzo
print ("Il prezzo finale e'", importo, "euro")  
