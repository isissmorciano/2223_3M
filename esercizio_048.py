print("***********************************************************************")
print("|    Il programma ti stampa N numeri, sempre il doppio del precedente |")
print("***********************************************************************")
N = int(input("Inserisci il valore di N: "))
num = 1

for i in range(N):
    print(num)
    num *= 2

