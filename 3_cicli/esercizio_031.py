#es 31

#Scrivere 10 volte la parola "ciao", sommare i numeri da 10 a 20 (compresi gli estremi), sommare i numeri pari fino a 30 (30 incluso) e moltiplicare i numeri da 1 a 10

#Inizio

#Printare 10 volte ciao
for i in range(10):
    print("Ciao")

#Sommare i numeri da 10 a 20 (compresi gli estremi)
n = 0
for i in range(10, 21):
    n += i

print(f"La somma e' {n}")

#Sommare i numeri pari fino a 30 (30 incluso)
somma = 0
for i in range(0, 31, 2):
    somma += i

print(f"La somma e' {somma}")

#Moltiplicare i numeri da 1 a 10
molti = 1
for i in range(1,11):
    molti = molti * i

print(f"La moltiplicazione e' {molti}")