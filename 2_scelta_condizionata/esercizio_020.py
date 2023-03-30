#consegna
print("Inserisci un numero (da 1 a 7) e il programma stampa a che giorno della settimana corrisponde.")

Ng = int(input("Che numero vuoi inserire?: "))
if Ng <=7 and Ng >= 1:
    match Ng:
        case 1:
            print("\nMonday")
        case 2:
            print("\nTuesday")
        case 3:
            print("\nWednesday")
        case 4:
            print("\nThursday")
        case 5:
            print("\nFriday")
        case 6:
            print("\nSaturday")
        case 7:
            print("\nSunday")
else :
    print ("\nerrore.")