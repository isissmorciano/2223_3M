#Esercizio numero 3
# dato il giornaliero di un ombrellone di 12 euro, 
# lettini di 5 euro e sedie a sdraio di 6.50 euro, 
# elaborare un algoritmo che chiede all'utente di inserire il numero di giorni 
# ed i servizi che vuole prenotare e calcola la spesa complessiva
#Inizio
#Inserimento lettini,strai,ombrelloni e giorni
n_giorni=int(input("Inserisci giorni: "))
n_lettini=int(input("Inserisci lettini: "))
n_sdrai=int(input("Inserisci sdrai: "))
n_ombrelloni=int(input("Inserisci ombrelloni: "))
#Calcolo del prezzo individuale lettini,ombrelloni e strai
n_lettini=5*n_lettini
n_ombrelloni=12*n_ombrelloni
n_sdrai=6.5*n_sdrai
#Calcolo del prezzo totale
prezzo_totale=(n_ombrelloni+n_sdrai+n_lettini)*n_giorni
print("Il prezzo totale è: ",prezzo_totale)
#Fine
