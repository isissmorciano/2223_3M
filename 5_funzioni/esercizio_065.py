#Pelusi Matteo 3M
#es 65

#definisco la funzione differenza
def differenza(num1, num2, num3):
    Vmin = min(num1, num2, num3)
    Vmax = max(num1, num2, num3)
    return Vmax - Vmin

#Main
# richiesta informazioni
num1 = int(input("Inserisci il primo numero intero: "))
num2 = int(input("Inserisci il secondo numero intero: "))
num3 = int(input("Inserisci il terzo numero intero: "))

# Calcolo della differenza 
differenza_num = differenza(num1, num2, num3)
#stampa a schermo
print("La differenza è:",differenza_num)
