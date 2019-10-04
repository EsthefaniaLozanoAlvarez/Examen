#L-1
# Utilizando ciclos (loops), “dibujar” el siguiente triángulo de 10 renglones de alto únicamente con números nones.:
cadena=""
num=1
for i in range (1,22):
    for j in range (1,i):
        if(num%2!=0 and num < 22):
            cadena+=str(num)
            print(cadena)
        num=num+1


