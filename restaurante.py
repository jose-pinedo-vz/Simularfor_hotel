import random

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



def validar(lista) -> bool:
    if sum(lista) == 100:
        return True
    else:
        return False
    
def transformarListas(lista) -> list:
    for i in range(len(lista)):
        lista[i] = lista[i] / 100
    print(lista)
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

def validaciones() -> None:
    # validar si las provavilidades son correctas
    global flujo_siario_prob, grupo_prob, tem_preparacion_prob, condumo_prob, categorai_platillos_prob
    global suministro_prob, even_rh_prob, Evento_Ale_prob, porcen_ora_critica_prob, hora_critica_prob

    listas_a_validar = [
        flujo_siario_prob, grupo_prob, tem_preparacion_prob, condumo_prob,
        suministro_prob, even_rh_prob, Evento_Ale_prob, 
        porcen_ora_critica_prob, hora_critica_prob, categorai_platillos_prob
    ]

    for p in listas_a_validar:
        if not validar(p):
            print(f"Error: Una de las listas de probabilidad no suma 100%")
            return False
        

    # validar que los datos sean consistentes o si dan las provavilidades con las consecuencais
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
    regular = 400
    caro = 200
    raro = 40

    cantidadMinimaDeStock = [200, 70, 10]
    cantidadDelStockmaxiom = [400, 200, 50]


    platillos_lista = [regular, caro, raro]
    ganancias_por_platillo = [50, 150, 300]
    ganancias_netas = [20, 50, 100]

    cantidad_de_mesas = 15
    cantidad_de_cosineros = 8
    horas_habiles = 8
    platillos_encargados = []
    estado_encarga = 0
    lleganAlimentos = 0




    for _ in range(5):
        print("dia: ", _ + 1)
        personas = provavilidar(flojo_diario,  flujo_siario_prob)
        print("canditad de personas en el dia: ", personas)

        

        
        grupo_Porcent = provavilidar(grupo, grupo_prob)
        print(f"promedio de personas por grupo: {grupo_Porcent}")
        print(f"mesas totales por hora: {cantidad_de_mesas} ")
        mesas_ocupadas = personas / grupo_Porcent / horas_habiles
        print(f"mesas ocupadas por hora {mesas_ocupadas}")

        criticas = provavilidar(hora_critica, hora_critica_prob)
        if criticas == 1:
            print("ubo una hora critica")
            porcentaje_de_persnas = provavilidar(porcen_ora_critica, porcen_ora_critica_prob)
            print(f"llego el {porcentaje_de_persnas} de personas en el dia")
            print(f"la cantidad de personas fueron de {personas * (porcentaje_de_persnas / 100)}")

            if mesas_ocupadas > cantidad_de_mesas:
                print("saturaciones de mesas, perdida de clietes")
                print(f"la cantidad de personas atendidsas fue de {(mesas_ocupadas - cantidad_de_mesas) * grupo_Porcent}")
                personas = (mesas_ocupadas - cantidad_de_mesas) * grupo_Porcent


        if mesas_ocupadas > cantidad_de_mesas:
            print("saturaciones de mesas, perdida de clietes")
            personas = (mesas_ocupadas - cantidad_de_mesas) * grupo_Porcent


        platillos_por_persona = provavilidar(consumo, condumo_prob)
        print(f"el promedio de platos por persona fue de: {platillos_por_persona}")

        total_de_platillos = platillos_por_persona * personas
        print(f"fueron un total de {total_de_platillos} platillos")

        temp_cosina_promedio = provavilidar(tem_preparacion, tem_preparacion_prob)
        print(f"tiempo promedio de preparacion de los platillos: {temp_cosina_promedio}")

        horas_cosina_totales = temp_cosina_promedio * total_de_platillos
        print(f"Total de minutos cosinando: {horas_cosina_totales}")
        
        minutos_por_cosinero = horas_cosina_totales / cantidad_de_cosineros
        print(f"cada mesero devera de trabajar {minutos_por_cosinero} minutos al dia")

        distribucion_platillos = provavilidar(categorai_platillos, categorai_platillos_prob)
        print(f"distribucion de los platillos {distribucion_platillos}")

        for i in range(len(distribucion_platillos)):
            print(f"de la categoria {i + 1} son {total_de_platillos * (distribucion_platillos[i]/100)}")

        for i in range(len(distribucion_platillos)):
            print(f"restantes de platillos {i + 1} son {platillos_lista[i] - (total_de_platillos * (distribucion_platillos[i]/100))}")
            platillos_lista[i] = platillos_lista[i] - (total_de_platillos * (distribucion_platillos[i]/100)) 

        print("platillos restandes del dia: ", platillos_lista)


        ganancias = 0
        for i in range(len(distribucion_platillos)):
            print(f"platillos {i} =  {ganancias_por_platillo[i] * (total_de_platillos * (distribucion_platillos[i]/100))}")
            ganancias += ganancias_por_platillo[i] * total_de_platillos * (distribucion_platillos[i]/100)
        
        print("ganancais totales: ", ganancias)
        

        ganancias = 0
        for i in range(len(distribucion_platillos)):
            print(f"platillos {i} =  {ganancias_netas[i] * (total_de_platillos * (distribucion_platillos[i]/100))}")
            ganancias += ganancias_netas[i] * total_de_platillos * (distribucion_platillos[i]/100)
        
        print("ganancais netas: ", ganancias)
        

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
                for i in range(len(distribucion_platillos)):
                    platillos_encargados.append(cantidadDelStockmaxiom[i] - platillos_lista[i])

            
                print(f"se encargo mercancia y llega en {lleganAlimentos} dias")
                print(f"cantidad de alimentos encargados {platillos_encargados}")
                estado_encarga = 1
            else:
                print("ya se encargaron ingredientes o esta bien los que ya se teienen")

        
        if _ == lleganAlimentos:
            for i in range(len(platillos_encargados)):
                platillos_lista[i] += platillos_encargados[i]

            platillos_encargados = []
            print("Cosina abastesida")
            estado_encarga = 0

        print("platillos restandes del dia: ", platillos_lista)

        
# validaciones()


import customtkinter as ctk

class cocina:
    def __init__(self):
        self.ventana = ctk.CTk()
        self.ventana.title("COSINA - RESTAURANTE")
        
        try: self.ventana.state("zoomed")
        except: self.ventana.attributes("-zoomed", True)

        self.frame_scroll = ctk.CTkScrollableFrame(self.ventana)
        self.frame_scroll.pack(fill="both", expand=True, padx=20, pady=20)

        self.datosFijos = ctk.CTkFrame(
            self.frame_scroll, 
            width=384, 
            height=150, 
            fg_color="#404040" 
        )
        
        self.datosFijos.pack(pady=10, padx=10)


        ancho_fijo = 250
        alto_fijo = 40


        # primeras 2 fials y colupnas
        label1 = ctk.CTkLabel(self.datosFijos, text="Cantidad de cocineros:", font=("Arial", 16))
        label1.grid(row=0, column=0, padx=10, pady=5)

        self.CantidadDeCosineros = ctk.CTkEntry(self.datosFijos, font=("Arial", 16), width=ancho_fijo, height=alto_fijo)
        self.CantidadDeCosineros.grid(row=1, column=0, padx=10, pady=5)

        label2 = ctk.CTkLabel(self.datosFijos, text="Mesas disponibles:", font=("Arial", 16), width=ancho_fijo, height=alto_fijo)
        label2.grid(row=0, column=1, padx=10, pady=5)

        self.cantidadDeMesas = ctk.CTkEntry(self.datosFijos, font=("Arial", 16), width=ancho_fijo, height=alto_fijo)
        self.cantidadDeMesas.grid(row=1, column=1, padx=10, pady=5)

        label3 = ctk.CTkLabel(self.datosFijos, text="Horas laborales:", font=("Arial", 16), width=ancho_fijo, height=alto_fijo)
        label3.grid(row=0, column=2, padx=10, pady=5)

        self.Horaslaborales = ctk.CTkEntry(self.datosFijos, font=("Arial", 16), width=ancho_fijo, height=alto_fijo)
        self.Horaslaborales.grid(row=1, column=2, padx=10, pady=5)

        label4 = ctk.CTkLabel(self.datosFijos, text="Cantidad de personal extra:", font=("Arial", 16))
        label4.grid(row=0, column=3, padx=10, pady=5)

        self.personal = ctk.CTkEntry(self.datosFijos, font=("Arial", 16), width=ancho_fijo, height=alto_fijo)
        self.personal.grid(row=1, column=3, padx=10, pady=5)

        label5 = ctk.CTkLabel(self.datosFijos, text="sueldo de los cocineros por mes:", font=("Arial", 16))
        label5.grid(row=0, column=4, padx=10, pady=5)

        self.SueldoCosinero = ctk.CTkEntry(self.datosFijos, font=("Arial", 16), width=ancho_fijo, height=alto_fijo)
        self.SueldoCosinero.grid(row=1, column=4, padx=10, pady=5)

        label6 = ctk.CTkLabel(self.datosFijos, text="sueldo del resto del personal:", font=("Arial", 16))
        label6.grid(row=0, column=5, padx=10, pady=5)

        self.sueldoPersonal = ctk.CTkEntry(self.datosFijos, font=("Arial", 16), width=ancho_fijo, height=alto_fijo)
        self.sueldoPersonal.grid(row=1, column=5, padx=10, pady=5)

        label7 = ctk.CTkLabel(self.datosFijos, text="pago total de servicios mensuales:", font=("Arial", 16))
        label7.grid(row=0, column=6, padx=10, pady=5)

        self.pagoServicios = ctk.CTkEntry(self.datosFijos, font=("Arial", 16), width=ancho_fijo, height=alto_fijo)
        self.pagoServicios.grid(row=1, column=6, padx=10, pady=5)


        self.frame_scroll.grid_columnconfigure(0, weight=0)

        self.ventana.mainloop()

