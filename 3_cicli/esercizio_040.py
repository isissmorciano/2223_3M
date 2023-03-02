print("|-----------------------------------------------------------------------------------|")
print("|                        ti calcola il peso il programma                            |")
print("|-----------------------------------------------------------------------------------|")
kilo=2

#inserire quanti ci sono
persona=int(input("Inserisci quanti persona ci sono:"))
for i in range(persona):
    t=float(input("Inserisci la tua altezza: "))
    peso=float(input("Inserisci il tuo peso: "))
    obeso=t/peso

    #inizio cilo
    if obeso<=kilo:
        print("Sei obeso")
    else:
        print("Non sei obeso")