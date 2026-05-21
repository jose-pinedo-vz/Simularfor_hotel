def cuadradosMedios(semilla, nf):
    lista = []
    cadena_inicial = ""
    n = 0
    semilla = str(semilla)

    def generarMuchosNumeros(semilla, n, nf, cadena):
        if n >= nf:
            return cadena  
        else:
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
            lista.append(int(aleatorio) / (10 ** largo))
            cadena += (f"Numeros aleatiorios {aleatorio} -- {int(aleatorio) / (10 ** largo)}\n")
            
            return generarMuchosNumeros(aleatorio, n + 1, nf, cadena)

    nuevaCadena = generarMuchosNumeros(semilla, n, nf, cadena_inicial)
    return lista, nuevaCadena

