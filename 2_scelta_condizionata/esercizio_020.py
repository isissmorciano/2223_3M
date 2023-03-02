#consegna
print("inserisci un numeri(da 1 a 7) ti dira che giorno della settimana è")

Ng = int(input(" che numero vuoi inserire ?  "))
if Ng <=7 and Ng >= 1:
    match Ng:
        case 1:
            print("monday")
        case 2:
            print("tuesday")
        case 3:
            print("wednesday")
        case 4:
            print("thursday")
        case 5:
            print("friday")
        case 6:
            print("saturday")
        case 7:
            print("sunday")
else :
    print ("errore")