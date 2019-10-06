# FN-5
# Un número será “líder” si es mayor al promedio del resto en una lista. Crear una función que dado un arreglo de al menos 
# 3 números enteros (mayores o iguales a 0), regrese el número líder.

def promedio(valores,pos):
    resultado = 0.0
    for x in range(0,len(valores)):
        if x != pos:
            resultado = resultado + valores[x]
    regresa=resultado/(len(valores)-1)      
    return regresa

def sacaLider(listas):
    anterior=-1
    resultado=[]
    for i in range(0,len(listas)):
        if listas[i] > promedio(listas,i):
            resultado.append(listas[i])
            anterior=listas[i]
    if anterior >= 0:
        return resultado
    else:
        print("No hay lider")


a = [3,2,10,1]#10
b=[5,0,1,2]#5
c=[1,1,4,1]#4

#print(promedio(lider,0))
print(sacaLider(a))
print(sacaLider(b))
print(sacaLider(c))
