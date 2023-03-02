#Livelli albero di natale=15
print("****************************************************")
print("| Il programma crea un albero di natale di 15 lvl  |")
print("****************************************************")
n = 15
for i in range(1, n+1):
    print(" "*(n-i) + "*"*(2*i-1))