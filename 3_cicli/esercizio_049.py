print(f'*******************************************************************************************')
print(f'|                Questo programma ti scrive il nome del cd con durata maggiore                 |')
print(f'*******************************************************************************************f')


N=int(input(f'Quanti cd vuoi prendere in considerazione? '))
max=0

for i in range(N):
    titolo=str(input(f'Inserisci titolo cd: '))
    nb=int(input("Quanti brani compongono il cd? "))

    
    for i in range(nb):
        tb=str(input(f'Inserisci il titolo del brano: '))
        db=int(input(f'Inserisci la durata del brano in minuti: '))


        if db>max:
            max=db

print(max)