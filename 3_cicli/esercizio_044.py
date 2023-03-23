#Di N città si conoscono il numero di abitanti e il numero di quelli attivi. 
#Calcola per ciascuna città l'indice di attività (attivi/abitanti * 100)
#e stampa il nome della città con l'indice più basso e di quella con l'indice più alto.

print("**********************************************************************")
print("|        Il programma di dice tra N città chi ha il tasso di attività|")
print("|                                     maggiore e minore              |")
print("**********************************************************************")

#dichiarazione delle variabili
indice =0
nome_max = str
nome_min = str
#intrudizione
print("questo programma dato un numero di citta ti calcola l'indice di abitnti di ogni citta e ti stampa il più basso")
#Inserimento dei dati in input
numero_città = int(input("inserisci il numero  delle citta: "))
#Ciclo for 
for i in range(1,numero_città+1) :
    nome_citta = input(f"nome della città {i}° città:  ")
    abitanti = int(input("quanti abitanti che ci sono :  "))
    abitanti_attivi = int(input("quanti abitanti attivi ci sono :  "))
#Calcolo dell'indice degli abitanti        
    indice_abitanti =abitanti_attivi /abitanti*100
#Condizioni per calcolare l'indice max e min
    if indice == 0 :
        indice = indice_abitanti
    if indice_abitanti >= indice : 
        indice_max = indice_abitanti
        nome_max = nome_citta
    if indice_abitanti <= indice :
        indice_min= indice_abitanti
        nome_min= nome_citta
#Stampo a schermo la città con il maggior indice di abitanti e quella con il minore.    
print("La città con il maggior indice di abitanti è {nome_max} con indice {indice_max}")
print("La città con il minor indice di abitanti è {nome_min} con indice {indice_min}")