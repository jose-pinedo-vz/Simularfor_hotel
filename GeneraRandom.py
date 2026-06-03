'''"""
se le tien que pasar el indice del numero que queremos y lo retornara
"""
def aleatorio(indice: int) -> float:
    ruta = f"GeneradorDeNumeroAleatorios/Aleatorios.txt"
    valor = ""
    with open(ruta, "r") as file:
        for i in range(indice):
            valor = file.readline()
    
    return float(valor)



# en este caso le pasamos i para que siempre no de un valor diferente
# for i in range(1, 100):
#     print(aleatorio(i))'''


import os

def aleatorio(indice: int) -> float:
    carpeta_actual = os.path.dirname(os.path.abspath(__file__))

    ruta = os.path.join(carpeta_actual, "GeneradorDeNumeroAleatorios", "Aleatorios.txt")

    with open(ruta, "r", encoding="utf-8") as file:
        for i, linea in enumerate(file, start=1):
            if i==indice:
                return float(linea.strip())

    raise ValueError(f"No existe el índice {indice}")