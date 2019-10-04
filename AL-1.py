#AL-1
#Dentro del rango [2, 100] de números naturales, indicar cuáles son primos y cuáles no.
lista_primos=[]
lista_noprimos=[]
lista=[]
for i in range (2,101):
    lista.append(i)
print(lista)
for j in range (2,101):
    if((j%2!=0 or j==2) and (j%3!=0 or j==3) and (j%5!=0 or j==5) and (j%7!=0 or j==7) and (j%11!=0 or j==11)):
        lista_primos.append(j)
    else:
        lista_noprimos.append(j)
print("Los primos son: "+str(lista_primos))
print("Los no primos son: "+str(lista_noprimos))
