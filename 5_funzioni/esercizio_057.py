#esercizio 57
#definizione funzione descrizione()
def descrizione(nome:str,eta:int) -> str:
    return f"{nome} ha eta' {eta}"
#main
nome=input("Inserisci nome: ")
eta=int(input("Inserisci l'eta': "))
print(descrizione(nome,eta))
