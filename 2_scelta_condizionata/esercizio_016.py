#inizio
#spiegazione
print("Sul prezzo di un prodotto viene applicato il 15%  di sconto se acquista un massimo di 10 prodotti ed un 20%  se qcquista più di 10 prodotti")
x=int(input("quanti prodotti vuoi acquistare "))
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
#fine