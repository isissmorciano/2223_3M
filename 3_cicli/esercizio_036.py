#Esercizio N36
#Il programma calcola il prodotto di due numeri interi senza usare la moltiplicazione

#inizio
num1=int(input("Inserire il primo numero (l'ordine dei numeri non ha importanza): "))
num2=int(input("Inserire il secondo numero: "))

#elaboro prodotto
x=num1
for num2 in range(1, num2):
    
    num1=num1+x

#stampo a schermo
print("\nIl prodotto è: ", num1)
#fine
