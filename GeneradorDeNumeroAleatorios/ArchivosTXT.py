from pathlib import Path

def AbrirArchivo(numeros):
    print("llega al modulo de insercion")

    ruta_script = Path(__file__)

    carpeta = Path(__file__).resolve().parent

    archivo = carpeta / "Aleatorios.txt"
    print(numeros)

    with open(archivo, "a+") as f:
        for num in numeros:
            num=float(num)
            f.write(str(round(num,5))+"\n")


