#Mostro i punti dei vari titoli di studio
print('''
╔══════════════╗
‖elementare = 1‖
‖media = 2     ‖
‖superiore = 4 ‖
‖laurea = 7    ‖
‖ntitolo = 0   ‖
╚══════════════╝''')
#Chiedo il titolo di studio 
tt = input('\nInserisci titolo di studio: ')
#Verifico quale titolo di studio è
match(tt):
	case 'elementare':
		a = 'elementare'
		b = 1
	case 'media':
		a = 'media'
		b = 2 + 1
	case 'superiore':
		a = 'superiore'
		b = 4 + 2 + 1
	case 'laurea':
		a = 'laurea'
		b = 7 + 4 + 2 + 1
	case 'ntitolo':
		a = 'nessun titolo'
		b = 0
#Scrivo il titolo di studio e il punteggio finale
print('\nTitolo di studio:',a)
print('Punteggio finale:',b) 
