def congruencial(n: int, itera: int, v) -> str:
    cadena = ""
    lista = []
    V = v
    
    cadena2 = ""
    e = len(str(n))
    cadena += (f"e: {e} - 2e: {2*e} \n")
    a = 0
    a2 = 0
    t = 0 
    objetivo = 10**(e / 2)
    cadena += (f"valor de 10^e / 2 = {objetivo} \n\n")
    error = 200
    a1 = 0 
    a2 = 0
    a = 0
    valor = 0

    cadena += "Valores de sercania: \n"

    while True:
        error_antes = error
        for num in V:
            a1 = 200 * int(t) + int(num)
            cadena += f"200({t}) + {num} = {a1} \n"
            a2 = 200 * int(t) - int(num)
            cadena += f"200({t}) - {num} = {a2} \n"


            err1 = abs(objetivo - a1)
            err2 = abs(objetivo - a2)

            a = min(err1, err2)


            if a < error:
                error = a
                valor = a1 if err1 < err2 else a2

        if error == error_antes:
            break
        
        t += 1

    cadena += (f"\n\nvalor del arreglo mas serca {valor}, con t: {t - 1} \n")

    cadena2 += (f"semilla: {n} \n")
    n = int(n)
    aleatorio = 0

    for j in range(itera):
        aleatorio = valor * n
        cadena2 += (f"formula a(n) {n}*{valor} = {aleatorio} \n")
        n = ""
        aleatorio = str(aleatorio)
        
        ceros = ""
        for i in range(e*2 - len(aleatorio)):
            ceros += "0"

        aleatorio = ceros + aleatorio
        cadena2 += (f"aleatorio: {(int(aleatorio[e:]) / 10**e)} \n\n")
        lista.append(int(aleatorio[e:]) / 10**e)
        n = int(aleatorio[e:])

    return cadena, lista, cadena2
        





        
