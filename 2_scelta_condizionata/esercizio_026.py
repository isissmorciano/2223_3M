#Es n.26 Salvatore Ciaramidaro 3^M

#Inserimento input
nominativo = input(f'Inserire il proprio nome e cognome: ')
voto1 = int(input(f'Inserire un voto da 1 a 10: '))
voto2 = int(input(f'Inserire un voto da 1 a 10: '))
voto3 = int(input(f'Inserire un voto da 1 a 10: '))
voto4 = int(input(f'Inserire un voto da 1 a 10: f'))


#Calcolo media dei 4 voti
media = ((voto1 + voto2 + voto3 + voto4)/4)

#Determinazione media sufficiente o insufficiente
#La media è sufficiente se è compreso tra 6 e 10
if (media>=6) and (media<=10):
	print(f'Studente: {nominativo}')
	print(f'Media: {media}')
	print(f'Media sufficiente')
#La media è insufficiente se è compresa tra 1 e minore di 6
elif (media>=1) and (media<6):
	print(f'Studente: {nominativo}')
	print(f'Media: {media}')
	print(f'Media insufficiente')