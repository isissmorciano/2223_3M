#Inizio
print("**************************************************************************************")
print("*Questo programma calcola il quadrato di un numero usando però i primi N numeri primi*")
print("**************************************************************************************")

#Richiesta del numero
n=int(input("\nInserisci il numero del quale vuoi il quadrato:  "))
x=1
n1=1

#Calcolo del quadrato
for i in range(1,n):
    x=x+2
    n1=n1+x
print(n1)

#Fine