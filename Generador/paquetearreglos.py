from numpy import *
import random
import numpy as np

def paquetearreglo():
    n = 20
    arre = np.zeros(n)
    lismayor = []
    for i in range(n):
        arre[i] = random.randint(1, 100)
    print("Arreglo original:", arre)
    
    # Guardar copia del arreglo original
    arre_original = arre.copy()
    
    band = True
    while band == True:
        band = False
        for j in range(n):
            for i in range(j+1, n):
                if arre[i] == arre[j]:
                    print("error hay un numero repetido")
                    arre[j] = random.randint(1, 100)
                    band = True
                    print("Arreglo sin numeros repetidos: ", arre)
    
    for j in range(5):
        mayor = 0
        posicion = 0
        for i in range(len(arre)):
            if arre[i] > mayor:
                mayor = arre[i]
                posicion = i
        lismayor.append(int(mayor))
        arre[posicion] = -1
    
    print("Los 5 números mayores son:", lismayor)
    

    mayor_diferencia = 0
    elemento1 = 0
    elemento2 = 0
    
    for i in range(n):
        for j in range(i+1, n):
            diferencia = abs(arre_original[i] - arre_original[j])
            if diferencia > mayor_diferencia:
                mayor_diferencia = diferencia
                elemento1 = arre_original[i]
                elemento2 = arre_original[j]
    
    print("La mayor diferencia es:", mayor_diferencia)
    print("Entre los elementos:", elemento1, "y", elemento2)

paquetearreglo()
