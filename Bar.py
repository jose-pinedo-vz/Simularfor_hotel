import customtkinter as ctk
from CTkTable import CTkTable
from tkinter import ttk
import random
from datetime import datetime, timedelta
import math

class Bar(ctk.CTkToplevel):

    def __init__(self, master=None):
        super().__init__(master)
        self.detalles_diarios = {} 

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
        # SE AGREGA KPI DE UTILIDAD
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

        self.tab_dashboard(self.tabview.tab("Tablas"))
        self.tab_parametros(self.tabview.tab("Parámetros"))

        self.mc_container = ctk.CTkFrame(self.tabview.tab("Monte Carlo"), fg_color="transparent")
        self.mc_container.pack(fill="both", expand=True)

        
        cols = ("dia", "clientes", "cola", "abandonos", "bebidas", "ingreso", "meseros_req", "bartender_req","Rn1","luz", "Rn2","costag","agua", "utilidad")
        self.tabla_mc = ttk.Treeview(self.mc_container, columns=cols, show="headings")
        self.tabla_mc.heading("dia", text="Días")
        self.tabla_mc.heading("clientes", text="Clientes")
        self.tabla_mc.heading("cola", text="Cola")
        self.tabla_mc.heading("abandonos", text="Aband.")
        self.tabla_mc.heading("bebidas", text="Bebidas")
        self.tabla_mc.heading("ingreso", text="Ingreso")
        self.tabla_mc.heading("meseros_req", text="Meseros Req.")
        self.tabla_mc.heading("bartender_req", text="Bartender Req.")
        self.tabla_mc.heading("Rn1", text="Rn")
        self.tabla_mc.heading("luz", text="Costo Luz")
        self.tabla_mc.heading("Rn2", text="Rn")
        self.tabla_mc.heading("costag", text="Costo_Agua")
        self.tabla_mc.heading("agua", text="Costo_Tot_Agua")
        self.tabla_mc.heading("utilidad", text="Utilidad")
        
        for c in cols:
            self.tabla_mc.column(c, anchor="center", width=100)

        scroll = ttk.Scrollbar(self.mc_container, orient="vertical", command=self.tabla_mc.yview)
        self.tabla_mc.configure(yscrollcommand=scroll.set)
        self.tabla_mc.pack(side="left", fill="both", expand=True)
        scroll.pack(side="right", fill="y")
        self.tabla_mc.bind("<Double-1>", self.on_double_click_mc)

    def tab_dashboard(self, parent):
        def editar_celda(tabla, datos, fila, col):
            if fila == 0: return
            ventana = ctk.CTkToplevel(self)
            ventana.title("Editar valor")
            ventana.geometry("300x140")
            ventana.grab_set()
            ventana.lift()                 
            ventana.attributes("-topmost", True)  
            ventana.focus_force()
            ctk.CTkLabel(ventana, text=f"Fila {fila} Columna {col}", font=("Arial", 14, "bold")).pack(pady=10)
            entry = ctk.CTkEntry(ventana, width=220)
            entry.pack(pady=5)
            entry.insert(0, str(datos[fila][col]))
            def guardar():
                nuevo = entry.get()
                datos[fila][col] = nuevo
                tabla.insert(fila, col, nuevo)
                ventana.destroy()
            ctk.CTkButton(ventana, text="Guardar", command=guardar).pack(pady=10)

        inferior = ctk.CTkScrollableFrame(parent, fg_color="transparent")
        inferior.pack(fill="both", expand=True, padx=10, pady=10)

        # Tablas de lógica ya existentes...
        self.datos_personas = [["Personas que llegan", "Probabilidad", "Prob. Acumulada", "Rango (Rn)"], 
                               ["0", "0.15", "0.15", "0.0000 - 0.1500"], 
                               ["2", "0.4", "0.55", "0.1501 - 0.5500"], 
                               ["4", "0.25", "0.8", "0.5501 - 0.8000"], 
                               ["6", "0.15", "0.95", "0.8001 - 0.9500"], 
                               ["8", "0.05", "1", "0.9501 - 1.0000"]]
        tabla_personas = CTkTable(inferior, row=len(self.datos_personas), column=len(self.datos_personas[0]), values=self.datos_personas, header_color="#2632dc", command=lambda e: editar_celda(tabla_personas, self.datos_personas, e[0], e[1]))
        tabla_personas.pack(pady=10, fill="x")

        self.min_lleg = [["Minutos de espera", "Probabilidad", "Prob. Acumulada", "Rango (Rn)"], 
                         ["2", "0.4", "0.4", "0.0000 - 0.4000"], 
                         ["5", "0.35", "0.75", "0.4001 - 0.7500"], 
                         ["8", "0.15", "0.9", "0.7501 - 0.9000"], 
                         ["10", "0.1", "1", "0.9001 - 1.0000"]]
        tabla_espera = CTkTable(inferior, row=len(self.min_lleg), column=len(self.min_lleg[0]), values=self.min_lleg, header_color="#2632dc", command=lambda e: editar_celda(tabla_espera, self.min_lleg, e[0], e[1]))
        tabla_espera.pack(pady=10, fill="x")

        self.decision = [["Decisión", "Probabilidad", "Prob. Acumulada", "Rango (Rn)"], 
                         ["Esperar", "0.25", "0.25", "0.000 - 0.250"], 
                         ["Abandonar", "0.75", "1.0", "0.251 - 1.0"]]
        tabla_decision = CTkTable(inferior, row=len(self.decision), column=len(self.decision[0]), values=self.decision, header_color="#951414", command=lambda e: editar_celda(tabla_decision, self.decision, e[0], e[1]))
        tabla_decision.pack(pady=10, fill="x")

        self.tiempo_bar = [["Tiempo en el Bar", "Probabilidad", "Prob. Acumulada", "Rango (Rn)"], 
                           ["30", "0.2", "0.2", "0.000 - 0.200"], 
                           ["45", "0.3", "0.5", "0.201 - 0.500"], 
                           ["60", "0.25", "0.75", "0.501 - 0.750"], 
                           ["90", "0.25", "1.0", "0.751 - 1.0"]]
        tabla_TiemBar = CTkTable(inferior, row=len(self.tiempo_bar), column=len(self.tiempo_bar[0]), values=self.tiempo_bar, header_color="#951414", command=lambda e: editar_celda(tabla_TiemBar, self.tiempo_bar, e[0], e[1]))
        tabla_TiemBar.pack(pady=10, fill="x")

        self.bebidas = [["Tipo de Bebida", "Probabilidad", "Prob. Acumulada", "Rango (Rn)","Ganancia"], 
                        ["Bebida Simple", "0.5", "0.5", "0.000 - 0.500","42.00"], 
                        ["Preparado", "0.3", "0.8", "0.501 - 0.800","66.00"], 
                        ["Cocteleria", "0.15", "0.95", "0.801 - 0.950", "105.00"], 
                        ["Botella", "0.05", "1.0", "0.951 - 1.0","840.00"]]
        tabla_Beb = CTkTable(inferior, row=len(self.bebidas), column=len(self.bebidas[0]), values=self.bebidas, header_color="#7C4E03", command=lambda e: editar_celda(tabla_Beb, self.bebidas, e[0], e[1]))
        tabla_Beb.pack(pady=10, fill="x")

        self.promedio = [["Promedio bebidas", "Probabilidad", "Prob. Acumulada", "Rango (Rn)"], 
                         ["1.5", "0.1", "0.1", "0.000 - 0.100"], 
                         ["2.0", "0.25", "0.35", "0.101 - 0.350"], 
                         ["2.5", "0.35", "0.7", "0.351 - 0.700"], 
                         ["3.0", "0.2", "0.9", "0.701 - 0.900"], 
                         ["3.5", "0.1", "1.0", "0.901 - 1.0"]]
        tabla_prom = CTkTable(inferior, row=len(self.promedio), column=len(self.promedio[0]), values=self.promedio, header_color="#7C4E03", command=lambda e: editar_celda(tabla_prom, self.promedio, e[0], e[1]))
        tabla_prom.pack(pady=10, fill="x")

        self.serv_mesero = [["Servicio Mesero (min)", "Probabilidad", "Prob. Acumulada", "Rango"], 
                            ["5", "0.4", "0.4", "0.0-0.4"], 
                            ["10", "0.4", "0.8", "0.4-0.8"], 
                            ["15", "0.2", "1.0", "0.8-1.0"]]
        tabla_s_mes = CTkTable(inferior, row=len(self.serv_mesero), column=len(self.serv_mesero[0]), values=self.serv_mesero, header_color="#065f46", command=lambda e: editar_celda(tabla_s_mes, self.serv_mesero, e[0], e[1]))
        tabla_s_mes.pack(pady=10, fill="x")

        self.prep_bartender = [["Prep. Bartender (min)", "Probabilidad", "Prob. Acumulada", "Rango"], 
                               ["2", "0.5", "0.5", "0.0-0.5"], 
                               ["4", "0.3", "0.8", "0.5-0.8"], 
                               ["6", "0.2", "1.0", "0.8-1.0"]]
        tabla_s_bar = CTkTable(inferior, row=len(self.prep_bartender), column=len(self.prep_bartender[0]), values=self.prep_bartender, header_color="#065f46", command=lambda e: editar_celda(tabla_s_bar, self.prep_bartender, e[0], e[1]))
        tabla_s_bar.pack(pady=10, fill="x")

        #TABLAS: GASTOS DE LUZ Y AGUA
        self.tabla_luz = [["Costo Luz Diario", "Probabilidad", "Prob. Acumulada", "Rango"], 
                          ["80.0", "0.3", "0.3", "0.0-0.3"], 
                          ["120.0", "0.5", "0.8", "0.3-0.8"], 
                          ["180.0", "0.2", "1.0", "0.8-1.0"]]
        t_luz = CTkTable(inferior, row=len(self.tabla_luz), column=len(self.tabla_luz[0]), values=self.tabla_luz, header_color="#4338ca", command=lambda e: editar_celda(t_luz, self.tabla_luz, e[0], e[1]))
        t_luz.pack(pady=10, fill="x")

        self.tabla_agua = [["Costo Agua por Cliente", "Probabilidad", "Prob. Acumulada", "Rango"], 
                           ["1.5", "0.5", "0.5", "0.0-0.5"], 
                           ["2.5", "0.3", "0.8", "0.5-0.8"], 
                           ["4.0", "0.2", "1.0", "0.8-1.0"]]
        t_agua = CTkTable(inferior, row=len(self.tabla_agua), column=len(self.tabla_agua[0]), values=self.tabla_agua, header_color="#4338ca", command=lambda e: editar_celda(t_agua, self.tabla_agua, e[0], e[1]))
        t_agua.pack(pady=10, fill="x")

    def tab_parametros(self, parent):
        self.inputs = {}
        params_list = [("Días", "3"), ("Capacidad del Bar", "50"), ("Horas laborales", "8"), ("Hora de apertura", "8"), ("Meseros", "2"), ("Bartenders", "1")]
        for i, (txt, val) in enumerate(params_list):
            ctk.CTkLabel(parent, text=txt).grid(row=i, column=0, padx=20, pady=10, sticky="w")
            ent = ctk.CTkEntry(parent, width=220)
            ent.grid(row=i, column=1, padx=10)
            ent.insert(0, val)
            self.inputs[txt] = ent

    def ejecutar(self):
        for item in self.tabla_mc.get_children(): self.tabla_mc.delete(item)
        self.detalles_diarios = {}

        try:
            dias = int(self.inputs["Días"].get())
            capac = int(self.inputs["Capacidad del Bar"].get())
            horas = int(self.inputs["Horas laborales"].get())
            apertura = (self.inputs["Hora de apertura"].get())
            num_meseros = int(self.inputs["Meseros"].get())
            num_bartenders = int(self.inputs["Bartenders"].get())
            minutos_totales = horas * 60
        except: return

        hora_base = datetime.strptime(f"{int(apertura):02d}:00" if apertura.isdigit() else apertura, "%H:%M")
        total_meseros_sugeridos, total_bartenders_sugeridos = 0, 0
        total_utilidad_simulacion = 0
        costo_total_ingreso=0
        cliente_total=0
        abandonos_total=0
        cola_total=0

        for d in range(1, dias + 1):
            tiempo_actual, clientes_dia, acumulado, ocup_act, cola_variable, abandonos_acum = 0, 0, 0, 0, 0, 0
            total_cola_dia, total_bebidas_dia, total_ingresos_dia = 0, 0, 0
            carga_trabajo_meseros, carga_trabajo_bartenders = 0, 0
            personas_adentro, log_llegadas = [], []

            while tiempo_actual < minutos_totales:
                rn_ll = random.random()
                grupo = self.pers(rn_ll)
                rn_min = random.random()
                m = self.minutos(rn_min)
                acumulado += m 
                hora_llegada = hora_base + timedelta(minutes=acumulado)
                tiempo_actual += m
                if tiempo_actual >= minutos_totales: break

                salieron_ahora = 0
                i = 0
                while i < len(personas_adentro):
                    h_salida, cant_sale = personas_adentro[i]
                    if h_salida <= hora_llegada:
                        salieron_ahora += cant_sale 
                        ocup_act -= cant_sale
                        personas_adentro.pop(i)
                        if cola_variable > 0:
                            pueden_entrar = min(cola_variable, capac - ocup_act)
                            if pueden_entrar > 0:
                                cola_variable -= pueden_entrar
                                ocup_act += pueden_entrar
                                h_salida_cola = hora_llegada + timedelta(minutes=self.tiem_perman(random.random()))
                                personas_adentro.append((h_salida_cola, pueden_entrar))
                    else: i += 1

                rn_des=random.random(); rn_ida=random.random()
                des="---"; perm=0; hora_salida_str ="---"
                rn_beb=0; tipo_b="---"; rn_p_beb=0; prom=0; beb_consumidas=0; pago_total = 0
                rn_s_mes=0; t_mesero=0; rn_s_bar=0; t_bartender = 0

                #Comprobar si hay espacio en el bar
                if ocup_act + grupo <= capac:
                    ocup_act += grupo
                    perm = self.tiem_perman(rn_ida)
                    h_salida_nuevo = hora_llegada + timedelta(minutes=perm)
                    personas_adentro.append((h_salida_nuevo, grupo))
                    hora_salida_str, des = h_salida_nuevo.strftime('%H:%M'), "Entra"

                    rn_beb = random.random()
                    tipo_b = self.Bebidas(rn_beb)
                    rn_p_beb = random.random()
                    prom = self.prom_beb(rn_p_beb)
                    beb_consumidas = grupo * prom
                    for row in self.bebidas:
                        if row[0] == tipo_b: pago_total = beb_consumidas * float(row[4])

                    total_bebidas_dia += beb_consumidas
                    total_ingresos_dia += pago_total

                    rn_s_mes = random.random()
                    t_mesero = self.get_tiempo_servicio(rn_s_mes, self.serv_mesero)
                    rn_s_bar = random.random()
                    t_bartender = self.get_tiempo_servicio(rn_s_bar, self.prep_bartender)
                    
                    carga_trabajo_meseros += t_mesero
                    carga_trabajo_bartenders += (t_bartender * beb_consumidas)
                else:
                    if self.desicion_bar(rn_des) == "Esperar":
                        cola_variable += grupo
                        total_cola_dia += grupo
                        des = "A Cola"
                    else:
                        abandonos_acum += grupo
                        des = "Abandona"

                clientes_dia += grupo
                log_llegadas.append((f"{rn_ll:.4f}", grupo, f"{rn_min:.4f}", m, hora_llegada.strftime('%H:%M'), f"{rn_des:.4f}", des, 
                                     f"{rn_ida:.4f}", perm, hora_salida_str, salieron_ahora, ocup_act, cola_variable, abandonos_acum, 
                                     f"{rn_beb:.4f}", tipo_b, f"{rn_p_beb:.4f}", prom, f"{beb_consumidas:.1f}", f"${pago_total:.2f}", 
                                     f"{rn_s_mes:.4f}", t_mesero, f"{rn_s_bar:.4f}", t_bartender))

            # --- CÁLCULO DE GASTOS DIARIOS (LUZ Y AGUA) ---
            rn_luz = random.random()
            costo_luz_dia = self.get_costo_luz(rn_luz)

            cliente_total+=clientes_dia
            cola_total+=total_cola_dia
            abandonos_total+=abandonos_acum

            costo_total_ingreso+=total_ingresos_dia
            
            # El agua depende de los clientes que llegaron
            costo_agua_total = 0
            #for _ in range(clientes_dia):
            #    costo_agua_total += self.get_costo_agua(random.random())
            rn_agua=random.random()
            cos_agu=self.get_costo_agua(rn_agua)
            costo_agua_total=cos_agu*clientes_dia

            utilidad_dia = total_ingresos_dia - (costo_luz_dia + costo_agua_total)
            total_utilidad_simulacion += utilidad_dia

            meseros_necesarios = math.ceil(carga_trabajo_meseros / minutos_totales)
            bartenders_necesarios = math.ceil(carga_trabajo_bartenders / minutos_totales)
            total_meseros_sugeridos = max(total_meseros_sugeridos, meseros_necesarios)
            total_bartenders_sugeridos = max(total_bartenders_sugeridos, bartenders_necesarios)

            self.detalles_diarios[d] = log_llegadas
            self.tabla_mc.insert("", "end", values=(f"Día {d}", clientes_dia, total_cola_dia, abandonos_acum, f"{total_bebidas_dia:.1f}", 
                                                    f"${total_ingresos_dia:,.2f}", meseros_necesarios, bartenders_necesarios,f"{rn_luz:.4f}",
                                                    f"${costo_luz_dia:.2f}", f"{rn_agua:.4f}",cos_agu,f"${costo_agua_total:.2f}", f"${utilidad_dia:,.2f}"))

        abasto = "SÍ" if (num_meseros >= total_meseros_sugeridos and num_bartenders >= total_bartenders_sugeridos) else "NO"
        self.kpis_labels["Clientes"].configure(text=str(cliente_total))
        self.kpis_labels["Abandonos"].configure(text=str(abandonos_total))
        self.kpis_labels["Espera"].configure(text=str(cola_total))
        self.kpis_labels["Meseros Sugeridos"].configure(text=str(total_meseros_sugeridos))
        self.kpis_labels["Bartenders Sugeridos"].configure(text=str(total_bartenders_sugeridos))
        self.kpis_labels["Utilidad Total"].configure(text=f"${total_utilidad_simulacion:,.2f}")
        self.kpis_labels["Abasto Personal"].configure(text=abasto, text_color="green" if abasto=="SÍ" else "red")
        self.kpis_labels["Ingresos"].configure(text=str(f"${costo_total_ingreso:,.2f}"))
        self.tabview.set("Monte Carlo")
    
    # --- FUNCIONES DE RANGOS ---
    def get_costo_luz(self, alea):
        for i in range(1, len(self.tabla_luz)):
            if alea < float(self.tabla_luz[i][2]): return float(self.tabla_luz[i][0])
        #return float(self.tabla_luz[1][0])

    def get_costo_agua(self, alea):
        for i in range(1, len(self.tabla_agua)):
            if alea < float(self.tabla_agua[i][2]): return float(self.tabla_agua[i][0])
        #return float(self.tabla_agua[1][0])

    def pers(self,alea):
        for i in range(1,len(self.datos_personas)):
            if alea < float(self.datos_personas[i][2]): return int(self.datos_personas[i][0])
    def minutos(self,alea):
        for i in range(1,len(self.min_lleg)):
            if alea < float(self.min_lleg[i][2]): return int(self.min_lleg[i][0])
    def desicion_bar(self,alea):
        for i in range(1,len(self.decision)):
            if alea < float(self.decision[i][2]): return (self.decision[i][0])
    def tiem_perman(self,alea):
        for i in range(1,len(self.tiempo_bar)):
            if alea < float(self.tiempo_bar[i][2]): return int(self.tiempo_bar[i][0])
    def prom_beb(self, alea):
        for i in range(1, len(self.promedio)):
            if alea < float(self.promedio[i][2]): return float(self.promedio[i][0])
        return 0
    def Bebidas(self, alea):
        for i in range(1, len(self.bebidas)):
            if alea < float(self.bebidas[i][2]): return self.bebidas[i][0]
        return "---"
    def get_tiempo_servicio(self, alea, tabla):
        for i in range(1, len(tabla)):
            if alea < float(tabla[i][2]): return int(tabla[i][0])
        #return int(tabla[1][0])
    
    def on_double_click_mc(self, event):
        item = self.tabla_mc.selection()[0]
        val = self.tabla_mc.item(item, "values")[0]
        self.mostrar_ventana_detalle(int(val.replace("Día ", "")))

    def mostrar_ventana_detalle(self, dia):
        ventana = ctk.CTkToplevel(self); ventana.title(f"Detalle Día {dia}"); ventana.geometry("1550x700")
        ventana.lift() 
        ventana.focus_force() 
        ventana.attributes("-topmost", True)
        container = ctk.CTkFrame(ventana); container.pack(fill="both", expand=True, padx=20, pady=20)
        cols = ("Rn1", "cantidad","Rn2","minuto","hora","Rn3","desic","Rn4","perm","hora_ida", "salieron", 
                "ocup_bar", "cola", "abandonos", "rn_b", "tipo", "rn_p", "prom", "tot_beb", "pago", "rn_mes", "t_mes", "rn_bar", "t_bar")
        tabla_det = ttk.Treeview(container, columns=cols, show="headings")
        headings = [("Rn1", "Rn"), ("cantidad", "Grupo"), ("Rn2", "Rn"), ("minuto", "Min_Lleg"), ("hora", "Hora Lleg"), 
                    ("Rn3", "Rn"), ("desic", "Acción"), ("Rn4", "Rn"), ("perm", "Min_Perm"), ("hora_ida", "Hora Salida"), 
                    ("salieron", "Salieron"), ("ocup_bar", "En Bar"), ("cola", "En Cola"), ("abandonos", "Aband. Acum"), 
                    ("rn_b", "Rn_Beb"), ("tipo", "Tipo Beb"), ("rn_p", "Rn_Prom"), ("prom", "Prom"), ("tot_beb", "Beb. Tot"), 
                    ("pago", "Pago $"), ("rn_mes", "Rn_Mes"), ("t_mes", "T_Mes"), ("rn_bar", "Rn_Bart"), ("t_bar", "T_Bart")]
        for col, txt in headings:
            tabla_det.heading(col, text=txt); tabla_det.column(col, width=65, anchor="center")
        tabla_det.pack(side="left", fill="both", expand=True)
        if dia in self.detalles_diarios:
            for fila in self.detalles_diarios[dia]: tabla_det.insert("", "end", values=fila)

    def nueva_simul(self):
        for item in self.tabla_mc.get_children(): self.tabla_mc.delete(item)
        self.detalles_diarios = {}
        for k in self.kpis_labels: self.kpis_labels[k].configure(text="---")

if __name__ == "__main__":
    root = ctk.CTk(); root.withdraw() 
    app = Bar(master=root); root.mainloop()