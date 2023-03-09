import statistics
#Pelusi Matteo

import random
tot_num=0
num1=0


#N1 creare una lista di 8 numeri random tra 1 e 10 (estremi inclusi)
lista_num = []
for i in range(8):
    n = random.randint(1, 10)
    lista_num.append(n)
    lista_num.sort() #ordino per comoditá
print(lista_num)

#N2  calcolare il massimo dei numeri
NumAlto=lista_num[-1]

#N3 calcolare il minimo dei numeri
NumBasso=lista_num[0]

#N4 calcolare la moda dei numeri
Moda=statistics.mode(lista_num)

#N5 creare una lista con i tre risultati
lista_risultati = [NumAlto,NumBasso,Moda]

#N6 stampare la lista con i risultati
print(lista_risultati)
