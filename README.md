# 2223_3M

formato dei file degli esercizi: **esercizio_056.py**

## Input/Output: print() e input()

1. Dato un importo, calcolare lo sconto del 5% e applicare un'IVA dell'8%.
2. Dato un nominativo di un alunno e 3 voti di una materia, visualizzare la media dei voti.
3. Dato il giornaliero di un ombrellone di 12 euro, lettini di 5 euro e sedie a sdraio di 6.50 euro, elaborare un algoritmo che chiede all'utente di inserire il numero di giorni ed i servizi che vuole prenotare e calcola la spesa complessiva.
4. Un cinema sta facendo la seguente promozione: adulto 10 euro, minorenne 6 euro. Il cinema lavora solo con gruppi su prenotazione, calcolare la spesa complessiva dato il numero di persone nel gruppo.
5. Scrivi un algoritmo che determini la circonferenza e l’area di un  cerchio conoscendo il raggio.
6. Calcola il tempo trascorso tra due date espresse in giorni, mesi e anni (es: 12/06/2020). Consideriamo i mesi di 30 giorni.
7. Letto in input il valore di X calcola il valore dell’espressione aX^2 + bX sapendo che A vale 10 e B vale 15.
8. Dato in input il nominativo e l’età di uno studente, visualizzare a video la posizione del registro, il nominativo, il nome della scuola e la data odierna.
9. Crea un programma che permetta di calcolare e visualizzare la spesa necessaria per pavimentare una stanza di dimensione 7\*4 avendo in input: il costo delle piastrelle al metro quadrato, il costo orario della manodopera e il numero di ore impiegate. Al costo finale aggiungi l’X% di IVA.
10. Un cliente ha deciso di costruire una piccola casetta per gli attrezzi da giardino. Hai bisogno di L assi larghe per il tetto, P assi di legno piccole per le pareti e Q riquadri di legno per il pavimento. Realizza un programma che dopo avere preso in input L,P,Q e il loro prezzo unitario (senza IVA), calcoli e visualizzi la spesa da sostenere, sapendo che il venditore ha uno sconto del 10% ma chiede 30 euro per la consegna.
11. Data un'equazione di 2° grado che abbia come soluzione “due numeri reali distinti” (Delta>0), calcoli tali valori, il fuoco e il vertice. Visualizzare oltre ai valori sopracitati anche il valore del delta.
12. Dato un importo, applicare lo sconto del 5% e considerare l'IVA al 12%.
13. Un giocatore di D&D vuole visualizzare le sei statische del suo personaggio, dati i sei valori compresi tra 3-18, visualizzarli in ordine con accanto l'etichetta che lo descriva: Str, Int, Sag, Dex, Cos, Cha.
14. Data una sequenza di 8 bit, dare il corrispendente valore decimale. (Dati 8 varibili, da b0 a b7).

## Scelta Condizionata: if e switch

15. Determina se un numero è positivo/negativo.
16. Sul prezzo di un prodotto viene praticato lo sconto del X% se si acquistano fino a 10 pezzi e dell'Y% se si acquistano più di 10 pezzi. Presi in input il pezzo di un prodotto e il numero di pezzi da acquistare, stampa la spesa da sostenere.
17. Verifica se un carattere digitato da tastiera corrisponde a: "S" o "s" visualizzare il messaggio "Si", "N" o "n" visualizzare il messaggio "No", un altro carattere visualizzare il massaggio "Errato".
18. Presi in input i dati relativi all'acquisto di una merce (codice merce, quantità, descrizione, prezzo unitario, tipo di pagamento(se contanti o rateale)), calcola e stampa l'importo totale delle merce, sapendo che se il pagamento è in contanti il prezzo va diminuito del 10%, se è rateale va diminuito del 15%.
Un parcheggio ha tariffa 2 euro per la prima ora di sosta e 1 euro per ogni ora successiva. Conoscendo l'orario di entrata e di uscita di un'autovettura(espresso in ore e minuti), emetti uno scontrino con l'ora di entrata, l'ora di uscita, il tempo di durata della sosta e la relativa spesa. (suggerimento: trasforma dapprima gli orari di entrata e di uscita in minuti). 
19. Determina se un anno fornito in input è bisestile. Un anno è bisestile se è divisibile per 4, gli anni secolari non sono bisestili se non sono divisibili per 4.
20. Converti il giorno della settimana da numerico a stringa. (es. 1 --> Monday, 2 --> Tuesday) 
21. Crea un programma che verifichi se la data inserita è corretta (attenzione: i mesi sono 12, non in tutti i mesi ci sono 31 giorni, alcuni anni sono bisestili)
22. Il programma legge tre lunghezze dei lati di un triangolo e dice se il triangolo è scaleno, isoscele o equilatero. 
23. Scrivere un programma che legga il nominativo di uno studente e un voto, e dica se è insufficiente o sufficiente, e se è insufficiente distingua tra gravemente insufficiente (minore o uguale a 4) o insufficiente (compreso tra 4 (escluso) e 6 (escluso)). Si visualizzi il nominativo e il giudizio, non il valore del voto.
24. In un concorso a punteggio conseguito nelle prove scritte vanno aggiunti i punti relativi ai titli di studio secondo il seguente schema: elementare 1 punto, media 2 punti, superiore 4 punti, laurea 7 punti, nessun titolo 0 punti. Calcola il punteggio finale conoscendo il punteggio iniziale e il titolo di studio.
25. In una copisteria, il costo unitario delle fotocopie varia a seconda del numero da effetture secondo la seguente tabella: n.1-19 0,10 euro, n.20-100 0,08 euro, piu di 100 0,05 euro. Inoltre se le fotocopie sono da rilegare viene aggiunto un costo di 1,80 euro. Dati in input il numero di fotocopie da effetturare, il nome del cliente e un indicazione che segnali se il plico è da rilegare, calcola il costo totale e stampa il seguente prospetto: 
 Gentile Sig. ___
 il suo preventivo è di ___ euro
 compresa la rilegatura.
 L'ultima riga è da scrivere solo se è richiesta la rilegatura.
26. Uno studente ha effettuato 4 prove ottenendo voti compresi tra 1 e 10. Scrivi un programma che calcoli la media dei voti e stampi il seguente prospetto:
STUDENTE_____
MEDIA____
RISULTA____
Stampa la scritta "sufficiente" se la media è >6, "insufficiente" altrimenti.
27. Scrivi un programma che, tramite menu, permetta di calcolare il quadrato, il cubo e la radice quadrata di un numero fornito in Input. Prevedi opportuni messaggi di errore se la scelta è errata e se viene richiesta la radice quadrata di un numero negativo.
28. Scrivi un programma che, tramite menu, permetta di calcolare l'area e il perimetro di un triangolo, distinguendo i casi di triangolo rettangolo, isoscele, equilatero e generico.
29. Un campeggio vuole calcolare il costo degli affitti dei suoi bungalow. Scrivi un programma che effettui il calcolo dell'affitto di un bungalow (massimo per 2 settimane) tenendo presenti le seguenti tariffe: quota fissa 100 euro, una settimana 600 euro, due settimane 1100 euro e eventuale supplemento lenzuola 20 euro a settimana
30. Generare una lettera casuale tra A ed E e convertirla in un voto numerico
A-B = 3
C = 2
D-E = 1
31. Scrivere 10 volte la parola "ciao", sommare i numeri da 10 a 20 (compresi gli estremi), sommare i numeri pari fino a 30 (30 incluso) e moltiplicare i numeri da 1 a 10
32. Scrivi un programma che calcoli il valore della circonferenza e quello dell'area di tutti i cerchi con raggio compreso tra 1 e 20.
33. Dati N numeri interi positivi e negativi trova la somma dei valori assoluti.
34. In un quiz vengono poste N domande(facili e difficili). Se il concorrente risponde correttamente a una domanda facile ottiene 2 punti, altrimenti ne perde 4, per le domande difficili ottieme 4 punti se la risposta è giusta, ne perde 2 se è sbagliata. Calcola il punteggio complessivo.
35. Dato N inserito dall'utente: stampare il massimo numero inserito, stampare il minimo numero inserito, stampare la media dei numeri inseriti, stampare la media di solo i numeri positivi inseriti. 
36. Determina il prodotto di due numeriinteri utilizzando solamente l'operazione di addizione.
## Cicli-loop 
37. Siano dati in input il codice fiscale, il reddito e il nome di una serie di contribuenti, stampa il nomi e i codici fiscali dei contribuenti con reddito superiore a 30.000 euro.
38. Dati in input i risultati relativi a N seggi elettorali, per ogni seggio hai le seguenti informazioni : numero iscritti, numero votanti, numero di schede nulle, numero di schede bianche. Scrivi un programma che stampi il seguente prospetto: percentuale votanti su tutti i seggi, percentuale schede bianche, percentuale schede nulle.
39. Scrivi un programma che presi in input l'anno corrente e i dati relativi a N dipendenti di un'azienda con nome e anno di nascita, stampi il numero di dipendenti di età pensionabile(età>=65) e il numero di dipendenti minorenni(età<18).
40. Di N persone sono forniti il peso e l'altezza. Calcola per ciascuna l'indice di obesità(peso/altezza). Conta a mano a mano il numero di quelle che hanno indice di obesità maggiore di un valore K prefissato.
41. Crea un programma che esegua le seguenti istruzioni: 1) lasciare una moneta fino a che non esce testa, 2) lanciare una moneta fino a che non esce testa 2 volte di fila, 3) lanciare due dadi fino a che non esce lo stesso numero in entrambi, 4) stampare i valori usciti ad ogni lancio solo se la somma dei valori e' maggiore di 5, 5)terminare forzatamente l'esecuzione se la somma dei valori e' 11.
42. Siano dati in input i dati relativi a una serie di alberghi di una determinta località. Per ogni albergo hai in input: nome albergo, categoria, numero posti disponibili. Supponendo di  avere in input un numero intero indicante il numero di posti da prenotare, stampa uno dei seguenti messaggi: La prenotazione può essere effettuata nell'hotel... e rimangono disponibili ancora... posti. Oppure La prenotazione non può essere effetuata perche mancano.... posti. A seconda che il numero di posti da prenotare sia minore o uguale al numero di posti disponibili oppure se i posti da prenotare sono più dei posti disponibili.
43. Scrivi un programma che,presi in input i dati relativi a una serie di prodotti con: codice, descrizione, prezzo. Stampi il codice e la descrizione relativi al prodotto più costoso.
44. Di N città si conoscono il numero di abitanti e il numero di quelli attivi. Calcola per ciascuna città l'indice di attività (attivi/abitanti * 100) e stampa il nome della città con l'indice più basso e di quella con l'indice più alto.
45. Crea un programma che utilizzi un ciclo nidificato per visualizzare un albero di natale con caratteri a scelta.
46. Crea un programma che utilizzi un ciclo nidificato per visualizzare una superficie colllinare.





