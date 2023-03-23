#Esercizio 2

#inizio
#Dato un nominativo di un alunno e 3 voti di una materia visualizzare la media dei voti

#Scritta a schermo di cosa fa il programma
print("Dato un nominativo di un alunno e 3 voti di una materia visualizzare la media dei voti")

#Inserimento dell'importo
nome = input("Inserisci il tuo nome: ")

#Inserimento dei tre voti
voto1=int(input("Inserisci il primo voto: "))
voto2=int(input("Inserisci il secondo voto: "))
voto3=int(input("Inserisci il terzo voto: "))

#Calcolo media
media=(voto1+voto2+voto3)/3

#Scrivo la media con il nome dell' alunno
print("L'alunno ", nome,"ha come media:", media)
#fine