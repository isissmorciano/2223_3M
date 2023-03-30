#esercizio 25

#In una copisteria, il costo unitario delle fotocopie varia a seconda del numero da effetture secondo la seguente tabella: 
#n.1-19 0,10 euro, n.20-100 0,08 euro, piu di 100 0,05 euro. Inoltre se le fotocopie sono da rilegare viene aggiunto un costo di 1,80 euro. 
#Dati in input il numero di fotocopie da effetturare, il nome del cliente e un indicazione che segnali se il plico è da rilegare, calcola il costo totale e stampa il seguente prospetto:
#Gentile Sig. ___ il suo preventivo è di ___ euro compresa la rilegatura. L'ultima riga è da scrivere solo se è richiesta la rilegatura.

#dichiarazioni delle variabili
numero=int(input("Inserisci il numero di fotocopie che vuoi: "))
nome=str(input("Inserisca il suo nome: "))
#condizioni
if numero>0 and numero<20:
	prezzo=numero*0,10
	print(f"Il costo per {numero} di fotocopie' e' di : " ,prezzo,"euro")
if numero>19 and numero<101:
	prezzo=(numero*0.08)
	print(f"Il costo per {numero} di fotocopie' e' di : " ,prezzo,"euro")
if	numero>100:
	prezzo=(numero*0.05)
	print(f"Il costo per {numero} di fotocopie' e' di : " ,prezzo,"euro")
#richiesta della rilegatura
rilegatura=str(input("Vuoi la rilegatura(S/N)?"))
if rilegatura=='S':
	prezzo=(prezzo+1.8)
	print("Gentile signore: ",nome)
	print("Il suo preventivo con rilegatura è:  ",prezzo,"euro")
if rilegatura=='N':
	print("Gentile signor",nome)
	print("Il suo preventivo è di:", prezzo,"euro")
