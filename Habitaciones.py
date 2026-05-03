import customtkinter as ctk
from CTkTable import CTkTable
from tkinter import messagebox
import random

COLOR_FONDO = "#5D4037"
COLOR_TEXTO = "#FFFFFF"
COLOR_CONTORNO = "#4281FF"

class Habitaciones:
    def __init__(self):
        self.ventana=ctk.CTk()
        self.ventana.title("Área de Habitaciones")
        self.ventana.geometry("1400x750")
        self.ventana.configure(fg_color=COLOR_FONDO)

        try:
            self.ventana.state("zoomed")
        except:
            self.ventana.attributes("-zoomed", True)

        # DATOS
        self.datos_llegadas=[[0, 0.29],
                             [1, 0.30],
                             [2, 0.20],
                             [3, 0.21]]

        self.datos_tipo=[["Individual", 0.40],
                         ["Doble", 0.40],
                         ["Suite", 0.20]]

        self.datos_estancia=[[1, 0.25],
                             [2, 0.35],
                             [3, 0.25],
                             [4, 0.15]]
        
        self.reiniciar_llegadas=False
        self.reiniciar_tipo=False
        self.reiniciar_estancia=False

       # SCROLL
        self.frame_scroll=ctk.CTkScrollableFrame(self.ventana)
        self.frame_scroll.pack(fill="both", expand=True, padx=20, pady=20)

        # TITULO
        titulo=ctk.CTkLabel(self.frame_scroll, text="Simulación de habitaciones", text_color=COLOR_TEXTO, font=("Arial", 28, "bold", "italic"))
        titulo.pack(pady=20)

        # FRAME DATOS
        self.frame_datos=ctk.CTkFrame(self.frame_scroll, border_width=2, border_color=COLOR_CONTORNO)
        self.frame_datos.pack(fill="x", padx=20, pady=20)

        ancho_entry=180
        alto_entry=40

        ctk.CTkLabel(self.frame_datos, text="Habitaciones individuales:", text_color=COLOR_TEXTO, font=("Arial", 16)).grid(row=0, column=0, padx=20, pady=(20, 5))
        self.entry_individuales=ctk.CTkEntry(self.frame_datos, width=ancho_entry, height=alto_entry)
        self.entry_individuales.grid(row=1, column=0, padx=20, pady=(0, 20))
        self.entry_individuales.insert(0, "10")

        ctk.CTkLabel(self.frame_datos, text="Habitaciones dobles:", text_color=COLOR_TEXTO, font=("Arial", 16)).grid(row=0, column=1, padx=20, pady=(20, 5))
        self.entry_dobles=ctk.CTkEntry(self.frame_datos, width=ancho_entry, height=alto_entry)
        self.entry_dobles.grid(row=1, column=1, padx=20, pady=(0, 20))
        self.entry_dobles.insert(0, "8")

        ctk.CTkLabel(self.frame_datos, text="Habitaciones suite:", text_color=COLOR_TEXTO, font=("Arial", 16)).grid(row=0, column=2, padx=20, pady=(20, 5))
        self.entry_suites=ctk.CTkEntry(self.frame_datos, width=ancho_entry, height=alto_entry)
        self.entry_suites.grid(row=1, column=2, padx=20, pady=(0, 20))
        self.entry_suites.insert(0, "5")

        ctk.CTkLabel(self.frame_datos, text="Costo de mantenimiento:", text_color=COLOR_TEXTO, font=("Arial", 16)).grid(row=2, column=0, padx=20, pady=(10, 5))
        self.entry_mantenimiento=ctk.CTkEntry(self.frame_datos, width=ancho_entry, height=alto_entry)
        self.entry_mantenimiento.grid(row=3, column=0, padx=20, pady=(0, 20))
        self.entry_mantenimiento.insert(0, "200")

        ctk.CTkLabel(self.frame_datos, text="Costo de limpieza:", text_color=COLOR_TEXTO, font=("Arial", 16)).grid(row=2, column=1, padx=20, pady=(10, 5))
        self.entry_limpieza=ctk.CTkEntry(self.frame_datos, width=ancho_entry, height=alto_entry)
        self.entry_limpieza.grid(row=3, column=1, padx=20, pady=(0, 20))
        self.entry_limpieza.insert(0, "100")

        ctk.CTkLabel(self.frame_datos, text="Días a simular:", text_color=COLOR_TEXTO, font=("Arial", 16)).grid(row=2, column=2, padx=20, pady=(10, 5))
        self.entry_dias=ctk.CTkEntry(self.frame_datos, width=ancho_entry, height=alto_entry)
        self.entry_dias.grid(row=3, column=2, padx=20, pady=(0, 20))
        self.entry_dias.insert(0, "20")

        self.btn_simular=ctk.CTkButton(self.frame_datos, text="Simular", width=ancho_entry, height=alto_entry, fg_color="#D6C49E", text_color="#000000", command=self.simular)
        self.btn_simular.grid(row=3, column=3, padx=20, pady=(0, 20))

        # KPIS
        self.frame_kpis=ctk.CTkFrame(self.frame_scroll, border_width=2, border_color=COLOR_CONTORNO)
        self.frame_kpis.pack(fill="x", padx=20, pady=20)

        self.lbl_ingresos=ctk.CTkLabel(self.frame_kpis, text="Ingresos Totales: $0", text_color="#00FF99", font=("Arial", 18, "bold"))
        self.lbl_ingresos.grid(row=0, column=0, padx=40, pady=30)

        self.lbl_costos=ctk.CTkLabel(self.frame_kpis, text="Costos Totales: $0", text_color="#FF6666", font=("Arial", 18, "bold"))
        self.lbl_costos.grid(row=0, column=1, padx=40, pady=30)

        self.lbl_ganancias=ctk.CTkLabel(self.frame_kpis, text="Ganancia Neta: $0", text_color="#FFD700", font=("Arial", 18, "bold"))
        self.lbl_ganancias.grid(row=0, column=2, padx=40, pady=30)

        # BOTONES
        self.frame_botones=ctk.CTkFrame(self.frame_scroll, border_width=2, border_color=COLOR_CONTORNO)
        self.frame_botones.pack(fill="x", padx=20, pady=20)

        botones=[("Limpiar", self.limpiar),
                 ("Valores Bajos", self.valores_bajos),
                 ("Valores Medios", self.valores_medios),
                 ("Valores Altos", self.valores_altos)]
        
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

        self.crear_tabla("Llegadas por día", "Clientes", self.datos_llegadas, 0)

        self.crear_tabla("Tipo de habitación", "Tipo", self.datos_tipo, 1)

        self.crear_tabla("Duración de estancia", "Noches", self.datos_estancia, 2)

        # RESULTADOS
        self.frame_resultados=ctk.CTkFrame(self.frame_scroll, border_width=2, border_color=COLOR_CONTORNO)
        self.frame_resultados.pack(fill="both", expand=True, padx=20, pady=20)

        titulo_resultados=ctk.CTkLabel(self.frame_resultados, text="RESULTADOS DE LA SIMULACIÓN", text_color=COLOR_TEXTO, font=("Arial", 20, "bold"))
        titulo_resultados.pack(pady=20)

        tabla_resultados=[["Día", "Llegadas", "Habitaciones", "Ingresos", "Costos", "Ganancia"],
                          ["", "", "", "", "", ""],
                          ["", "", "", "", "", ""],
                          ["", "", "", "", "", ""],
                          ["", "", "", "", "", ""]]

        self.tabla_simulacion=CTkTable(self.frame_resultados, values=tabla_resultados)
        self.tabla_simulacion.pack(padx=20, pady=20)
        self.ventana.mainloop()

    def limpiar(self):
        self.entry_individuales.delete(0, "end")

        self.entry_dobles.delete(0, "end")

        self.entry_suites.delete(0, "end")

        self.entry_mantenimiento.delete(0, "end")

        self.entry_limpieza.delete(0, "end")

        self.entry_dias.delete(0, "end")

        self.lbl_ingresos.configure(text="Ingresos Totales: $0")

        self.lbl_costos.configure(text="Costos Totales: $0")

        self.lbl_ganancias.configure(text="Ganancia Neta: $0")

        for widget in self.frame_resultados.winfo_children():
            widget.destroy()

        messagebox.showinfo("Correcto", "Datos limpiados")

    def valores_bajos(self):
        self.entry_individuales.delete(0, "end")
        self.entry_individuales.insert(0, "5")

        self.entry_dobles.delete(0, "end")
        self.entry_dobles.insert(0, "3")

        self.entry_suites.delete(0, "end")
        self.entry_suites.insert(0, "2")

        self.entry_mantenimiento.delete(0, "end")
        self.entry_mantenimiento.insert(0, "100")

        self.entry_limpieza.delete(0, "end")
        self.entry_limpieza.insert(0, "50")

        self.entry_dias.delete(0, "end")
        self.entry_dias.insert(0, "10")
    
    def valores_medios(self):
        self.entry_individuales.delete(0, "end")
        self.entry_individuales.insert(0, "10")

        self.entry_dobles.delete(0, "end")
        self.entry_dobles.insert(0, "8")

        self.entry_suites.delete(0, "end")
        self.entry_suites.insert(0, "5")

        self.entry_mantenimiento.delete(0, "end")
        self.entry_mantenimiento.insert(0, "200")

        self.entry_limpieza.delete(0, "end")
        self.entry_limpieza.insert(0, "100")

        self.entry_dias.delete(0, "end")
        self.entry_dias.insert(0, "20")
    
    def valores_altos(self):
        self.entry_individuales.delete(0, "end")
        self.entry_individuales.insert(0, "25")

        self.entry_dobles.delete(0, "end")
        self.entry_dobles.insert(0, "20")

        self.entry_suites.delete(0, "end")
        self.entry_suites.insert(0, "10")

        self.entry_mantenimiento.delete(0, "end")
        self.entry_mantenimiento.insert(0, "500")

        self.entry_limpieza.delete(0, "end")
        self.entry_limpieza.insert(0, "250")

        self.entry_dias.delete(0, "end")
        self.entry_dias.insert(0, "50")

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

        if encabezado=="Clientes":
            self.tabla_llegadas=tabla

        elif encabezado=="Tipo":
            self.tabla_tipo=tabla

        else:
            self.tabla_estancia=tabla

    # CALCULAR TABLA
    def calcular_tabla(self, datos, encabezado):
        tabla=[[encabezado, "Probabilidad", "Prob. Acumulada", "Rango"]]

        acumulada=0
        for i, fila in enumerate(datos):
            valor=fila[0]
            prob=fila[1]
            inicio=acumulada
            acumulada+=prob

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
            if suma==1:
                if encabezado=="Clientes":
                    if self.reiniciar_llegadas==False:
                        messagebox.showwarning("Advertencia", "La tabla ya suma 1\n" "Si agregas otro dato se reiniciará")
                        self.reiniciar_llegadas=True
                        return
                    else:
                        datos.clear()
                        self.reiniciar_llegadas=False
                
                elif encabezado=="Tipo":
                    if self.reiniciar_tipo==False:
                        messagebox.showwarning("Advertencia", "La tabla ya suma 1\n" "Si agregas otro dato se reiniciará")
                        self.reiniciar_tipo=True
                        return
                    else:
                        datos.clear()
                        self.reiniciar_tipo=False

                else:
                    if self.reiniciar_estancia==False:
                        messagebox.showwarning("Advertencia", "La tabla ya suma 1\n" "Si agregas otro dato se reiniciará")
                        self.reiniciar_estancia=True
                        return
                    else:
                        datos.clear()
                        self.reiniciar_estancia=False

            for fila in datos:
                if fila[0]==valor:
                    messagebox.showerror("Error", "Ese valor ya existe")
                    return

            datos.append([valor, prob])

            nueva_suma=0
            for fila in datos:
                nueva_suma=nueva_suma + fila[1]
            nueva_suma=round(nueva_suma, 4)

            if nueva_suma>1:
                datos.pop()
                messagebox.showerror("Error", "La suma de probabilidades no puede superar 1")
                return

            try:
                datos.sort()
            except:
                pass

            if encabezado=="Clientes":
                self.tabla_llegadas.destroy()
            elif encabezado=="Tipo":
                self.tabla_tipo.destroy()
            else:
                self.tabla_estancia.destroy()

            nueva_tabla=CTkTable(frame, values=self.calcular_tabla(datos, encabezado))
            nueva_tabla.pack(padx=10, pady=10)

            if encabezado=="Clientes":
                self.tabla_llegadas=nueva_tabla
            elif encabezado=="Tipo":
                self.tabla_tipo=nueva_tabla
            else:
                self.tabla_estancia=nueva_tabla

            entrada1.delete(0, "end")
            entrada2.delete(0, "end")

            if nueva_suma==1:
                messagebox.showinfo("Correcto", "La tabla ya suma 1")

        except ValueError:
            messagebox.showerror("Error", "Ingresa valores válidos")

        except Exception as error:
            messagebox.showerror("Error", str(error))
    
    # CREAR HOTEL
    def crear_hotel(self):
        try:
            individuales=int(self.entry_individuales.get())
            dobles=int(self.entry_dobles.get())
            suites=int(self.entry_suites.get())

            self.habitaciones_individuales={}
            self.habitaciones_dobles={}
            self.habitaciones_suite={}
            # INDIVIDUALES
            for i in range(1, individuales + 1):
                nombre="I" + str(i)
                self.habitaciones_individuales[nombre]=0

            # DOBLES
            for i in range(1, dobles + 1):
                nombre="D" + str(i)
                self.habitaciones_dobles[nombre]=0

            # SUITES
            for i in range(1, suites + 1):
                nombre="S" + str(i)
                self.habitaciones_suite[nombre]=0

            # CLIENTES
            self.clientes=[]

        except:
            messagebox.showerror("Error", "No se pudo crear el hotel")

    # ASIGNAR HABITACIÓN
    def asignar_habitacion(self, tipo, dia_actual, noches):
        # INDIVIDUAL
        if tipo=="Individual":
            for habitacion in self.habitaciones_individuales:
                salida=self.habitaciones_individuales[habitacion]
                if salida<=dia_actual:
                    self.habitaciones_individuales[habitacion]=dia_actual + noches
                    return habitacion

        # DOBLE
        elif tipo=="Doble":
            for habitacion in self.habitaciones_dobles:
                salida=self.habitaciones_dobles[habitacion]
                if salida<=dia_actual:
                    self.habitaciones_dobles[habitacion]=dia_actual + noches
                    return habitacion

        # SUITE
        elif tipo=="Suite":
            for habitacion in self.habitaciones_suite:
                salida=self.habitaciones_suite[habitacion]
                if salida<=dia_actual:
                    self.habitaciones_suite[habitacion]=dia_actual + noches
                    return habitacion
        return None

    # LIBERAR HABITACIONES
    def liberar_habitaciones(self, dia_actual):
        # INDIVIDUALES
        for habitacion in self.habitaciones_individuales:
            salida=self.habitaciones_individuales[habitacion]
            if salida<=dia_actual:
                self.habitaciones_individuales[habitacion]=0

        # DOBLES
        for habitacion in self.habitaciones_dobles:
            salida=self.habitaciones_dobles[habitacion]
            if salida<=dia_actual:
                self.habitaciones_dobles[habitacion]=0

        # SUITES
        for habitacion in self.habitaciones_suite:
            salida=self.habitaciones_suite[habitacion]
            if salida<=dia_actual:
                self.habitaciones_suite[habitacion]=0

    # CONTAR OCUPADAS
    def contar_ocupadas(self):
        ocupadas_individual=0
        ocupadas_dobles=0
        ocupadas_suite=0

        for habitacion in self.habitaciones_individuales:
            if self.habitaciones_individuales[habitacion]>0:
                ocupadas_individual=ocupadas_individual + 1

        for habitacion in self.habitaciones_dobles:
            if self.habitaciones_dobles[habitacion]>0:
                ocupadas_dobles=ocupadas_dobles + 1

        for habitacion in self.habitaciones_suite:
            if self.habitaciones_suite[habitacion]>0:
                ocupadas_suite=ocupadas_suite + 1

        return ocupadas_individual, ocupadas_dobles, ocupadas_suite

    # CONTAR DISPONIBLES
    def contar_disponibles(self):
        disponibles_individual=0
        disponibles_dobles=0
        disponibles_suite=0

        for habitacion in self.habitaciones_individuales:
            if self.habitaciones_individuales[habitacion]==0:
                disponibles_individual=disponibles_individual + 1

        for habitacion in self.habitaciones_dobles:
            if self.habitaciones_dobles[habitacion]==0:
                disponibles_dobles=disponibles_dobles + 1

        for habitacion in self.habitaciones_suite:
            if self.habitaciones_suite[habitacion]==0:
                disponibles_suite=disponibles_suite + 1

        return disponibles_individual, disponibles_dobles, disponibles_suite
    
    # BUSCAR RESULTADO
    def buscar_resultado(self, numero, datos):
        acumulada=0
        for valor, probabilidad in datos:
            acumulada=acumulada + probabilidad
            if numero<=acumulada:
                return valor
            
    # LEER ALEATORIOS
    def leer_aleatorios(self):
        aleatorios=[]
        '''archivo=open("Aleatorios.txt", "r")
        for linea in archivo:
            linea=linea.strip()
            if linea!="":
                numero=round(float(linea), 4)
                if numero>=0 and numero<=1:
                    aleatorios.append(numero)
        archivo.close()'''
        for i in range(10000):
            alea=round(random.random(), 4)
            aleatorios.append(alea)
        random.shuffle(aleatorios)
        return aleatorios

    # CONTAR SALIDAS
    def contar_salidas(self, dia_actual):
        salidas=0
        # INDIVIDUALES
        for habitacion in self.habitaciones_individuales:
            if self.habitaciones_individuales[habitacion]==dia_actual:
                salidas=salidas + 1

        # DOBLES
        for habitacion in self.habitaciones_dobles:
            if self.habitaciones_dobles[habitacion]==dia_actual:
                salidas=salidas + 1

        # SUITES
        for habitacion in self.habitaciones_suite:
            if self.habitaciones_suite[habitacion]==dia_actual:
                salidas=salidas + 1

        return salidas

    # VALIDAR TABLAS
    def validar_tablas(self):
        suma_llegadas=0
        for fila in self.datos_llegadas:
            suma_llegadas=suma_llegadas + fila[1]

        suma_tipo=0
        for fila in self.datos_tipo:
            suma_tipo=suma_tipo + fila[1]
        
        suma_estancia=0
        for fila in self.datos_estancia:
            suma_estancia=suma_estancia + fila[1]

        suma_llegadas=round(suma_llegadas, 4)
        suma_tipo=round(suma_tipo, 4)
        suma_estancia=round(suma_estancia, 4)

        if suma_llegadas!=1:
            messagebox.showerror("Error", "La tabla de llegadas debe sumar 1")
            return False

        if suma_tipo!=1:
            messagebox.showerror("Error", "La tabla de tipos debe sumar 1")
            return False

        if suma_estancia!=1:
            messagebox.showerror("Error", "La tabla de estancia debe sumar 1")
            return False
        return True

    # SIMULACIÓN
    def simular(self):
        try:
            # VALIDAR TABLAS
            if self.validar_tablas()==False:
                return

            # CREAR HOTEL
            self.crear_hotel()

            # ENTRADAS
            dias=int(self.entry_dias.get())
            mantenimiento=float(self.entry_mantenimiento.get())
            limpieza=float(self.entry_limpieza.get())
            
            if dias<=0:
                messagebox.showerror("Error", "Los días deben ser mayores a 0")
                return

            if mantenimiento<0 or limpieza<0:
                messagebox.showerror("Error", "Los costos no pueden ser negativos")
                return

            # PRECIOS
            precios={"Individual":500,
                     "Doble":800,
                     "Suite":1500}

            # ALEATORIOS
            aleatorios=self.leer_aleatorios()
            if len(aleatorios)<(dias * 10):
                messagebox.showerror("Error", "No hay suficientes números aleatorios")
                return

            indice=0
            # TABLAS
            tabla_llegadas=[["Día", "Aleatorio", "Llegadas"]]

            tabla_clientes=[["Día", "Cliente", "Aleatorio Tipo", "Tipo", "Habitación", "Estado", "Aleatorio Estancia", "Noches", "Salida"]]

            tabla_ocupacion=[["Día", "Ocupadas I", "Ocupadas D", "Ocupadas S", "Disponibles I", "Disponibles D", "Disponibles S", "% Ocupación"]]

            tabla_costos=[["Día", "Salidas", "Costo Limpieza", "Aleatorio Mantenimiento", "Mantenimiento Extra", "Costo Total"]]

            tabla_finanzas=[["Día", "Ingresos", "Costos", "Ganancia"]]

            tabla_resumen=[["Métrica", "Valor"]]

            ingresos_totales=0
            costos_totales=0
            ganancias_totales=0

            clientes_totales=0
            clientes_rechazados=0

            cliente_global=1

            total_habitaciones=(len(self.habitaciones_individuales) + len(self.habitaciones_dobles) + len(self.habitaciones_suite))

            suma_ocupacion=0

            # DÍAS
            for dia in range(1, dias + 1):

                # SALIDAS
                salidas=self.contar_salidas(dia)

                # COSTO LIMPIEZA
                costo_limpieza=salidas * limpieza

                # LIBERAR HABITACIONES
                self.liberar_habitaciones(dia)

                # ALEATORIO LLEGADAS
                alea_llegadas=aleatorios[indice]

                indice=indice + 1

                # LLEGADAS
                llegadas=self.buscar_resultado(alea_llegadas, self.datos_llegadas)
                tabla_llegadas.append([dia, alea_llegadas, llegadas])
                                      
                ingresos_dia=0
                # CLIENTES
                for cliente in range(1, llegadas + 1):
                    clientes_totales=clientes_totales + 1

                    # ALEATORIO TIPO
                    alea_tipo=aleatorios[indice]
                    indice=indice + 1
                    tipo=self.buscar_resultado(alea_tipo, self.datos_tipo)

                    # ALEATORIO ESTANCIA
                    alea_estancia=aleatorios[indice]
                    indice=indice + 1
                    noches=self.buscar_resultado(alea_estancia, self.datos_estancia)

                    # ASIGNAR HABITACIÓN
                    habitacion=self.asignar_habitacion(tipo, dia, noches)
                    if habitacion==None:
                        habitacion="-"

                    # SI HAY HABITACIÓN
                    if habitacion!="-":
                        estado="Aceptado"
                        salida=dia + noches
                        ingreso=precios[tipo] * noches
                        ingresos_dia=ingresos_dia + ingreso
                        self.clientes.append({"Cliente":cliente_global,
                                              "Habitacion":habitacion,
                                              "Entrada":dia,
                                              "Salida":salida})

                    else:
                        estado="Rechazado"
                        salida="-"
                        ingreso=0
                        clientes_rechazados=clientes_rechazados + 1

                    # TABLA CLIENTES
                    tabla_clientes.append([dia, cliente_global, alea_tipo, tipo, habitacion, estado, alea_estancia, noches, "dia " + str(salida)])
                    cliente_global=cliente_global + 1

                # MANTENIMIENTO ALEATORIO
                alea_mantenimiento=aleatorios[indice]
                indice=indice + 1

                if alea_mantenimiento<=0.20:
                    mantenimiento_extra=200
                else:
                    mantenimiento_extra=0

                # COSTOS
                costo_total=(costo_limpieza + mantenimiento + mantenimiento_extra)

                # GANANCIA
                ganancia=ingresos_dia - costo_total
                ingresos_totales=ingresos_totales + ingresos_dia
                costos_totales=costos_totales + costo_total
                ganancias_totales=ganancias_totales + ganancia

                # OCUPADAS
                ocupadas_individual, ocupadas_dobles, ocupadas_suite=self.contar_ocupadas()

                # DISPONIBLES
                disponibles_individual, disponibles_dobles, disponibles_suite=self.contar_disponibles()

                # TOTAL OCUPADAS
                total_ocupadas=(ocupadas_individual + ocupadas_dobles + ocupadas_suite)

                # PORCENTAJE
                porcentaje_ocupacion=(total_ocupadas/total_habitaciones) * 100

                suma_ocupacion=(suma_ocupacion + porcentaje_ocupacion)

                # TABLA OCUPACIÓN
                tabla_ocupacion.append([dia, ocupadas_individual, ocupadas_dobles, ocupadas_suite, disponibles_individual, disponibles_dobles, disponibles_suite, f"{porcentaje_ocupacion:.2f}%"])

                # TABLA COSTOS
                tabla_costos.append([dia, salidas, f"${costo_limpieza:,.2f}", alea_mantenimiento, f"${mantenimiento_extra:,.2f}", f"${costo_total:,.2f}"])

                # TABLA FINANZAS
                tabla_finanzas.append([dia, f"${ingresos_dia:,.2f}", f"${costo_total:,.2f}", f"${ganancia:,.2f}"])

            # PROMEDIO OCUPACIÓN
            promedio_ocupacion=suma_ocupacion / dias

            # TABLA RESUMEN
            tabla_resumen.append(["Clientes Totales", clientes_totales])
            tabla_resumen.append(["Clientes Rechazados", clientes_rechazados])
            tabla_resumen.append(["Ocupación Promedio", f"{promedio_ocupacion:.4f}%"])
            tabla_resumen.append(["Ingresos Totales", f"${ingresos_totales:,.4f}"])
            tabla_resumen.append(["Costos Totales", f"${costos_totales:,.4f}"])
            tabla_resumen.append(["Ganancia Total", f"${ganancias_totales:,.4f}"])

            # KPIS
            self.lbl_ingresos.configure(text=f"Ingresos Totales: ${ingresos_totales:,.2f}")

            self.lbl_costos.configure(text=f"Costos Totales: ${costos_totales:,.2f}")

            self.lbl_ganancias.configure(text=f"Ganancia Neta: ${ganancias_totales:,.2f}")

            # LIMPIAR FRAME
            for widget in self.frame_resultados.winfo_children():
                widget.destroy()

            # TÍTULO
            titulo=ctk.CTkLabel(self.frame_resultados, text="RESULTADOS DE LA SIMULACIÓN", text_color=COLOR_TEXTO, font=("Arial", 22, "bold"))
            titulo.pack(pady=20)

            # TABLA LLEGADAS
            ctk.CTkLabel(self.frame_resultados, text="LLEGADAS", text_color=COLOR_TEXTO, font=("Arial", 18, "bold")).pack(pady=10)
            self.tabla_llegadas_resultado=CTkTable(self.frame_resultados, values=tabla_llegadas)
            self.tabla_llegadas_resultado.pack(pady=10)

            # TABLA CLIENTES
            ctk.CTkLabel(self.frame_resultados, text="CLIENTES", text_color=COLOR_TEXTO, font=("Arial", 18, "bold")).pack(pady=10)
            frame_clientes=ctk.CTkScrollableFrame(self.frame_resultados, orientation="horizontal", width=1200, height=1000)
            frame_clientes.pack(fill="x", padx=20, pady=10)
            self.tabla_clientes=CTkTable(frame_clientes, values=tabla_clientes)
            self.tabla_clientes.pack(padx=10, pady=10)

            # TABLA OCUPACIÓN
            ctk.CTkLabel(self.frame_resultados, text="OCUPACIÓN", text_color=COLOR_TEXTO, font=("Arial", 18, "bold")).pack(pady=10)
            self.tabla_ocupacion=CTkTable(self.frame_resultados, values=tabla_ocupacion)
            self.tabla_ocupacion.pack(pady=10)

            # TABLA COSTOS
            ctk.CTkLabel(self.frame_resultados, text="COSTOS", text_color=COLOR_TEXTO, font=("Arial", 18, "bold")).pack(pady=10)
            self.tabla_costos=CTkTable(self.frame_resultados, values=tabla_costos)
            self.tabla_costos.pack(pady=10)

            # TABLA FINANZAS
            ctk.CTkLabel(self.frame_resultados, text="FINANZAS", text_color=COLOR_TEXTO, font=("Arial", 18, "bold")).pack(pady=10)
            self.tabla_finanzas=CTkTable(self.frame_resultados, values=tabla_finanzas)
            self.tabla_finanzas.pack(pady=10)

            # TABLA RESUMEN
            ctk.CTkLabel(self.frame_resultados, text="RESUMEN GENERAL", text_color=COLOR_TEXTO, font=("Arial", 18, "bold")).pack(pady=10)
            self.tabla_resumen=CTkTable(self.frame_resultados, values=tabla_resumen)
            self.tabla_resumen.pack(pady=10)

            # MENSAJE
            messagebox.showinfo("Correcto", "Simulación realizada")

        except ValueError:
            messagebox.showerror("Error", "Ingresa valores válidos")

        except FileNotFoundError:
            messagebox.showerror("Error", "No se encontró el archivo Aleatorios.txt")

        except Exception as error:
            messagebox.showerror("Error", str(error))


Habitaciones()