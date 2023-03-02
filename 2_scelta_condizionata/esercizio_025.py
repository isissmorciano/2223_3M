print("*******************************************************************************")
print("Il programma di dice quanto pagare le fotocopie a seconda di quante ne vuoi")
print("********************************************************************************")
#variabili
numero=int(input("Inserisci il numero di fotocopie che vuoi"))
nome=str(input("Inserisca il suo nome: "))
#condizioni
if numero>0 and numero<20:
	prezzo=(numero*0.10)
	print("Il costo è: " ,prezzo)
if numero>19 and numero<101:
	prezzo=(numero*0.08)
	print("Il costo è: " ,prezzo)
if	numero>100:
	prezzo=(numero*0.05)
	print("Il costo è: " ,prezzo)
rilegatura=str(input("Vuoi la rilegatura(S/N)?"))
if rilegatura=='S':
	prezzo=(prezzo+1.8)
	print("Gentile signore: ",nome)
	print("Il suo preventivo con rilegatura è:  ",prezzo)
if rilegatura=='N':
	print("Gentile signor",nome)
	print("Il suo preventivo è di:", prezzo)
