#Dato N inserito dall'utente:
#- stampare il massimo numero inserito
#- stampare il minimo numero inserito
#- stampare la media dei numeri inseriti
#- stampare la media di solo i numeri positivi inseriti

#Assegno un valore a tutte le variabili che non ne hanno.
massimo=0
media=0
mediapos=0
poscont=0
totale= 0
minimo=0
#Inserisco un valore per n, cioè il numero di volte che il programma ti chiederà di scrivere un numero.
n=int(input("Quante numeri vuoi scrivere? "))

for i in range(1,n+1): #Fallo per tot volte
    num=int(input(f"Scrivi il {i}° numero: "))
    #Affinchè minimo non sia fisso 0
    if minimo == 0:
        minimo = num
    #Serve a salvare il numero più grande
    if massimo < num:
        massimo = num         
    #Salva il numero più piccolo registrato
    elif num < minimo:
        minimo = num
    #Salva la media dei numeri positivi
    if num > 0:
        mediapos = mediapos + num
        poscont = poscont + 1
    media = media + num
    totale = totale + num
    
#Calcolo la media alla fine
media=media/n
mediapos=mediapos/poscont
#Scrivo il risultato a schermo.
print("")
print(f"Il numero più alto che hai inserito è: {massimo}") 
print(f"Il numero più basso che hai inserito è: {minimo}") 
print(f"La media è: {media}") 
print(f"La media positiva è:{mediapos}")