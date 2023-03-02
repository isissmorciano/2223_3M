#Chiedo il numero di contribuenti
contribuenti = int(input("Inserisci numero di contribuenti: "))
#Creo un loop dove chiedo nome, codice fiscale e reddito
for i in range(contribuenti):
    nome = input("Nome > ")
    c_fiscale = input("Codice fiscale > ")
    reddito = int(input("Reddito > "))
    #Stampo il nome e codice fiscale in caso il reddito sia maggiore o uguale a 30000.
    if reddito >= 30000:
        print("Nome:",nome,"\nCodice Fiscale:",c_fiscale)