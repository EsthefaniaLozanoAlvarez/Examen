# FN-3
#Crear una función que remueva los elementos repetidos en un arreglo y regrese un nuevo arreglo con los elementos restantes.
def repetidos(lista_original):
    lista_nueva = []
    conta=0
    for j in range (len(lista_original)):
        conta=0
        for i in range (0,len(lista_original)):
            if( lista_original[j]==lista_original[i]):
                conta=conta+1 
        if(conta==1):   
            lista_nueva.append(lista_original[j])
    print(lista_nueva)
    return lista_nueva

repetidos([9,3,1,3,2,9]) #[1,2]
repetidos([6, 2, 2, 2, 1, 8]) #[6,1,8]
repetidos([1]) #[1]