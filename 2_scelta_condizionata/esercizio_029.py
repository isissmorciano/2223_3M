#Inizio
#spiegazione
print("Calcolare il costo di una vacanza.")

gio = int(input("Inserire giorni di permanenza: "))

if gio<=7:
	sco= 600/gio
	costo=100+(600-sco)+20
	print("Il costo totale è: ", costo)

elif gio<=14:
	sco= 1100/gio
	costo=100+(1100-sco)+40
	print("\nIl costo totale è: ", costo)

else:
	print("Errore")