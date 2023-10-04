import math

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
        denom1 = denom1 + pow(val1 - valores_array1, 2)
    denom2 = 0.0
    for val2 in valores_array2:
        denom2 = denom2 + pow(val2 - valores_array2, 2)
    denom = math.sqrt(denom1) * math.sqrt(denom2)
    coefiente_pearson = num / denom
    return coefiente_pearson


# Función para imprimir la matriz
def imprimir_matriz(matriz):
    for fila in matriz:
        print(' '.join(map(str, fila)))

# Nombre del archivo de entrada
nombre_archivo = 'entrada.txt'

# Leer la matriz desde el archivo
calificacion_minima, calificacion_maxima, matriz = leer_matriz_desde_archivo(nombre_archivo)

# Imprimo la matriz y las calificaciones

imprimir_matriz(matriz)
print(calificacion_maxima)
print(calificacion_minima)

print(calcular_coeficiente_de_correlacion(matriz[1], matriz[2]))



