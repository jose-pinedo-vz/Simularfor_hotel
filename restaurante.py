import random
import math

flojo_diario = [60, 100, 160, 200, 240]
flujo_siario_prob = [10, 25, 40, 20, 5]

grupo = [2, 4, 6, 7, 8]
grupo_prob = [10, 40, 30, 15, 5]

tem_preparacion = [5, 10, 20, 30]
tem_preparacion_prob = [20, 55, 15, 10]

consumo = [1, 2, 3]
condumo_prob = [20, 60, 20]

suministro = [1, 2, 4, 5]
suministro_prob = [60, 25, 10, 5]

even_rh = ["nada", "renuncia", "despedido", "renunacia multiple"]
even_rh_prob = [92, 3, 4, 1]

Evento_Ale_prob = [80, 10, 5, 5]
Evento_Ale = ["Nada", "Merma o accidente menor", "Falla en equipo", "Devolucion de platillo"]

hora_critica = [0, 1]
hora_critica_prob = [90, 10]

porcen_ora_critica = [30, 40, 50]
porcen_ora_critica_prob = [40, 30, 30]

categorai_platillos = [[70, 20, 10], [60, 25, 15], [50, 30, 20]]
categorai_platillos_prob = [60, 30, 10]



# otros datos
platillos_disponibles = ["normal", "caro", "exotico"]
platilllosEmpesamos = [400, 200, 40]

cantidadMinimaDeStock = [200, 70, 10]
cantidadDelStockmaxiom = [400, 300, 50]

platillos_lista = platilllosEmpesamos[:]
ganancias_por_platillo = [150, 600, 900]
ganancias_netas = [100, 300, 350]

cantidad_de_mesas = 15
cantidad_de_cosineros = 8
sueldo_cosineros = 15000
horas_habiles = 8
personal = 10
sueldo_personal = 8000

pago_servicios = 2000

def CargarMedios():
    global flojo_diario, flujo_siario_prob, grupo, grupo_prob, tem_preparacion, tem_preparacion_prob, consumo, condumo_prob, suministro, \
        suministro_prob, even_rh, even_rh_prob, Evento_Ale_prob, Evento_Ale, hora_critica, hora_critica_prob, porcen_ora_critica, \
        porcen_ora_critica_prob, categorai_platillos, categorai_platillos_prob, platillos_disponibles, cantidadMinimaDeStock, cantidadDelStockmaxiom


    flojo_diario = [60, 100, 160, 200, 240]
    flujo_siario_prob = [10, 25, 40, 20, 5]

    grupo = [2, 4, 6, 7, 8]
    grupo_prob = [10, 40, 30, 15, 5]

    tem_preparacion = [5, 10, 20, 30]
    tem_preparacion_prob = [20, 55, 15, 10]

    consumo = [1, 2, 3]
    condumo_prob = [20, 60, 20]

    suministro = [1, 2, 4, 5]
    suministro_prob = [60, 25, 10, 5]

    even_rh = ["nada", "renuncia", "despedido", "renunacia multiple"]
    even_rh_prob = [92, 3, 4, 1]

    Evento_Ale_prob = [80, 10, 5, 5]
    Evento_Ale = ["Nada", "Merma o accidente menor", "Falla en equipo", "Devolucion de platillo"]

    hora_critica = [0, 1]
    hora_critica_prob = [90, 10]

    porcen_ora_critica = [30, 40, 50]
    porcen_ora_critica_prob = [40, 30, 30]

    categorai_platillos = [[70, 20, 10], [60, 25, 15], [50, 30, 20]]
    categorai_platillos_prob = [60, 30, 10]

    platillos_disponibles = ["normal", "caro", "exotico"]
    platilllosEmpesamos = [400, 200, 40]

    cantidadMinimaDeStock = [200, 70, 10]
    cantidadDelStockmaxiom = [400, 200, 50]

    global cantidad_de_mesas, cantidad_de_cosineros, sueldo_cosineros, horas_habiles, personal, sueldo_personal, pago_servicios, platillos_lista, \
        ganancias_por_platillo, ganancias_netas

    platillos_lista = platilllosEmpesamos[:]
    ganancias_por_platillo = [50, 150, 300]
    ganancias_netas = [20, 50, 100]

    cantidad_de_mesas = 15
    cantidad_de_cosineros = 8
    sueldo_cosineros = 15000
    horas_habiles = 8
    personal = 10
    sueldo_personal = 8000

    pago_servicios = 2000

    print("Si carga")


def validar(lista) -> bool:
    if sum(lista) == 100:
        return True
    else:
        return False

def transformarListas(lista) -> list:
    for i in range(len(lista)):
        lista[i] = lista[i] / 100
    return lista

def rangos(lista) -> list:
    lista_acumulada = [0]
    for i in range(len(lista)):
        nuevo_valor = lista_acumulada[-1] + lista[i]
        lista_acumulada.append(round(nuevo_valor, 3))
    return lista_acumulada

def provavilidar(lista1, lista2):
    rand = random.random()
    for i in range(len(lista2) - 1):
        if lista2[i] <= rand < lista2[i+1]:
            return lista1[i]

def validaciones(Dias_a_Simular) -> float:
    # validar si las provavilidades son correctas
    global flujo_siario_prob, grupo_prob, tem_preparacion_prob, condumo_prob, categorai_platillos_prob
    global suministro_prob, even_rh_prob, Evento_Ale_prob, porcen_ora_critica_prob, hora_critica_prob
    global flojo_diario

    CargarMedios()

    listas_a_validar = [
        flujo_siario_prob, grupo_prob, tem_preparacion_prob, condumo_prob,
        suministro_prob, even_rh_prob, Evento_Ale_prob,
        porcen_ora_critica_prob, hora_critica_prob, categorai_platillos_prob
    ]

    for p in listas_a_validar:
        if not validar(p):
            print(f"Error: Una de las listas de probabilidad no suma 100%")
            return False

    if len(flojo_diario) != len(flujo_siario_prob):
        print("Error en los datos")
        return

    if len(grupo) != len(grupo_prob):
        print("Error en los datos")
        return

    if len(tem_preparacion) != len(tem_preparacion_prob):
        print("Error en los datos")
        return

    if len(consumo) != len(condumo_prob):
        print("Error en los datos")
        return

    if len(suministro) != len(suministro_prob):
        print("Error en los datos")
        return

    if len(even_rh) != len(even_rh_prob):
        print("Error en los datos")
        return

    if len(Evento_Ale) != len(Evento_Ale_prob):
        print("Error en los datos")
        return

    if len(porcen_ora_critica) != len(porcen_ora_critica_prob):
        print("Error en los datos")
        return


    if len(hora_critica) != len(hora_critica_prob):
        print("Error en los datos")
        return

    if len(categorai_platillos) != len(categorai_platillos_prob):
        print("Error en los datos")
        return


    # paso la lista a decimal
    transformarListas(flujo_siario_prob)
    transformarListas(grupo_prob)
    transformarListas(tem_preparacion_prob)
    transformarListas(condumo_prob)
    transformarListas(suministro_prob)
    transformarListas(even_rh_prob)
    transformarListas(Evento_Ale_prob)
    transformarListas(porcen_ora_critica_prob)
    transformarListas(hora_critica_prob)
    transformarListas(categorai_platillos_prob)

    # creo los rangos
    flujo_siario_prob = rangos(flujo_siario_prob)
    grupo_prob = rangos(grupo_prob)
    tem_preparacion_prob = rangos(tem_preparacion_prob)
    condumo_prob = rangos(condumo_prob)
    suministro_prob = rangos(suministro_prob)
    even_rh_prob = rangos(even_rh_prob)
    Evento_Ale_prob = rangos(Evento_Ale_prob)
    porcen_ora_critica_prob = rangos(porcen_ora_critica_prob)
    hora_critica_prob = rangos(hora_critica_prob)
    categorai_platillos_prob = rangos(categorai_platillos_prob)

    print("los datos estan correctos")

    # platillos con los que empesamos


    platillos_encargados = []
    estado_encarga = 0
    lleganAlimentos = 0

    diasDeENcarga = []
    platillosDeEncarga = []
    # global flojo_diario
    flojo_diario_auxilia = flojo_diario[:]
    inicio_fin_semana = 5

    SumaTotal = 0
    GastosTotal = 0

    for _ in range(Dias_a_Simular):
        print("dia: ", _ + 1)
        flojo_diario = flojo_diario_auxilia[:]
        if inicio_fin_semana <= (_ + 1) and (_ + 1) <= inicio_fin_semana + 2:
            print("Fin de semana")
            for i in range(len(flojo_diario)):
                flojo_diario[i] = flojo_diario[i] * 1.20

        if (_ + 1) > inicio_fin_semana + 2:
            print("Final del fin de semana")
            inicio_fin_semana += 7


        personas = provavilidar(flojo_diario,  flujo_siario_prob)
        print("canditad de personas en el dia: ", personas)
        print("Platillos con lo que se inicia: ", platillos_lista)

        if _ in diasDeENcarga:
            for idx, dia_pedido in enumerate(diasDeENcarga):
                if _ == dia_pedido:
                    pedido = platillosDeEncarga[idx]
                    for cat in range(len(platillos_lista)):
                        platillos_lista[cat] += pedido[cat]
                    # print("Cocina abastecid")
            estado_encarga = 0
            print("Cantidad de platillos: ", platillos_lista)

        grupo_Porcent = provavilidar(grupo, grupo_prob)
        print(f"promedio de personas por grupo: {grupo_Porcent}")
        print(f"mesas totales por hora: {cantidad_de_mesas} ")
        mesas_ocupadas = math.ceil(personas / grupo_Porcent / horas_habiles)
        print(f"mesas ocupadas por hora {mesas_ocupadas}")

        criticas = provavilidar(hora_critica, hora_critica_prob)
        if criticas == 1:
            print("ubo una hora critica")
            porcentaje_de_persnas = provavilidar(porcen_ora_critica, porcen_ora_critica_prob)
            print(f"llego el {porcentaje_de_persnas} de personas en el dia")
            print(f"la cantidad de personas fueron de {personas * (porcentaje_de_persnas / 100)} en una sola hora")

            if mesas_ocupadas > cantidad_de_mesas:
                # print("saturaciones de mesas, perdida de clietes")
                print(f"la cantidad de personas atendidsas fue de {(mesas_ocupadas - cantidad_de_mesas) * grupo_Porcent}")
                personas = (mesas_ocupadas - cantidad_de_mesas) * grupo_Porcent

        if mesas_ocupadas > cantidad_de_mesas:
            # print("saturaciones de mesas, perdida de clietes")
            personas = (mesas_ocupadas - cantidad_de_mesas) * grupo_Porcent

        platillos_por_persona = provavilidar(consumo, condumo_prob)
        print(f"el promedio de platos por persona fue de: {platillos_por_persona}")

        total_de_platillos = platillos_por_persona * personas
        # print(f"fueron un total de {total_de_platillos} platillos")

        temp_cosina_promedio = provavilidar(tem_preparacion, tem_preparacion_prob)
        # print(f"tiempo promedio de preparacion de los platillos: {temp_cosina_promedio}")

        horas_cosina_totales = temp_cosina_promedio * total_de_platillos
        # print(f"Total de minutos cosinando: {horas_cosina_totales}")

        minutos_por_cosinero = horas_cosina_totales / cantidad_de_cosineros
        # print(f"cada mesero devera de trabajar {minutos_por_cosinero} minutos al dia")

        distribucion_platillos = provavilidar(categorai_platillos, categorai_platillos_prob)
        print(f"distribucion de los platillos {distribucion_platillos}")

        for i in range(len(distribucion_platillos)):
            print(f"de la categoria {i + 1} son {total_de_platillos * (distribucion_platillos[i]/100)}")


        platillosRechasados = 0
        for i in range(len(distribucion_platillos)):
            # print(f"restantes de platillos {i + 1} son {platillos_lista[i] - (total_de_platillos * (distribucion_platillos[i]/100))}")
            if platillos_lista[i] - (total_de_platillos * (distribucion_platillos[i]/100)) < 0:
                platillosRechasados += math.ceil(abs(platillos_lista[i] - (total_de_platillos * (distribucion_platillos[i]/100))))
                platillos_lista[i] = 0
            else:
                platillos_lista[i] = int(platillos_lista[i] - (total_de_platillos * (distribucion_platillos[i]/100)))

        print("platillos restandes del dia: ", platillos_lista)
        print(f"Platillos rechasados {platillosRechasados}")


        ganancias = 0
        for i in range(len(distribucion_platillos)):
            # print(f"platillos {i} =  {ganancias_por_platillo[i] * (total_de_platillos * (distribucion_platillos[i]/100))}")
            ganancias += ganancias_por_platillo[i] * total_de_platillos * (distribucion_platillos[i]/100)

        print("ganancais totales: ", ganancias)

        gastos = ganancias

        ganancias = 0
        for i in range(len(distribucion_platillos)):
            # print(f"platillos {i} =  {ganancias_netas[i] * (total_de_platillos * (distribucion_platillos[i]/100))}")
            ganancias += ganancias_netas[i] * total_de_platillos * (distribucion_platillos[i]/100)

        print("ganancais netas: ", ganancias)

        ganancias = ganancias
        gastos = gastos - ganancias


        # evento aleatiorio
        eventoProb = provavilidar(Evento_Ale, Evento_Ale_prob)
        print("Evento catastrofico del dia? ", eventoProb)
        # event rh
        eventoRH = provavilidar(even_rh, even_rh_prob)
        print("Eventos con el personal: ", eventoRH)

        for i in range(len(distribucion_platillos)):
            if platillos_lista[i] <= cantidadMinimaDeStock[i] and estado_encarga == 0:
                tiempo_de_llegada = provavilidar(suministro, suministro_prob)
                print("se encargan alimentos y se tardan en llegar: ", tiempo_de_llegada, " dias")
                lleganAlimentos = _ + tiempo_de_llegada
                for j in range(len(distribucion_platillos)):
                    platillos_encargados.append(cantidadDelStockmaxiom[j] - platillos_lista[j])

                # print(f"se encargo mercancia y llega en {lleganAlimentos} dias")
                diasDeENcarga.append(lleganAlimentos)
                print(f"cantidad de alimentos encargados {platillos_encargados}")
                platillosDeEncarga.append(platillos_encargados)
                platillos_encargados = []
                estado_encarga = 1

        print("platillos restandes del dia: ", platillos_lista)

        print("Final dia ", _ + 1)
        print(f"ganancias {ganancias}")
        SumaTotal += ganancias

        costo_cocineros = (sueldo_cosineros / 30) * cantidad_de_cosineros
        costo_personal = (sueldo_personal / 30) * personal
        costo_servicios = pago_servicios / 30

        total_fijos = costo_cocineros + costo_personal + costo_servicios
        total_fijos = round(total_fijos, 2)
        print(f"gastos: {total_fijos}")
        GastosTotal += total_fijos

    # cosina.Bacias()
    # cosina.cargarValoresmedios()

    return GastosTotal, SumaTotal



import customtkinter as ctk

class cocina:
    def __init__(self):
        self.ventana = ctk.CTkToplevel()
        self.ventana.title("COSINA - RESTAURANTE")

        try: self.ventana.state("zoomed")
        except: self.ventana.attributes("-zoomed", True)

        color_fondo = "#5D4037"
        color_hover = "#3E2723"
        color_texto = "#FFFFFF"
        color_Extra = "#8C8680"
        color_contorno_azul = "#FFFFFF"

        self.ventana.configure(fg_color=color_hover)

        self.frame_scroll = ctk.CTkScrollableFrame(
            self.ventana,
            fg_color=color_hover
        )
        self.frame_scroll.pack(fill="both", expand=True, padx=10, pady=8)


        ancho_entry = 148
        alto_entry = 36
        ancho_txt = 138
        alto_txt = 180
        pad_col = 6
        pad_row = 4


        self.datosFijos = ctk.CTkFrame(
            self.frame_scroll,
            fg_color=color_fondo,
            border_width=2,
            border_color=color_contorno_azul
        )
        self.datosFijos.pack(pady=10, padx=10, fill="x")

        label1 = ctk.CTkLabel(self.datosFijos, text="Cantidad de cocineros:", font=("Arial", 13), text_color=color_texto, wraplength=ancho_entry)
        label1.grid(row=0, column=0, padx=pad_col, pady=(10, 2), sticky="ew")

        self.CantidadDeCosineros = ctk.CTkEntry(self.datosFijos, font=("Arial", 13), width=ancho_entry, height=alto_entry)
        self.CantidadDeCosineros.grid(row=1, column=0, padx=pad_col, pady=(2, 10))

        label2 = ctk.CTkLabel(self.datosFijos, text="Mesas disponibles:", font=("Arial", 13), text_color=color_texto, wraplength=ancho_entry)
        label2.grid(row=0, column=1, padx=pad_col, pady=(10, 2), sticky="ew")

        self.cantidadDeMesas = ctk.CTkEntry(self.datosFijos, font=("Arial", 13), width=ancho_entry, height=alto_entry)
        self.cantidadDeMesas.grid(row=1, column=1, padx=pad_col, pady=(2, 10))

        label3 = ctk.CTkLabel(self.datosFijos, text="Horas laborales:", font=("Arial", 13), text_color=color_texto, wraplength=ancho_entry)
        label3.grid(row=0, column=2, padx=pad_col, pady=(10, 2), sticky="ew")

        self.Horaslaborales = ctk.CTkEntry(self.datosFijos, font=("Arial", 13), width=ancho_entry, height=alto_entry)
        self.Horaslaborales.grid(row=1, column=2, padx=pad_col, pady=(2, 10))

        label4 = ctk.CTkLabel(self.datosFijos, text="Cantidad de personal extra:", font=("Arial", 13), text_color=color_texto, wraplength=ancho_entry)
        label4.grid(row=0, column=3, padx=pad_col, pady=(10, 2), sticky="ew")

        self.personal = ctk.CTkEntry(self.datosFijos, font=("Arial", 13), width=ancho_entry, height=alto_entry)
        self.personal.grid(row=1, column=3, padx=pad_col, pady=(2, 10))

        label5 = ctk.CTkLabel(self.datosFijos, text="Sueldo cocineros / mes:", font=("Arial", 13), text_color=color_texto, wraplength=ancho_entry)
        label5.grid(row=0, column=4, padx=pad_col, pady=(10, 2), sticky="ew")

        self.SueldoCosinero = ctk.CTkEntry(self.datosFijos, font=("Arial", 13), width=ancho_entry, height=alto_entry)
        self.SueldoCosinero.grid(row=1, column=4, padx=pad_col, pady=(2, 10))

        label6 = ctk.CTkLabel(self.datosFijos, text="Sueldo resto del personal:", font=("Arial", 13), text_color=color_texto, wraplength=ancho_entry)
        label6.grid(row=0, column=5, padx=pad_col, pady=(10, 2), sticky="ew")

        self.sueldoPersonal = ctk.CTkEntry(self.datosFijos, font=("Arial", 13), width=ancho_entry, height=alto_entry)
        self.sueldoPersonal.grid(row=1, column=5, padx=pad_col, pady=(2, 10))

        label7 = ctk.CTkLabel(self.datosFijos, text="Pago total servicios mensuales:", font=("Arial", 13), text_color=color_texto, wraplength=ancho_entry)
        label7.grid(row=0, column=6, padx=pad_col, pady=(10, 2), sticky="ew")

        self.pagoServicios = ctk.CTkEntry(self.datosFijos, font=("Arial", 13), width=ancho_entry, height=alto_entry)
        self.pagoServicios.grid(row=1, column=6, padx=pad_col, pady=(2, 10))


        self.datosPlatillos = ctk.CTkFrame(
            self.frame_scroll,
            fg_color=color_fondo,
            border_width=2,
            border_color=color_contorno_azul
        )
        self.datosPlatillos.pack(pady=10, padx=10, fill="x")

        label8 = ctk.CTkLabel(self.datosPlatillos, text="Platillos disponibles:", font=("Arial", 13), text_color=color_texto, wraplength=ancho_txt)
        label8.grid(row=0, column=0, padx=pad_col, pady=(10, 2), sticky="ew")

        self.nombreplatillos = ctk.CTkTextbox(self.datosPlatillos, font=("Arial", 13), width=ancho_txt, height=alto_txt)
        self.nombreplatillos.grid(row=1, column=0, padx=pad_col, pady=(2, 10))

        label9 = ctk.CTkLabel(self.datosPlatillos, text="Distribución de su venta:", font=("Arial", 13), text_color=color_texto, wraplength=ancho_txt)
        label9.grid(row=0, column=1, padx=pad_col, pady=(10, 2), sticky="ew")

        self.distribucionPlatillos = ctk.CTkTextbox(self.datosPlatillos, font=("Arial", 13), width=ancho_txt, height=alto_txt)
        self.distribucionPlatillos.grid(row=1, column=1, padx=pad_col, pady=(2, 10))

        label10 = ctk.CTkLabel(self.datosPlatillos, text="Porcentaje de platillos:", font=("Arial", 13), text_color=color_texto, wraplength=ancho_txt)
        label10.grid(row=0, column=2, padx=pad_col, pady=(10, 2), sticky="ew")

        self.Text_categorai_platillos = ctk.CTkTextbox(self.datosPlatillos, font=("Arial", 13), width=ancho_txt, height=alto_txt)
        self.Text_categorai_platillos.grid(row=1, column=2, padx=pad_col, pady=(2, 10))

        label11 = ctk.CTkLabel(self.datosPlatillos, text="Prob de porcentaje:", font=("Arial", 13), text_color=color_texto, wraplength=ancho_txt)
        label11.grid(row=0, column=3, padx=pad_col, pady=(10, 2), sticky="ew")

        self.Text_categorai_platillos_prob = ctk.CTkTextbox(self.datosPlatillos, font=("Arial", 13), width=ancho_txt, height=alto_txt)
        self.Text_categorai_platillos_prob.grid(row=1, column=3, padx=pad_col, pady=(2, 10))

        label12 = ctk.CTkLabel(self.datosPlatillos, text="Cantidad inicial de Stock:", font=("Arial", 13), text_color=color_texto, wraplength=ancho_txt)
        label12.grid(row=0, column=4, padx=pad_col, pady=(10, 2), sticky="ew")

        self.txt_cantidadStock = ctk.CTkTextbox(self.datosPlatillos, font=("Arial", 13), width=ancho_txt, height=alto_txt)
        self.txt_cantidadStock.grid(row=1, column=4, padx=pad_col, pady=(2, 10))

        label13 = ctk.CTkLabel(self.datosPlatillos, text="Cantidad mínima de Stock:", font=("Arial", 13), text_color=color_texto, wraplength=ancho_txt)
        label13.grid(row=0, column=5, padx=pad_col, pady=(10, 2), sticky="ew")

        self.txt_cantidadStock_min = ctk.CTkTextbox(self.datosPlatillos, font=("Arial", 13), width=ancho_txt, height=alto_txt)
        self.txt_cantidadStock_min.grid(row=1, column=5, padx=pad_col, pady=(2, 10))

        label14 = ctk.CTkLabel(self.datosPlatillos, text="Costo del platillo:", font=("Arial", 13), text_color=color_texto, wraplength=ancho_txt)
        label14.grid(row=0, column=6, padx=pad_col, pady=(10, 2), sticky="ew")

        self.texr_costoDelPlatillo = ctk.CTkTextbox(self.datosPlatillos, font=("Arial", 13), width=ancho_txt, height=alto_txt)
        self.texr_costoDelPlatillo.grid(row=1, column=6, padx=pad_col, pady=(2, 10))

        label15 = ctk.CTkLabel(self.datosPlatillos, text="Ganancia del platillo:", font=("Arial", 13), text_color=color_texto, wraplength=ancho_txt)
        label15.grid(row=0, column=7, padx=pad_col, pady=(10, 2), sticky="ew")

        self.texr_gananciaDelPlatillo = ctk.CTkTextbox(self.datosPlatillos, font=("Arial", 13), width=ancho_txt, height=alto_txt)
        self.texr_gananciaDelPlatillo.grid(row=1, column=7, padx=pad_col, pady=(2, 10))


        self.datosBariables = ctk.CTkFrame(
            self.frame_scroll,
            fg_color=color_fondo,
            border_width=2,
            border_color=color_contorno_azul
        )
        self.datosBariables.pack(pady=10, padx=10, fill="x")

        label16 = ctk.CTkLabel(self.datosBariables, text="Flujo de personas por dia:", font=("Arial", 13), text_color=color_texto, wraplength=ancho_txt)
        label16.grid(row=0, column=0, padx=pad_col, pady=(10, 2), sticky="ew")

        self.text_FlujodePersonasPorDia = ctk.CTkTextbox(self.datosBariables, font=("Arial", 13), width=ancho_txt, height=alto_txt)
        self.text_FlujodePersonasPorDia.grid(row=1, column=0, padx=pad_col, pady=(2, 10))

        label17 = ctk.CTkLabel(self.datosBariables, text="Prob flujo de personas:", font=("Arial", 13), text_color=color_texto, wraplength=ancho_txt)
        label17.grid(row=0, column=1, padx=pad_col, pady=(10, 2), sticky="ew")

        self.text_FlujodePersonasPorDia_prob = ctk.CTkTextbox(self.datosBariables, font=("Arial", 13), width=ancho_txt, height=alto_txt)
        self.text_FlujodePersonasPorDia_prob.grid(row=1, column=1, padx=pad_col, pady=(2, 10))

        label18 = ctk.CTkLabel(self.datosBariables, text="Promedio de grupo:", font=("Arial", 13), text_color=color_texto, wraplength=ancho_txt)
        label18.grid(row=0, column=2, padx=pad_col, pady=(10, 2), sticky="ew")

        self.text_TamaniodelGrupo = ctk.CTkTextbox(self.datosBariables, font=("Arial", 13), width=ancho_txt, height=alto_txt)
        self.text_TamaniodelGrupo.grid(row=1, column=2, padx=pad_col, pady=(2, 10))

        label19 = ctk.CTkLabel(self.datosBariables, text="Prob promedio de grupo:", font=("Arial", 13), text_color=color_texto, wraplength=ancho_txt)
        label19.grid(row=0, column=3, padx=pad_col, pady=(10, 2), sticky="ew")

        self.text_TamaniodelGrupoprob = ctk.CTkTextbox(self.datosBariables, font=("Arial", 13), width=ancho_txt, height=alto_txt)
        self.text_TamaniodelGrupoprob.grid(row=1, column=3, padx=pad_col, pady=(2, 10))

        label20 = ctk.CTkLabel(self.datosBariables, text="Preparacion platillo:", font=("Arial", 13), text_color=color_texto, wraplength=ancho_txt)
        label20.grid(row=0, column=4, padx=pad_col, pady=(10, 2), sticky="ew")

        self.tex_preapracion_platillo = ctk.CTkTextbox(self.datosBariables, font=("Arial", 13), width=ancho_txt, height=alto_txt)
        self.tex_preapracion_platillo.grid(row=1, column=4, padx=pad_col, pady=(2, 10))

        label21 = ctk.CTkLabel(self.datosBariables, text="Prob preparacion platillo:", font=("Arial", 13), text_color=color_texto, wraplength=ancho_txt)
        label21.grid(row=0, column=5, padx=pad_col, pady=(10, 2), sticky="ew")

        self.tex_preapracion_platillo_prob = ctk.CTkTextbox(self.datosBariables, font=("Arial", 13), width=ancho_txt, height=alto_txt)
        self.tex_preapracion_platillo_prob.grid(row=1, column=5, padx=pad_col, pady=(2, 10))



        label22 = ctk.CTkLabel(self.datosBariables, text="Consumo por persona:", font=("Arial", 13), text_color=color_texto, wraplength=ancho_txt)
        label22.grid(row=2, column=0, padx=pad_col, pady=(10, 2), sticky="ew")

        self.text_consumoPorPersona = ctk.CTkTextbox(self.datosBariables, font=("Arial", 13), width=ancho_txt, height=alto_txt)
        self.text_consumoPorPersona.grid(row=3, column=0, padx=pad_col, pady=(2, 10))

        label23 = ctk.CTkLabel(self.datosBariables, text="Prob consumo:", font=("Arial", 13), text_color=color_texto, wraplength=ancho_txt)
        label23.grid(row=2, column=1, padx=pad_col, pady=(10, 2), sticky="ew")

        self.text_comsumoPorPersona_prob = ctk.CTkTextbox(self.datosBariables, font=("Arial", 13), width=ancho_txt, height=alto_txt)
        self.text_comsumoPorPersona_prob.grid(row=3, column=1, padx=pad_col, pady=(2, 10))

        label24 = ctk.CTkLabel(self.datosBariables, text="Suministro:", font=("Arial", 13), text_color=color_texto, wraplength=ancho_txt)
        label24.grid(row=2, column=2, padx=pad_col, pady=(10, 2), sticky="ew")

        self.text_suministro = ctk.CTkTextbox(self.datosBariables, font=("Arial", 13), width=ancho_txt, height=alto_txt)
        self.text_suministro.grid(row=3, column=2, padx=pad_col, pady=(2, 10))

        label25 = ctk.CTkLabel(self.datosBariables, text="Prob suministro:", font=("Arial", 13), text_color=color_texto, wraplength=ancho_txt)
        label25.grid(row=2, column=3, padx=pad_col, pady=(10, 2), sticky="ew")

        self.text_suministroProb = ctk.CTkTextbox(self.datosBariables, font=("Arial", 13), width=ancho_txt, height=alto_txt)
        self.text_suministroProb.grid(row=3, column=3, padx=pad_col, pady=(2, 10))

        label26 = ctk.CTkLabel(self.datosBariables, text="Evento de RH:", font=("Arial", 13), text_color=color_texto, wraplength=ancho_txt)
        label26.grid(row=2, column=4, padx=pad_col, pady=(10, 2), sticky="ew")

        self.text_eventoRh = ctk.CTkTextbox(self.datosBariables, font=("Arial", 13), width=ancho_txt, height=alto_txt)
        self.text_eventoRh.grid(row=3, column=4, padx=pad_col, pady=(2, 10))

        label27 = ctk.CTkLabel(self.datosBariables, text="Prob evento de RH:", font=("Arial", 13), text_color=color_texto, wraplength=ancho_txt)
        label27.grid(row=2, column=5, padx=pad_col, pady=(10, 2), sticky="ew")

        self.text_eventoRh_prob = ctk.CTkTextbox(self.datosBariables, font=("Arial", 13), width=ancho_txt, height=alto_txt)
        self.text_eventoRh_prob.grid(row=3, column=5, padx=pad_col, pady=(2, 10))


        label28 = ctk.CTkLabel(self.datosBariables, text="Evento aleatorios:", font=("Arial", 13), text_color=color_texto, wraplength=ancho_txt)
        label28.grid(row=4, column=0, padx=pad_col, pady=(10, 2), sticky="ew")

        self.text_eventoAle = ctk.CTkTextbox(self.datosBariables, font=("Arial", 13), width=ancho_txt, height=alto_txt)
        self.text_eventoAle.grid(row=5, column=0, padx=pad_col, pady=(2, 10))

        label29 = ctk.CTkLabel(self.datosBariables, text="Prob evento aleatorios:", font=("Arial", 13), text_color=color_texto, wraplength=ancho_txt)
        label29.grid(row=4, column=1, padx=pad_col, pady=(10, 2), sticky="ew")

        self.text_eventoAle_prob = ctk.CTkTextbox(self.datosBariables, font=("Arial", 13), width=ancho_txt, height=alto_txt)
        self.text_eventoAle_prob.grid(row=5, column=1, padx=pad_col, pady=(2, 10))

        label30 = ctk.CTkLabel(self.datosBariables, text="Horas criticas:", font=("Arial", 13), text_color=color_texto, wraplength=ancho_txt)
        label30.grid(row=4, column=2, padx=pad_col, pady=(10, 2), sticky="ew")

        self.textHorasCriticas = ctk.CTkTextbox(self.datosBariables, font=("Arial", 13), width=ancho_txt, height=alto_txt)
        self.textHorasCriticas.grid(row=5, column=2, padx=pad_col, pady=(2, 10))

        label31 = ctk.CTkLabel(self.datosBariables, text="Prob horas criticas:", font=("Arial", 13), text_color=color_texto, wraplength=ancho_txt)
        label31.grid(row=4, column=3, padx=pad_col, pady=(10, 2), sticky="ew")

        self.textHorasCriticasprob = ctk.CTkTextbox(self.datosBariables, font=("Arial", 13), width=ancho_txt, height=alto_txt)
        self.textHorasCriticasprob.grid(row=5, column=3, padx=pad_col, pady=(2, 10))


        self.Botonsitos = ctk.CTkFrame(
            self.frame_scroll,
            fg_color=color_fondo,
            border_width=2,
            border_color=color_contorno_azul
        )
        self.Botonsitos.pack(pady=10, padx=10, fill="x")

        ancho_btn = 200
        alto_btn  = 55

        self.cargar = ctk.CTkButton(
            self.Botonsitos, text="Cargar elementos",
            width=ancho_btn, height=alto_btn,
            fg_color=color_Extra, hover_color=color_hover,
            text_color=color_texto, font=("Arial", 14, "bold"),
            command=lambda: self.extraervalores()
        )
        self.cargar.grid(row=0, column=0, padx=20, pady=20)

        self.Baciar = ctk.CTkButton(
            self.Botonsitos, text="Vaciar",
            width=ancho_btn, height=alto_btn,
            fg_color=color_Extra, hover_color=color_hover,
            text_color=color_texto, font=("Arial", 14, "bold"),
            command=lambda: self.Bacias()
        )
        self.Baciar.grid(row=0, column=1, padx=20, pady=20)

        self.bj = ctk.CTkButton(
            self.Botonsitos, text="Valores bajos",
            width=ancho_btn, height=alto_btn,
            fg_color=color_Extra, hover_color=color_hover,
            text_color=color_texto, font=("Arial", 14, "bold"),
            command=lambda: self.piloto()
        )
        self.bj.grid(row=0, column=2, padx=20, pady=20)

        self.at = ctk.CTkButton(
            self.Botonsitos, text="Valores altos",
            width=ancho_btn, height=alto_btn,
            fg_color=color_Extra, hover_color=color_hover,
            text_color=color_texto, font=("Arial", 14, "bold")
        )
        self.at.grid(row=0, column=3, padx=20, pady=20)

        self.md = ctk.CTkButton(
            self.Botonsitos, text="Valores medios",
            width=ancho_btn, height=alto_btn,
            fg_color=color_Extra, hover_color=color_hover,
            text_color=color_texto, font=("Arial", 14, "bold"),
            command=lambda: self.cargarValoresmedios()
        )
        self.md.grid(row=0, column=4, padx=20, pady=20)

        self.cargarElementosEninterface()



    def cargarElementosEninterface(self):
        # primera parte
        self.CantidadDeCosineros.delete(0, "end")
        self.CantidadDeCosineros.insert(0, str(cantidad_de_cosineros))

        self.cantidadDeMesas.delete(0, "end")
        self.cantidadDeMesas.insert(0, str(cantidad_de_mesas))

        self.Horaslaborales.delete(0, "end")
        self.Horaslaborales.insert(0, str(horas_habiles))

        self.personal.delete(0, "end")
        self.personal.insert(0, str(personal))

        self.sueldoPersonal.delete(0, "end")
        self.sueldoPersonal.insert(0, str(sueldo_personal))

        self.SueldoCosinero.delete(0, "end")
        self.SueldoCosinero.insert(0, str(sueldo_cosineros))

        self.pagoServicios.delete(0, "end")
        self.pagoServicios.insert(0, str(pago_servicios))

        # parte 2
        self.nombreplatillos.delete("1.0", "end")
        print("Experimentos: ", platillos_disponibles)
        for platillo in platillos_disponibles:
            self.nombreplatillos.insert("end", str(platillo) + "\n")


        self.Text_categorai_platillos.delete("1.0", "end")
        for lista in categorai_platillos:
            for elemento in lista:
                self.Text_categorai_platillos.insert("end", str(elemento) + " ")
            self.Text_categorai_platillos.insert("end", "\n")


        self.Text_categorai_platillos_prob.delete("1.0", "end")
        for elemento in categorai_platillos_prob:
            self.Text_categorai_platillos_prob.insert("end", str(elemento) + "\n")

        self.txt_cantidadStock.delete("1.0", "end")
        for elemento in platillos_lista:
            self.txt_cantidadStock.insert("end", str(elemento) + "\n")

        self.txt_cantidadStock_min.delete("1.0", "end")
        for elemento in cantidadMinimaDeStock:
            self.txt_cantidadStock_min.insert("end", str(elemento) + "\n")

        self.texr_costoDelPlatillo.delete("1.0", "end")
        for elemento in ganancias_por_platillo:
            self.texr_costoDelPlatillo.insert("end", str(elemento) + "\n")

        self.texr_gananciaDelPlatillo.delete("1.0", "end")
        for elemento in ganancias_netas:
            self.texr_gananciaDelPlatillo.insert("end", str(elemento) + "\n")


        # parte 3
        self.text_FlujodePersonasPorDia.delete("1.0", "end")
        for elemento in flojo_diario:
            self.text_FlujodePersonasPorDia.insert("end", str(elemento) + "\n")

        self.text_FlujodePersonasPorDia_prob.delete("1.0", "end")
        for elemento in flujo_siario_prob:
            self.text_FlujodePersonasPorDia_prob.insert("end", str(elemento) + "\n")

        self.text_TamaniodelGrupo.delete("1.0", "end")
        for elemento in grupo:
            self.text_TamaniodelGrupo.insert("end", str(elemento) + "\n")

        self.text_TamaniodelGrupoprob.delete("1.0", "end")
        for elemento in grupo_prob:
            self.text_TamaniodelGrupoprob.insert("end", str(elemento) + "\n")

        self.tex_preapracion_platillo.delete("1.0", "end")
        for elemento in tem_preparacion:
            self.tex_preapracion_platillo.insert("end", str(elemento) + "\n")

        self.tex_preapracion_platillo_prob.delete("1.0", "end")
        for elemento in tem_preparacion_prob:
            self.tex_preapracion_platillo_prob.insert("end", str(elemento) + "\n")

        self.text_consumoPorPersona.delete("1.0", "end")
        for elemento in consumo:
            self.text_consumoPorPersona.insert("end", str(elemento) + "\n")

        self.text_comsumoPorPersona_prob.delete("1.0", "end")
        for elemento in condumo_prob:
            self.text_comsumoPorPersona_prob.insert("end", str(elemento) + "\n")

        self.text_suministro.delete("1.0", "end")
        for elemento in suministro:
            self.text_suministro.insert("end", str(elemento) + "\n")

        self.text_suministroProb.delete("1.0", "end")
        for elemento in suministro_prob:
            self.text_suministroProb.insert("end", str(elemento) + "\n")

        self.text_eventoRh.delete("1.0", "end")
        for elemento in even_rh:
            self.text_eventoRh.insert("end", str(elemento) + "\n")

        self.text_eventoRh_prob.delete("1.0", "end")
        for elemento in even_rh_prob:
            self.text_eventoRh_prob.insert("end", str(elemento) + "\n")

        self.text_eventoAle.delete("1.0", "end")
        for elemento in Evento_Ale:
            self.text_eventoAle.insert("end", str(elemento) + "\n")

        self.text_eventoAle_prob.delete("1.0", "end")
        for elemento in Evento_Ale_prob:
            self.text_eventoAle_prob.insert("end", str(elemento) + "\n")

        self.textHorasCriticas.delete("1.0", "end")
        for elemento in porcen_ora_critica:
            self.textHorasCriticas.insert("end", str(elemento) + "\n")

        self.textHorasCriticasprob.delete("1.0", "end")
        for elemento in porcen_ora_critica_prob:
            self.textHorasCriticasprob.insert("end", str(elemento) + "\n")


    def extraervalores(self):
        print("Si llega")

        global flojo_diario, flujo_siario_prob, grupo, grupo_prob, tem_preparacion, tem_preparacion_prob, consumo, condumo_prob, suministro, \
            suministro_prob, even_rh, even_rh_prob, Evento_Ale_prob, Evento_Ale, hora_critica, hora_critica_prob, porcen_ora_critica, \
            porcen_ora_critica_prob, categorai_platillos, categorai_platillos_prob, platillos_disponibles, cantidadMinimaDeStock, cantidadDelStockmaxiom


        texto_crudo = self.text_FlujodePersonasPorDia.get("1.0", "end")
        flojo_diario = [float(x) for x in texto_crudo.split()]

        texto_crudo = self.text_comsumoPorPersona_prob.get("1.0", "end")
        flujo_siario_prob = [int(x) for x in texto_crudo.split()]

        texto_crudo = self.text_TamaniodelGrupo.get("1.0", "end")
        grupo = [int(x) for x in texto_crudo.split()]

        texto_crudo = self.text_TamaniodelGrupoprob.get("1.0", "end")
        grupo_prob = [int(x) for x in texto_crudo.split()]

        texto_crudo = self.tex_preapracion_platillo.get("1.0", "end")
        tem_preparacion = [int(x) for x in texto_crudo.split()]

        #pulir
        texto_crudo = self.tex_preapracion_platillo_prob.get("1.0", "end")
        tem_preparacion_prob = [int(x) for x in texto_crudo.split()]

        texto_crudo = self.text_consumoPorPersona.get("1.0", "end")
        consumo = [int(x) for x in texto_crudo.split()]

        texto_crudo = self.text_comsumoPorPersona_prob.get("1.0", "end")
        condumo_prob = [int(x) for x in texto_crudo.split()]


        texto_crudo = self.text_suministro.get("1.0", "end")
        suministro = [int(x) for x in texto_crudo.split()]

        texto_crudo = self.text_suministroProb.get("1.0", "end")
        suministro_prob = [int(x) for x in texto_crudo.split()]

        texto_crudo = self.text_eventoRh.get("1.0", "end")
        even_rh = [x for x in texto_crudo.split()]

        texto_crudo = self.text_eventoRh_prob.get("1.0", "end")
        even_rh_prob = [int(x) for x in texto_crudo.split()]



        texto_crudo = self.text_eventoAle_prob.get("1.0", "end")
        Evento_Ale_prob = [int(x) for x in texto_crudo.split()]

        texto_crudo = self.text_eventoAle.get("1.0", "end")
        Evento_Ale = [x for x in texto_crudo.split()]



        texto_crudo = self.textHorasCriticas.get("1.0", "end")
        hora_critica = [int(x) for x in texto_crudo.split()]

        texto_crudo = self.textHorasCriticasprob.get("1.0", "end")
        hora_critica_prob = [int(x) for x in texto_crudo.split()]


        # texto_crudo = self..get("1.0", "end")
        # porcen_ora_critica = [int(x) for x in texto_crudo.split()]

        # texto_crudo = self.tex_preapracion_platillo_prob.get("1.0", "end")
        # porcen_ora_critica_prob = [int(x) for x in texto_crudo.split()]


        texto_crudo = self.Text_categorai_platillos.get("1.0", "end").strip()

        categorai_platillos = []

        for linea in texto_crudo.split('\n'):
            if linea.strip():
                fila = [int(x) for x in linea.split()]
                categorai_platillos.append(fila)


        texto_crudo = self.Text_categorai_platillos_prob.get("1.0", "end")
        categorai_platillos_prob = [int(x) for x in texto_crudo.split()]


        texto_crudo = self.nombreplatillos.get("1.0", "end")
        platillos_disponibles = [x for x in texto_crudo.split()]

        texto_crudo = self.txt_cantidadStock.get("1.0", "end")
        platilllosEmpesamos = [int(x) for x in texto_crudo.split()]


        texto_crudo = self.txt_cantidadStock_min.get("1.0", "end")
        cantidadMinimaDeStock = [int(x) for x in texto_crudo.split()]

        texto_crudo = self.txt_cantidadStock.get("1.0", "end")
        cantidadDelStockmaxiom = [int(x) for x in texto_crudo.split()]

        global cantidad_de_mesas, cantidad_de_cosineros, sueldo_cosineros, horas_habiles, personal, sueldo_personal, pago_servicios, platillos_lista, \
            ganancias_por_platillo, ganancias_netas

        platillos_lista = platilllosEmpesamos[:]


        texto_crudo = self.texr_costoDelPlatillo.get("1.0", "end")
        ganancias_por_platillo = [float(x) for x in texto_crudo.split()]

        texto_crudo = self.texr_gananciaDelPlatillo.get("1.0", "end")
        ganancias_netas = [float(x) for x in texto_crudo.split()]


        cantidad_de_mesas = int(self.cantidadDeMesas.get())
        cantidad_de_cosineros = int(self.CantidadDeCosineros.get())
        sueldo_cosineros = float(self.SueldoCosinero.get())
        horas_habiles = int(self.Horaslaborales.get())
        personal = int(self.personal.get())
        sueldo_personal = float(self.sueldoPersonal.get())

        pago_servicios = float(self.pagoServicios.get())

        print("Todo salio bien")

        self.cargarElementosEninterface()




    def Bacias(self):
        flojo_diario.clear()
        flujo_siario_prob.clear()

        grupo.clear()
        grupo_prob.clear()

        tem_preparacion.clear()
        tem_preparacion_prob.clear()

        consumo.clear()
        condumo_prob.clear()

        suministro.clear()
        suministro_prob.clear()

        even_rh.clear()
        even_rh_prob.clear()

        Evento_Ale_prob.clear()
        Evento_Ale.clear()

        hora_critica.clear()
        hora_critica_prob.clear()

        porcen_ora_critica.clear()
        porcen_ora_critica_prob.clear()

        categorai_platillos.clear()
        categorai_platillos_prob.clear()

        # otros datos
        platillos_disponibles.clear()
        platilllosEmpesamos.clear()

        cantidadMinimaDeStock.clear()
        cantidadDelStockmaxiom.clear()

        platillos_lista.clear()
        ganancias_por_platillo.clear()
        ganancias_netas.clear()

        global cantidad_de_mesas, cantidad_de_cosineros, sueldo_cosineros, horas_habiles, personal, sueldo_personal, pago_servicios

        cantidad_de_mesas = 0
        cantidad_de_cosineros = 0
        sueldo_cosineros = 0
        horas_habiles = 0
        personal = 0
        sueldo_personal = 0
        pago_servicios = 0

        self.cargarElementosEninterface()

    def cargarValoresmedios(self):
        global flojo_diario, flujo_siario_prob, grupo, grupo_prob, tem_preparacion, tem_preparacion_prob, consumo, condumo_prob, suministro, \
            suministro_prob, even_rh, even_rh_prob, Evento_Ale_prob, Evento_Ale, hora_critica, hora_critica_prob, porcen_ora_critica, \
            porcen_ora_critica_prob, categorai_platillos, categorai_platillos_prob, platillos_disponibles, cantidadMinimaDeStock, cantidadDelStockmaxiom

        global cantidad_de_mesas, cantidad_de_cosineros, sueldo_cosineros, horas_habiles, personal, sueldo_personal, pago_servicios, platillos_lista, \
            ganancias_por_platillo, ganancias_netas

        flojo_diario = [60, 100, 160, 200, 240]
        flujo_siario_prob = [10, 25, 40, 20, 5]

        grupo = [2, 4, 6, 7, 8]
        grupo_prob = [10, 40, 30, 15, 5]

        tem_preparacion = [5, 10, 20, 30]
        tem_preparacion_prob = [20, 55, 15, 10]

        consumo = [1, 2, 3]
        condumo_prob = [20, 60, 20]

        suministro = [1, 2, 4, 5]
        suministro_prob = [60, 25, 10, 5]

        even_rh = ["nada", "renuncia", "despedido", "renunacia multiple"]
        even_rh_prob = [92, 3, 4, 1]

        Evento_Ale_prob = [80, 10, 5, 5]
        Evento_Ale = ["Nada", "Merma o accidente menor", "Falla en equipo", "Devolucion de platillo"]

        hora_critica = [0, 1]
        hora_critica_prob = [90, 10]

        porcen_ora_critica = [30, 40, 50]
        porcen_ora_critica_prob = [40, 30, 30]

        categorai_platillos = [[70, 20, 10], [60, 25, 15], [50, 30, 20]]
        categorai_platillos_prob = [60, 30, 10]


        # otros datos
        platillos_disponibles = ["normal", "caro", "exotico"]
        platilllosEmpesamos = [400, 200, 40]

        cantidadMinimaDeStock = [200, 70, 10]
        cantidadDelStockmaxiom = [400, 300, 50]

        platillos_lista = platilllosEmpesamos[:]
        ganancias_por_platillo = [150, 600, 900]
        ganancias_netas = [100, 300, 350]

        cantidad_de_mesas = 15
        cantidad_de_cosineros = 8
        sueldo_cosineros = 15000
        horas_habiles = 8
        personal = 10
        sueldo_personal = 8000

        pago_servicios = 2000

        print("Si carga")

        self.cargarElementosEninterface()


    def piloto(self):
        validaciones()



        self.ventana.mainloop()
