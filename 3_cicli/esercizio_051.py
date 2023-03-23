print("**************************************************************************************************************************************")
print("|                    Leggi dalla tastiera una serie di coppie di numeri interi, una coppia per ogni riga.                              | ")        
print("|Conta le coppie che presentano due valori che siano uguali. La serie termina quando entrambi ii valori letti in input sono uguali a 0.|")
print("**************************************************************************************************************************************")
count = 0
while True:
    x= int(input()) 
    y = int(input())
    if x == 0 and y == 0:
        break
    if x == y:
        count += 1