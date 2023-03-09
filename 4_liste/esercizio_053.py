#creare una nuova lista che contiene solo i cognomi piu lunghi di 8 caratteri che contengono la lettera E, stampare i cognomi ordinati dalla Z alla A, creare una copia della lista cognomi lunghi con la E, creare una nuova lista che contiene solo i cognomi che contengono la lettera C, unire le due liste 'cognomi lunghi con la E' e 'cognomi che contengono la lettera C
thislist=["amati", "baffert", "chiarabinie","Ciaramidoroe","Cornacchia","D'elia","Bianco","Franci",]
lista2=[]
x=0
#1
for i in thislist:
    x=x+1
    print(x,i)

#2. 
for i in thislist:
  if "e" in i and len(i)>=8 :
    lista2.append(i)
print(lista2)

#3. 


for i in thislist:
    print(i)

#4.
for i in thislist:
   if "e" in i and len(i)>=8 :
       lista2.append(i)
cognomi = lista2.copy()
print(cognomi)



#5. 
list_c =[]
for i in thislist:
    if "c" in i  :
        list_c.append(i)
        print(i)
#6.

list3 = list_c+lista2 
print(list3)