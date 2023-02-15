#Esercizio 5

#Scrivi un algoritmo che determini la circonferenza e l’area di un cerchio conoscendo il raggio.

#inizio

#raggio e pgreco

raggio = int(input("Determinare il raggio: "))
pgreco = 3.14

#determinazione della circonferenza

circonferenza = (pgreco * 2) * raggio

circonferenza = round(circonferenza, 2)

print(f"La circonferenza ottenuta e': {circonferenza}")

#determinazione dell'area

area = (pgreco) * (raggio**2)

print(f"L'area ottenuta e': {area}")
