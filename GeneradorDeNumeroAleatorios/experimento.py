def aleatoreo(indice):
    ruta_archivo = "Aleatorios.txt"
    try:
        with open(ruta_archivo, "r") as archivo:
            lineas = [linea.strip() for linea in archivo.readlines() if linea.strip()]
            
            if 0 <= indice < len(lineas):
                return float(lineas[indice])
            else:
                print(f"Error: El índice {indice} está fuera de rango.")
                return None
                
    except FileNotFoundError:
        print("Error: No se encontró el archivo Aleatorios.txt")
        return None
    

cont = 0
for i in range(100):
    cont = cont + 1
    num = aleatoreo(cont)
    print(num)