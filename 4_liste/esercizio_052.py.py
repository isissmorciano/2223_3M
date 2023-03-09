#Pelusi Matteo

#elenco in ordine alfabetico
thislist = ["Amati","Andruccioli","Arcolin","Baffert","Chiarabini","Ciaramidaro","Cornacchia","Delbianco","Delia","Franci","Gibertini","Lupascu","Maccione","Massa","Pelusi","Savioli","Sejdi","Serra","Shkafi","Tamburini","Tonelli","Trebbi"]

#aggiunta di un cognome alla fine
thislist.append("Uva")

#eliminazione del primo cognome
del thislist[0]

#aggiunta pippo nell'elenco
thislist.insert(14,"Pippo")

#Modifica da pippo a pluto
thislist[14]="Pluto"

#scrittura a schermo
print(thislist)
print(thislist[3])