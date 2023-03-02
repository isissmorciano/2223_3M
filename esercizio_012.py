#esercizio 12

#Dato un importo, applicare lo sconto del 5% e considerare l'IVA al 12%.

#inizio

importo = int(input("Inserire l'importo: "))

#calcolo dello sconto

risultato = (importo / (5/100)) 

risultato = risultato + (importo * (12/100))

#risultato importo

print(f"L'importo totale e': {risultato}")
