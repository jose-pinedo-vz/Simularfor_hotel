import customtkinter as ctk
from CTkTable import CTkTable


class Bar(ctk.CTkToplevel):

    def __init__(self,master=None):
        super().__init__(master)

        self.title("Simulación Monte Carlo - Bar del Hotel")
        self.geometry("1400x850")

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

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

        botones = ["Nueva Simulación", "Ejecutar"]

        for txt in reversed(botones):
            ctk.CTkButton(
                header,
                text=txt,
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

        kpis = [
            ("Huéspedes", "---"),
            ("Abandonos", "---"),
            ("Meseros", "---"),
            ("Bartenders", "---"),
            ("Ingresos", "---"),
            ("Utilidad", "---")
            
        ]

        for t, v in kpis:
            card = ctk.CTkFrame(cards, width=180, height=90, fg_color="black")
            card.pack(side="left", padx=6)
            card.pack_propagate(False)

            ctk.CTkLabel(
                card,
                text=t,
                text_color="white",
                font=("bold italic", 12)
            ).pack(pady=(12, 0))

            ctk.CTkLabel(
                card,
                text=v,
                text_color="white",
                font=("Segoe UI", 20, "bold")
            ).pack()

    # ---------------------------------------------------
    # TABS
    # ---------------------------------------------------
    def tabs(self, parent):
        tabview = ctk.CTkTabview(parent)
        tabview.pack(fill="both", expand=True, padx=15, pady=(0, 15))

        tabview.add("Parámetros")
        tabview.add("Tablas")

        self.tab_dashboard(tabview.tab("Tablas"))
        self.tab_parametros(tabview.tab("Parámetros"))

    # ---------------------------------------------------
    # TAB DASHBOARD
    # ---------------------------------------------------
    def tab_dashboard(self, parent):

    # =====================================================
    # FUNCION PARA EDITAR CELDA AL HACER CLICK
    # =====================================================
        def editar_celda(tabla, datos, fila, col):
            if fila == 0:
                return   # no editar encabezado

            ventana = ctk.CTkToplevel(self)
            ventana.title("Editar valor")
            ventana.geometry("300x140")
            ventana.grab_set()

            ctk.CTkLabel(
                ventana,
                text=f"Fila {fila}  Columna {col}",
                font=("Arial", 14, "bold")
            ).pack(pady=10)

            entry = ctk.CTkEntry(ventana, width=220)
            entry.pack(pady=5)
            entry.insert(0, str(datos[fila][col]))

            def guardar():
                nuevo = entry.get()
                datos[fila][col] = nuevo
                tabla.insert(fila, col, nuevo)
                ventana.destroy()

            ctk.CTkButton(
                ventana,
                text="Guardar",
                command=guardar
            ).pack(pady=10)

        # =====================================================
        # TABLA PRINCIPAL
        # =====================================================
        '''datos = [
            ["#", "RND", "Grupo", "Llegada", "Espera", "Bebida", "Pago", "Utilidad"],
            [1, "0.24", 1, "18:02", 0, "Simple", "Habitación", "$42"],
            [2, "0.67", 2, "18:05", 3, "Preparado", "Tarjeta", "$133"],
            [3, "0.91", 4, "18:09", 8, "Botella", "Efectivo", "$840"],
            [4, "0.44", 1, "18:15", 1, "Simple", "Habitación", "$42"],
            [5, "0.72", 3, "18:19", 5, "Coctelería", "Tarjeta", "$315"]
        ]

        tabla = CTkTable(
            master=parent,
            values=datos,
            row=len(datos),
            column=len(datos[0]),
            header_color="#2563eb",
            hover_color="#1d4ed8",
            command=lambda x: editar_celda(tabla, datos, x["row"], x["column"])
        )
        tabla.pack(fill="x", padx=10, pady=10)'''

        # =====================================================
        # CONTENEDOR INFERIOR
        # =====================================================
        inferior = ctk.CTkScrollableFrame(parent, fg_color="transparent")
        inferior.pack(fill="both", expand=True, padx=10, pady=10)

        # =====================================================
        # TABLA 1 - TAMAÑO PERSONAS
        # =====================================================
        personas = [
            ["Tamaño", "Prob.", "Acum.", "Rango"],
            [100, 0.30, 0.30, "0.000-0.300"],
            [150, 0.40, 0.70, "0.301-0.700"],
            [200, 0.15, 0.85, "0.701-0.850"],
            [250, 0.10, 0.95, "0.851-0.950"],
            [300, 0.05, 1.00, "0.951-1.000"]
        ]

        frame1 = ctk.CTkFrame(inferior)
        frame1.grid(row=0, column=0, padx=8, pady=8)

        ctk.CTkLabel(frame1, text="Tamaño de Personas").pack(pady=5)

        tabla1 = CTkTable(
            master=frame1,
            values=personas,
            row=len(personas),
            column=4,
            header_color="#16a34a",
            command=lambda x: editar_celda(tabla1, personas, x["row"], x["column"])
        )
        tabla1.pack()

        # =====================================================
        # TABLA 2 - DECISION
        # =====================================================
        decision = [
            ["Decisión", "Prob.", "Acum.", "Rango"],
            ["Esperar", 0.25, 0.25, "0.000-0.250"],
            ["Abandonar", 0.75, 1.00, "0.251-1.000"]
        ]

        frame2 = ctk.CTkFrame(inferior)
        frame2.grid(row=0, column=1, padx=8, pady=8)

        ctk.CTkLabel(frame2, text="Decisión Cliente").pack(pady=5)

        tabla2 = CTkTable(
            master=frame2,
            values=decision,
            row=len(decision),
            column=4,
            header_color="#f59e0b",
            command=lambda x: editar_celda(tabla2, decision, x["row"], x["column"])
        )
        tabla2.pack()

        # =====================================================
        # TABLA 3 - INCIDENTES
        # =====================================================
        incidentes = [
            ["Incidente", "Prob.", "Acum.", "Rango"],
            ["Ninguno", 0.89, 0.89, "0.000-0.890"],
            ["Vaso roto", 0.05, 0.94, "0.891-0.940"],
            ["Derrame", 0.03, 0.97, "0.941-0.970"],
            ["TPV falla", 0.02, 0.99, "0.971-0.990"],
            ["Conflictivo", 0.01, 1.00, "0.991-1.000"]
        ]

        frame3 = ctk.CTkFrame(inferior)
        frame3.grid(row=1, column=0, padx=8, pady=8)

        ctk.CTkLabel(frame3, text="Tipo de Incidente").pack(pady=5)

        tabla3 = CTkTable(
            master=frame3,
            values=incidentes,
            row=len(incidentes),
            column=4,
            header_color="#dc2626",
            command=lambda x: editar_celda(tabla3, incidentes, x["row"], x["column"])
        )
        tabla3.pack()

        # =====================================================
        # TABLA 4 - BEBIDAS
        # =====================================================
        bebidas = [
            ["Bebida", "Prob.", "Ganancia"],
            ["Simple", 0.50, "$42"],
            ["Preparado", 0.30, "$66"],
            ["Coctelería", 0.15, "$105"],
            ["Botella", 0.05, "$840"]
        ]

        frame4 = ctk.CTkFrame(inferior)
        frame4.grid(row=1, column=1, padx=8, pady=8)

        ctk.CTkLabel(frame4, text="Tipos de Bebida").pack(pady=5)

        tabla4 = CTkTable(
            master=frame4,
            values=bebidas,
            row=len(bebidas),
            column=3,
            header_color="#7c3aed",
            command=lambda x: editar_celda(tabla4, bebidas, x["row"], x["column"])
        )
        tabla4.pack()

    # ---------------------------------------------------
    # TAB PARAMETROS
    # ---------------------------------------------------
    def tab_parametros(self, parent):

        params = [
            ("Días", "8"),
            ("Capacidad por Día", "150"),
            ("Prob. Consumo", "2.5"),
            ("Horas laborales", "8"),
            ("Bartenders", "2"),
            ("Minutos de Preparación", "4"),
            ("Meseros", "3"),
            ("Min. Cilientes Ate", "4")
        ]

        for i, (txt, val) in enumerate(params):
            ctk.CTkLabel(parent, text=txt).grid(
                row=i, column=0, padx=20, pady=10, sticky="w"
            )

            ent = ctk.CTkEntry(parent, width=220)
            ent.grid(row=i, column=1, padx=10)
            ent.insert(0, val)


if __name__ == "__main__":
    root = ctk.CTk() 
    app = Bar()
    app.mainloop()