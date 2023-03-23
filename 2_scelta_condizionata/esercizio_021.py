# Programma che, inserita in input una data in forma numerica, controlla se essa è valida

giorno = int(input("Inserisci il giorno: "))
mese = int(input("Inserisci il mese: "))
anno = int(input("Inserisci l'anno (<= 3000): "))
print('\n')

# Verifica se l'anno è bisestile
if anno % 4 == 0:
    bisestile = True
    print("L'anno è bisestile")
    print(f'')
else:
    bisestile = False

# Verifica se il mese è valido
max_giorni = 0
if mese == 1 or mese == 3 or mese == 5 or mese == 7 or mese == 8 or mese == 10 or mese == 12:
    max_giorni = 31
elif mese == 4 or mese == 6 or mese == 9 or mese == 11:
    max_giorni = 30
elif mese == 2:
    if bisestile:
        max_giorni = 29
    else:
        max_giorni = 28
else:
    print("ERRORE: Il mese deve essere compreso tra 1 e 12")

# Verifica se il giorno è valido
if giorno < 1 or giorno > max_giorni:
    print(f"ERRORE: Il giorno deve essere compreso tra 1 e {max_giorni}")
else:
    print("Hai inserito una data valida!")
    