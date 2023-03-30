#-consegna Presi  ento è in contanti il prezzo va diminuito del 10%, se è rateale va diminuito del 15%. Un parcheggio ha tariffa 2 euro per la prima ora di sosta e 1 euro per ogni ora successiva. 
#-Conoscendo l'orario di entrata e di uscita di un'autovettura(espresso in ore e minuti), emetti uno scontrino con l'ora di entrata, l'ora di uscita, il tempo di durata della sosta e la relativa spesa.
#-(suggerimento: trasforma dapprima gli orari di entrata e di uscita in minuti).


#menu

print("--------------------------------------------------------------------------")
print("-                 SCEGLIERE TRA LE 2 OPZIONI PER PAGARE LA MERCE         -")
print("-                                                                        -")  
print("-      1)contanti                                              2)rate    -")   
print("--------------------------------------------------------------------------")

#scelta opzioni

opzioni=int(input("Quale vuoi fare delle 2e opzioni?(1)(2)"))

#condizioni

if opzioni== 1:

 codice = int(input("inserire codice merce:"))
 qta = int(input("inserire la quantita:"))
 descrizione = input("inserire la descrizione del prodotto:")
 prezzo=float(input("inserire il prezzo del prodotto: "))
 totale=qta*prezzo
 sconto=totale-(totale*10/100)
 print("******************************************************")
 print("descrizione del prodotto : ",descrizione)
 print("codice prodotto : ",codice)
 print("pezzi presi : ",qta)
 print("il prezzo finale è : ",sconto)

 #inizio ciclo 2
if opzioni== 2:
 codice = int(input("inserire codice merce:"))
 qta = int(input("inserire la quantita:"))
 descrizione = input("inserire una descrizione del prodotto:")
 prezzo=float(input("inserire il prezzo del prodotto: "))
 totale = qta * prezzo
 sconto=totale+(totale*15/100) 
 print("*****************************************************")
 print("descrizione del prodotto: ",descrizione)   
 print("Codice prodotto: ",codice)
 print("La quantità presa è: ",qta)
 print("Il prezzo finale è: ",sconto)







    