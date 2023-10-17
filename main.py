import math
import argparse

# Función para leer la matriz desde un archivo
def leer_matriz_desde_archivo(nombre_archivo):
    matriz = []

    # Abrir el archivo en modo lectura
    with open(nombre_archivo, 'r') as archivo:
        lineas = archivo.readlines()

        # Leer la calificación mínima y máxima de las primeras dos líneas
        calificacion_minima = float(lineas[0].strip())
        calificacion_maxima = float(lineas[1].strip())

        # Leer el resto de las líneas y construir la matriz
        for linea in lineas[2:]:
            valores = linea.strip().split()
            fila = []

            for x in valores:
                if x != "-":
                    aux = float(x)
                    if aux < calificacion_minima or aux > calificacion_maxima:
                        raise ValueError(f"Error: El valor {aux} no está dentro del rango permitido ({calificacion_minima} - {calificacion_maxima})")
                fila.append(x)  # Guarde el valor tal como está en la matriz

            matriz.append(fila)

    return calificacion_minima, calificacion_maxima, matriz


def quitar_guiones(array1, array2):
    # Crear nuevas listas sin guiones y valores correspondientes en ambos arrays
    valores_array1 = []
    valores_array2 = []

    for val1, val2 in zip(array1, array2):
        if val1 != '-' and val2 != '-':
            valores_array1.append(float(val1))
            valores_array2.append(float(val2))
    return valores_array1, valores_array2


def calcular_coeficiente_de_correlacion(array1, array2):
    try:
        valores_array1, valores_array2 = quitar_guiones(array1, array2)

        media_cal_a1 = sum(valores_array1) / len(valores_array1)
        media_cal_a2 = sum(valores_array2) / len(valores_array2)

        num = 0.0
        for val1, val2 in zip(valores_array1, valores_array2):
            num += ((val1 - media_cal_a1) * (val2 - media_cal_a2))

        denom1 = 0.0
        for val1 in valores_array1:
            resta = val1 - media_cal_a1
            denom1 = denom1 + pow(resta, 2)
        denom2 = 0.0
        for val2 in valores_array2:
            resta = val2 - media_cal_a2
            denom2 = denom2 + pow(resta, 2)
        denom = math.sqrt(denom1) * math.sqrt(denom2)
        coefiente_pearson = num / denom
        return coefiente_pearson
    
    except Exception as e:
        raise ValueError("Valores insuficientes en la matriz para realizar la predicción error code:001") from e

def calcular_similitud_distancia_euclídea(array1, array2):
    try:
        valores_array1, valores_array2 = quitar_guiones(array1, array2)

        suma = 0.0
        for val1, val2 in zip(valores_array1, valores_array2):
            suma += pow((val1 - val2), 2)
        distancia_euclidea = math.sqrt(suma)
        return distancia_euclidea
    except Exception as e:
        raise ValueError("Valores insuficientes en la matriz para realizar la predicción error code:003") from e

def calcular_similitud_coseno(array1, array2):
    try:
        valores_array1, valores_array2 = quitar_guiones(array1, array2)

        numerador = 0.0
        for val1, val2 in zip(valores_array1, valores_array2):
            numerador += (val1 * val2)

        denominador1 = 0.0
        for val1 in valores_array1:
            denominador1 += pow(val1, 2)
        denominador1 = math.sqrt(denominador1)

        denominador2 = 0.0
        for val2 in valores_array2:
            denominador2 += pow(val2, 2)
        denominador2 = math.sqrt(denominador2)

        denominador = denominador1 * denominador2
        similitud_coseno = numerador / denominador
        return similitud_coseno
    except Exception as e:
        raise ValueError("Valores insuficientes en la matriz para realizar la predicción error code:002") from e

def calcular_prediccion_simple(matriz, cantidad_vecinos, posicion, tipo_similitud):
    try:
        lista_tuplas = []
        if tipo_similitud == 1:
            for i in range(len(matriz)):
                if matriz[i][posicion[1]] != '-':
                    lista_tuplas.append(
                        (calcular_coeficiente_de_correlacion(matriz[posicion[0]], matriz[i]), i))

        elif tipo_similitud == 2:

            for i in range(len(matriz)):
                if matriz[i][posicion[1]] != '-':
                    lista_tuplas.append(
                        (calcular_similitud_coseno(matriz[posicion[0]], matriz[i]), i))

        elif tipo_similitud == 3:

            for i in range(len(matriz)):
                if matriz[i][posicion[1]] != '-':
                    lista_tuplas.append(
                        (calcular_similitud_distancia_euclídea(matriz[posicion[0]], matriz[i]), i))

        # Ordenar la lista de tuplas por similitud
        lista_tuplas.sort(reverse=True)

        # Tomar los primeros k vecinos
        lista_tuplas = lista_tuplas[:cantidad_vecinos]

        # Calcular la calificación predicha
        numerador = 0.0
        denominador = 0.0
        for tupla in lista_tuplas:
            numerador += tupla[0] * float(matriz[tupla[1]][posicion[1]])
            denominador += abs(tupla[0])

        prediccion = numerador / denominador
        return prediccion

    except Exception as e:
        raise ValueError("Valores insuficientes en la matriz para realizar la predicción") from e

def calcular_prediccion_diferencia_media(matriz, cantidad_vecinos, posicion, tipo_similitud):

    lista_tuplas = []
    if tipo_similitud == 1:
        for i in range(len(matriz)):
            if matriz[i][posicion[1]] != '-':
                lista_tuplas.append(
                    (calcular_coeficiente_de_correlacion(matriz[posicion[0]], matriz[i]), i))

    elif tipo_similitud == 2:

        for i in range(len(matriz)):
            if matriz[i][posicion[1]] != '-':
                lista_tuplas.append(
                    (calcular_similitud_coseno(matriz[posicion[0]], matriz[i]), i))

    elif tipo_similitud == 3:

        for i in range(len(matriz)):
            if matriz[i][posicion[1]] != '-':
                lista_tuplas.append(
                    (calcular_similitud_distancia_euclídea(matriz[posicion[0]], matriz[i]), i))

    # Ordenar la lista de tuplas por similitud
    lista_tuplas.sort(reverse=True)

    # Tomar los primeros k vecinos
    lista_tuplas = lista_tuplas[:cantidad_vecinos]

    # Calcular la calificación predicha

    numerador = 0.0
    denominador = 0.0
    for tupla in lista_tuplas:
        numerador += tupla[0] * (float(matriz[tupla[1]][posicion[1]]) -
                                 calcular_media_usuario(matriz[tupla[1]]))
        denominador += abs(tupla[0])
    prediccion = calcular_media_usuario(
        matriz[posicion[0]]) + (numerador / denominador)
    return prediccion

def normalizar_matriz(matriz, minima, maxima):
    print ("minima: ", minima)
    print ("maxima: ", maxima)

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] != '-':
                valor = float(matriz[i][j])
                matriz[i][j] = str((valor - minima) / (maxima - minima))

    return matriz

def desnormalizar_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] != '-':
                valor = float(matriz[i][j])
                matriz[i][j] = str((valor * (calificacion_maxima - calificacion_minima)) + calificacion_minima)

    return matriz

def calcular_media_usuario(array):
    valores_array = []
    for val in array:
        if val != '-':
            valores_array.append(float(val))
    media = sum(valores_array) / len(valores_array)
    return media

def imprimir_matriz(matriz):
    for fila in matriz:
        print(' '.join(map(str, fila)))

# Crear un objeto ArgumentParser
parser = argparse.ArgumentParser(
    description='Procesar archivos de entrada y salida.')

# Agregar argumentos de línea de comandos
parser.add_argument('-i', '--input', type=str, required=True,
                    help='Nombre del archivo de entrada')
parser.add_argument('-o', '--output', type=str, required=True,
                    help='Nombre del archivo de salida')
parser.add_argument('-m', '--metrica', type=int, choices=[1, 2, 3], required=True,
                    help='Métrica de similitud (1 -> coeficiente de correlación de Pearson, 2 -> similitud del coseno, 3 -> distancia euclídea)')
parser.add_argument('-v', '--neighbour', type=int,
                    required=True, help='Cantidad de vecinos (entero)')
parser.add_argument('-t', '--type', type=int, choices=[1, 2], required=True,
                    help='Tipo de prediccion (1 -> prediccion simple o 2 -> diferencia con la media)')

# Analizar los argumentos
args = parser.parse_args()

# Acceder a los nombres de archivo proporcionados
nombre_archivo_entrada = args.input
nombre_archivo_salida = args.output

# Acceder a los vecinos y el tipo de prediccion
cantidad_vecinos = args.neighbour
tipo_prediccion = args.type
metrica = args.metrica

# Ahora puedes usar nombre_archivo_entrada y nombre_archivo_salida en tu programa
print(f"Nombre de archivo de entrada: {nombre_archivo_entrada}")
print(f"Nombre de archivo de salida: {nombre_archivo_salida}")

# Ahora puedes usar cantidad_vecinos y tipo_prediccion en tu programa
print(f"Métrica de similitud: {metrica}")
print(f"Cantidad de vecinos: {cantidad_vecinos}")
print(f"Tipo de prediccion: {tipo_prediccion}")

# Leer la matriz desde el archivo
calificacion_minima, calificacion_maxima, matriz = leer_matriz_desde_archivo(
    nombre_archivo_entrada)

# Imprimo la matriz y las calificaciones

print(calificacion_maxima)
print(calificacion_minima)
imprimir_matriz(matriz)

print("matriz prediccion")
# Calcular la prediccion para cada valor desconocido como float de 3 decimales y reemplazarlo en la matriz

matriz = normalizar_matriz(matriz, calificacion_minima , calificacion_maxima)
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
imprimir_matriz(matriz)
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] == '-':
            if tipo_prediccion == 1:
                matriz[i][j] = round(calcular_prediccion_simple(
                    matriz, cantidad_vecinos, (i, j), metrica), 5)
            elif tipo_prediccion == 2:
                matriz[i][j] = round(calcular_prediccion_diferencia_media(
                    matriz, cantidad_vecinos, (i, j), metrica), 5)

matriz = desnormalizar_matriz(matriz)

# Escribir la matriz en la consola
imprimir_matriz(matriz)

# Escribir la matriz en el archivo de salida
with open(nombre_archivo_salida, 'w') as archivo:
    archivo.write(str(calificacion_minima) + '\n')
    archivo.write(str(calificacion_maxima) + '\n')
    for fila in matriz:
        archivo.write(' '.join(map(str, fila)) + '\n')
