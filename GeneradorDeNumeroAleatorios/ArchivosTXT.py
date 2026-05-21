from pathlib import Path

def AbrirArchivo(numeros):
    print("llega al modulo de insercion")

    # Ruta del archivo .py actual
    ruta_script = Path(__file__)

    # Carpeta donde está el script
    carpeta = Path(__file__).resolve().parent

    # Abrir un archivo en la misma carpeta que el script
    archivo = carpeta / "Aleatorios.txt"
    print(numeros)

    with open(archivo, "a+") as f:
        for num in numeros:
            num=float(num)
            f.write(str(round(num,5))+"\n")


