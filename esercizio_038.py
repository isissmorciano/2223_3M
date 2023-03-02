#Dati in input i risultati relativi a N seggi elettorali, per ogni seggio hai le seguenti informazioni : numero iscritti, numero votanti, numero di schede nulle, numero di schede bianche. Scrivi un programma che stampi il seguente prospetto: percentuale votanti su tutti i seggi, percentuale schede bianche, percentuale schede nulle.
#Importiamo random 
import random

#Stabilisce il numero di volte che vai a fare il ciclo
elezioni = int(input("Quanti seggi eletoriali ci sono? "))

#Calcolo casuale degli iscritti, votanti, schede nulle e bianche
for i in range(elezioni):
 
    iscritti=random.randint(1,100)
    votanti=random.randint(1,100)
    schedeNulle=random.randint(1,50)
    schedeBianche=random.randint(1,50)
    print("")
    print(f"Gli iscritti sono: {iscritti}")
    print(f"I votanti sono: {votanti}")
    print(f"Le schede nulle sono: {schedeNulle}")
    print(f"Le schede bianche sono: {schedeBianche}")
    print("")

#Ciclo per calcolare la percentuale
for i in range(1):

    perc_i = iscritti * (elezioni / 100)
    perc_v = votanti * (elezioni / 100)
    perc_sn = schedeNulle * (elezioni / 100)
    perc_sb = schedeBianche * (elezioni / 100)
#Stampo a schermo i risultati.
    print(f"Le percentuali sono:")
    print(f"Iscritti = {iscritti}%")
    print(f"Votanti = {votanti}%")
    print(f"Schede nulle = {schedeNulle}%")
    print(f"Schede bianche = {schedeBianche}")
