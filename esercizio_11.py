#Esercizio 11
#Data un'equazione di 2° grado che abbia come soluzione “due numeri reali distinti” (Delta>0), calcoli tali valori, il fuoco e il vertice. Visualizzare oltre ai valori sopracitati anche il valore del delta.
#Per fare la radice quadrata, importo la libreria math
import math 

#Scritta a schermo di cosa fa il programma
print ("Data un equazione di 2° grado che abbia \
come soluzione “due numeri reali distinti” (Delta>0), calcoli tali valori, \
il fuoco e il vertice.  Visualizzare oltre ai \
valori sopracitati anche il valore del delta.")

#Inserimento dei valori di a b c
print ("Inserisco i valori delle assi larghe, piccole e numero di riquadri e l'iva")
a  = int(input("Inserisci il numero da associare ad a: "))
b  = int(input("Inserisci il numero da associare a b: "))
c  = int(input("Inserisci il numero da associare a c: "))

#Calcolo della disequazione 
delta = (b * b) - (4 * a * c) 
radice = math.sqrt(abs(delta)) 
x1 = ((-b + radice)/(2 * a)) 
x2 = ((-b - radice)/(2 * a)) 
fuoco = ((-b / (2 * a)),(((4 * a * c) - (b * b) + 1) / (4 * a)))
vertice = ((-b / (2 * a)),(((4 * a * c) - (b * b)) / (4 * a)))
          
#Lettura a schermo del risultato
print ("Il delta è: ", radice)  
print ("Il primo valore di x è :", x1 ) 
print ("Il secondo valore di x è :", x2 ) 
print ("Il fuoco è:", fuoco) 
print ("Il vertice è:", vertice) 