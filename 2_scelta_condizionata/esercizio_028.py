#Questo programma calcola l'area e il perimetro di un triangolo isoscele, equilatero o scaleno.
#inizio

print("|------------------------------------------------------|")
print("|Verrà calcolata l'area e il preimetro del triangolo.  |")
print("|1) Equilatero                                         |")
print("|2) Isoscele                                           |")
print("|3) Scaleno                                            |")
print("|4) Rettangolo                                         |")
print("|------------------------------------------------------|")

opz=str(input("\nScegliere il tipo di triangolo che si vuole calcolare: "))

ipo=float(input("Inserire primo lato (ipotenusa): "))
cat1=float(input("Inserire secondo lato (cateto 1): "))
cat2=float(input("Inserire terzo lato (cateto 2): "))

match opz:
	case "1":
		per=ipo+cat1+cat2
		area=(3**(1/2)/4)*ipo**2
		print("Triangolo Equilatero\nPerimetro: ", per, "\nArea: ", area)

	case "2":
		per=ipo+cat1+cat2
		h=(cat1**2-(ipo/2)**2)**(1/2)
		area=(ipo*h)/2
		print("Triangolo Iscoscele\nPerimetro: ", per, "\nArea: ", area)

	case "3":
		per=ipo+cat1+cat2
		h=cat1*cat2/ipo
		area=ipo*h/2
		print("Triangolo Scaleno\nPerimetro: ", per, "\nArea: ", area)

	case "4":
		per=ipo+cat1+cat2
		area=(cat1*cat2)/2
		print("Triangolo Rettangolo\nPerimetro: ", per, "\nArea: ", area)
	case _:
		print("Scegliere un'opzione valida.")