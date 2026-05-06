import customtkinter as ctk
from CTkTable import CTkTable
from tkinter import ttk
import random
from datetime import datetime, timedelta

class Bar(ctk.CTkToplevel):

    def __init__(self, master=None):
        super().__init__(master)
        self.detalles_diarios = {} # Diccionario para no saturar la memoria

        self.title("Simulación Monte Carlo - Bar del Hotel")
        self.geometry("1400x850")

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Configuración de estilo para las tablas Treeview (para que se vean oscuras)
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

    # ---------------------------------------------------
    # HEADER
    # ---------------------------------------------------
    def header(self):
        header = ctk.CTkFrame(self, height=60, fg_color="#111827", corner_radius=0)
        header.pack(fill="x")
        header.pack_propagate(False)

        titulo = ctk.CTkLabel(
            header,
            text="🍸 Simulación Monte Carlo - Bar del Hotel",
            font=("Segoe UI", 20, "bold")
        )
        titulo.pack(side="left", padx=20)

        botones = [("Nueva Simulación", self.nueva_simul), ("Ejecutar", self.ejecutar)]

        for txt, v in reversed(botones):
            ctk.CTkButton(
                header,
                text=txt,
                command=v,
                width=120,
                height=34
            ).pack(side="right", padx=8, pady=10)

    # ---------------------------------------------------
    # MAIN
    # ---------------------------------------------------
    def layout_principal(self):
        main = ctk.CTkFrame(self, fg_color="#0f172a")
        main.pack(fill="both", expand=True)
        self.content(main)

    # ---------------------------------------------------
    # CONTENT
    # ---------------------------------------------------
    def content(self, parent):
        content = ctk.CTkFrame(parent, fg_color="#e5e7eb")
        content.pack(side="left", fill="both", expand=True)

        self.cards(content)
        self.tabs(content)

    # ---------------------------------------------------
    # KPI CARDS
    # ---------------------------------------------------
    def cards(self, parent):
        cards = ctk.CTkFrame(parent, fg_color="transparent")
        cards.pack(fill="x", padx=15, pady=15)

        self.kpis_labels = {}
        kpis = [("Huéspedes", "---"), ("Abandonos", "---"), ("Meseros", "---"),
                ("Bartenders", "---"), ("Ingresos", "---"), ("Utilidad", "---")]

        for t, v in kpis:
            card = ctk.CTkFrame(cards, width=180, height=90, fg_color="black")
            card.pack(side="left", padx=6)
            card.pack_propagate(False)

            ctk.CTkLabel(card, text=t, text_color="white", font=("bold italic", 12)).pack(pady=(12, 0))
            lbl_val = ctk.CTkLabel(card, text=v, text_color="white", font=("Segoe UI", 20, "bold"))
            lbl_val.pack()
            self.kpis_labels[t] = lbl_val

    # ---------------------------------------------------
    # TABS
    # ---------------------------------------------------
    def tabs(self, parent):
        self.tabview = ctk.CTkTabview(parent)
        self.tabview.pack(fill="both", expand=True, padx=15, pady=(0, 15))

        self.tabview.add("Parámetros")
        self.tabview.add("Tablas")
        self.tabview.add("Monte Carlo")

        self.tab_dashboard(self.tabview.tab("Tablas"))
        self.tab_parametros(self.tabview.tab("Parámetros"))

        # Configuración de la TABLA PRINCIPAL (Treeview para velocidad)
        self.mc_container = ctk.CTkFrame(self.tabview.tab("Monte Carlo"), fg_color="transparent")
        self.mc_container.pack(fill="both", expand=True)

        cols = ("dia", "clientes", "hora_term")
        self.tabla_mc = ttk.Treeview(self.mc_container, columns=cols, show="headings")
        self.tabla_mc.heading("dia", text="Días")
        self.tabla_mc.heading("clientes", text="Total_Clientes")
        self.tabla_mc.heading("hora_term", text="Hora_Term")
        self.tabla_mc.column("dia", anchor="center")
        self.tabla_mc.column("clientes", anchor="center")
        self.tabla_mc.column("hora_term", anchor="center")

        scroll = ttk.Scrollbar(self.mc_container, orient="vertical", command=self.tabla_mc.yview)
        self.tabla_mc.configure(yscrollcommand=scroll.set)
        
        self.tabla_mc.pack(side="left", fill="both", expand=True)
        scroll.pack(side="right", fill="y")

        # Evento de doble click para ver detalle
        self.tabla_mc.bind("<Double-1>", self.on_double_click_mc)

    # ---------------------------------------------------
    # TAB DASHBOARD
    # ---------------------------------------------------
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

        #|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
        # ---------------- Tabla 1: Personas que llegan ----------------
        self.datos_personas = [
            ["Personas que llegan", "Probabilidad", "Prob. Acumulada", "Rango (Rn)"],
            ["0", "0.15", "0.15", "0.0000 - 0.1500"],
            ["2", "0.4", "0.55", "0.1501 - 0.5500"],
            ["4", "0.25", "0.8", "0.5501 - 0.8000"],
            ["6", "0.15", "0.95", "0.8001 - 0.9500"],
            ["8", "0.05", "1", "0.9501 - 1.0000"],
        ]

        tabla_personas = CTkTable(
            inferior,
            row=len(self.datos_personas),
            column=len(self.datos_personas[0]),
            values=self.datos_personas,
            header_color="#2632dc",
            command=lambda e: editar_celda(tabla_personas, self.datos_personas, e[0], e[1])
        )
        tabla_personas.pack(pady=10, fill="x")

        # ---------------- Tabla 2: Minutos de espera ----------------
        self.min_lleg = [
            ["Minutos de espera", "Probabilidad", "Prob. Acumulada", "Rango (Rn)"],
            ["2", "0.4", "0.4", "0.0000 - 0.4000"],
            ["5", "0.35", "0.75", "0.4001 - 0.7500"],
            ["8", "0.15", "0.9", "0.7501 - 0.9000"],
            ["10", "0.1", "1", "0.9001 - 1.0000"],
        ]

        tabla_espera = CTkTable(
            inferior,
            row=len(self.min_lleg),
            column=len(self.min_lleg[0]),
            values=self.min_lleg,
            header_color="#2632dc",
            command=lambda e: editar_celda(tabla_espera, self.min_lleg, e[0], e[1])
            #colors=[("white", "darkgreen")] + [("black", "white")] * (len(self.min_lleg)-1)
        )
        tabla_espera.pack(pady=10, fill="x")
        #|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
        # ---------------- Tabla 3: Decisón ----------------
        self.decision = [
            ["Decisión", "Probabilidad", "Prob. Acumulada", "Rango (Rn)"],
            ["Esperar", "0.25", "0.25", "0.000 - 0.250"],
            ["Abandonar", "0.75", "1.0", "0.251 - 1.0"]
        ]

        tabla_decision = CTkTable(
            inferior,
            row=len(self.decision),
            column=len(self.decision[0]),
            values=self.decision,
            header_color="#951414",
            command=lambda e: editar_celda(tabla_decision, self.decision, e[0], e[1])
            #colors=[("white", "darkgreen")] + [("black", "white")] * (len(self.min_lleg)-1)
        )
        tabla_decision.pack(pady=10, fill="x")

        # ---------------- Tabla : Tiempo en el Bar ----------------
        self.tiempo_bar = [
            ["Tiempo en el Bar", "Probabilidad", "Prob. Acumulada", "Rango (Rn)"],
            ["30", "0.2", "0.2", "0.000 - 0.200"],
            ["45", "0.3", "0.5", "0.201 - 0.500"],
            ["60", "0.25", "0.75", "0.501 - 0.750"],
            ["90", "0.25", "1.0", "0.751 - 1.0"]
        ]

        tabla_TiemBar = CTkTable(
            inferior,
            row=len(self.tiempo_bar),
            column=len(self.tiempo_bar[0]),
            values=self.tiempo_bar,
            header_color="#951414",
            command=lambda e: editar_celda(tabla_TiemBar, self.tiempo_bar, e[0], e[1])
            #colors=[("white", "darkgreen")] + [("black", "white")] * (len(self.min_lleg)-1)
        )
        tabla_TiemBar.pack(pady=10, fill="x")

        # Tablas de rangos (Personas, Decisión, Incidentes, Bebidas)
        # Se omiten detalles por brevedad pero se mantienen en tu lógica original
        # [Aquí irían tus definiciones de tabla1, tabla2, etc.]

    # ---------------------------------------------------
    # TAB PARAMETROS
    # ---------------------------------------------------
    def tab_parametros(self, parent):
        self.inputs = {}
        params_list = [("Días", "3"), ("Capacidad del Bar", "50"), ("Horas laborales", "8"),("Hora de apertura", "8")]

        for i, (txt, val) in enumerate(params_list):
            ctk.CTkLabel(parent, text=txt).grid(row=i, column=0, padx=20, pady=10, sticky="w")
            ent = ctk.CTkEntry(parent, width=220)
            ent.grid(row=i, column=1, padx=10)
            ent.insert(0, val)
            self.inputs[txt] = ent

    # ---------------------------------------------------
    # LÓGICA DE SIMULACIÓN Y DETALLE
    # ---------------------------------------------------
    def ejecutar(self):
        # 1. Limpiar tabla y datos
        for item in self.tabla_mc.get_children():
            self.tabla_mc.delete(item)
        self.detalles_diarios = {}

        # 2. Obtener Parámetros
        try:
            dias = int(self.inputs["Días"].get())
            horas = int(self.inputs["Horas laborales"].get())
            apertura = (self.inputs["Hora de apertura"].get())
            minutos_totales = horas * 60
        except: return

        if apertura.isdigit():
            # Lo convertimos a formato HH:00
            hora_apertura = f"{int(apertura):02d}:00"
        else:
            # Si ya viene con minutos (ej. "08:10"), lo dejamos igual
            hora_apertura = apertura
        

        # 3. Simulación por Minutos
        for d in range(1, dias + 1):
            tiempo_actual = 0
            clientes_dia = 0
            acumulado=0
            ocup_act=0
            log_llegadas = [] # Guardaremos: (Minuto, Cantidad)
            hora = datetime.strptime(hora_apertura, "%H:%M")

            while tiempo_actual < minutos_totales:
                # Intervalo de llegada (Tabla que definimos antes)
                rn_ll = random.random()
                grupo=self.pers(rn_ll)
                
                rn_min = random.random()
                m=self.minutos(rn_min)

                acumulado += m 
                hora_llegada = hora + timedelta(minutes=acumulado)

                tiempo_actual+=m
                if tiempo_actual >= minutos_totales: break

                
                #if grupo > 0:
                clientes_dia += grupo
                log_llegadas.append((f"{rn_ll:.4f}", f"{grupo}", f"{rn_min:.4f}", f"{m}", f"{hora_llegada.strftime('%H:%M')}"))

            # Guardar en memoria y llenar tabla principal
            self.detalles_diarios[d] = log_llegadas
            self.tabla_mc.insert("", "end", values=(f"Día {d}", clientes_dia, hora_llegada.strftime('%H:%M')))

        self.tabview.set("Monte Carlo")
    
    #|||||||||||||||| FUNCIONES DE LAS RANGOS DE LAS TABLAS|||||||||||||||||||||||||||||||||||||||||||||||
    def pers(self,alea):
        for i in range(1,len(self.datos_personas)):
            if alea < float(self.datos_personas[i][2]):
                return int(self.datos_personas[i][0])
    
    def minutos(self,alea):
        for i in range(1,len(self.min_lleg)):
            if alea < float(self.min_lleg[i][2]):
                return int(self.min_lleg[i][0])
    
    #|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

    def on_double_click_mc(self, event):
        item = self.tabla_mc.selection()[0]
        val = self.tabla_mc.item(item, "values")[0]
        dia_num = int(val.replace("Día ", ""))
        self.mostrar_ventana_detalle(dia_num)

    def mostrar_ventana_detalle(self, dia):
        ventana = ctk.CTkToplevel(self)
        ventana.title(f"Detalle de Llegadas - Día {dia}")
        ventana.geometry("800x600")
        #ventana.grab_set()
        
        ventana.lift()
        ventana.focus_force()
        ventana.attributes("-topmost", True)

        ctk.CTkLabel(ventana, text=f"Flujo de Lleegadas - Día {dia}", font=("Arial", 16, "bold")).pack(pady=10)

        # Tabla de detalle
        container = ctk.CTkFrame(ventana)
        container.pack(fill="both", expand=True, padx=20, pady=20)

        cols = ("Rn1", "cantidad","Rn2","minuto","hora")
        tabla_det = ttk.Treeview(container, columns=cols, show="headings")
        tabla_det.heading("Rn1", text="Rn")
        tabla_det.heading("cantidad", text="Tamaño del Grupo")
        tabla_det.heading("Rn2", text="Rn")
        tabla_det.heading("minuto", text="Minutos_de_Llegada")
        tabla_det.heading("hora", text="Hora")
        
        scroll = ttk.Scrollbar(container, orient="vertical", command=tabla_det.yview)
        tabla_det.configure(yscrollcommand=scroll.set)
        
        tabla_det.pack(side="left", fill="both", expand=True)
        scroll.pack(side="right", fill="y")

        # Cargar datos guardados
        for rn1, grupo, rn2, minuto, hora in self.detalles_diarios[dia]:
            tabla_det.insert("", "end", values=(rn1, grupo, rn2, minuto, hora))

    def nueva_simul(self):
        for item in self.tabla_mc.get_children():
            self.tabla_mc.delete(item)
        self.detalles_diarios = {}
        for k in self.kpis_labels: self.kpis_labels[k].configure(text="---")

if __name__ == "__main__":
    root = ctk.CTk()
    root.withdraw() # Ocultar la raíz para usar solo la Toplevel
    app = Bar(master=root)
    root.mainloop()