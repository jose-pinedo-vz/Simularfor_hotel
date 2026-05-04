import customtkinter as ctk
from CTkTable import CTkTable
from tkinter import messagebox
import random

COLOR_FONDO = "#5D4037"
COLOR_TEXTO = "#FFFFFF"
COLOR_CONTORNO = "#4281FF"

class Marketing:
    def __init__(self):
        self.ventana=ctk.CTk()
        self.ventana.title("Área de Marketing")
        self.ventana.geometry("1400x750")
        self.ventana.configure(fg_color=COLOR_FONDO)

        try:
            self.ventana.state("zoomed")
        except:
            self.ventana.attributes("-zoomed", True)

        # DATOS
        self.datos_leads=[[20, 0.30],
                          [40, 0.50],
                          [60, 0.20]]

        self.datos_conversion=[[10, 0.30],
                               [20, 0.50],
                               [30, 0.20]]

        self.datos_campaña=[["Facebook", 0.50],
                            ["Google Ads", 0.30],
                            ["Orgánico", 0.20]]

        self.datos_costos=[[300, 0.30],
                            [500, 0.50],
                            [800, 0.20]]

        self.reiniciar_leads=False
        self.reiniciar_conversion=False
        self.reiniciar_campaña=False
        self.reiniciar_costos=False

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

        self.btn_simular=ctk.CTkButton(self.frame_datos, text="Simular", width=ancho_entry, height=alto_entry, fg_color="#D6C49E", text_color="#000000", command=self.simular)
        self.btn_simular.grid(row=3, column=3, padx=20, pady=(0, 20))

        # KPIS
        self.frame_kpis=ctk.CTkFrame(self.frame_scroll, border_width=2, border_color=COLOR_CONTORNO)
        self.frame_kpis.pack(fill="x", padx=20, pady=20)

        self.lbl_leads=ctk.CTkLabel(self.frame_kpis, text="Leads Totales: 0", text_color="#00FF99", font=("Arial", 18, "bold"))
        self.lbl_leads.grid(row=0, column=0, padx=40, pady=30)

        self.lbl_reservas=ctk.CTkLabel(self.frame_kpis, text="Reservas Totales: 0", text_color="#FFD700", font=("Arial", 18, "bold"))
        self.lbl_reservas.grid(row=0, column=1, padx=40, pady=30)

        self.lbl_ingresos=ctk.CTkLabel(self.frame_kpis, text="Ingresos Totales: $0", text_color="#00BFFF", font=("Arial", 18, "bold"))
        self.lbl_ingresos.grid(row=0, column=2, padx=40, pady=30)

        self.lbl_ganancia=ctk.CTkLabel(self.frame_kpis, text="Ganancia Total: $0", text_color="#FF6666", font=("Arial", 18, "bold"))
        self.lbl_ganancia.grid(row=0, column=3, padx=40, pady=30)

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

        self.crear_tabla("Generación de Leads", "Leads", self.datos_leads, 0)

        self.crear_tabla("Tabla de Conversión",  "Conversión", self.datos_conversion, 1)

        self.crear_tabla("Tipo de campaña", "Campaña", self.datos_campaña, 2)

        self.crear_tabla("Costo marketing", "Costo", self.datos_costos, 3)

        # RESULTADOS
        self.frame_resultados=ctk.CTkFrame(self.frame_scroll, border_width=2, border_color=COLOR_CONTORNO)
        self.frame_resultados.pack(fill="both", expand=True, padx=20, pady=20)

        titulo_resultados=ctk.CTkLabel(self.frame_resultados, text="RESULTADOS DE LA SIMULACIÓN", text_color=COLOR_TEXTO, font=("Arial", 20, "bold"))
        titulo_resultados.pack(pady=20)

        tabla=[[["Día", "Aleatorio", "Leads"]]]

        self.tabla_inicio=CTkTable(self.frame_resultados, values=[["Día", "Leads", "Reservas"]])
        self.tabla_inicio.pack(pady=20)

        self.ventana.mainloop()

    # LIMPIAR
    def limpiar(self):
        self.entry_presupuesto.delete(0, "end")
        self.entry_campañas.delete(0, "end")
        self.entry_precio.delete(0, "end")
        self.entry_personal.delete(0, "end")
        self.entry_dias.delete(0, "end")

        self.lbl_leads.configure(text="Leads Totales: 0")
        self.lbl_reservas.configure(text="Reservas Totales: 0")
        self.lbl_ingresos.configure(text="Ingresos Totales: $0")
        self.lbl_ganancia.configure(text="Ganancia Total: $0")

        for widget in self.frame_resultados.winfo_children():
            widget.destroy()

        messagebox.showinfo("Correcto", "Datos limpiados")

    # VALORES BAJOS
    def valores_bajos(self):
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

    # VALORES MEDIOS
    def valores_medios(self):
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

    # VALORES ALTOS
    def valores_altos(self):
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

        if encabezado=="Leads":
            self.tabla_leads=tabla

        elif encabezado=="Conversión":
            self.tabla_conversion=tabla

        elif encabezado=="Campaña":
            self.tabla_campaña=tabla

        else:
            self.tabla_costos=tabla

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
                if encabezado=="Leads":
                    if self.reiniciar_leads==False:
                        messagebox.showwarning("Advertencia", "La tabla ya suma 1 Si agregas otro dato se reiniciará")
                        self.reiniciar_leads=True
                        return
                    else:
                        datos.clear()
                        self.reiniciar_leads=False

                elif encabezado=="Conversión":
                    if self.reiniciar_conversion==False:
                        messagebox.showwarning("Advertencia", "La tabla ya suma 1 Si agregas otro dato se reiniciará")
                        self.reiniciar_conversion=True
                        return
                    else:
                        datos.clear()
                        self.reiniciar_conversion=False

                elif encabezado=="Canal":
                    if self.reiniciar_canales==False:
                        messagebox.showwarning("Advertencia", "La tabla ya suma 1 Si agregas otro dato se reiniciará")
                        self.reiniciar_canales=True
                        return
                    else:
                        datos.clear()
                        self.reiniciar_canales=False

                else:
                    if self.reiniciar_costos==False:
                        messagebox.showwarning("Advertencia", "La tabla ya suma 1 Si agregas otro dato se reiniciará")
                        self.reiniciar_costos=True
                        return
                    else:
                        datos.clear()
                        self.reiniciar_costos=False

            if suma==1:
                datos.clear()

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

            if encabezado=="Leads":
                self.tabla_leads.destroy()

            elif encabezado=="Conversión":
                self.tabla_conversion.destroy()

            elif encabezado=="Campaña":
                self.tabla_campaña.destroy()

            else:
                self.tabla_costos.destroy()

            nueva_tabla=CTkTable(frame, values=self.calcular_tabla(datos, encabezado))
            nueva_tabla.pack(padx=10, pady=10)

            if encabezado=="Leads":
                self.tabla_leads=nueva_tabla

            elif encabezado=="Conversión":
                self.tabla_conversion=nueva_tabla

            elif encabezado=="Campaña":
                self.tabla_campaña=nueva_tabla

            else:
                self.tabla_costos=nueva_tabla

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
        suma_leads=0
        for fila in self.datos_leads:
            suma_leads=suma_leads + fila[1]

        suma_conversion=0
        for fila in self.datos_conversion:
            suma_conversion=suma_conversion + fila[1]

        suma_campana=0
        for fila in self.datos_campaña:
            suma_campana=suma_campana + fila[1]

        suma_costos=0
        for fila in self.datos_costos:
            suma_costos=suma_costos + fila[1]

        suma_leads=round(suma_leads, 4)
        suma_conversion=round(suma_conversion, 4)
        suma_campana=round(suma_campana, 4)
        suma_costos=round(suma_costos, 4)

        if suma_leads!=1:
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

        return True

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

            if presupuesto<=0 or campañas<=0 or precio<=0 or personal<=0 or dias<=0 or costo_empleado<=0 or costo_campaña<=0:
                messagebox.showerror("Error", "Todos los valores deben ser mayores a 0")
                return

            aleatorios=self.leer_aleatorios()
            indice=0

            tabla_simulacion=[["Día", "Alea Leads", "Leads", "Alea Conversión", "% Conversión", "Reservas", "alea Canal", "Canal", "Precio", "Ingresos", "Alea Costo", "Costo Marketing", "Ganancia"]]

            tabla_resumen=[["Indicador", "Valor"]]

            tabla_comportamiento=[["Día", "Leads", "Reservas", "Ingresos", "Costos", "Ganancia"]]

            tabla_acumulada=[["Día", "Ganancia acumulada"]]

            leads_totales=0
            reservas_totales=0
            ingresos_totales=0
            costos_totales=0
            ganancia_total=0
            conversion_total=0

            acumulada=0

            dias_rentables=[]
            dias_debiles=[]

            for dia in range(1, dias + 1):
                alea_leads=aleatorios[indice]
                indice=indice + 1
                leads=self.buscar_resultado(alea_leads, self.datos_leads)

                alea_conversion=aleatorios[indice]
                indice=indice + 1
                conversion=self.buscar_resultado(alea_conversion, self.datos_conversion)

                alea_campana=aleatorios[indice]
                indice=indice + 1
                campana=self.buscar_resultado(alea_campana, self.datos_campaña)

                alea_costo=aleatorios[indice]
                indice=indice + 1
                costo_marketing=self.buscar_resultado(alea_costo, self.datos_costos)

                reservas=int(leads * (conversion / 100))

                ingresos=reservas * precio

                costo_total=costo_marketing + (personal * costo_empleado) + (campañas * costo_campaña)

                ganancia=ingresos - costo_total

                acumulada=acumulada + ganancia

                leads_totales=leads_totales + leads
                reservas_totales=reservas_totales + reservas
                ingresos_totales=ingresos_totales + ingresos
                costos_totales=costos_totales + costo_total
                ganancia_total=ganancia_total + ganancia
                conversion_total=conversion_total + conversion

                tabla_simulacion.append([dia, alea_leads, leads, alea_conversion, str(conversion) + "%", reservas, alea_campana, campana, precio, ingresos, alea_costo, costo_marketing, ganancia])

                tabla_comportamiento.append([dia, leads, reservas, ingresos, costo_total,ganancia])

                tabla_acumulada.append([dia, acumulada])

                dias_rentables.append([dia, ganancia])
                dias_debiles.append([dia, ganancia])

            promedio_conversion=conversion_total / dias

            roi=ganancia_total / costos_totales

            tabla_resumen.append(["Leads Totales", leads_totales])
            tabla_resumen.append(["Reservas Totales", reservas_totales])
            tabla_resumen.append(["Conversión Promedio", f"{promedio_conversion:.2f}%"])
            tabla_resumen.append(["Ingresos Totales", f"${ingresos_totales:,.2f}"])
            tabla_resumen.append(["Costos Totales", f"${costos_totales:,.2f}"])
            tabla_resumen.append(["Ganancia Total", f"${ganancia_total:,.2f}"])
            tabla_resumen.append(["ROI", f"{roi:.2f}"])

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

            self.lbl_leads.configure(text=f"Leads Totales: {leads_totales}")
            self.lbl_reservas.configure(text=f"Reservas Totales: {reservas_totales}")
            self.lbl_ingresos.configure(text=f"Ingresos Totales: ${ingresos_totales:,.2f}")
            self.lbl_ganancia.configure(text=f"Ganancia Total: ${ganancia_total:,.2f}")

            for widget in self.frame_resultados.winfo_children():
                widget.destroy()

            titulo=ctk.CTkLabel(self.frame_resultados, text="RESULTADOS DE LA SIMULACIÓN", text_color=COLOR_TEXTO, font=("Arial", 22, "bold"))
            titulo.pack(pady=20)

            ctk.CTkLabel(self.frame_resultados, text="SIMULACIÓN", text_color=COLOR_TEXTO, font=("Arial", 18, "bold")).pack(pady=10)
            frame_simulacion=ctk.CTkScrollableFrame(self.frame_resultados, orientation="horizontal", width=1200, height=2000)
            frame_simulacion.pack(fill="x", padx=20, pady=10)
            self.tabla_simulacion=CTkTable(frame_simulacion, values=tabla_simulacion)
            self.tabla_simulacion.pack(padx=10, pady=10)

            ctk.CTkLabel(self.frame_resultados, text="RESULTADOS", text_color=COLOR_TEXTO, font=("Arial", 18, "bold")).pack(pady=10)
            self.tabla_resumen=CTkTable(self.frame_resultados, values=tabla_resumen)
            self.tabla_resumen.pack(pady=10)

            ctk.CTkLabel(self.frame_resultados, text="COMPORTAMIENTO POR DÍA", text_color=COLOR_TEXTO, font=("Arial", 18, "bold")).pack(pady=10)
            self.tabla_comportamiento=CTkTable(self.frame_resultados, values=tabla_comportamiento)
            self.tabla_comportamiento.pack(pady=10)

            ctk.CTkLabel(self.frame_resultados, text="GANANCIA ACUMULADA", text_color=COLOR_TEXTO, font=("Arial", 18, "bold")).pack(pady=10)
            self.tabla_acumulada=CTkTable(self.frame_resultados, values=tabla_acumulada)
            self.tabla_acumulada.pack(pady=10)

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

Marketing()