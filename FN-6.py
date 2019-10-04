# FN-6
# Escribir una función que sume las diferencias entre números consecutivos en un arreglo. Los números en el arreglo se encuentran ordenados descendentemente.

def sumDif(arr):
    for i in range (len(arr)):
        diferencia=arr[0]
        diferencia=diferencia-arr[i]
    print(diferencia)


sumDif([10, 2, 1]) #(10 - 2) + (2 - 1) = 9
sumDif([11, 10, 5]) #(11 - 10) + (10 - 5) = 6
sumDif([4, 3, 2, 1]) #(4 - 3) + (3 - 2) + (2 - 1)= 3
