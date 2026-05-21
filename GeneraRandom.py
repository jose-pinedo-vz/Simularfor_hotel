"""
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
#     print(aleatorio(i))