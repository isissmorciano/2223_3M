#Creare una funzione descrizione_eta_casuale() con un parametro nome. L'eta e' calcolata in modo casuale La funzione restituisce una stringa formattata nel seguente modo: "nome ha eta anni." descrizione_eta_casuale("Pippo")
import random
def descrizione_eta_casuale():
    eta = random.randint(0,200)
    nome = "pippo"
    return nome ,"ha ",eta,"anni"
s=descrizione_eta_casuale()
print(s)

