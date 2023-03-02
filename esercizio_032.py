#Esercizio 32
#Scrivi un programma che calcoli il valore della circonferenza e quello dell'area di tutti i cerchi con raggio compreso tra 1 e 20.

#Importo la libreria math
import math

#Faccio ciclo che calcola la circonferenza e l' area
for i in range(1, 21):
    circonferenza = 2 * math.pi * i
    area = math.pi * i ** 2
    print(f"Raggio: {i}, Circonferenza: {circonferenza}, Area: {area}")
