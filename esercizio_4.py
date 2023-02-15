#Esercizio 4
#Un cinema sta facendo la seguente promozione: 
#adulto 10 euro, minorenne 6 euro, il cinema lavora sono con gruppi su prenotazione, 
#calcolare la spesa complessiva dato il numero di persone nel gruppo

#Scritta a schermo dei prezzi
print ("Un cinema stà facendo la seguente promozione: intero adulto 10 euro, minorenni  6 euro,  e anziani 5 euro. Il cinema lavora solo per gruppi/comitive su prenotazione.")

#Inserimento del numero di minorenni, maggiorenni, anziani
minor = int(input("Inserisci il numero di minorenni "))
adult = int(input("Inserisci il numero di maggiorenni "))
elder = int(input("Inserisci il numero di anziani "))

#Calcolo del prezzo
prezzoTotale = (minor * 6 + adult * 10 + elder * 5)
#Lettura a schermo del prezzo totale
print ("Il prezzo totale e'", prezzoTotale, "euro") 
