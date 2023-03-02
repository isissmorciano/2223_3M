
#spiegazione
#inizio
#inserimento dell'anno
anno=int(input("Inserire l'anno desiderato: "))
#calcoli e visualizzazione del risultato
if(anno%4 == 0) and (anno%100 != 0) or (anno%400 == 0):
    print("è un'anno bisestile")
else:
    print("non è bisestile")