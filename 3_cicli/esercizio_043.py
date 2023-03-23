print("""*************************************************************************************
|            Questo programma scrive tra una serie di prodotti il più costoso       |
*************************************************************************************""")
i=0
N=int(input("Quanti prodotti vuoi inserire?:  "))

prezzo=float(input("Inserisci il prezzo del primo:  "))
descrizione= str(input("inserisci la descrizione: "))
code= str(input("inserisci il codice: "))   
for i in range(N-1):
    n = float(input("Inserisci il prossimo prezzo:  "))
    codicen = str(input("inserisci codice prodotto: "))
    descrizionen = str(input("inserisci la descrizione: "))

    if n > prezzo:
        prezzo = n
        code = codicen
        descrizione = descrizionen

    i += 1

print("La descrizione e codice del prodotto più costoso sono: ", code, descrizione)

    

