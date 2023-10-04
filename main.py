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
                fila.append(x)  # Guarde el valor tal como está en la matriz

            matriz.append(fila)

    return calificacion_minima, calificacion_maxima, matriz

def calcular_coeficiente_de_correlacion(array1, array2):
    # Crear nuevas listas sin guiones y valores correspondientes en ambos arrays
    valores_array1 = []
    valores_array2 = []

    for val1, val2 in zip(array1, array2):
        if val1 != '-' and val2 != '-':
            valores_array1.append(float(val1))
            valores_array2.append(float(val2))

    media_cal_a1 = sum(valores_array1) / len(valores_array1)
    media_cal_a2 = sum(valores_array2) / len(valores_array2)
    
    num = 0.0
    for val1,val2 in zip(valores_array1, valores_array2):
        num += ((val1 - media_cal_a1) * (val2 - media_cal_a2))
    
    denom1  = 0.0
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

def calcular_distancia_euclídea(array1, array2):
    # Crear nuevas listas sin guiones y valores correspondientes en ambos arrays
    valores_array1 = []
    valores_array2 = []

    for val1, val2 in zip(array1, array2):
        if val1 != '-' and val2 != '-':
            valores_array1.append(float(val1))
            valores_array2.append(float(val2))

    suma = 0.0
    for val1, val2 in zip(valores_array1, valores_array2):
        suma += pow((val1 - val2), 2)
    distancia_euclídea = math.sqrt(suma)
    return distancia_euclídea

def calcular_similitud_coseno(array1, array2):
    #Crear nuevas listas sin guiones y valores correspondientes en ambos arrays
    valores_array1 = []
    valores_array2 = []

    for val1, val2 in zip(array1, array2):
        if val1 != '-' and val2 != '-':
            valores_array1.append(float(val1))
            valores_array2.append(float(val2))
    
    num = 0.0
    for val1, val2 in zip(valores_array1, valores_array2):
        num += (val1 * val2)

    denom1 = 0.0
    for val1 in valores_array1:
        denom1 += pow(val1, 2)

    denom2 = 0.0
    for val2 in valores_array2:
        denom2 += pow(val2, 2)

    denom = math.sqrt(denom1) * math.sqrt(denom2)
    similitud_coseno = num / denom
    return similitud_coseno    

    


# Función para imprimir la matriz
def imprimir_matriz(matriz):
    for fila in matriz:
        print(' '.join(map(str, fila)))

# Crear un objeto ArgumentParser
parser = argparse.ArgumentParser(description='Procesar archivos de entrada y salida.')

# Agregar argumentos de línea de comandos
parser.add_argument('-i', '--input', type=str, required=True, help='Nombre del archivo de entrada')
parser.add_argument('-o', '--output', type=str, required=True, help='Nombre del archivo de salida')
parser.add_argument('-v', '--neighbour', type=int, required=True, help='Cantidad de vecinos (entero)')
parser.add_argument('-t', '--type', type=int, choices=[1, 2], required=True, help='Tipo de prediccion (1 -> prediccion simple o 2 -> diferencia con la media)')

# Analizar los argumentos
args = parser.parse_args()

# Acceder a los nombres de archivo proporcionados
nombre_archivo_entrada = args.input
nombre_archivo_salida = args.output

# Acceder a los vecinos y el tipo de prediccion
cantidad_vecinos = args.neighbour
tipo_prediccion = args.type

# Ahora puedes usar nombre_archivo_entrada y nombre_archivo_salida en tu programa
print(f"Nombre de archivo de entrada: {nombre_archivo_entrada}")
print(f"Nombre de archivo de salida: {nombre_archivo_salida}")

# Ahora puedes usar cantidad_vecinos y tipo_prediccion en tu programa
print(f"Cantidad de vecinos: {cantidad_vecinos}")
print(f"Tipo de prediccion: {tipo_prediccion}")

# Leer la matriz desde el archivo
calificacion_minima, calificacion_maxima, matriz = leer_matriz_desde_archivo(nombre_archivo_entrada)

# Imprimo la matriz y las calificaciones

imprimir_matriz(matriz)
print(calificacion_maxima)
print(calificacion_minima)

print(calcular_coeficiente_de_correlacion(matriz[0], matriz[1]))
print(calcular_distancia_euclídea(matriz[0], matriz[1]))
print(calcular_similitud_coseno(matriz[0], matriz[1]))
