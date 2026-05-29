import customtkinter as ctk
from CTkTable import CTkTable
from tkinter import messagebox
import random
from GeneraRandom import aleatorio

COLOR_FONDO = "#5D4037"
COLOR_TEXTO = "#FFFFFF"
COLOR_CONTORNO = "#4281FF"

class Marketing:
    def __init__(self):
        self.ventana=ctk.CTk()
        self.ventana.title("Área de Habitaciones")
        self.ventana.configure(fg_color=COLOR_FONDO)
        ancho=self.ventana.winfo_screenwidth()
        alto=self.ventana.winfo_screenheight()
        self.ventana.geometry(f"{ancho}x{alto}+0+0")

        # DATOS
        self.datos_vistas=[[20, 0.30],
                          [40, 0.50],
                          [60, 0.20]]

        self.datos_conversion=[[10, 0.30],
                               [20, 0.20],
                               [30, 0.50]]

        self.datos_campaña=[["Facebook", 0.50],
                            ["Google Ads", 0.30],
                            ["Orgánico", 0.20]]

        self.datos_costos=[[100, 0.30],
                            [300, 0.50],
                            [500, 0.20]]
        
        self.datos_cancelaciones=[[0, 0.50],
                                  [1, 0.30],
                                  [2, 0.20]]
        
        self.datos_habitacion=[["Individual", 0.50],
                               ["Doble", 0.35],
                               ["Suite", 0.15]]
        
        self.datos_estancia=[[1, 0.40],
                             [2, 0.35],
                             [3, 0.25]]

        self.reiniciar_vistas=False
        self.reiniciar_conversion=False
        self.reiniciar_campaña=False
        self.reiniciar_costos=False
        self.reiniciar_cancelaciones=False
        self.reiniciar_habitacion=False
        self.reiniciar_estancia=False

        # SCROLL
        self.frame_scroll=ctk.CTkScrollableFrame(self.ventana)
        self.frame_scroll.pack(fill="both", expand=True, padx=20, pady=20)

        # TITULO
        titulo=ctk.CTkLabel(self.frame_scroll, text="Simulación de marketing", text_color=COLOR_TEXTO, font=("Arial", 28, "bold", "italic"))
        titulo.pack(pady=20)

        # FRAME DATOS
        self.frame_datos=ctk.CTkFrame(self.frame_scroll, border_width=2, border_color=COLOR_CONTORNO)
        self.frame_datos.pack(fill="x", padx=20, pady=20)

        ancho_entry=180
        alto_entry=40

        ctk.CTkLabel(self.frame_datos, text="Presupuesto:", text_color=COLOR_TEXTO, font=("Arial", 16)).grid(row=0, column=0, padx=20, pady=(20, 5))
        self.entry_presupuesto=ctk.CTkEntry(self.frame_datos, width=ancho_entry, height=alto_entry)
        self.entry_presupuesto.grid(row=1, column=0, padx=20, pady=(0, 20))
        self.entry_presupuesto.insert(0, "50000")

        ctk.CTkLabel(self.frame_datos, text="Campañas por mes:", text_color=COLOR_TEXTO, font=("Arial", 16)).grid(row=0, column=1, padx=20, pady=(20, 5))
        self.entry_campañas=ctk.CTkEntry(self.frame_datos, width=ancho_entry, height=alto_entry)
        self.entry_campañas.grid(row=1, column=1, padx=20, pady=(0, 20))
        self.entry_campañas.insert(0, "5")

        ctk.CTkLabel(self.frame_datos, text="Precio promedio:", text_color=COLOR_TEXTO, font=("Arial", 16)).grid(row=0, column=2, padx=20, pady=(20, 5))
        self.entry_precio=ctk.CTkEntry(self.frame_datos, width=ancho_entry, height=alto_entry)
        self.entry_precio.grid(row=1, column=2, padx=20, pady=(0, 20))
        self.entry_precio.insert(0, "500")

        ctk.CTkLabel(self.frame_datos, text="Personal disponible:", text_color=COLOR_TEXTO, font=("Arial", 16)).grid(row=0, column=3, padx=20, pady=(20, 5))
        self.entry_personal=ctk.CTkEntry(self.frame_datos, width=ancho_entry, height=alto_entry)
        self.entry_personal.grid(row=1, column=3, padx=20, pady=(0, 20))
        self.entry_personal.insert(0, "6")

        ctk.CTkLabel(self.frame_datos, text="Días a simular:", text_color=COLOR_TEXTO, font=("Arial", 16)).grid(row=2, column=0, padx=20, pady=(10, 5))
        self.entry_dias=ctk.CTkEntry(self.frame_datos, width=ancho_entry, height=alto_entry)
        self.entry_dias.grid(row=3, column=0, padx=20, pady=(0, 20))
        self.entry_dias.insert(0, "10")

        ctk.CTkLabel(self.frame_datos, text="Costo personal por dia:", text_color=COLOR_TEXTO, font=("Arial", 16)).grid(row=2, column=1, padx=20, pady=(10, 5))
        self.entry_costo_empleado=ctk.CTkEntry(self.frame_datos, width=ancho_entry, height=alto_entry)
        self.entry_costo_empleado.grid(row=3, column=1, padx=20, pady=(0, 20))
        self.entry_costo_empleado.insert(0, "300")

        ctk.CTkLabel(self.frame_datos, text="Costo campaña por dia:", text_color=COLOR_TEXTO, font=("Arial", 16)).grid(row=2, column=2, padx=20, pady=(10, 5))
        self.entry_costo_campaña=ctk.CTkEntry(self.frame_datos, width=ancho_entry, height=alto_entry)
        self.entry_costo_campaña.grid(row=3, column=2, padx=20, pady=(0, 20))
        self.entry_costo_campaña.insert(0, "150")

                # HABITACIONES
        ctk.CTkLabel(self.frame_datos, text="Habitaciones Individuales:", text_color=COLOR_TEXTO, font=("Arial", 16)).grid(row=4, column=0, padx=20, pady=(10, 5))
        self.entry_individual=ctk.CTkEntry(self.frame_datos, width=ancho_entry, height=alto_entry)
        self.entry_individual.grid(row=5, column=0, padx=20, pady=(0, 20))
        self.entry_individual.insert(0, "10")

        ctk.CTkLabel(self.frame_datos, text="Habitaciones Dobles:", text_color=COLOR_TEXTO, font=("Arial", 16)).grid(row=4, column=1, padx=20, pady=(10, 5))
        self.entry_doble=ctk.CTkEntry(self.frame_datos, width=ancho_entry, height=alto_entry)
        self.entry_doble.grid(row=5, column=1, padx=20, pady=(0, 20))
        self.entry_doble.insert(0, "8")

        ctk.CTkLabel(self.frame_datos, text="Habitaciones Suites:", text_color=COLOR_TEXTO, font=("Arial", 16)).grid(row=4, column=2, padx=20, pady=(10, 5))
        self.entry_suite=ctk.CTkEntry(self.frame_datos, width=ancho_entry, height=alto_entry)
        self.entry_suite.grid(row=5, column=2, padx=20, pady=(0, 20))
        self.entry_suite.insert(0, "4")

        self.btn_simular=ctk.CTkButton(self.frame_scroll, text="Simular", width=ancho_entry, height=alto_entry, fg_color="#D6C49E", text_color="#000000", command=self.simular)
        self.btn_simular.pack(pady=20)

        # KPIS
        self.frame_kpis=ctk.CTkFrame(self.frame_scroll, border_width=2, border_color=COLOR_CONTORNO)
        self.frame_kpis.pack(fill="x", padx=20, pady=20)

        self.lbl_vistas=ctk.CTkLabel(self.frame_kpis, text="Vistas: 0", text_color="#00FF99", font=("Arial", 18, "bold"))
        self.lbl_vistas.grid(row=0, column=0, padx=40, pady=30)

        self.lbl_reservas=ctk.CTkLabel(self.frame_kpis, text="Posibles reservaciones: 0", text_color="#FFD700", font=("Arial", 18, "bold"))
        self.lbl_reservas.grid(row=0, column=1, padx=40, pady=30)

        self.lbl_ingresos=ctk.CTkLabel(self.frame_kpis, text="Posibles ingresos: $0", text_color="#00BFFF", font=("Arial", 18, "bold"))
        self.lbl_ingresos.grid(row=0, column=2, padx=40, pady=30)

        self.lbl_ganancia=ctk.CTkLabel(self.frame_kpis, text="Posibles ganancias: $0", text_color="#FF6666", font=("Arial", 18, "bold"))
        self.lbl_ganancia.grid(row=0, column=3, padx=40, pady=30)

        # BOTONES
        self.frame_botones=ctk.CTkFrame(self.frame_scroll, border_width=2, border_color=COLOR_CONTORNO)
        self.frame_botones.pack(fill="x", padx=20, pady=20)

        botones=[("Limpiar", self.limpiar),
                 ("Sistema estresado", self.sistema_estresado),
                 ("Sistema equilibrado", self.sistema_equilibrado),
                 ("Siatema con ocio", self.sistema_oseo)]

        for i, (texto, comando) in enumerate(botones):
            boton=ctk.CTkButton(self.frame_botones, text=texto, width=180, height=40, fg_color="#FFBF42", text_color="#000000", command=comando)
            boton.grid(row=0, column=i, padx=20, pady=30)

        # FRAME PROBABILIDADES
        self.frame_probabilidades=ctk.CTkFrame(self.frame_scroll, border_width=2, border_color=COLOR_CONTORNO)
        self.frame_probabilidades.pack(fill="x", padx=20, pady=20)

        titulo_prob=ctk.CTkLabel(self.frame_probabilidades, text="TABLAS DE PROBABILIDAD", text_color=COLOR_TEXTO, font=("Arial", 22, "bold"))
        titulo_prob.pack(pady=20)

        self.contenedor=ctk.CTkFrame(self.frame_probabilidades, fg_color="transparent")
        self.contenedor.pack(padx=20, pady=20)

        self.crear_tabla("Generación vistas", "Vistas", self.datos_vistas, 0)

        self.crear_tabla("Tabla de Conversión",  "Conversión", self.datos_conversion, 1)

        self.crear_tabla("Tipo de campaña", "Campaña", self.datos_campaña, 2)

        self.crear_tabla("Costo marketing", "Costo", self.datos_costos, 3)

        self.crear_tabla("Tipo de Habitación", "Habitación", self.datos_habitacion, 4)

        self.crear_tabla("Cancelaciones", "Cancelaciones", self.datos_cancelaciones, 5)
        
        self.crear_tabla("Estancia", "Estancia", self.datos_estancia, 6)

        # RESULTADOS
        self.frame_resultados=ctk.CTkFrame(self.frame_scroll, border_width=2, border_color=COLOR_CONTORNO)
        self.frame_resultados.pack(fill="both", expand=True, padx=20, pady=20)

        titulo_resultados=ctk.CTkLabel(self.frame_resultados, text="RESULTADOS DE LA SIMULACIÓN", text_color=COLOR_TEXTO, font=("Arial", 20, "bold"))
        titulo_resultados.pack(pady=20)

        self.ventana.mainloop()

    # LIMPIAR
    def limpiar(self):
        self.entry_presupuesto.delete(0, "end")
        self.entry_campañas.delete(0, "end")
        self.entry_precio.delete(0, "end")
        self.entry_personal.delete(0, "end")
        self.entry_dias.delete(0, "end")

        self.lbl_vistas.configure(text="Vistas: 0")
        self.lbl_reservas.configure(text="Posibles reservas: 0")
        self.lbl_ingresos.configure(text="Posibles ingresos: $0")
        self.lbl_ganancia.configure(text="Posibles ganancias: $0")

        for widget in self.frame_resultados.winfo_children():
            widget.destroy()

        messagebox.showinfo("Correcto", "Datos limpiados")

    # VALORES BAJOS
    def sistema_estresado(self):
        self.modo_sistema = "estresado"

        self.entry_presupuesto.delete(0, "end")
        self.entry_presupuesto.insert(0, "15000")

        self.entry_campañas.delete(0, "end")
        self.entry_campañas.insert(0, "2")

        self.entry_precio.delete(0, "end")
        self.entry_precio.insert(0, "300")

        self.entry_personal.delete(0, "end")
        self.entry_personal.insert(0, "2")

        self.entry_dias.delete(0, "end")
        self.entry_dias.insert(0, "10")

        self.datos_vistas = [[30, 0.20], [60, 0.50], [100, 0.30]]
        self.datos_conversion = [[5, 0.30], [15, 0.50], [25, 0.20]]

    # VALORES MEDIOS
    def sistema_equilibrado(self):
        self.modo_sistema = "equilibrado"

        self.entry_presupuesto.delete(0, "end")
        self.entry_presupuesto.insert(0, "50000")

        self.entry_campañas.delete(0, "end")
        self.entry_campañas.insert(0, "5")

        self.entry_precio.delete(0, "end")
        self.entry_precio.insert(0, "500")

        self.entry_personal.delete(0, "end")
        self.entry_personal.insert(0, "6")

        self.entry_dias.delete(0, "end")
        self.entry_dias.insert(0, "20")

        self.datos_vistas = [[20, 0.30], [40, 0.50], [60, 0.20]]
        self.datos_conversion = [[10, 0.30], [20, 0.50], [30, 0.20]]

    # VALORES ALTOS
    def sistema_oseo(self):
        self.modo_sistema = "ocio"

        self.entry_presupuesto.delete(0, "end")
        self.entry_presupuesto.insert(0, "90000")

        self.entry_campañas.delete(0, "end")
        self.entry_campañas.insert(0, "10")

        self.entry_precio.delete(0, "end")
        self.entry_precio.insert(0, "900")

        self.entry_personal.delete(0, "end")
        self.entry_personal.insert(0, "15")

        self.entry_dias.delete(0, "end")
        self.entry_dias.insert(0, "30")

        self.datos_vistas = [[10, 0.50], [20, 0.30], [30, 0.20]]
        self.datos_conversion = [[5, 0.50], [10, 0.30], [15, 0.20]]

    # CREAR TABLAS
    def crear_tabla(self, titulo, encabezado, datos, fila):
        frame=ctk.CTkFrame(self.contenedor)
        frame.grid(row=fila, column=0, padx=20, pady=20)

        ctk.CTkLabel(frame, text=titulo, text_color=COLOR_TEXTO, font=("Arial", 16, "bold")).pack(pady=10)

        entrada1=ctk.CTkEntry(frame, width=150, placeholder_text=encabezado)
        entrada1.pack(pady=5)

        entrada2=ctk.CTkEntry(frame, width=150, placeholder_text="Probabilidad")
        entrada2.pack(pady=5)

        boton=ctk.CTkButton(frame, text="Agregar", command=lambda: self.agregar_dato(entrada1, entrada2, datos, encabezado, frame))
        boton.pack(pady=10)

        tabla=CTkTable(frame, values=self.calcular_tabla(datos, encabezado))
        tabla.pack(padx=10, pady=10)

        if encabezado=="Vistas":
            self.tabla_vistas=tabla

        elif encabezado=="Conversión":
            self.tabla_conversion=tabla

        elif encabezado=="Campaña":
            self.tabla_campaña=tabla

        elif encabezado=="Costo":
            self.tabla_costos=tabla

        elif encabezado=="Habitación":
            self.tabla_habitacion=tabla

        elif encabezado=="Cancelaciones":
            self.tabla_cancelaciones=tabla

        elif encabezado=="Estancia":
            self.tabla_estancia=tabla

    # CALCULAR TABLA
    def calcular_tabla(self, datos, encabezado):
        tabla=[[encabezado, "Probabilidad", "Prob. Acumulada", "Rango"]]

        acumulada=0

        for i, fila in enumerate(datos):
            valor=fila[0]
            prob=fila[1]

            inicio=acumulada
            acumulada=acumulada + prob

            if i==0:
                rango=(f"0.0000 - {acumulada:.4f}")
            else:
                rango=(f"{inicio + 0.0001:.4f} - {acumulada:.4f}")

            tabla.append([valor, f"{prob:.4f}", f"{acumulada:.4f}", rango])

        return tabla

    # AGREGAR DATOS
    def agregar_dato(self, entrada1, entrada2, datos, encabezado, frame):
        try:
            valor=entrada1.get().strip()
            prob=entrada2.get().strip()

            if valor=="" or prob=="":
                messagebox.showerror("Error", "Todos los campos son obligatorios")
                return

            prob=float(prob)

            if prob<=0 or prob>1:
                messagebox.showerror("Error", "Probabilidad inválida")
                return

            try:
                valor=int(valor)
            except:
                pass

            suma=0
            for fila in datos:
                suma=suma + fila[1]

            suma=round(suma, 4)

            # ADVERTENCIA ANTES DE REINICIAR TABLA
            if suma==1:
                if encabezado=="Vistas":
                    if self.reiniciar_vistas==False:
                        messagebox.showwarning("Advertencia", "La tabla ya suma 1 Si agregas otro dato se reiniciará")
                        self.reiniciar_vistas=True
                        return
                    else:
                        datos.clear()
                        self.reiniciar_vistas=False

                elif encabezado=="Conversión":
                    if self.reiniciar_conversion==False:
                        messagebox.showwarning("Advertencia", "La tabla ya suma 1 Si agregas otro dato se reiniciará")
                        self.reiniciar_conversion=True
                        return
                    else:
                        datos.clear()
                        self.reiniciar_conversion=False

                elif encabezado=="Campaña":
                    if self.reiniciar_campaña==False:
                        messagebox.showwarning("Advertencia", "La tabla ya suma 1 Si agregas otro dato se reiniciará")
                        self.reiniciar_campaña=True
                        return
                    else:
                        datos.clear()
                        self.reiniciar_campaña=False

                elif encabezado=="Costo":
                    if self.reiniciar_costos==False:
                        messagebox.showwarning("Advertencia", "La tabla ya suma 1 Si agregas otro dato se reiniciará")
                        self.reiniciar_costos=True
                        return
                    else:
                        datos.clear()
                        self.reiniciar_costos=False

                elif encabezado=="Habitacion":
                    if self.reiniciar_habitacion==False:
                        messagebox.showwarning("Advertencia", "La tabla ya suma 1 Si agregas otro dato se reiniciará")
                        self.reiniciar_habitacion=True
                        return
                    else:
                        datos.clear()
                        self.reiniciar_habitacion=False

                elif encabezado=="Cancelaciones":
                    if self.reiniciar_cancelaciones==False:
                        messagebox.showwarning("Advertencia", "La tabla ya suma 1 Si agregas otro dato se reiniciará")
                        self.reiniciar_cancelaciones=True
                        return
                    else:
                        datos.clear()
                        self.reiniciar_cancelaciones=False

                elif encabezado=="Estancia":
                    if self.reiniciar_estancia==False:
                        messagebox.showwarning("Advertencia", "La tabla ya suma 1 Si agregas otro dato se reiniciará")
                        self.reiniciar_estancia=True
                        return
                    else:
                        datos.clear()
                        self.reiniciar_estancia=False

            datos.append([valor, prob])

            nueva_suma=0
            for fila in datos:
                nueva_suma=nueva_suma + fila[1]

            nueva_suma=round(nueva_suma, 4)

            if nueva_suma>1:
                datos.pop()
                messagebox.showerror("Error", "La suma no puede superar 1")
                return

            try:
                datos.sort()
            except:
                pass

            if encabezado=="Vistas":
                self.tabla_vistas.destroy()

            elif encabezado=="Conversión":
                self.tabla_conversion.destroy()

            elif encabezado=="Campaña":
                self.tabla_campaña.destroy()

            elif encabezado=="Costo":
                self.tabla_costos.destroy()

            elif encabezado=="Habitación":
                self.tabla_habitacion.destroy()

            elif encabezado=="Cancelaciones":
                self.tabla_cancelaciones.destroy()

            elif encabezado=="Estancia":
                self.tabla_estancia.destroy()

            nueva_tabla=CTkTable(frame, values=self.calcular_tabla(datos, encabezado))
            nueva_tabla.pack(padx=10, pady=10)

            if encabezado=="Vistas":
                self.tabla_vistas=nueva_tabla

            elif encabezado=="Conversión":
                self.tabla_conversion=nueva_tabla

            elif encabezado=="Campaña":
                self.tabla_campaña=nueva_tabla

            elif encabezado=="Costo":
                self.tabla_costos=nueva_tabla

            elif encabezado=="Habitación":
                self.tabla_habitacion=nueva_tabla

            elif encabezado=="Cancelaciones":
                self.tabla_cancelaciones=nueva_tabla

            elif encabezado=="Estancia":
                self.tabla_estancia=nueva_tabla

            entrada1.delete(0, "end")
            entrada2.delete(0, "end")

        except:
            messagebox.showerror("Error", "No se pudo agregar")

    # BUSCAR RESULTADO
    def buscar_resultado(self, numero, datos):
        acumulada=0
        for valor, probabilidad in datos:
            acumulada=acumulada + probabilidad
            if numero<=acumulada:
                return valor

    def validar_tablas(self):
        suma_vistas=0
        for fila in self.datos_vistas:
            suma_vistas=suma_vistas + fila[1]

        suma_conversion=0
        for fila in self.datos_conversion:
            suma_conversion=suma_conversion + fila[1]

        suma_campana=0
        for fila in self.datos_campaña:
            suma_campana=suma_campana + fila[1]

        suma_costos=0
        for fila in self.datos_costos:
            suma_costos=suma_costos + fila[1]

        suma_cancelaciones=0
        for fila in self.datos_cancelaciones:
            suma_cancelaciones=suma_cancelaciones + fila[1]

        suma_habitacion = 0
        for fila in self.datos_habitacion:
            suma_habitacion += fila[1]

        suma_vistas=round(suma_vistas, 4)
        suma_conversion=round(suma_conversion, 4)
        suma_campana=round(suma_campana, 4)
        suma_costos=round(suma_costos, 4)
        suma_cancelaciones=round(suma_cancelaciones, 4)
        suma_habitacion = round(suma_habitacion, 4)

        if suma_vistas!=1:
            messagebox.showerror("Error", "La tabla de leads debe sumar 1")
            return False

        if suma_conversion!=1:
            messagebox.showerror("Error", "La tabla de conversión debe sumar 1")
            return False

        if suma_campana!=1:
            messagebox.showerror("Error", "La tabla de campañas debe sumar 1")
            return False

        if suma_costos!=1:
            messagebox.showerror("Error", "La tabla de costos debe sumar 1")
            return False

        if suma_cancelaciones!=1:
            messagebox.showerror("Error", "La tabla de cancelaciones debe sumar 1")
            return False
        
        if suma_habitacion != 1:
            messagebox.showerror("Error", "La tabla de habitaciones debe sumar 1")
            return False

        return True

    def obtener_temporada(self, dia):
        ciclo=dia % 30
        if ciclo==0:
            ciclo=30

        #TEMPORADA BAJA
        if ciclo>=1 and ciclo<=10:
            return "Baja", {"factor_vistas": 0.7, 
                            "factor_precio": 0.8}

        # TEMPORADA MEDIA
        elif ciclo>=11 and ciclo<=20:
            return "Media", {"factor_vistas": 1.0,
                             "factor_precio": 1.0}

        # TEMPORADA ALTA
        else:
            return "Alta", {"factor_vistas": 1.5,
                            "factor_precio": 1.4}

    # SIMULACIÓN
    def simular(self):
        try:
            if self.validar_tablas()==False:
                return

            presupuesto=float(self.entry_presupuesto.get())
            campañas=int(self.entry_campañas.get())
            precio=float(self.entry_precio.get())
            personal=int(self.entry_personal.get())
            dias=int(self.entry_dias.get())
            costo_empleado=float(self.entry_costo_empleado.get())
            costo_campaña=float(self.entry_costo_campaña.get())

            individuales=int(self.entry_individual.get())
            dobles=int(self.entry_doble.get())
            suites=int(self.entry_suite.get())

            self.habitaciones={"Individual": individuales,
                               "Doble": dobles,
                               "Suite": suites}

            self.disponibles={"Individual": individuales,
                              "Doble": dobles,
                              "Suite": suites}

            self.reservas_activas=[]

            if presupuesto<=0 or campañas<=0 or precio<=0 or personal<=0 or dias<=0 or costo_empleado<=0 or costo_campaña<=0:
                messagebox.showerror("Error", "Todos los valores deben ser mayores a 0")
                return

            tabla_simulacion=[["Día", "Alea vistas", "Vistas", "Temporada", "Alea Conversión", "% Conversión", "Reservas", "Cancelaciones", "Reservas reales", "alea Canal", "Canal", "Precio", "Ingresos", "Alea Costo", "Costo Marketing", "Ganancia"]]

            tabla_resumen=[["Indicador", "Valor"]]

            tabla_comportamiento=[["Día", "Temporada", "Vistas", "Reservas", "Ingresos", "Costos", "Ganancia"]]

            tabla_acumulada=[["Día", "Ganancia acumulada"]]

            tabla_dias=[["Día", "Reservas", "Ingresos", "Ganancia"]]

            vistas_totales=0
            reservas_totales=0
            ingresos_totales=0
            costos_totales=0
            ganancia_total=0
            conversion_total=0

            acumulada=0

            indice=1

            dias_rentables=[]
            dias_debiles=[]

            self.reservas_por_dia={}
            self.tabla_dias=None

            self.precios_por_dia = {}

            for dia in range(1, dias + 1):
                temporada, factores=self.obtener_temporada(dia)

                alea_campana=aleatorio(indice)
                indice=indice + 1
                campana=self.buscar_resultado(alea_campana, self.datos_campaña)
                if campana == "Facebook":
                    factor_campana = 1.2
                    factor_conversion = 1.1
                elif campana == "Google Ads":
                    factor_campana = 1.0
                    factor_conversion = 1.0
                else:
                    factor_campana = 0.8
                    factor_conversion = 0.9

                alea_vistas=aleatorio(indice)
                indice=indice + 1
                vistas=self.buscar_resultado(alea_vistas, self.datos_vistas)
                vistas = int(vistas * factores["factor_vistas"] * factor_campana)

                alea_conversion=aleatorio(indice)
                indice=indice + 1
                conversion=self.buscar_resultado(alea_conversion, self.datos_conversion) * factor_conversion

                alea_costo=aleatorio(indice)
                indice=indice + 1
                costo_marketing=self.buscar_resultado(alea_costo, self.datos_costos)

                reservas=int(vistas * (conversion / 100))

                alea_cancelacion=aleatorio(indice)
                indice=indice + 1
                tasa_cancelacion=self.buscar_resultado(alea_cancelacion, self.datos_cancelaciones) / 100
                cancelaciones=int(reservas * tasa_cancelacion)

                reservas=reservas - cancelaciones

                reservas_reales=0
                reservas_dia=[]
                for i in range(reservas):
                    alea_habitacion=aleatorio(indice)
                    indice+=1
                    alea_estancia=aleatorio(indice)
                    indice+=1

                    tipo=self.buscar_resultado(alea_habitacion, self.datos_habitacion)
                    estancia=self.buscar_resultado(alea_estancia, self.datos_estancia)
                    if self.disponibles[tipo]>0:
                        self.disponibles[tipo]-=1
                        reservas_reales+=1
                        reservas_dia.append({"Aleatorio habitacion": alea_habitacion, "Tipo": tipo, "Aleatorio estancia": alea_estancia, "Estancia": estancia})

                self.reservas_por_dia[dia]=reservas_dia

                total=sum(self.habitaciones.values())
                if total>0:
                    ocupacion=(reservas_reales / total) * 100
                else:
                    ocupacion=0

                precio_final=precio * factores["factor_precio"]
                self.precios_por_dia[dia] = precio_final
                
                ingresos=reservas_reales * precio_final

                costo_total=costo_marketing + (personal * costo_empleado) + (campañas * costo_campaña)

                ganancia=ingresos - costo_total

                acumulada=acumulada + ganancia

                vistas_totales=vistas_totales + vistas
                reservas_totales=reservas_totales + reservas
                ingresos_totales=ingresos_totales + ingresos
                costos_totales=costos_totales + costo_total
                ganancia_total=ganancia_total + ganancia
                conversion_total=conversion_total + conversion

                tabla_simulacion.append([dia, alea_vistas, vistas, temporada, alea_conversion, str(conversion) + "%", reservas, cancelaciones, reservas_reales, alea_campana, campana, precio_final, ingresos, alea_costo, costo_marketing, ganancia])

                tabla_comportamiento.append([dia, temporada, vistas, reservas, ingresos, costo_total,ganancia])

                tabla_acumulada.append([dia, acumulada])

                tabla_dias.append([dia, reservas_reales, ingresos, ganancia])

                dias_rentables.append([dia, ganancia])

                dias_debiles.append([dia, ganancia])

                if costos_totales > presupuesto:
                    messagebox.showwarning("Presupuesto agotado", f"Se detiene en día {dia}")
                    break

            promedio_conversion=conversion_total / dias
            
            if costos_totales>0:
                roi=ganancia_total / costos_totales
            else:
                roi=0
        
            tabla_resumen.append(["Vistas Totales", vistas_totales])
            tabla_resumen.append(["Reservas Totales", reservas_totales])
            tabla_resumen.append(["Conversión Promedio", f"{promedio_conversion:.2f}%"])
            tabla_resumen.append(["Ingresos Totales", f"${ingresos_totales:,.2f}"])
            tabla_resumen.append(["Costos Totales", f"${costos_totales:,.2f}"])
            tabla_resumen.append(["Ganancia Total", f"${ganancia_total:,.2f}"])
            tabla_resumen.append(["Rentabilidad", f"{roi:.2f}"])

            #ANÁLISIS
            analisis=[]
            #Marketing
            if costos_totales>presupuesto * 0.8:
                analisis.append(["Marketing", "La inversión en marketing es Alta y se acerca al límite del presupuesto."])
            else:
                analisis.append(["Marketing", "La inversión en marketing es controlada dentro del presupuesto."])

            #Rentabilidad
            roi=ganancia_total / costos_totales if costos_totales > 0 else 0
            if roi<0.2:
                analisis.append(["Rentabilidad", "Baja rentabilidad. El sistema no es eficiente en convertir costos en ganancias."])
            elif roi < 0.5:
                analisis.append(["Rentabilidad", "Rentabilidad media. El sistema es estable pero mejorable."])
            else:
                analisis.append(["Rentabilidad", "Alta rentabilidad. El sistema es eficiente."])

            # 5. Cancelaciones
            if reservas_totales>0:
                tasa_cancelacion=(reservas_totales - reservas_reales) / reservas_totales
            else:
                tasa_cancelacion=0

            if tasa_cancelacion>0.3:
                analisis.append(["Cancelaciones", "Alta tasa de cancelación. Afecta significativamente ingresos."])
            else:
                analisis.append(["Cancelaciones", "Tasa de cancelación dentro de rango aceptable."])

            # ORDENAR DÍAS RENTABLES
            for i in range(len(dias_rentables)):
                for j in range(i + 1, len(dias_rentables)):
                    if dias_rentables[i][1] < dias_rentables[j][1]:
                        auxiliar=dias_rentables[i]
                        dias_rentables[i]=dias_rentables[j]
                        dias_rentables[j]=auxiliar

            # ORDENAR DÍAS DÉBILES
            for i in range(len(dias_debiles)):
                for j in range(i + 1, len(dias_debiles)):
                    if dias_debiles[i][1] > dias_debiles[j][1]:
                        auxiliar=dias_debiles[i]
                        dias_debiles[i]=dias_debiles[j]
                        dias_debiles[j]=auxiliar

            sobrante_presupuesto=presupuesto - costos_totales

            self.lbl_vistas.configure(text=f"Vistas: {vistas_totales}")
            self.lbl_reservas.configure(text=f"Posibles reservas: {reservas_totales}")
            self.lbl_ingresos.configure(text=f"Posibles ingresos: ${ingresos_totales:,.2f}")
            self.lbl_ganancia.configure(text=f"Sobra del presupuesto: ${sobrante_presupuesto:,.2f}")

            for widget in self.frame_resultados.winfo_children():
                widget.destroy()

            titulo=ctk.CTkLabel(self.frame_resultados, text="RESULTADOS DE LA SIMULACIÓN", text_color=COLOR_TEXTO, font=("Arial", 22, "bold"))
            titulo.pack(pady=20)

            self.tabs=ctk.CTkTabview(self.frame_resultados, width=1300, height=800)
            self.tabs.pack(fill="both", expand=True, padx=20, pady=20)

            # CREAR TABS
            self.tabs.add("Simulación")
            self.tabs.add("Resumen")
            self.tabs.add("Comportamiento")
            self.tabs.add("Acumulado")
            self.tabs.add("Análisis")

            ctk.CTkLabel(self.tabs.tab("Simulación"), text="SIMULACIÓN DIARIA", text_color=COLOR_TEXTO, font=("Arial", 18, "bold")).pack(pady=10)
            frame_simulacion=ctk.CTkScrollableFrame(self.tabs.tab("Simulación"), orientation="horizontal", width=1200, height=500)
            frame_simulacion.pack(fill="both", expand=True, padx=20, pady=10)
            self.tabla_simulacion=CTkTable(frame_simulacion, values=tabla_simulacion)
            self.tabla_simulacion.pack(padx=10, pady=10)

            ctk.CTkLabel(self.tabs.tab("Resumen"), text="RESUMEN GENERAL", text_color=COLOR_TEXTO, font=("Arial", 18, "bold")).pack(pady=10)
            frame_resumen=ctk.CTkScrollableFrame(self.tabs.tab("Resumen"), orientation="horizontal", width=1000, height=500)
            frame_resumen.pack(fill="both", expand=True, padx=20, pady=10)
            self.tabla_resumen=CTkTable(frame_resumen, values=tabla_resumen)
            self.tabla_resumen.pack(padx=10, pady=10)

            ctk.CTkLabel(self.tabs.tab("Comportamiento"), text="COMPORTAMIENTO POR DÍA", text_color=COLOR_TEXTO, font=("Arial", 18, "bold")).pack(pady=10)
            frame_dias = ctk.CTkScrollableFrame(self.tabs.tab("Comportamiento"), width=1200, height=600)
            frame_dias.pack(fill="both", expand=True, padx=20, pady=10)

            for i, fila in enumerate(tabla_dias[1:], start=1):
                dia=fila[0]
                res=fila[1]
                ing=fila[2]
                gan=fila[3]
                texto=f"  Día {dia}   |   Reservas: {res}   |   Ingresos: ${ing:,.2f}   |   Ganancia: ${gan:,.2f}"
                btn=ctk.CTkButton(frame_dias, text=texto, anchor="w", fg_color="#3B3B3B", hover_color="#4A4A4A", text_color="#FFFFFF", font=("Arial", 14), height=38, command=lambda d=dia: self.mostrar_detalle_dia(d))
                btn.pack(pady=3, padx=10, fill="x")

            ctk.CTkLabel(self.tabs.tab("Acumulado"), text="GANANCIA ACUMULADA", text_color=COLOR_TEXTO, font=("Arial", 18, "bold")).pack(pady=10)
            frame_acumulado=ctk.CTkScrollableFrame(self.tabs.tab("Acumulado"), orientation="horizontal", width=1000, height=500)
            frame_acumulado.pack(fill="both", expand=True, padx=20, pady=10)
            self.tabla_acumulada=CTkTable(frame_acumulado, values=tabla_acumulada)
            self.tabla_acumulada.pack(padx=10, pady=10)

            ctk.CTkLabel(self.tabs.tab("Análisis"), text="ANÁLISIS DEL SISTEMA", text_color=COLOR_TEXTO, font=("Arial", 18, "bold")).pack(pady=10)
            frame_analisis=ctk.CTkScrollableFrame(self.tabs.tab("Análisis"), width=1000, height=600)
            frame_analisis.pack(fill="both", expand=True, padx=20, pady=10)
            tabla_analisis=[["Área", "Diagnóstico"]]
            tabla_analisis+=analisis
            tabla = CTkTable(frame_analisis, values=tabla_analisis)
            tabla.pack(padx=10, pady=10)

            rentables=""
            for dato in dias_rentables[:3]:
                dia=dato[0]
                ganancia=dato[1]
                rentables=rentables + "Día " + str(dia) + " → $" + str(ganancia) + "\n"

            debiles=""
            for dato in dias_debiles[:3]:
                dia=dato[0]
                ganancia=dato[1]
                debiles=debiles + "Día " + str(dia) + " → $" + str(ganancia) + "\n"

            frame_extra=ctk.CTkFrame(self.frame_resultados)
            frame_extra.pack(fill="x", padx=20, pady=20)

            ctk.CTkLabel(frame_extra, text="Días más rentables\n\n" + rentables, justify="left", text_color="#00FF99", font=("Arial", 16, "bold")).grid(row=0, column=0, padx=40, pady=20)

            ctk.CTkLabel(frame_extra, text="Días más débiles\n\n" + debiles, justify="left", text_color="#FF6666", font=("Arial", 16, "bold")).grid(row=0, column=1, padx=40, pady=20)

            if costos_totales>presupuesto:
                messagebox.showwarning("Advertencia", "Los costos superan el presupuesto")
            else:
                messagebox.showinfo("Correcto", "Simulación realizada")

        except ValueError:
            messagebox.showerror("Error", "Ingresa datos válidos")

        except Exception as error:
            messagebox.showerror("Error", str(error))

    def mostrar_detalle_dia(self, dia):
        ventana_detalle = ctk.CTkToplevel(self.ventana)
        ventana_detalle.title(f"Detalle del Día {dia}")
        ventana_detalle.configure(fg_color=COLOR_FONDO)
        ventana_detalle.geometry("900x500")
        ventana_detalle.lift()
        ventana_detalle.focus_force()

        ctk.CTkLabel(ventana_detalle, text=f"Reservaciones del Día {dia}", text_color=COLOR_TEXTO, font=("Arial", 20, "bold")).pack(pady=15)
        precio_dia=self.precios_por_dia.get(dia, 0)
        datos=self.reservas_por_dia.get(dia, [])

        if not datos:
            ctk.CTkLabel(ventana_detalle, text="No hubo reservaciones este día.", text_color="#AAAAAA", font=("Arial", 14)).pack(pady=20)
            return
        
        frame_scroll=ctk.CTkScrollableFrame(ventana_detalle, orientation="horizontal", width=860,height=380)
        frame_scroll.pack(padx=20, pady=10, fill="both", expand=True)

        # Encabezados
        encabezados=["Reserva", "Aleatorio Habitación", "Tipo Habitación", "Aleatorio Estancia", "Días de Estancia", "Precio por Noche", "Total Estancia"]
        valores_tabla=[encabezados]

        for i, r in enumerate(datos, start=1):
            total_estancia = precio_dia * r["Estancia"]
            valores_tabla.append([str(i), f"{r['Aleatorio habitacion']:.4f}", r["Tipo"], f"{r['Aleatorio estancia']:.4f}", str(r["Estancia"]), f"${precio_dia:,.2f}", f"${total_estancia:,.2f}"])

        tabla=CTkTable(frame_scroll, values=valores_tabla, header_color="#4281FF")
        tabla.pack(padx=10, pady=10)

        total_dia=sum(precio_dia * r["Estancia"] for r in datos)
        ctk.CTkLabel(ventana_detalle, text=f"Total generado el día {dia}:  ${total_dia:,.2f}", text_color="#00FF99", font=("Arial", 16, "bold")).pack(pady=10)

        ctk.CTkButton(ventana_detalle, text="Cerrar", fg_color="#D6C49E", text_color="#000000", command=ventana_detalle.destroy).pack(pady=10)
