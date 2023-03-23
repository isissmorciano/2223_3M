#Inizio

#Spiegazione 
print("Inserire due date in gg/mm/aaaa considerando che tutti i mesi hanno un massimo di 30 giorni per convenzione. Verrà calcolato il tempo trascorso tra le due date.")

#Richiesta variabili 
print("\nPrima data:")
gg1 = int(input("\nInserire Giorno: "))
mm1 = int(input("Inserire Mese: "))
aaaa1= int(input("Inserire Anno: "))

print("\nSeconda data:")
gg2 = int(input("\nInserire Giorno: "))
mm2 = int(input("Inserire Mese: "))
aaaa2 = int(input("Inserire Anno: "))

#Calcoli
somma1 = gg1 + (mm1*30) + (aaaa1*360)		
somma2 = gg2 + (mm2*30) + (aaaa2*360)		


if aaaa1>aaaa2:
	differenza = int(somma1 - somma2)				
	anni = int(differenza/360)
	differenza = differenza-anni*360
	mesi = int(differenza/30)
	giorni = differenza-mesi*30

elif aaaa2>aaaa1:
	differenza = int(somma2 - somma1)				
	anni = int(differenza/360)
	differenza = differenza-anni*360
	mesi = int(differenza/30)
	giorni = differenza-mesi*30

else:
	if mm1==mm2:
		if gg1>gg2:
			differenza = int(somma1 - somma2)				
			anni = int(differenza/360)
			differenza = differenza-anni*360
			mesi = int(differenza/30)
			giorni = differenza-mesi*30
			
		elif gg2>gg1:
			differenza = int(somma2 - somma1)				
			anni = int(differenza/360)
			differenza = differenza-anni*360
			mesi = int(differenza/30)
			giorni = differenza-mesi*30

		else:
			differenza = int(somma1 - somma2)				
			anni = int(differenza/360)
			differenza = differenza-anni*360
			mesi = int(differenza/30)
			giorni = differenza-mesi*30
	
	elif mm1>mm2:
		differenza = int(somma1 - somma2)				
		anni = int(differenza/360)
		differenza = differenza-anni*360
		mesi = int(differenza/30)
		giorni = differenza-mesi*30		
	
	else:
		differenza = int(somma2 - somma1)				
		anni = int(differenza/360)
		differenza = differenza-anni*360
		mesi = int(differenza/30)
		giorni = differenza-mesi*30

#Lettura a schermo del risultato
print("Il tempo trascorso tra le date è di ",anni,"anno/i,",mesi,"mese/i e ",giorni,"giorno/i.")