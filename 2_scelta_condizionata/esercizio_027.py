#Inizio
#Richiesta numeri di opzione e da calcolare
scelta=int(input(f'inserisci il numero di scelta: '))
num=float(input(f'inserisci il numero: '))
#calcolo scelta
if (scelta== 1):
	num=num**2
	print(num)
if (scelta== 2):
	num=num**3
	print(num)
if (scelta== 3):
	if (num<= 0):
		print(f'errore')
	else:
		num=num**(1/2)
		print(num)
#controllo se inserito numero fuori dal menu'
if scelta!= 1 and scelta!= 2 and scelta!= 3:
	print(f'errore')