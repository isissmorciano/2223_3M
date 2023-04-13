filename = 'es1.txt'
with open(filename) as file:
    for line in file:
        voto = line.rstrip()
        print(f'voto: {voto}')

