# Creare una funzione che restituisce se un numero intero ha almeno 3 divisori.
# Creare poi un programma che dica se un numero passato dall’utente e il più 
# grande numero intero più piccolo del suo quadrato hanno almeno tre divisori.
#inizializzazione funzione
def tre_divisori_minimo(num):
    divisori = 0
    for i in range(1, num + 1):
        if num % i == 0:
            divisori += 1
            if divisori >= 3:
                return True
    return False

# chiedi all'utente di inserire un numero
numero = int(input("Inserisci un numero intero: "))

# calcola il più grande numero intero più piccolo del quadrato del numero inserito
quadrato = numero ** 2
num_intero = quadrato - 1

# verifica se entrambi i numeri hanno almeno 3 divisori
if tre_divisori_minimo(numero) and tre_divisori_minimo(num_intero):
    print(f"{numero} e {num_intero} hanno entrambi almeno 3 divisori.")
else:
    print(f"{numero} e/o {num_intero} non hanno entrambi almeno 3 divisori.")
