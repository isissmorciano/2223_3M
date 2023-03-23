#Calcolare l'n-esimo numero della successione di Fibonacci. Creare la funzione iterative_fibonacci(n:int) -> int che calcola il numero in modo iterativo. Creare la funzione recursive_fibonacci(n:int) -> int che calcola il numero in modo ricorsivo.
n=int(input("inserisci il numero: "))

#funzione iterativa
def iterative_fibonacci(n:int)->int :
    if n<=0:    
        print("no")
        exit(1)
    elif n==1:
        return 0   
    else:
        fib_2prec=0
        fib_prec=1
        for i in range(2, n):
            fibn = fib_2prec+fib_prec
            print(f'n di fibonacci: {fibn} n di fibonacci precedente{fib_prec} n di fibonacci precedente a quest ultimo{fib_2prec}')
            fib_2prec=fib_prec
            fib_prec=fibn
        return fibn
fibn =iterative_fibonacci(n)
print(fibn)
n=int(input("inserisci il numero: "))

#funzione ricorsiva
def recursive_fibonacci(n):
    if n<=0:
        print("non credo")
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return recursive_fibonacci(n-1)+recursive_fibonacci(n-2)
risultato=recursive_fibonacci(n)
print(risultato)
