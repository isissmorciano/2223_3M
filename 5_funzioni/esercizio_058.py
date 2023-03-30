#Esercizio N58
#Creare una funzione numero_casuale che restituisce un numero casuale tra 0 e 99. La funzione restituisce il numero generato numero_casuale().

import random
#inizio
#definisco funzione
def numero_casuale():
    num=random.randint(0,99)
#stampo a schermo numero generato    
    print(num)

numero_casuale()
#fine