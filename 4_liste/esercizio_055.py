#.Data in input una lista dei soli nominativi femminili, dire quanti sono i nomi femminili e generare una nuova lista con i nomi femminili e il volitivo esempio: "Sig.ra Maria" e visualizzarlo.
print("*************************************************************************************")
print("| Dice quanti sono i nomi femminili e generare una nuova lista con i nomi femminili |")
print("*************************************************************************************")


#Nomi nella lista
Lista_Nomi=["Signora Marina", "Signor Luigi", "Signora Sara ", "Signor Eugenio", "Signor Annibale", "Signora Lara", "Signora Barbara", "Signor Gabriele", "Signora Graziana", "Signor Mirco"]

Nuova_Lista = [x for x in Lista_Nomi if "Signora" in x ]



print("####################################################################################################################################################")
#Cambiamento da Signora a Sig.ra
for i in(Nuova_Lista):
    print("Sig.ra", i[8:])
