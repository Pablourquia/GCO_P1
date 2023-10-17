# GCO_P1
Como parámetros el programa tiene los siguientes
optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Nombre del archivo de entrada
  -o OUTPUT, --output OUTPUT
                        Nombre del archivo de salida
  -m {1,2,3}, --metrica {1,2,3}
                        Métrica de similitud (1 -> coeficiente de correlación de Pearson, 2 -> similitud del coseno, 3 -> distancia euclídea)
  -v NEIGHBOUR, --neighbour NEIGHBOUR
                        Cantidad de vecinos (entero)
  -t {1,2}, --type {1,2}
                        Tipo de prediccion (1 -> prediccion simple o 2 -> diferencia con la media)

Ejemplo de ejecución:
  python3 main.py -i entrada.txt -o salida.txt -m 1 -v 2 -t 2



Códigos de error en tiempo de ejecución
  001: error en calcular_coeficiente_de_correlacion
  002: error en calcular_similitud_coseno
  003: error en calcular_similitud_distancia_euclídea