#inizio

#input
carattere = str(input("Inserisci il carattere: "))

#Elaborazione
if carattere == 'S' or carattere == 's':
    print("Si")

if carattere == 'N' or carattere == 'n':
    print("No")

if carattere != 'S' and carattere != 's' and carattere != 'N' and carattere != 'n':
    print("Errato")
