#A-2
#Crear un programa que indique qué números de una lista son divisibles por un número dado. El orden en el resultado no importa.

def divisiblesPor(lista,n):
    lista_nueva=[]
    for i in range (len(lista)):
        if(lista[i]%n==0):
            lista_nueva.append(lista[i])
    print(lista_nueva)
return lista_nueva

divisiblesPor([1, 2, 3, 4, 5, 6], 2) #[2,4,6]
divisiblesPor([9, 12, 3, 0, 1, 4], 3) #[9, 12, 3]
divisiblesPor([10, 11, 3], 1) # [10, 11, 3]