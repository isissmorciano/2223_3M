#Esercizio 60
#Creare una funzione(?) descrizione_casuale(). Il nome e' scelto in modo casuale da una lista di nomi interna alla fuzione. L'eta e' calcolata in modo casuale La funzione restituisce una stringa formattata nel seguente modo: "nome ha eta anni." descrizione_casuale()

#Inizio
import random
lista = ["giorgio" , "franci", "gregorio","Manuele"]
def scelta():
    nome=random.choice(lista)
    eta = random.randint(1,199)
    return nome , "ha eta ", eta
s = scelta()
print(s)
#Fine
