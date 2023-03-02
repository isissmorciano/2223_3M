#Esercizio 9
#Crea un programma che permetta di calcolare e visualizzare la spesa necessaria per pavimentare una stanza di dimensione 7*4 avendo in input: il costo delle piastrelle al metro quadrato, il costo orario della manodopera e il numero di ore impiegate. Al costo finale aggiungi l’X% di IVA

#Scritta a schermo di cosa fa il programma
print ("Programma che permetta di calcolare e visualizza  la spesa necessaria per pavimentare \
una stanza di dimensione 7*4")

#Inserimento dei valori delle piastrelle, manodopera, ore e iva

print ("Inserimento dei valori delle piastrelle, costo manodopera e numero di ore impiegate")
piastrelle  = int(input("Inserisci il valore delle piastrelle al metro quadrato: "))
manodopera = int(input("Inserisci il costo della manodopera: "))
ore = int(input("Inserisci le ore impiegate: "))
iva = int(input("Inserisci il costo dell'iva: "))

#Calcolo del costo finale 
metriquadri = 7 * 4 
totale = (piastrelle * metriquadri) + (manodopera * ore) 
totaleIva = totale + (totale * iva / 100)

#Lettura a schermo del risultato
print ("Il totale è:", totale, "euro")  
print ("Il totale applicando l'iva è:", totaleIva, "euro") 
