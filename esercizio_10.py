#Cristian Uva 3M 5/10/2022
#Esercizio 10
#Un cliente ha deciso di costruire una piccola casetta per gli attrezzi da giardino. Hai bisogno di L assi larghe per il tetto, P assi di legno piccole per le pareti e Q riquadri di legno per il pavimento. Realizza un programma che dopo avere preso in input L,P,Q e il loro prezzo unitario (senza IVA), calcoli e visualizzi la spesa da sostenere, sapendo che il venditore ha uno sconto del 10% ma chiede 30 euro per la consegna.

#Inserimento dei valori delle assi piccole, larghe, riquadri il loro prezzo e l'iva
print ("Inserisco i valori delle assi larghe, piccole e numero di riquadri e l'iva")
assiL  = int(input("Inserisci il numero delle assi larghe: "))
assiP = int(input("Inserisci il numero delle assi piccole: "))
riquadri = int(input("Inserisci il numero dei riquadri: "))
assiLprezzo  = int(input("Inserisci il costo delle assi larghe: "))
assiPprezzo = int(input("Inserisci il costo delle assi piccole: "))
riquadriPrezzo = int(input("Inserisci il costo dei riqadri: "))
iva = int(input("Inserisci l'iva: "))

#Calcolo del costo finale consegna, totale, totaleSconto, totaleIva, totaleConsegna
totale = (assiL * assiLprezzo) + (assiP * assiPprezzo) + (riquadri * riquadriPrezzo) 
totaleSconto = totale - (totale / 100 * 10)
totaleIva = totaleSconto + (totaleSconto * iva / 100)
totaleConsegna = totaleIva + 30

#Lettura a schermo del risultato
print ("Il totale privo di iva è:", totale)  
print ("Il totale scontato privo di iva è:", totaleSconto) 
print ("Il totale applicando l'iva è:", totaleIva) 
print ("Il totale applicando l'iva e il costo della consegna è:", totaleConsegna) 