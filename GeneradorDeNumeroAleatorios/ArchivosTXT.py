from pathlib import Path

def AbrirArchivo(numeros):

    # Ruta del archivo .py actual
    ruta_script = Path(__file__)

    # Carpeta donde está el script
    carpeta = Path(__file__).resolve().parent

    # Abrir un archivo en la misma carpeta que el script
    archivo = carpeta / "Aleatorios.txt"

    with open(archivo, "a+") as f:
        
        f.write("\n")
        for num in numeros:
            num=round(num,5)
            f.write(str(num)+"\n")


