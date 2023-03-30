#Inizio

#Utilizzo del programma
print("------------------------------------------------------------------------------------------------------------")
print("-          Il programma calcola area e perimetro di un triangolo e distingue la sua tipologia.             -")
print("------------------------------------------------------------------------------------------------------------")

#Richiesta variabili
l1 = float(input("Digita la misura del 1° lato: "))
l2 = float(input("Digita la misura del 2° lato: "))
l3 = float(input("\nDigita la misura del 3° lato: "))

#Elaborazione dati
if l1 != l2 and l1!= l3 and l2 != l3:
	print("\nIl triangolo è scaleno.")

	perimetro = (l1 + l2 + l3)

	base = float(input("\nInserire il valore della base: "))
	alte = float(input("Inserire il valore dell'altezza: "))

	area = base * (alte / 2)

	print("Il perimetro del triangolo è: ",perimetro)
	print("L'area del triangolo è: ",area)

elif l1 == l2 and l1 == l3:
	print("Il triangolo è equilatero.")

	perimetro = (l1 + l2 + l3)

	alte = 3**(1/2)
	alte = alte * l1
	alte = alte / 2

	area = l1 * (alte / 2)
	
	print("Il perimetro del triangolo è: ",perimetro)
	print("l'area del triangolo è: ",area)

else:
	print("Il triangolo è isoscele.")
	
	if l1 != l2 and l1!=l3:

		alte =l1/2
		alte = l2**2 + alte**(1/2)
		alte = alte ** (1/2)

		perimetro = l1 + l2 + l3
		area = (l1 * alte)/2
		print("Il perimetro del triangolo è: ",perimetro)
		print("l'area del triangolo è: ", area)
	
	elif l2!=l1 and l2!=l3:

		alte =l2/2
		alte = l1**2 + alte**(1/2)
		alte = alte ** (1/2)

		perimetro = l1 + l2 + l3
		area = (l2 * alte)/2
		print("Il perimetro del triangolo è: ",perimetro)
		print("l'area del triangolo è: ", area)
	
	else: 

		alte =l3/2
		alte = l2**2 + alte**(1/2)
		alte = alte ** (1/2)

		perimetro = l1 + l2 + l3
		area = (l3 * alte)/2
		print("Il perimetro del triangolo è: ",perimetro)
		print("l'area del triangolo è: ", area)

#Fine