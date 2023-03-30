#ESERCIZIO 17
# Sul prezzo di un prodotto viene praticato lo sconto del X% se si acquistano fino a 10 pezzi e dell'Y% se si acquistano più di 10 pezzi. 
# Presi in input il pezzo di un prodotto e il numero di pezzi da acquistare, stampa la spesa da sostenere.

#Inizio
#Main
print("Sul prezzo di un prodotto viene applicato il 15%  di sconto se acquista un massimo di 10 prodotti ed un 20%  se qcquista più di 10 prodotti")
x=int(input("quanti prodotti vuoi acquistare "))

#Elaborazione
if x>10:
	p=int(input("quanto costa il prodotto "))
	p=p*x
	pf=p-(p*15/100)
	print("il prezzo finale è : ",pf)
else:
	p=int(input("quanto costa il prodotto "))
	p=p*x
	pf=p-(p*10/100)
	print("il prezzo finale è : ",pf)
#Fine
