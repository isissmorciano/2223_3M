import random
#Creare una funzione(?) numero_casuale() che restituisce un numero casuale tra 0 e 99. La funzione restituisce il numero generato numero_casuale(). Utilizzare il type-hinting.
def numero_casuale():
    num=random.randint(0,99)
    print(num)

numero_casuale()