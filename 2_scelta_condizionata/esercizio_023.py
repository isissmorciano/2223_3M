print("**********************************")
print("| inserire il nominativo e il voto (1-10) e iò programma dice se è \n sufficemte imsufficente e gravemente insufficente")
print("**********************************")
nominativo=str(input("inserire nome e cognome dello studente \n con le iniziali maiuscole: "))
voto=int(input("inserisci il voto: "))
if voto >= 6:
    print("il voto è sufficente")
elif voto > 4 and voto < 6:
    print("il voto è insufficente")
else:
    print("il voto è gravemente insufficente")
