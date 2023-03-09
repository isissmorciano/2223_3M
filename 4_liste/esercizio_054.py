#.Data una lista con elementi: "Signore Mario" e/o "Signora Maria", dre in output una lista dei soli nomi femminili senza volitivo.
print("*******************************************************************************************")
print("| Questo programma tramite l'utilizzo delle liste, stampa i nomi femminili senza volitivo |")
print("| Dice quanti sono i nomi femminili e generare una nuova lista con i nomi femminili       |")
print("*******************************************************************************************")

#Es1
#Nomi nella lista
Lista_Nomi=["Signora Marina", "Signor Luigi", "Signora Sara ", "Signor Eugenio", "Signor Annibale", "Signora Lara", "Signora Barbara", "Signor Gabriele", "Signora Graziana", "Signor Mirco"]

Nuova_Lista = [x for x in Lista_Nomi if "Signora" in x ]
print(Nuova_Lista)
#ciclo
for i in Nuova_Lista:
    print(i[8:])

#Es 2
print("####################################################################################################################################################")
for i in(Nuova_Lista):
    print("Sig.ra", i[8:])
