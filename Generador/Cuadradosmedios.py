import random
def cuadradosMedios(semilla, nf):
    lista = []
    cadena_inicial = ""
    n = 0
    semilla = str(semilla)

    def generarMuchosNumeros(semilla, n, nf, cadena):
        if n >= nf:
            return cadena  
        else:
            semilla = str(semilla)
            cadena += (f"Semilla: {semilla} - e = {len(semilla)} ")
            num = str(semilla)
            e = len(num) * 2
            num = str(int(num) ** 2)

            while len(num) < e:
                num = "0" + num

            cadena += (f"Semilla al Cuadrado: {num} ")

            inicio = (len(num) - len(str(semilla))) // 2
            aleatorio = num[inicio : inicio + len(str(semilla))]
            largo = len(aleatorio)
            if int(aleatorio) / (10 ** largo) in lista:
                aleatorio = random.randint(1000, 9999)
                print("el valor se repito y se creo una nueva semilla")
                try:
                    cadena += f"\nLa semilla se repite y se genera una nueva: {aleatorio}\n"
                    return generarMuchosNumeros(aleatorio, n + 1, nf, cadena)
                except:
                    print("parese que ubo un error en iteraciones, paresen ser demaciadas")
                    return cadena

            lista.append(int(aleatorio) / (10 ** largo))
            cadena += (f"Numeros aleatorios {aleatorio} -- {str(int(aleatorio) / (10 ** largo))}\n")
            
            print(aleatorio)
            validar = str(aleatorio[2:])
            if validar == "00":
                print("a partir de aqui ubo un error")
                elemento ="1"
                for i in range(len(str(lista[0])) - 3):
                    elemento += "0"
                print("elemento: ", elemento)
                elemento2 = elemento + "0"
                aleatorio = random.randint(int(elemento), int(elemento2))
                cadena += f"La semilla original murio y se genero una nueva semilla {aleatorio}\n"
            try:
                return generarMuchosNumeros(aleatorio, n + 1, nf, cadena)
            except:
                print("parese que ubo un error en iteraciones, paresen ser demaciadas")
                return cadena

    nuevaCadena = generarMuchosNumeros(str(semilla), n, nf, cadena_inicial)
    return lista, nuevaCadena


# semilla = 2432
# nf = 100

# cadena, lista = cuadradosMedios(semilla, nf)

# print(cadena)
# print(lista)