#Inizio

#Spiegazione del programma e richiesta del carattere

carattere = str(input("Inserire un carattere tra ''S''  o  ''s'' oppure ''N''  o  ''n'' : "))
carattere = carattere.upper()
carattere.lower() == carattere.upper()

print("Se hai inserito  la lettera ESSE verrà comunicato il messaggio ''Sì'' , se invece hai inserito la lettera ENNE verrà comunicato il messaggio ''No'' .")
print("Se il carattere inserito non è tra questi, verrà comunicato un errore.")

#Comunicazione all'utente del messaggio Sì oppure No

if carattere == "S":
	print("Sì")

elif carattere == "N":
	print("No")

else:
	print("Errato, carattere non compreso tra ''S'', ''s'', ''N'', ''n'' .")
#Fine