# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import numpy as np


print('Vamos a ingresar el orden de la matriz a calcular ')
print ('Ingresa primeo el numero de filas ')
filasA = int(input())
print('Ingresa ahora el numero de columnas')
columnasA = int(input())
contador = 0

if columnasA == filasA:

    # Creando la matriz sin elementos
    matrizA = []
    for i in range(filasA):
        matrizA.append([0] * columnasA)

    # Rellenando la matriz
    print('Ingrese la matriz A')
    for fila in range(filasA):
        for columna in range(columnasA):
            matrizA[fila][columna] = float(
                input(f'Ingrese la posición número {fila}, {columna}:  '))
    print('La matriz introducida es', matrizA)
    MatrizAt = np.transpose(matrizA)
    print('Y tiene matrix transpuesta ', MatrizAt )
 # Calculamos si una matriz es simétrica o no lo es verificando entrada a entrada en la matriz
    for fila in range(filasA):
        for columna in range(columnasA):
            normal = matrizA[fila][columna]
            transpuesta = matrizA[columna][fila]
            if normal == transpuesta:
                contador += 1


    if contador == (filasA * columnasA):
        print('Por tanto, la matriz es simétrica')
    else:
        print('Matriz adjunta no coincide con la matriz dada, por tanto se concluye que la matriz NO es simétrica')
    print('La matriz tiene determinante ', np.linalg.det(matrizA))
    #np.linalg usa el modulo de algebra lineal de numpy, det es para determinate, inv para calculo de inversas
    if np.linalg.det(matrizA) != 0:
        print('los decimales que aparecen son un redondeo de las operaciones en bytes, la matriz es invertible, '
              'y tiene inversa dada por')
        print(np.linalg.inv(matrizA))
    else:
        print('la matriz introducida tiene determinante cero y por ende no es invertible')
else:
    print('Debido a que la matriz no es cuadrada, se concluye que No es simétrica y no se puede calcular el determinante')
print('los valores propios de la matriz son:')
# np.linalg usa el modulo de algebra lineal de numpy, eigenvals es para valores propios en general
print(np.linalg.eigvals(matrizA))



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
