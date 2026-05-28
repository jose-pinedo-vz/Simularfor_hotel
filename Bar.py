import customtkinter as ctk
from CTkTable import CTkTable
from tkinter import ttk
import random
from datetime import datetime, timedelta
import math
import tkinter.messagebox as messagebox
import os

class Bar(ctk.CTkToplevel):

    def __init__(self, master=None):
        super().__init__(master)
        self.detalles_diarios = {} 
        #self.lista_aleatorios = []
        self.indice_aleatorio = 0
        self.cargar_archivo_aleatorios("GeneradorDeNumeroAleatorios/Aleatorios.txt")

        self.title("Simulación Monte Carlo - Bar del Hotel")
        self.geometry("1400x850")

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.style = ttk.Style()
        self.style.theme_use("default")
        self.style.configure("Treeview", 
                            background="#1e293b", 
                            foreground="white", 
                            fieldbackground="#1e293b", 
                            rowheight=28,
                            borderwidth=0)
        self.style.configure("Treeview.Heading", background="#0f172a", foreground="white", font=("Segoe UI", 10, "bold"))
        self.style.map("Treeview", background=[('selected', '#2563eb')])

        self.header()
        self.layout_principal()

        self.lift()                 
        self.attributes("-topmost", True)  
        self.focus_force()

    def header(self):
        header = ctk.CTkFrame(self, height=60, fg_color="#111827", corner_radius=0)
        header.pack(fill="x")
        header.pack_propagate(False)

        titulo = ctk.CTkLabel(header, text="🍸 Simulación Monte Carlo - Bar del Hotel", font=("Segoe UI", 20, "bold"))
        titulo.pack(side="left", padx=20)

        botones = [("Nueva Simulación", self.nueva_simul), ("Ejecutar", self.ejecutar)]
        for txt, v in reversed(botones):
            ctk.CTkButton(header, text=txt, command=v, width=120, height=34).pack(side="right", padx=8, pady=10)

    def layout_principal(self):
        main = ctk.CTkFrame(self, fg_color="#0f172a")
        main.pack(fill="both", expand=True)
        self.content(main)

    def content(self, parent):
        content = ctk.CTkFrame(parent, fg_color="#e5e7eb")
        content.pack(side="left", fill="both", expand=True)
        self.cards(content)
        self.tabs(content)

    def cards(self, parent):
        cards = ctk.CTkFrame(parent, fg_color="transparent")
        cards.pack(fill="x", padx=15, pady=15)
        self.kpis_labels = {}
        kpis = [("Clientes", "---"), ("Abandonos", "---"), ("Espera", "---"),("Meseros Sugeridos", "---"),
                ("Bartenders Sugeridos", "---"), ("Ingresos", "---"), ("Abasto Personal", "---"),("Utilidad Total", "---")]

        for t, v in kpis:
            card = ctk.CTkFrame(cards, width=180, height=90, fg_color="black")
            card.pack(side="left", padx=6)
            card.pack_propagate(False)
            ctk.CTkLabel(card, text=t, text_color="white", font=("bold italic", 12)).pack(pady=(12, 0))
            lbl_val = ctk.CTkLabel(card, text=v, text_color="white", font=("Segoe UI", 18, "bold"))
            lbl_val.pack()
            self.kpis_labels[t] = lbl_val

    def tabs(self, parent):
        self.tabview = ctk.CTkTabview(parent)
        self.tabview.pack(fill="both", expand=True, padx=15, pady=(0, 15))
        
        self.tabview.add("Parámetros")
        self.tabview.add("Tablas")
        self.tabview.add("Monte Carlo")
        self.tabview.add("Resumen Global") 

        self.tab_dashboard(self.tabview.tab("Tablas"))
        self.tab_parametros(self.tabview.tab("Parámetros"))
        self.tab_resumen(self.tabview.tab("Resumen Global"))

        self.mc_container = ctk.CTkFrame(self.tabview.tab("Monte Carlo"), fg_color="transparent")
        self.mc_container.pack(fill="both", expand=True)

        cols = (
            "dia", "clientes", "cola", "abandonos", "bebidas", "ingreso", "meseros_req", "bartender_req",
            "Rn1", "luz", "Rn2", "costag", "agua", 
            "rn_inc", "tipo_inc", "costo_inc",   
            "rn_ins", "tipo_ins", "costo_ins",   
            "utilidad", "mesas", "botellas", "limpieza_req", "beb_fav", "despidos_m", "despidos_b", "perdida"
        )
        
        self.tabla_mc = ttk.Treeview(self.mc_container, columns=cols, show="headings")
        
        self.tabla_mc.heading("dia", text="Días")
        self.tabla_mc.heading("clientes", text="Clientes")
        self.tabla_mc.heading("cola", text="Cola")
        self.tabla_mc.heading("abandonos", text="Aband.")
        self.tabla_mc.heading("bebidas", text="Bebidas")
        self.tabla_mc.heading("ingreso", text="Ingreso")
        self.tabla_mc.heading("meseros_req", text="Meseros Req.")
        self.tabla_mc.heading("bartender_req", text="Bartender Req.")
        self.tabla_mc.heading("Rn1", text="Rn Luz")
        self.tabla_mc.heading("luz", text="Costo Luz")
        self.tabla_mc.heading("Rn2", text="Rn Agua")
        self.tabla_mc.heading("costag", text="Tarifa Agua")
        self.tabla_mc.heading("agua", text="Costo Total Agua")
        self.tabla_mc.heading("rn_inc", text="Rn Incidente")
        self.tabla_mc.heading("tipo_inc", text="Tipo Incidente")
        self.tabla_mc.heading("costo_inc", text="Costo Incidente")
        self.tabla_mc.heading("rn_ins", text="Rn Insumo")
        self.tabla_mc.heading("tipo_ins", text="Tipo Insumo")
        self.tabla_mc.heading("costo_ins", text="Costo Insumo")
        self.tabla_mc.heading("utilidad", text="Utilidad Neta")
        self.tabla_mc.heading("mesas", text="Mesas Usadas")
        self.tabla_mc.heading("botellas", text="Botellas Alcohol")
        self.tabla_mc.heading("limpieza_req", text="Pers. Limpieza")
        self.tabla_mc.heading("beb_fav", text="Bebida Fav.")
        self.tabla_mc.heading("despidos_m", text="Despido Mesero")
        self.tabla_mc.heading("despidos_b", text="Despido Bartender")
        self.tabla_mc.heading("perdida", text="Pérdidas (Aband.)")
        
        for c in cols:
            self.tabla_mc.column(c, anchor="center", width=160)

        scroll_y = ttk.Scrollbar(self.mc_container, orient="vertical", command=self.tabla_mc.yview)
        scroll_x = ttk.Scrollbar(self.mc_container, orient="horizontal", command=self.tabla_mc.xview)
        
        self.tabla_mc.configure(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
        
        scroll_y.pack(side="right", fill="y")
        scroll_x.pack(side="bottom", fill="x")
        self.tabla_mc.pack(side="left", fill="both", expand=True)
        
        self.tabla_mc.bind("<Double-1>", self.on_double_click_mc)

    def tab_resumen(self, parent):
        self.resumen_labels = {}
        contenedor = ctk.CTkScrollableFrame(parent, fg_color="transparent")
        contenedor.pack(fill="both", expand=True, padx=20, pady=20)
        
        datos_resumen = [
            ("Ingresos Totales Brutos:", "$0.00"), ("Utilidad Neta (Ganancia Real):", "$0.00"),
            ("Pérdidas Totales por Abandono:", "$0.00"), ("Gasto Total en Sueldos (M+B+L):", "$0.00"),
            ("Gasto Total Insumos Extra:", "$0.00"), ("Gasto Total Limpieza (Insumos):", "$0.00"),
            ("Gasto Total Incidentes:", "$0.00"),
            ("Promedio Clientes/Día:", "0"), ("Promedio Bebidas/Día:", "0"),
            ("Bebida Global Más Consumida:", "---"), ("Total Botellas de Alcohol Vendidas:", "0"),
            ("Mesas Recomendadas (Máximo Pico):", "0")
        ]

        row_index = 0
        for txt, val in datos_resumen:
            ctk.CTkLabel(contenedor, text=txt, font=("Segoe UI", 16, "bold")).grid(row=row_index, column=0, sticky="w", pady=10, padx=20)
            lbl = ctk.CTkLabel(contenedor, text=val, font=("Segoe UI", 16), text_color="#10b981")
            lbl.grid(row=row_index, column=1, sticky="w", pady=10)
            self.resumen_labels[txt] = lbl
            row_index += 1

    def tab_dashboard(self, parent):
        def editar_celda(tabla, datos, fila, col):
            
            titulo_columna = str(datos[0][col])

            
            if "Acumulada" in titulo_columna or "Rango" in titulo_columna:
                return 

            
            ventana = ctk.CTkToplevel(self)
            ventana.title(f"Editando: {titulo_columna}")
            ventana.geometry("350x400") 
            ventana.grab_set()
            ventana.lift()                 
            ventana.attributes("-topmost", True)  
            ventana.focus_force()

            ctk.CTkLabel(ventana, text=f"Modificando columna: {titulo_columna}", font=("Arial", 14, "bold")).pack(pady=10)

            
            frame_entradas = ctk.CTkScrollableFrame(ventana, fg_color="transparent")
            frame_entradas.pack(fill="both", expand=True, padx=10, pady=5)

            
            entradas_texto = []

            
            for i in range(1, len(datos)):
                
                nombre_fila = str(datos[i][0])
                valor_actual = str(datos[i][col])

                
                ctk.CTkLabel(frame_entradas, text=nombre_fila, font=("Arial", 12)).pack(anchor="w", padx=5)
                
                
                entry = ctk.CTkEntry(frame_entradas, width=280)
                entry.insert(0, valor_actual)
                entry.pack(pady=(0, 10))

                
                entradas_texto.append((i, entry))

            
            def guardar_cambios():
                
                if "Probabilidad" in titulo_columna:
                    valores_nuevos = []
                    
                    
                    try:
                        for _, entry in entradas_texto:
                            valor = float(entry.get())
                            valores_nuevos.append(valor)
                    except ValueError:
                        
                        messagebox.showerror("Error de formato", "Por favor ingresa únicamente números con punto decimal.")
                        return

                    
                    suma_total = sum(valores_nuevos)
                    
                    if abs(suma_total - 1.0) > 0.0001:
                        messagebox.showerror("Error de Suma", f"La suma de las probabilidades debe dar exactamente 1.0\n\nTu suma actual da: {suma_total:.4f}\nPor favor, corrige los valores.")
                        return 
                    
                    
                    acumulado = 0.0
                    col_prob = col
                    col_acum = col + 1  
                    col_rango = col + 2 

                    for indice_lista, (fila_real, entry) in enumerate(entradas_texto):
                        prob_actual = valores_nuevos[indice_lista]
                        limite_inferior = acumulado
                        acumulado = acumulado + prob_actual
                        limite_superior = acumulado

                        
                        str_prob = str(prob_actual)
                        str_acum = f"{acumulado:.4f}"
                        
                        
                        if indice_lista == 0:
                            str_rango = f"0.0000 - {limite_superior:.4f}"
                        else:
                            str_rango = f"{(limite_inferior + 0.0001):.4f} - {limite_superior:.4f}"

                        
                        datos[fila_real][col_prob] = str_prob
                        datos[fila_real][col_acum] = str_acum
                        datos[fila_real][col_rango] = str_rango

                        
                        tabla.insert(fila_real, col_prob, str_prob)
                        tabla.insert(fila_real, col_acum, str_acum)
                        tabla.insert(fila_real, col_rango, str_rango)

                
                else:
                    for fila_real, entry in entradas_texto:
                        nuevo_valor = entry.get()
                        
                        datos[fila_real][col] = nuevo_valor
                        tabla.insert(fila_real, col, nuevo_valor)

                
                ventana.destroy()

            
            ctk.CTkButton(ventana, text="Guardar Cambios", fg_color="green", hover_color="darkgreen", command=guardar_cambios).pack(pady=10)

        inferior = ctk.CTkScrollableFrame(parent, fg_color="transparent")
        inferior.pack(fill="both", expand=True, padx=10, pady=10)

        # 1. Tabla Personas
        self.datos_personas = [["Personas que llegan", "Probabilidad", "Prob. Acumulada", "Rango (Rn)"], 
                               ["0", "0.15", "0.15", "0.0000 - 0.1500"], 
                               ["2", "0.4", "0.55", "0.1501 - 0.5500"], 
                               ["4", "0.25", "0.8", "0.5501 - 0.8000"], 
                               ["6", "0.15", "0.95", "0.8001 - 0.9500"], 
                               ["8", "0.05", "1", "0.9501 - 1.0000"]]
        tabla_personas = CTkTable(inferior, row=len(self.datos_personas), column=len(self.datos_personas[0]), values=self.datos_personas, header_color="#2632dc", command=lambda e: editar_celda(tabla_personas, self.datos_personas, e["row"], e["column"]))
        tabla_personas.pack(pady=10, fill="x")

        # 2. Tabla Espera
        self.min_lleg = [["Minutos de espera", "Probabilidad", "Prob. Acumulada", "Rango (Rn)"], 
                         ["2", "0.4", "0.4", "0.0000 - 0.4000"], 
                         ["5", "0.35", "0.75", "0.4001 - 0.7500"], 
                         ["8", "0.15", "0.9", "0.7501 - 0.9000"], 
                         ["10", "0.1", "1", "0.9001 - 1.0000"]]
        tabla_espera = CTkTable(inferior, row=len(self.min_lleg), column=len(self.min_lleg[0]), values=self.min_lleg, header_color="#2632dc", command=lambda e: editar_celda(tabla_espera, self.min_lleg, e["row"], e["column"]))
        tabla_espera.pack(pady=10, fill="x")

        # 3. Tabla Decisión
        self.decision = [["Decisión", "Probabilidad", "Prob. Acumulada", "Rango (Rn)"], 
                         ["Esperar", "0.25", "0.25", "0.000 - 0.250"], 
                         ["Abandonar", "0.75", "1.0", "0.251 - 1.0"]]
        tabla_decision = CTkTable(inferior, row=len(self.decision), column=len(self.decision[0]), values=self.decision, header_color="#951414", command=lambda e: editar_celda(tabla_decision, self.decision, e["row"], e["column"]))
        tabla_decision.pack(pady=10, fill="x")

        # 4. Tabla Tiempo Bar
        self.tiempo_bar = [["Tiempo en el Bar", "Probabilidad", "Prob. Acumulada", "Rango (Rn)"], 
                           ["30", "0.2", "0.2", "0.000 - 0.200"], 
                           ["45", "0.3", "0.5", "0.201 - 0.500"], 
                           ["60", "0.25", "0.75", "0.501 - 0.750"], 
                           ["90", "0.25", "1.0", "0.751 - 1.0"]]
        tabla_TiemBar = CTkTable(inferior, row=len(self.tiempo_bar), column=len(self.tiempo_bar[0]), values=self.tiempo_bar, header_color="#951414", command=lambda e: editar_celda(tabla_TiemBar, self.tiempo_bar, e["row"], e["column"]))
        tabla_TiemBar.pack(pady=10, fill="x")

        # 5. Tabla Bebidas
        self.bebidas = [["Tipo de Bebida", "Probabilidad", "Prob. Acumulada", "Rango (Rn)","Ganancia"], 
                        ["Bebida Simple", "0.5", "0.5", "0.000 - 0.500","42.00"], 
                        ["Preparado", "0.3", "0.8", "0.501 - 0.800","66.00"], 
                        ["Cocteleria", "0.15", "0.95", "0.801 - 0.950", "105.00"], 
                        ["Botella", "0.05", "1.0", "0.951 - 1.0","840.00"]]
        tabla_Beb = CTkTable(inferior, row=len(self.bebidas), column=len(self.bebidas[0]), values=self.bebidas, header_color="#7C4E03", command=lambda e: editar_celda(tabla_Beb, self.bebidas, e["row"], e["column"]))
        tabla_Beb.pack(pady=10, fill="x")

        # 6. Tabla Promedio
        self.promedio = [["Promedio bebidas", "Probabilidad", "Prob. Acumulada", "Rango (Rn)"], 
                         ["1.5", "0.1", "0.1", "0.000 - 0.100"], 
                         ["2.0", "0.25", "0.35", "0.101 - 0.350"], 
                         ["2.5", "0.35", "0.7", "0.351 - 0.700"], 
                         ["3.0", "0.2", "0.9", "0.701 - 0.900"], 
                         ["3.5", "0.1", "1.0", "0.901 - 1.0"]]
        tabla_prom = CTkTable(inferior, row=len(self.promedio), column=len(self.promedio[0]), values=self.promedio, header_color="#7C4E03", command=lambda e: editar_celda(tabla_prom, self.promedio, e["row"], e["column"]))
        tabla_prom.pack(pady=10, fill="x")

        # 7. Tabla Servicio Mesero
        self.serv_mesero = [["Servicio Mesero (min)", "Probabilidad", "Prob. Acumulada", "Rango"], 
                            ["5", "0.4", "0.4", "0.0-0.4"], 
                            ["10", "0.4", "0.8", "0.4-0.8"], 
                            ["15", "0.2", "1.0", "0.8-1.0"]]
        tabla_s_mes = CTkTable(inferior, row=len(self.serv_mesero), column=len(self.serv_mesero[0]), values=self.serv_mesero, header_color="#065f46", command=lambda e: editar_celda(tabla_s_mes, self.serv_mesero, e["row"], e["column"]))
        tabla_s_mes.pack(pady=10, fill="x")

        # 8. Tabla Preparación Bartender
        self.prep_bartender = [["Prep. Bartender (min)", "Probabilidad", "Prob. Acumulada", "Rango"], 
                               ["2", "0.5", "0.5", "0.0-0.5"], 
                               ["4", "0.3", "0.8", "0.5-0.8"], 
                               ["6", "0.2", "1.0", "0.8-1.0"]]
        tabla_s_bar = CTkTable(inferior, row=len(self.prep_bartender), column=len(self.prep_bartender[0]), values=self.prep_bartender, header_color="#065f46", command=lambda e: editar_celda(tabla_s_bar, self.prep_bartender, e["row"], e["column"]))
        tabla_s_bar.pack(pady=10, fill="x")

        # 9. Tabla Luz
        self.tabla_luz = [["Costo Luz Diario", "Probabilidad", "Prob. Acumulada", "Rango"], 
                          ["80.0", "0.3", "0.3", "0.0-0.3"], 
                          ["120.0", "0.5", "0.8", "0.3-0.8"], 
                          ["180.0", "0.2", "1.0", "0.8-1.0"]]
        t_luz = CTkTable(inferior, row=len(self.tabla_luz), column=len(self.tabla_luz[0]), values=self.tabla_luz, header_color="#4338ca", command=lambda e: editar_celda(t_luz, self.tabla_luz, e["row"], e["column"]))
        t_luz.pack(pady=10, fill="x")

        # 10. Tabla Agua
        self.tabla_agua = [["Costo Agua por Cliente", "Probabilidad", "Prob. Acumulada", "Rango"], 
                           ["1.5", "0.5", "0.5", "0.0-0.5"], 
                           ["2.5", "0.3", "0.8", "0.5-0.8"], 
                           ["4.0", "0.2", "1.0", "0.8-1.0"]]
        t_agua = CTkTable(inferior, row=len(self.tabla_agua), column=len(self.tabla_agua[0]), values=self.tabla_agua, header_color="#4338ca", command=lambda e: editar_celda(t_agua, self.tabla_agua, e["row"], e["column"]))
        t_agua.pack(pady=10, fill="x")
        
        # 11. Tabla Incidentes
        self.tabla_inc = [
            ["Tipo de Incidente", "Probabilidad", "Prob. Acumulada", "Rango", "Costo Consecuencia"], 
            ["Ninguno", "0.50", "0.50", "0.00-0.50", "0.0"], 
            ["Vaso Roto (Cobrar reposición)", "0.20", "0.70", "0.51-0.70", "300.0"], 
            ["Vómito (Limpieza profunda)", "0.10", "0.80", "0.71-0.80", "500.0"],
            ["Pelea (Pagar Seguridad/Multa)", "0.05", "0.85", "0.81-0.85", "1000.0"],
            ["Queja de cliente (Descuento dado)", "0.10", "0.95", "0.86-0.95", "200.0"],
            ["Fuga de agua (Llamar plomero)", "0.05", "1.00", "0.96-1.00", "800.0"]
        ]
        t_inc = CTkTable(inferior, row=len(self.tabla_inc), column=len(self.tabla_inc[0]), values=self.tabla_inc, header_color="#881337", command=lambda e: editar_celda(t_inc, self.tabla_inc, e["row"], e["column"]))
        t_inc.pack(pady=10, fill="x")

        # 12. Tabla Insumos
        self.tabla_insumos = [
            ["Tipo Insumo Extra", "Probabilidad", "Prob. Acumulada", "Rango", "Costo Extra"], 
            ["Ninguno", "0.30", "0.30", "0.00-0.30", "0.0"], 
            ["Hielo Extra", "0.25", "0.55", "0.31-0.55", "250.0"], 
            ["Cristalería de emergencia", "0.10", "0.65", "0.56-0.65", "800.0"],
            ["Artículos de Limpieza extra", "0.15", "0.80", "0.66-0.80", "300.0"],
            ["Garnituras extra (Limón, sal)", "0.10", "0.90", "0.81-0.90", "150.0"],
            ["Botanas extra", "0.10", "1.00", "0.91-1.00", "400.0"]
        ]
        t_ins = CTkTable(inferior, row=len(self.tabla_insumos), column=len(self.tabla_insumos[0]), values=self.tabla_insumos, header_color="#4338ca", command=lambda e: editar_celda(t_ins, self.tabla_insumos, e["row"], e["column"]))
        t_ins.pack(pady=10, fill="x")

    def tab_parametros(self, parent):
        self.inputs = {}
        # AGREGADO: Parámetro para saber cuántas bebidas rinde una botella
        params_list = [
            ("Días", "3"), ("Capacidad del Bar", "50"), ("Horas laborales", "8"), ("Hora de apertura", "8"), 
            ("Meseros", "2"), ("Bartenders", "1"), 
            ("Sueldo Mesero/Día", "300"), ("Sueldo Bartender/Día", "400"), ("Sueldo Limpieza/Día", "250"),
            ("Bebidas por Botella", "4"),("Promedio de consumo","150"),("Personal de Limpieza\nAtención Por Día","30")
        ]
        for i, (txt, val) in enumerate(params_list):
            ctk.CTkLabel(parent, text=txt).grid(row=i, column=0, padx=20, pady=10, sticky="w")
            ent = ctk.CTkEntry(parent, width=220)
            ent.grid(row=i, column=1, padx=10)
            ent.insert(0, val)
            self.inputs[txt] = ent

    def ejecutar(self):
        for item in self.tabla_mc.get_children(): 
            self.tabla_mc.delete(item)
            
        self.detalles_diarios = {}

        try:
            dias = int(self.inputs["Días"].get())
            capac = int(self.inputs["Capacidad del Bar"].get())
            horas = int(self.inputs["Horas laborales"].get())
            apertura = (self.inputs["Hora de apertura"].get())
            
            num_meseros = int(self.inputs["Meseros"].get())
            if num_meseros <= 0: num_meseros = 1  
            
            num_bartenders = int(self.inputs["Bartenders"].get())
            if num_bartenders <= 0: num_bartenders = 1 
            
            sueldo_m = float(self.inputs["Sueldo Mesero/Día"].get())
            sueldo_b = float(self.inputs["Sueldo Bartender/Día"].get())
            sueldo_l = float(self.inputs["Sueldo Limpieza/Día"].get())
            
            # NUEVO: Leer el rendimiento de la botella
            rendimiento_botella = int(self.inputs["Bebidas por Botella"].get())
            if rendimiento_botella <= 0: rendimiento_botella = 1 
            prom_cons= float(self.inputs["Promedio de consumo"].get())
            At_Lim=int(self.inputs["Personal de Limpieza\nAtención Por Día"].get())
            
            minutos_totales = horas * 60
        except: 
            return

        if apertura.isdigit():
            hora_base = datetime.strptime(f"{int(apertura):02d}:00", "%H:%M")
        else:
            hora_base = datetime.strptime(apertura, "%H:%M")
        
        total_meseros_sugeridos = 0
        total_bartenders_sugeridos = 0
        total_utilidad_simulacion = 0
        costo_total_ingreso = 0
        cliente_total = 0
        abandonos_total = 0
        cola_total = 0
        bebidas_totales = 0
        tot_perdidas = 0
        tot_sueldos = 0
        tot_insumos = 0
        tot_incidentes_costo = 0
        tot_limpieza = 0
        tot_botellas = 0
        max_mesas_global = 0
        conteo_global_beb = {}
        for i in range(1, len(self.bebidas)):
            nombre_bebida = self.bebidas[i][0]
            conteo_global_beb[nombre_bebida] = 0

        for d in range(1, dias + 1):
            tiempo_actual = 0
            clientes_dia = 0
            acumulado = 0
            ocup_act = 0
            cola_variable = 0
            abandonos_acum = 0
            total_cola_dia = 0
            total_bebidas_dia = 0
            total_ingresos_dia = 0
            carga_trabajo_meseros = 0
            carga_trabajo_bartenders = 0
            personas_adentro = []
            log_llegadas = []
            max_ocupacion_dia = 0 
            
            conteo_beb_dia = {}
            for i in range(1, len(self.bebidas)):
                nombre_bebida = self.bebidas[i][0]
                conteo_beb_dia[nombre_bebida] = 0

            reloj_meseros = [0] * num_meseros
            reloj_bartenders = [0] * num_bartenders

            while tiempo_actual < minutos_totales:
                rn_ll = self.obtener_aleatorio()
                grupo = self.pers(rn_ll)
                
                rn_min = self.obtener_aleatorio()
                m = self.minutos(rn_min)
                
                acumulado = acumulado + m 
                hora_llegada = hora_base + timedelta(minutes=acumulado)
                tiempo_actual = tiempo_actual + m
                
                if tiempo_actual >= minutos_totales: 
                    break

                salieron_ahora = 0
                i = 0
                while i < len(personas_adentro):
                    h_salida, cant_sale = personas_adentro[i]
                    if h_salida <= hora_llegada:
                        salieron_ahora = salieron_ahora + cant_sale 
                        ocup_act = ocup_act - cant_sale
                        personas_adentro.pop(i)
                        
                        if cola_variable > 0:
                            espacios_libres = capac - ocup_act
                            pueden_entrar = min(cola_variable, espacios_libres)
                            
                            if pueden_entrar > 0:
                                cola_variable = cola_variable - pueden_entrar
                                ocup_act = ocup_act + pueden_entrar
                                rn_permanencia_cola = self.obtener_aleatorio()
                                h_salida_cola = hora_llegada + timedelta(minutes=self.tiem_perman(rn_permanencia_cola))
                                personas_adentro.append((h_salida_cola, pueden_entrar))
                    else: 
                        i = i + 1

                rn_des = self.obtener_aleatorio()
                rn_ida = self.obtener_aleatorio()
                des = "---"
                perm = 0
                hora_salida_str = "---"
                rn_beb = 0
                tipo_b = "---"
                rn_p_beb = 0
                prom = 0
                beb_consumidas = 0
                pago_total = 0
                rn_s_mes = 0
                t_mesero = 0
                rn_s_bar = 0
                t_bartender = 0
                
                mesero_asignado = "---"
                ocio_mesero_min = 0
                bartender_asignado = "---"
                ocio_bartender_min = 0

                if ocup_act + grupo <= capac:
                    ocup_act = ocup_act + grupo
                    
                    if ocup_act > max_ocupacion_dia:
                        max_ocupacion_dia = ocup_act 
                        
                    perm = self.tiem_perman(rn_ida)
                    des = "Entra"

                    rn_beb = self.obtener_aleatorio()
                    tipo_b = self.Bebidas(rn_beb)
                    
                    rn_p_beb = self.obtener_aleatorio()
                    prom = self.prom_beb(rn_p_beb)
                    beb_consumidas = grupo * prom
                    
                    for row in self.bebidas:
                        if row[0] == tipo_b: 
                            precio = float(row[4])
                            pago_total = beb_consumidas * precio

                    total_bebidas_dia = total_bebidas_dia + beb_consumidas
                    total_ingresos_dia = total_ingresos_dia + pago_total
                    
                    # ALMACENAMOS LOS VASOS CONSUMIDOS EN EL DICCIONARIO
                    if tipo_b in conteo_beb_dia:
                        conteo_beb_dia[tipo_b] = conteo_beb_dia[tipo_b] + beb_consumidas
                        conteo_global_beb[tipo_b] = conteo_global_beb[tipo_b] + beb_consumidas

                    rn_s_mes = self.obtener_aleatorio()
                    t_mesero = self.get_tiempo_servicio(rn_s_mes, self.serv_mesero)
                    
                    rn_s_bar = self.obtener_aleatorio()
                    t_bartender = self.get_tiempo_servicio(rn_s_bar, self.prep_bartender)
                    
                    carga_trabajo_meseros = carga_trabajo_meseros + t_mesero
                    carga_trabajo_bartenders = carga_trabajo_bartenders + (t_bartender * beb_consumidas)
                    
                    mesero_libre = min(reloj_meseros)
                    idx_mesero = reloj_meseros.index(mesero_libre)
                    mesero_asignado = f"M-{idx_mesero + 1}"
                    
                    if tiempo_actual > mesero_libre:
                        ocio_mesero_min = tiempo_actual - mesero_libre
                    else:
                        ocio_mesero_min = 0
                    
                    inicio_atencion_mesero = max(tiempo_actual, mesero_libre)
                    espera_por_mesero = inicio_atencion_mesero - tiempo_actual
                    fin_atencion_mesero = inicio_atencion_mesero + t_mesero
                    reloj_meseros[idx_mesero] = fin_atencion_mesero 
                    
                    bartender_libre = min(reloj_bartenders)
                    idx_bar = reloj_bartenders.index(bartender_libre)
                    bartender_asignado = f"B-{idx_bar + 1}"
                    
                    if fin_atencion_mesero > bartender_libre:
                        ocio_bartender_min = fin_atencion_mesero - bartender_libre
                    else:
                        ocio_bartender_min = 0
                        
                    inicio_atencion_bar = max(fin_atencion_mesero, bartender_libre)
                    espera_por_bar = inicio_atencion_bar - fin_atencion_mesero
                    tiempo_preparacion_total = t_bartender * beb_consumidas
                    fin_atencion_bar = inicio_atencion_bar + tiempo_preparacion_total
                    reloj_bartenders[idx_bar] = fin_atencion_bar
                    
                    espera_total_servicio = espera_por_mesero + t_mesero + espera_por_bar + tiempo_preparacion_total
                    
                    h_salida_nuevo = hora_llegada + timedelta(minutes=int(espera_total_servicio + perm))
                    personas_adentro.append((h_salida_nuevo, grupo))

                    hora_salida_str = h_salida_nuevo.strftime('%H:%M')
                    
                else:
                    decision_tomada = self.desicion_bar(rn_des)
                    if decision_tomada == "Esperar":
                        cola_variable = cola_variable + grupo
                        total_cola_dia = total_cola_dia + grupo
                        des = "A Cola"
                    else:
                        abandonos_acum = abandonos_acum + grupo
                        des = "Abandona"

                clientes_dia = clientes_dia + grupo
                
                log_llegadas.append((
                    f"{rn_ll:.4f}", grupo, f"{rn_min:.4f}", m, hora_llegada.strftime('%H:%M'), 
                    f"{rn_des:.4f}", des, f"{rn_ida:.4f}", perm, hora_salida_str, 
                    salieron_ahora, ocup_act, cola_variable, abandonos_acum, 
                    f"{rn_beb:.4f}", tipo_b, f"{rn_p_beb:.4f}", prom, f"{beb_consumidas:.1f}", f"${pago_total:.2f}", 
                    f"{rn_s_mes:.4f}", t_mesero, mesero_asignado, ocio_mesero_min,  
                    f"{rn_s_bar:.4f}", t_bartender, bartender_asignado, ocio_bartender_min 
                ))

            # --- CÁLCULOS FINALES DEL DÍA ---
            rn_luz = self.obtener_aleatorio()
            costo_luz_dia = self.costo_luz(rn_luz)
            
            rn_agua = self.obtener_aleatorio()
            tarifa_agua = self.costo_agua(rn_agua)
            costo_agua_total = tarifa_agua * clientes_dia
            
            rn_inc = self.obtener_aleatorio()
            tipo_incidente, costo_incidente = self.get_incidente_detalle(rn_inc)
            
            rn_ins = self.obtener_aleatorio()
            tipo_insumo, costo_insumo = self.get_insumo_detalle(rn_ins)
            
            perdida_abandonos = abandonos_acum * prom_cons
            
            personal_limpieza = math.ceil(max_ocupacion_dia / At_Lim)
            if personal_limpieza == 0: 
                personal_limpieza = 1
                
            costo_material_limpieza = clientes_dia * 2.0
            costo_sueldo_limpieza = personal_limpieza * sueldo_l
            costo_limpieza_total_dia = costo_material_limpieza + costo_sueldo_limpieza
                
            mesas_usadas = math.ceil(max_ocupacion_dia / 4)
            if mesas_usadas > max_mesas_global:
                max_mesas_global = mesas_usadas
            
            bebida_fav_dia = "---"
            mayor_cantidad = -1
            for bebida, cantidad in conteo_beb_dia.items():
                if cantidad > mayor_cantidad:
                    mayor_cantidad = cantidad
                    bebida_fav_dia = bebida
            
            
            nombre_columna_botella = self.bebidas[4][0]

            tragos_vendidos_botella = conteo_beb_dia.get(nombre_columna_botella, 0)
            botellas_abiertas_dia = math.ceil(tragos_vendidos_botella / rendimiento_botella)
            
            
            sueldos_dia = (num_meseros * sueldo_m) + (num_bartenders * sueldo_b) + costo_sueldo_limpieza
            
            utilidad_dia = total_ingresos_dia - (
                costo_luz_dia + costo_agua_total + sueldos_dia + costo_incidente + costo_insumo + costo_material_limpieza
            )
            
            meseros_necesarios = math.ceil(carga_trabajo_meseros / minutos_totales)
            bartenders_necesarios = math.ceil(carga_trabajo_bartenders / minutos_totales)
            
            despidos_m = num_meseros - meseros_necesarios
            if despidos_m < 0: despidos_m = 0
            
            despidos_b = num_bartenders - bartenders_necesarios
            if despidos_b < 0: despidos_b = 0

            cliente_total = cliente_total + clientes_dia
            cola_total = cola_total + total_cola_dia
            abandonos_total = abandonos_total + abandonos_acum
            costo_total_ingreso = costo_total_ingreso + total_ingresos_dia
            bebidas_totales = bebidas_totales + total_bebidas_dia
            total_utilidad_simulacion = total_utilidad_simulacion + utilidad_dia
            tot_perdidas = tot_perdidas + perdida_abandonos
            tot_sueldos = tot_sueldos + sueldos_dia
            tot_insumos = tot_insumos + costo_insumo
            tot_incidentes_costo = tot_incidentes_costo + costo_incidente
            tot_limpieza = tot_limpieza + costo_limpieza_total_dia
            
            
            tot_botellas = tot_botellas + botellas_abiertas_dia
            
            if meseros_necesarios > total_meseros_sugeridos:
                total_meseros_sugeridos = meseros_necesarios
            if bartenders_necesarios > total_bartenders_sugeridos:
                total_bartenders_sugeridos = bartenders_necesarios

            self.detalles_diarios[d] = log_llegadas
            
            
            self.tabla_mc.insert("", "end", values=(
                f"Día {d}", clientes_dia, total_cola_dia, abandonos_acum, f"{total_bebidas_dia:.1f}", 
                f"${total_ingresos_dia:,.2f}", meseros_necesarios, bartenders_necesarios,
                f"{rn_luz:.4f}", f"${costo_luz_dia:.2f}", f"{rn_agua:.4f}", f"${tarifa_agua:.2f}", f"${costo_agua_total:.2f}", 
                f"{rn_inc:.4f}", tipo_incidente, f"${costo_incidente:.2f}",  
                f"{rn_ins:.4f}", tipo_insumo, f"${costo_insumo:.2f}",        
                f"${utilidad_dia:,.2f}", mesas_usadas, f"{botellas_abiertas_dia}", personal_limpieza, 
                bebida_fav_dia, despidos_m, despidos_b, f"${perdida_abandonos:,.2f}"
            ))

        if (num_meseros >= total_meseros_sugeridos) and (num_bartenders >= total_bartenders_sugeridos):
            abasto = "SÍ"
        else:
            abasto = "NO"
            
        self.kpis_labels["Clientes"].configure(text=str(cliente_total))
        self.kpis_labels["Abandonos"].configure(text=str(abandonos_total))
        self.kpis_labels["Espera"].configure(text=str(cola_total))
        self.kpis_labels["Meseros Sugeridos"].configure(text=str(total_meseros_sugeridos))
        self.kpis_labels["Bartenders Sugeridos"].configure(text=str(total_bartenders_sugeridos))
        self.kpis_labels["Utilidad Total"].configure(text=f"${total_utilidad_simulacion:,.2f}")
        
        if abasto == "SÍ":
            self.kpis_labels["Abasto Personal"].configure(text=abasto, text_color="green")
        else:
            self.kpis_labels["Abasto Personal"].configure(text=abasto, text_color="red")
            
        self.kpis_labels["Ingresos"].configure(text=str(f"${costo_total_ingreso:,.2f}"))
        
        bebida_fav_global = "Ninguna"
        mayor_cantidad = -1
        for bebida, cantidad in conteo_global_beb.items():
            if cantidad > mayor_cantidad:
                mayor_cantidad = cantidad
                bebida_fav_global = bebida
        
        self.resumen_labels["Ingresos Totales Brutos:"].configure(text=f"${costo_total_ingreso:,.2f}")
        
        if total_utilidad_simulacion > 0:
            self.resumen_labels["Utilidad Neta (Ganancia Real):"].configure(text=f"${total_utilidad_simulacion:,.2f}", text_color="green")
        else:
            self.resumen_labels["Utilidad Neta (Ganancia Real):"].configure(text=f"${total_utilidad_simulacion:,.2f}", text_color="red")
            
        self.resumen_labels["Pérdidas Totales por Abandono:"].configure(text=f"${tot_perdidas:,.2f}", text_color="red")
        self.resumen_labels["Gasto Total en Sueldos (M+B+L):"].configure(text=f"${tot_sueldos:,.2f}")
        self.resumen_labels["Gasto Total Insumos Extra:"].configure(text=f"${tot_insumos:,.2f}")
        self.resumen_labels["Gasto Total Limpieza (Insumos):"].configure(text=f"${tot_limpieza:,.2f}")
        self.resumen_labels["Gasto Total Incidentes:"].configure(text=f"${tot_incidentes_costo:,.2f}")
        
        promedio_clientes = cliente_total // dias
        self.resumen_labels["Promedio Clientes/Día:"].configure(text=f"{promedio_clientes}")
        
        promedio_bebidas = bebidas_totales / dias
        self.resumen_labels["Promedio Bebidas/Día:"].configure(text=f"{promedio_bebidas:.1f}")
        
        self.resumen_labels["Bebida Global Más Consumida:"].configure(text=bebida_fav_global)
        
        # EL RESUMEN AHORA MUESTRA EL NÚMERO DE BOTELLAS REALES ABIERTAS
        self.resumen_labels["Total Botellas de Alcohol Vendidas:"].configure(text=f"{tot_botellas} Botellas")
        
        self.resumen_labels["Mesas Recomendadas (Máximo Pico):"].configure(text=f"{max_mesas_global} Mesas")

        self.tabview.set("Resumen Global")
    
    def get_incidente_detalle(self, alea):
        for i in range(1, len(self.tabla_inc)):
            limite_superior = float(self.tabla_inc[i][2])
            if alea < limite_superior:
                tipo = self.tabla_inc[i][0]
                costo = float(self.tabla_inc[i][4])
                return tipo, costo
        return self.tabla_inc[1][0], float(self.tabla_inc[1][4])

    def get_insumo_detalle(self, alea):
        for i in range(1, len(self.tabla_insumos)):
            limite_superior = float(self.tabla_insumos[i][2])
            if alea < limite_superior:
                tipo = self.tabla_insumos[i][0]
                costo = float(self.tabla_insumos[i][4])
                return tipo, costo
        return self.tabla_insumos[1][0], float(self.tabla_insumos[1][4])

    def costo_luz(self, alea):
        for i in range(1, len(self.tabla_luz)):
            if alea < float(self.tabla_luz[i][2]): 
                return float(self.tabla_luz[i][0])
        return float(self.tabla_luz[1][0])

    def costo_agua(self, alea):
        for i in range(1, len(self.tabla_agua)):
            if alea < float(self.tabla_agua[i][2]): 
                return float(self.tabla_agua[i][0])
        return float(self.tabla_agua[1][0])

    def pers(self,alea):
        for i in range(1,len(self.datos_personas)):
            if alea < float(self.datos_personas[i][2]): 
                return int(self.datos_personas[i][0])
                
    def minutos(self,alea):
        for i in range(1,len(self.min_lleg)):
            if alea < float(self.min_lleg[i][2]): 
                return int(self.min_lleg[i][0])
                
    def desicion_bar(self,alea):
        for i in range(1,len(self.decision)):
            if alea < float(self.decision[i][2]): 
                return (self.decision[i][0])
                
    def tiem_perman(self,alea):
        for i in range(1,len(self.tiempo_bar)):
            if alea < float(self.tiempo_bar[i][2]): 
                return int(self.tiempo_bar[i][0])
                
    def prom_beb(self, alea):
        for i in range(1, len(self.promedio)):
            if alea < float(self.promedio[i][2]): 
                return float(self.promedio[i][0])
        return 0
        
    def Bebidas(self, alea):
        for i in range(1, len(self.bebidas)):
            if alea < float(self.bebidas[i][2]): 
                return self.bebidas[i][0]
        return "---"
        
    def get_tiempo_servicio(self, alea, tabla):
        for i in range(1, len(tabla)):
            if alea < float(tabla[i][2]): 
                return int(tabla[i][0])
        return int(tabla[1][0])
    
    def on_double_click_mc(self, event):
        item = self.tabla_mc.selection()[0]
        val = self.tabla_mc.item(item, "values")[0]
        self.mostrar_ventana_detalle(int(val.replace("Día ", "")))

    def mostrar_ventana_detalle(self, dia):
        ventana = ctk.CTkToplevel(self)
        ventana.title(f"Detalle Día {dia}")
        ventana.geometry("1550x700")
        ventana.lift() 
        ventana.focus_force() 
        ventana.attributes("-topmost", True)
        
        container = ctk.CTkFrame(ventana)
        container.pack(fill="both", expand=True, padx=20, pady=20)
        
        cols = (
            "Rn1", "cantidad","Rn2","minuto","hora","Rn3","desic","Rn4","perm","hora_ida", "salieron", 
            "ocup_bar", "cola", "abandonos", "rn_b", "tipo", "rn_p", "prom", "tot_beb", "pago", 
            "rn_mes", "t_mes", "quien_mes", "ocio_mes",
            "rn_bar", "t_bar", "quien_bar", "ocio_bar" 
        )
        
        style = ttk.Style()
        style.configure("Treeview", font=("Helvetica", 11))
        style.configure("Treeview.Heading", font=("Times New Roman", 12, "bold"))

        tabla_det = ttk.Treeview(container, columns=cols, show="headings")
        
        scroll_y = ttk.Scrollbar(container, orient="vertical", command=tabla_det.yview)
        scroll_x = ttk.Scrollbar(container, orient="horizontal", command=tabla_det.xview)
        tabla_det.configure(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
        
        scroll_y.pack(side="right", fill="y")
        scroll_x.pack(side="bottom", fill="x")
        tabla_det.pack(side="left", fill="both", expand=True)
        
        headings = [
            ("Rn1", "Rn Llegada"), ("cantidad", "Grupo"), ("Rn2", "Rn Minutos"), ("minuto", "Min_Lleg"), ("hora", "Hora Llegada"), 
            ("Rn3", "Rn Decisión"), ("desic", "Acción"), ("Rn4", "Rn Permanencia"), ("perm", "Min_Perm"), ("hora_ida", "Hora Salida"), 
            ("salieron", "Salieron"), ("ocup_bar", "En Bar"), ("cola", "En Cola"), ("abandonos", "Aband. Acum"), 
            ("rn_b", "Rn Bebida"), ("tipo", "Tipo Bebida"), ("rn_p", "Rn Promedio"), ("prom", "Promedio"), ("tot_beb", "Beb. Totales"), 
            ("pago", "Pago Total $"), 
            ("rn_mes", "Rn Mesero"), ("t_mes", "Tiempo Mesero"), ("quien_mes", "ID Mesero"), ("ocio_mes", "Ocio Mesero (min)"),
            ("rn_bar", "Rn Bartender"), ("t_bar", "Tiempo Bartender"), ("quien_bar", "ID Bartender"), ("ocio_bar", "Ocio Bartender (min)")
        ]
        
        for col, txt in headings:
            tabla_det.heading(col, text=txt)
            tabla_det.column(col, width=155, anchor="center")
        
        if dia in self.detalles_diarios:
            for fila in self.detalles_diarios[dia]: 
                tabla_det.insert("", "end", values=fila)

    def nueva_simul(self):
        for item in self.tabla_mc.get_children(): 
            self.tabla_mc.delete(item)
            
        self.detalles_diarios = {}
        
        for k in self.kpis_labels: 
            self.kpis_labels[k].configure(text="---")
            
        for k in self.resumen_labels: 
            self.resumen_labels[k].configure(text="---")
    

    def cargar_archivo_aleatorios(self, subcarpeta_y_nombre):
        # 1. Obtenemos la ruta absoluta de la carpeta donde está guardado V6.py
        directorio_actual = os.path.dirname(os.path.abspath(__file__))
        
        # 2. Combinamos esa ruta con la subcarpeta y el nombre del archivo
        # Esto hace que Python sepa exactamente dónde buscar, sin importar desde dónde lo ejecutes
        ruta_completa = os.path.join(directorio_actual, subcarpeta_y_nombre)
        
        try:
            with open(ruta_completa, "r") as f:
                self.lista_aleatorios = []
                for line in f:
                    linea_limpia = line.strip()
                    if linea_limpia != "":
                        self.lista_aleatorios.append(float(linea_limpia))
            
            print(f"Éxito: Se cargaron {len(self.lista_aleatorios)} números desde: {ruta_completa}")
            
        except FileNotFoundError:
            print(f"Error: No se pudo encontrar el archivo en la ruta: {ruta_completa}")
            self.lista_aleatorios = [0.5]

    def obtener_aleatorio(self):
        #if self.indice_aleatorio >= len(self.lista_aleatorios):
        #    self.indice_aleatorio = 0
        #numero = self.lista_aleatorios[self.indice_aleatorio]
        #self.indice_aleatorio += 1
        
        n=random.randint(0,len(self.lista_aleatorios)-1)
        numero = self.lista_aleatorios[n]
        return numero

if __name__ == "__main__":
    root = ctk.CTk(); root.withdraw() 
    app = Bar(master=root); root.mainloop()