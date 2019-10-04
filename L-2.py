#L-2 Utilizando ciclos (loops), “dibujar” el siguiente triángulo:
def piramide(n):
    for i in range (n):
            print (' '*(n-i-1) + '*'*(2*i+1))


n=5
piramide(n)