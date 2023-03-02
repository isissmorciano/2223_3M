print("*************************************************************************************")
print("|  Il programma ti dice se i dipendenti di una azienda sono minorenni o pensionabili|")
print("*************************************************************************************")
somma=0
sommamin=0


anno=int(input("Che hanno è?: "))
dipen=int(input("Quanti dipendenti ci sono?: "))
for i in range(dipen):
    nome=str(input("Inserisci il nome: "))
    annonascita=int(input("Inserisci anno di nascita: "))
    if anno-annonascita>=65:
        print("Dipendente pensionabile")
        somma=somma+1  
    elif anno-annonascita<=18:
        print("Dipendente minorenne")
        sommamin=sommamin+1
print("I dipendenti pensionabili sono: ", somma)
print("I dipendenti minorenni sono: ", sommamin)