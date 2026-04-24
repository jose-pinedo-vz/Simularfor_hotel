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



# otros datos
platillos_disponibles = ["normal", "caro", "exotico"]
platilllosEmpesamos = [400, 200, 40]

cantidadMinimaDeStock = [200, 70, 10]
cantidadDelStockmaxiom = [400, 200, 50]

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
        self.ventana = ctk.CTkToplevel()
        self.ventana.title("COSINA - RESTAURANTE")
        
        try: self.ventana.state("zoomed")
        except: self.ventana.attributes("-zoomed", True)

        self.frame_scroll = ctk.CTkScrollableFrame(self.ventana)
        self.frame_scroll.pack(fill="both", expand=True, padx=20, pady=10)


        color_contorno_azul = "#4281FF"

        self.datosFijos = ctk.CTkFrame(
            self.frame_scroll, 
            width=384, 
            height=150, 
            # fg_color="#4281FF" 
            border_width=2,
            border_color=color_contorno_azul
        )
        self.datosFijos.pack(pady=20, padx=20)

        ancho_fijo = 300
        alto_fijo = 60
        color_texto = "#FFFFff"


        # primeras 2 fials y colupnas
        label1 = ctk.CTkLabel(self.datosFijos, text="Cantidad de cocineros:", font=("Arial", 16), text_color=color_texto)
        label1.grid(row=0, column=0, padx=10, pady=5)

        self.CantidadDeCosineros = ctk.CTkEntry(self.datosFijos, font=("Arial", 16), width=ancho_fijo, height=alto_fijo)
        self.CantidadDeCosineros.grid(row=1, column=0, padx=10, pady=10)

        label2 = ctk.CTkLabel(self.datosFijos, text="Mesas disponibles:", font=("Arial", 16), width=ancho_fijo, height=alto_fijo, text_color=color_texto)
        label2.grid(row=0, column=1, padx=10, pady=5)

        self.cantidadDeMesas = ctk.CTkEntry(self.datosFijos, font=("Arial", 16), width=ancho_fijo, height=alto_fijo)
        self.cantidadDeMesas.grid(row=1, column=1, padx=10, pady=10)

        label3 = ctk.CTkLabel(self.datosFijos, text="Horas laborales:", font=("Arial", 16), width=ancho_fijo, height=alto_fijo, text_color=color_texto)
        label3.grid(row=0, column=2, padx=10, pady=5)

        self.Horaslaborales = ctk.CTkEntry(self.datosFijos, font=("Arial", 16), width=ancho_fijo, height=alto_fijo)
        self.Horaslaborales.grid(row=1, column=2, padx=10, pady=10)

        label4 = ctk.CTkLabel(self.datosFijos, text="Cantidad de personal extra:", font=("Arial", 16), text_color=color_texto)
        label4.grid(row=0, column=3, padx=10, pady=5)

        self.personal = ctk.CTkEntry(self.datosFijos, font=("Arial", 16), width=ancho_fijo, height=alto_fijo)
        self.personal.grid(row=1, column=3, padx=10, pady=10)

        label5 = ctk.CTkLabel(self.datosFijos, text="sueldo de los cocineros por mes:", font=("Arial", 16), text_color=color_texto)
        label5.grid(row=0, column=4, padx=10, pady=5)

        self.SueldoCosinero = ctk.CTkEntry(self.datosFijos, font=("Arial", 16), width=ancho_fijo, height=alto_fijo)
        self.SueldoCosinero.grid(row=1, column=4, padx=10, pady=10)

        label6 = ctk.CTkLabel(self.datosFijos, text="sueldo del resto del personal:", font=("Arial", 16), text_color=color_texto)
        label6.grid(row=0, column=5, padx=10, pady=5)

        self.sueldoPersonal = ctk.CTkEntry(self.datosFijos, font=("Arial", 16), width=ancho_fijo, height=alto_fijo)
        self.sueldoPersonal.grid(row=1, column=5, padx=10, pady=10)

        label7 = ctk.CTkLabel(self.datosFijos, text="pago total de servicios mensuales:", font=("Arial", 16), text_color=color_texto)
        label7.grid(row=0, column=6, padx=10, pady=5)

        self.pagoServicios = ctk.CTkEntry(self.datosFijos, font=("Arial", 16), width=ancho_fijo, height=alto_fijo)
        self.pagoServicios.grid(row=1, column=6, padx=10, pady=10)

        for i in range(6):
            ctk.CTkLabel(self.datosFijos, text="").grid(row=2, column=i)
        self.frame_scroll.grid_columnconfigure(0, weight=0)


        self.datosPlatillos = ctk.CTkFrame(
            self.frame_scroll, 
            width=384, 
            height=150, 
            # fg_color="#4281FF" 
            border_width=2,
            border_color=color_contorno_azul

        )
        self.datosPlatillos.pack(pady=20, padx=20)

        ancho_fijo = 300
        alto_fijo = 400
        color_texto = "#FFFFFF"

        label8 = ctk.CTkLabel(self.datosPlatillos, text="Platillos disponicles:", font=("Arial", 16), text_color=color_texto)
        label8.grid(row=0, column=0, padx=30, pady=20)

        self.nombreplatillos = ctk.CTkTextbox(self.datosPlatillos, font=("Arial", 16), width=ancho_fijo, height=alto_fijo)
        self.nombreplatillos.grid(row=1, column=0, padx=10, pady=5)

        label9 = ctk.CTkLabel(self.datosPlatillos, text="Distribucion de su venta:", font=("Arial", 16), text_color=color_texto)
        label9.grid(row=0, column=1, padx=10, pady=20)

        self.distribucionPlatillos = ctk.CTkTextbox(self.datosPlatillos, font=("Arial", 16), width=ancho_fijo, height=alto_fijo)
        self.distribucionPlatillos.grid(row=1, column=1, padx=10, pady=5)

        label10 = ctk.CTkLabel(self.datosPlatillos, text="Porcentaje de platillos", font=("Arial", 16), text_color=color_texto)
        label10.grid(row=0, column=2, padx=10, pady=20)

        self.Text_categorai_platillos = ctk.CTkTextbox(self.datosPlatillos, font=("Arial", 16), width=ancho_fijo, height=alto_fijo)
        self.Text_categorai_platillos.grid(row=1, column=2, padx=10, pady=5)

        label11 = ctk.CTkLabel(self.datosPlatillos, text="Prob de porcentaje", font=("Arial", 16), text_color=color_texto)
        label11.grid(row=0, column=3, padx=10, pady=5)

        self.Text_categorai_platillos_prob = ctk.CTkTextbox(self.datosPlatillos, font=("Arial", 16), width=ancho_fijo, height=alto_fijo)
        self.Text_categorai_platillos_prob.grid(row=1, column=3, padx=10, pady=5)

        label12 = ctk.CTkLabel(self.datosPlatillos, text="Cantidad inicial de Stock", font=("Arial", 16), text_color=color_texto)
        label12.grid(row=0, column=4, padx=10, pady=20)

        self.txt_cantidadStock = ctk.CTkTextbox(self.datosPlatillos, font=("Arial", 16), width=ancho_fijo, height=alto_fijo)
        self.txt_cantidadStock.grid(row=1, column=4, padx=10, pady=5)

        label12 = ctk.CTkLabel(self.datosPlatillos, text="Cantidad minima de Stock", font=("Arial", 16), text_color=color_texto)
        label12.grid(row=0, column=5, padx=10, pady=20)

        self.txt_cantidadStock_min = ctk.CTkTextbox(self.datosPlatillos, font=("Arial", 16), width=ancho_fijo, height=alto_fijo)
        self.txt_cantidadStock_min.grid(row=1, column=5, padx=10, pady=5)

        label13 = ctk.CTkLabel(self.datosPlatillos, text="Costo del platillo", font=("Arial", 16), text_color=color_texto)
        label13.grid(row=0, column=6, padx=10, pady=20)

        self.texr_costoDelPlatillo = ctk.CTkTextbox(self.datosPlatillos, font=("Arial", 16), width=ancho_fijo, height=alto_fijo)
        self.texr_costoDelPlatillo.grid(row=1, column=6, padx=10, pady=5)

        label14 = ctk.CTkLabel(self.datosPlatillos, text="Ganancia del paltillo", font=("Arial", 16), text_color=color_texto)
        label14.grid(row=0, column=7, padx=30, pady=20)

        self.texr_gananciaDelPlatillo = ctk.CTkTextbox(self.datosPlatillos, font=("Arial", 16), width=ancho_fijo, height=alto_fijo)
        self.texr_gananciaDelPlatillo.grid(row=1, column=7, padx=10, pady=5)

        for i in range(7):
            ctk.CTkLabel(self.datosPlatillos, text="").grid(row=2, column=i)

        self.datosBariables = ctk.CTkFrame(
            self.frame_scroll, 
            width=384, 
            height=150, 
            # fg_color="#4281FF" 
            border_width=2,
            border_color=color_contorno_azul

        )
        self.datosBariables.pack(pady=20, padx=20)


        label15 = ctk.CTkLabel(self.datosBariables, text="Flujo de personas por dia:", font=("Arial", 16), text_color=color_texto)
        label15.grid(row=0, column=0, padx=30, pady=20)

        self.text_FlujodePersonasPorDia = ctk.CTkTextbox(self.datosBariables, font=("Arial", 16), width=ancho_fijo, height=alto_fijo)
        self.text_FlujodePersonasPorDia.grid(row=1, column=0, padx=10, pady=5)

        label16 = ctk.CTkLabel(self.datosBariables, text="Prob del flujo de personas:", font=("Arial", 16), text_color=color_texto)
        label16.grid(row=0, column=1, padx=30, pady=20)

        self.text_FlujodePersonasPorDia_prob = ctk.CTkTextbox(self.datosBariables, font=("Arial", 16), width=ancho_fijo, height=alto_fijo)
        self.text_FlujodePersonasPorDia_prob.grid(row=1, column=1, padx=10, pady=5)

        label17 = ctk.CTkLabel(self.datosBariables, text="Promedio de grupo:", font=("Arial", 16), text_color=color_texto)
        label17.grid(row=0, column=2, padx=30, pady=20)

        self.text_TamaniodelGrupo = ctk.CTkTextbox(self.datosBariables, font=("Arial", 16), width=ancho_fijo, height=alto_fijo)
        self.text_TamaniodelGrupo.grid(row=1, column=2, padx=10, pady=5)

        label18 = ctk.CTkLabel(self.datosBariables, text="Prob de promedio de grupo:", font=("Arial", 16), text_color=color_texto)
        label18.grid(row=0, column=3, padx=30, pady=20)

        self.text_TamaniodelGrupoprob = ctk.CTkTextbox(self.datosBariables, font=("Arial", 16), width=ancho_fijo, height=alto_fijo)
        self.text_TamaniodelGrupoprob.grid(row=1, column=3, padx=10, pady=5)

        label19 = ctk.CTkLabel(self.datosBariables, text="Preparacion platillo:", font=("Arial", 16), text_color=color_texto)
        label19.grid(row=0, column=4, padx=30, pady=20)

        self.tex_preapracion_platillo = ctk.CTkTextbox(self.datosBariables, font=("Arial", 16), width=ancho_fijo, height=alto_fijo)
        self.tex_preapracion_platillo.grid(row=1, column=4, padx=10, pady=5)

        label20 = ctk.CTkLabel(self.datosBariables, text="prob de preparacion platillo:", font=("Arial", 16), text_color=color_texto)
        label20.grid(row=0, column=5, padx=30, pady=20)

        self.tex_preapracion_platillo_prob = ctk.CTkTextbox(self.datosBariables, font=("Arial", 16), width=ancho_fijo, height=alto_fijo)
        self.tex_preapracion_platillo_prob.grid(row=1, column=5, padx=10, pady=5)

        label21 = ctk.CTkLabel(self.datosBariables, text="Consumo por persona:", font=("Arial", 16), text_color=color_texto)
        label21.grid(row=2, column=0, padx=30, pady=20)

        self.text_consumoPorPersona = ctk.CTkTextbox(self.datosBariables, font=("Arial", 16), width=ancho_fijo, height=alto_fijo)
        self.text_consumoPorPersona.grid(row=3, column=0, padx=10, pady=5)

        label22 = ctk.CTkLabel(self.datosBariables, text="prob consumo:", font=("Arial", 16), text_color=color_texto)
        label22.grid(row=2, column=1, padx=30, pady=20)

        self.text_comsumoPorPersona_prob = ctk.CTkTextbox(self.datosBariables, font=("Arial", 16), width=ancho_fijo, height=alto_fijo)
        self.text_comsumoPorPersona_prob.grid(row=3, column=1, padx=10, pady=5)

        label23 = ctk.CTkLabel(self.datosBariables, text="Suministro:", font=("Arial", 16), text_color=color_texto)
        label23.grid(row=2, column=2, padx=30, pady=20)

        self.text_suministro = ctk.CTkTextbox(self.datosBariables, font=("Arial", 16), width=ancho_fijo, height=alto_fijo)
        self.text_suministro.grid(row=3, column=2, padx=10, pady=5)

        label24 = ctk.CTkLabel(self.datosBariables, text="Prob suministro:", font=("Arial", 16), text_color=color_texto)
        label24.grid(row=2, column=3, padx=30, pady=20)

        self.text_suministroProb = ctk.CTkTextbox(self.datosBariables, font=("Arial", 16), width=ancho_fijo, height=alto_fijo)
        self.text_suministroProb.grid(row=3,column=3, padx=10, pady=5)

        label25 = ctk.CTkLabel(self.datosBariables, text="Evento de RH:", font=("Arial", 16), text_color=color_texto)
        label25.grid(row=2, column=4, padx=30, pady=20)

        self.text_eventoRh = ctk.CTkTextbox(self.datosBariables, font=("Arial", 16), width=ancho_fijo, height=alto_fijo)
        self.text_eventoRh.grid(row=3, column=4, padx=10, pady=5)

        label125 = ctk.CTkLabel(self.datosBariables, text="Prob evento de RH:", font=("Arial", 16), text_color=color_texto)
        label125.grid(row=2, column=5, padx=30, pady=20)

        self.text_eventoRh_prob = ctk.CTkTextbox(self.datosBariables, font=("Arial", 16), width=ancho_fijo, height=alto_fijo)
        self.text_eventoRh_prob.grid(row=3, column=5, padx=10, pady=5)


        label26 = ctk.CTkLabel(self.datosBariables, text="Evento de aleatorios:", font=("Arial", 16), text_color=color_texto)
        label26.grid(row=4, column=0, padx=30, pady=20)

        self.text_eventoAle = ctk.CTkTextbox(self.datosBariables, font=("Arial", 16), width=ancho_fijo, height=alto_fijo)
        self.text_eventoAle.grid(row=5, column=0, padx=10, pady=5)

        label126 = ctk.CTkLabel(self.datosBariables, text="prob evento de aleatorios:", font=("Arial", 16), text_color=color_texto)
        label126.grid(row=4, column=1, padx=30, pady=20)

        self.text_eventoAle_prob = ctk.CTkTextbox(self.datosBariables, font=("Arial", 16), width=ancho_fijo, height=alto_fijo)
        self.text_eventoAle_prob.grid(row=5, column=1, padx=10, pady=5)
        


        label28 = ctk.CTkLabel(self.datosBariables, text="Horas criticas:", font=("Arial", 16), text_color=color_texto)
        label28.grid(row=4, column=2, padx=30, pady=20)

        self.textHorasCriticas = ctk.CTkTextbox(self.datosBariables, font=("Arial", 16), width=ancho_fijo, height=alto_fijo)
        self.textHorasCriticas.grid(row=5, column=2, padx=10, pady=5)

        label29 = ctk.CTkLabel(self.datosBariables, text="prob horas criticas:", font=("Arial", 16), text_color=color_texto)
        label29.grid(row=4, column=3, padx=30, pady=20)

        self.textHorasCriticasprob = ctk.CTkTextbox(self.datosBariables, font=("Arial", 16), width=ancho_fijo, height=alto_fijo)
        self.textHorasCriticasprob.grid(row=5, column=3, padx=10, pady=5)


        ancho_fijo = 300
        alto_fijo = 100
        color_texto = "#FFBF42"
        textaso = "#A442FF"

        self.Botonsitos = ctk.CTkFrame(
            self.frame_scroll, 
            width=384, 
            height=150, 
            # fg_color="#4281FF" 
            border_width=2,
            border_color=color_contorno_azul

        )
        self.Botonsitos.pack(pady=20, padx=20)

        self.cargar = ctk.CTkButton(self.Botonsitos, text="Cargar elementos", width=ancho_fijo, height=alto_fijo, fg_color=color_texto, text_color=textaso,
                                    command=lambda: self.cargarElementosEninterface())
        self.cargar.grid(row=0, column=0, padx=40, pady=40)

        self.Baciar = ctk.CTkButton(self.Botonsitos, text="Baciar", width=ancho_fijo, height=alto_fijo, fg_color=color_texto, text_color=textaso,
                                    command=lambda: self.Bacias())
        self.Baciar.grid(row=0, column=1, padx=40, pady=40)

        self.bj = ctk.CTkButton(self.Botonsitos, text="balores bajos", width=ancho_fijo, height=alto_fijo, fg_color=color_texto, text_color=textaso)
        self.bj.grid(row=0, column=2, padx=40, pady=40)

        self.at = ctk.CTkButton(self.Botonsitos, text="balores altos", width=ancho_fijo, height=alto_fijo, fg_color=color_texto, text_color=textaso)
        self.at.grid(row=0, column=3, padx=40, pady=40)

        self.md = ctk.CTkButton(self.Botonsitos, text="balores medios", width=ancho_fijo, height=alto_fijo, fg_color=color_texto, text_color=textaso,
                                command=lambda: self.cargarValoresmedios())
        self.md.grid(row=0, column=4, padx=40, pady=40)


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


        # pendientes
        texto_crudo = self.tex_preapracion_platillo_prob.get("1.0", "end")
        tem_preparacion_prob = [int(x) for x in texto_crudo.split()]

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

        cantidad_de_mesas = int(self.cantidadDeMesas.get())
        cantidad_de_cosineros = int(self.CantidadDeCosineros.get())
        sueldo_cosineros = float(self.SueldoCosinero.get())
        horas_habiles = int(self.Horaslaborales.get())
        personal = int(self.personal.get())
        sueldo_personal = float(self.sueldoPersonal.get())

        pago_servicios = float(self.pagoServicios.get())

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

        self.cargarElementosEninterface()



        self.ventana.mainloop()

