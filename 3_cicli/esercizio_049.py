print("*******************************************************************************************")
print("|                Questo programma ti scrive il nome del cd con durata maggiore                 |")
print("*******************************************************************************************")


N=int(input("Quanti cd vuoi prendere in considerazione?"))
max=0

for i in range(N):
    titolo=str(input("Inserisci titolo cd: "))
    nb=int(input("Quanti brani compongono il cd? "))

    
    for i in range(nb):
        tb=str(input("Inserisci il titolo del brano: "))
        db=int(input("Inserisci la durata del brano in minuti: "))


        if db>max:
            max=db

print(max)