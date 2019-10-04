#A-3
#Dado un arreglo de números enteros, indicar el conteo de números positivos y la suma de los números negativos. El número 0 (cero) no cuenta.

def posYneg(arr):
    positivos=0
    negativos=0
    for i in range (len(arr)):
        if(arr[i]>0):
            positivos=positivos+1
        else:
            negativos=negativos+arr[i]
    print("El número de los positivos es: "+ str(positivos))
    print("La suma de los negativos es: "+ str(negativos))


posYneg([9,-8,2,1,-2]) #3 positivos, -10 negativos
