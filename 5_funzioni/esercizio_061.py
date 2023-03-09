#Scrivere una procedura che permetta di scambiare il contenuto di due variabili intere. 
X=input("Inserisci il valore di X: ")
Y=input("Inserisci il valore di Y: ")
#inizio funzione
def scambio(X:int , Y:int ):
    
    temp=X
    X=Y
    Y=temp

    print(f"La variabile X è:", X)
    print(f"La variabile Y è:" , Y)

scambio(X,Y)
print("fine es 1")

