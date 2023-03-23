#Es 54
#Albergo quarta categoria = 1 stella
#Albergo terza categoria = 2 stelle
#Albergo seconda categoria= 3 stelle
#Albergo prima categoria = 4 stelle
#Albergo categoria lusso = 5 stelle

n=int(input("Inserisci il numero di alberghi: "))

#ciclo
for i in range(n):
    nome=str(input("Inserisci nome albergo: "))
    cat=int(input("Inserisci la categoria: "))
    pd=int(input("Inserisci i posti disponibili: "))
    pp=int(input("Inserisci i posti da prenotare: "))
    
    pm=(pd-pp)*-1
    #condizione
    if  pd>pp:
        pr=pd-pp
        print(f"\nLa prenotazione può essere effettuata nell'hotel {nome} e rimangono ancora {pr} posti")
    
    else:
        print(f"\nLa prenotazione non può essere effettuata perchè mancano {pm} posti.")