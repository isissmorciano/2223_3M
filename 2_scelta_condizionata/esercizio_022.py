#Inizio

#Spiegazione
print("Dare 3 valori di 3 lati di un triangolo, verrà comunicata la precisa tipologia.")

#Richiesta delle variabili
l1 = float(input("\nDigita misura del primo lato: "))
l2 = float(input("Digita misura del secondo lato: "))
l3 = float(input("Digita misura del terzo lato: "))

#Controllo della tipologia
if l1 != l2 and l1 != l3 and l2 != l3:

	print("\n\nIl triangolo è scaleno.")

elif l1 == l2 and l1 != l3 or l1 == l3 and l1 != l2 or l2 ==l3 and l2 != l1:

	print("\n\nIl triangolo è isoscele.")

else:
	print("\n\nIl triangolo è equilatero.")

#Fine