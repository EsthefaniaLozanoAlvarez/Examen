#L-1
# Utilizando ciclos (loops), “dibujar” el siguiente triángulo de 10 renglones de alto únicamente con números nones.:
cadena=""
num=1
n=22
for i in range (1,n):
    for j in range (1,i):
        if(num%2!=0 and num < n):
            cadena+=str(num)
            print(cadena)
        num=num+1


