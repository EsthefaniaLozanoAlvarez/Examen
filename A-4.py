# A-4
# En una lista de calificaciones, determinar el porcentaje de alumnos que aprobaron el curso. Se considera una calificación aprobatoria si es igual o mayor a 6.

def promed(arr):
    suma = 0
    for x in range(0,len(arr)):
        suma += arr[x]
    promedio = suma / len(arr)
    return promedio
def aprobados(alumnos):
    aproba = 0
    for i in range (0,len(alumnos)):
        if promed(alumnos[i]) >= 6:
            aproba += 1
    resultado = aproba / len(alumnos)
    return resultado * 100


prueba10 = [[9,8,7,5,2],[5,5,5,5,5,5],[0,1,2],[4,2,4,5,7,8],[1,1,1,1]] #20
print(aprobados(prueba10),"%")


