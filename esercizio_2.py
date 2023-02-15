#Cristian Uva 3M 30/09/2022
#Esercizio 2

#Scritta a schermo dei voti
print ("Inserisce i 3 voti e la materia di cui vuoi fare la media: ")

#Inserimento del numero della materia, voto1, voto2, voto3 
materia = input("Inserisci il nome della materia: ") 
voto1 = int(input("Inserisci il primo voto: "))
voto2 = int(input("Inserisci il secondo voto: "))
voto3 = int(input("Inserisci il terzo: "))

#Calcolo media
media = ((voto1 + voto2 + voto3) / 3)
#Lettura a schermo della media
print ("La media di " + materia, "e'", media) 