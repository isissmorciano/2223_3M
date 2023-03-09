#Scrivere una procedura che effettui il confronto,la convalidazione e il calcolo della differenza fra due date espresse in giorno, mese, anno.


#input
print('Inserisci due date dello stesso anno')

print('Inserisci la prima data')
giorno1 = int(input('Inserisci il giorno: '))
mese1 = int(input('Inserisci il mese: '))

print("inserisci la seconda data")
giorno2 = int(input('Inserisci il giorno: '))
mese2 = int(input('Inserisci il mese: '))



#verifichiamo che le date inserite siano corrette

if giorno1 == 0 or mese1 == 0:

    print("La data che inserita non è corretta.")
if mese1 == 2:   
        if giorno1 > 0 and giorno1 <= 29:
            print("La data inserita è corretta.")
        else:
            print("La data inserita non è corretta.")    
elif mese1 == 4 or mese1 == 6 or mese1 == 9 or mese1 == 11:
    if giorno1 > 0 and giorno1 <= 30:
        print("La data inserita è corretta.")
    else:
        print("La data inserita non è corretta.")
else:
    if giorno1 > 0 and giorno1 <= 31:
        print("La data inserita è corretta.")
    else: 
        print("La data inserita non è corretta.")
if giorno2 == 0 or mese2 == 0:

    print("La data che inserita non è corretta.")
if mese2 == 2:   
        if giorno2 > 0 and giorno2 <= 29:
            print("La data inserita è corretta.")
        else:
            print("La data inserita non è corretta.")    
elif mese2 == 4 or mese2 == 6 or mese2 == 9 or mese2 == 11:
    if giorno2 > 0 and giorno2 <= 30:
        print("La data inserita è corretta.")
    else:
        print("La data inserita non è corretta.")
else:
    if giorno2 > 0 and giorno2 <= 31:
        print("La data inserita è corretta.")
    else: 
        print("La data inserita non è corretta.")
        
# inizio a fare le verifiche
def diff_date(mese1: int, giorno1: int, mese2: int, giorno2: int):
    if mese1 >= mese2:
        mese = mese1 - mese2
        if giorno1 >= giorno2:
            giorno = giorno1 - giorno2
        else:
            giorno = giorno2 - giorno1
    else:
        mese = mese2 - mese1
        if giorno1 >= giorno2:
            giorno = giorno1 - giorno2
        else:
            giorno = giorno2 - giorno1
    return mese, giorno

mese, giorno = diff_date(mese1, giorno1, mese2, giorno2)
#stampa a scherm ogli input
print('Ci sono', mese, 'mesi e', giorno, 'giorni di distanza.')