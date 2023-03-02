#Esercizio 6
#Calcola il tempo trascorso tra due date espresse in giorni, mesi e anni (es: 12/06/2020). Consideriamo i mesi di 30 giorni.

#Scritta a schermo di cosa fa il programma
print ("Calcola il tempo trascorso tra due date espresse in giorni, mesi e anni \
considerando tutti i mesi di 30 giorni e gli anni 365 giorni: ")

#Inserimento dei valori dei giorni, mesi e anni della prima data
print ("Inserimento dei valori dei giorni, mesi e anni della prima data")
giorni = int(input("Inserisci il giorno: "))
mese = int(input("Inserisci il mese: "))
anno = int(input("Inserisci l'anno: "))

#Inserimento dei valori dei giorni, mesi e anni della seconda data
print ("Inserimento dei valori dei giorni, mesi e anni della seconda data")
giorni2 = int(input("Inserisci il giorno: "))
mese2 = int(input("Inserisci il mese: "))
anno2 = int(input("Inserisci l'anno: "))

#Calcolo della differenza tra le 2 date
data1 = (giorni + mese * 30 + anno * 360)
data2 = (giorni2 + mese2 * 30 + anno2 * 360)
differenza = int(data1 - data2)

#Calcolo degli anni, mesi e giorni
difAnni = int(differenza /360 )
differenza=differenza-(difAnni*360)
difMesi = int(differenza / 30)
difGiorni=differenza-(difMesi*30)

#Lettura a schermo del risultato
print ("La differenza dei giorni, mesi e anno tra i 2 è \n" 
	 ,difGiorni, "giorni", difMesi, "mese", difAnni, "anni") 
