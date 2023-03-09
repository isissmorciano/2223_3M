#Creare un programma che fa inserire all’utente tre caratteri e usando una funzione verifica e stampa quanti di questi sono lettere maiuscole.
# input
lettera1 = input("Inserisci la prima lettera: ")
lettera2 = input("Inserisci la seconda lettera: ")
lettera3 = input("Inserisci la terza lettera: ")

#inizializzazione funzione
def conta_maiusc(let1, let2, let3):
    count = 0
    if let1.isupper():
        count += 1
    if let2.isupper():
        count += 1
    if let3.isupper():
        count += 1
    return count

# output
n_maiuscole = conta_maiusc(lettera1, lettera2, lettera3)
print(f"Hai inserito {n_maiuscole} lettere maiuscole.")