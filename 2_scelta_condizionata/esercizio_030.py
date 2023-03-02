
import random

numero=int(random.randint(1, 5))
match numero:
    case 1:
        print("le lettera è la A→ numero 3.")
    case 2:
        print("le lettera è la B→ numero 3.")    
    case 3:
        print("la lettera è la C→ numero 2.")
    case 4:
        print("la lettera è la D→ numero 1.")
    case 5  :
        print("la lettera è la E→ numero 1.")