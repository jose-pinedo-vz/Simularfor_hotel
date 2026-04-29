import customtkinter as ctk
from CTkTable import CTkTable

COLOR_FONDO = "#5D4037"
COLOR_TEXTO = "#FFFFFF"
COLOR_EXTRA = "#8C8680"
COLOR_BOTON = "#3E2723"
COLOR_CONTORNO = "#4281FF"

class Habitaciones:
    def __init__(self):
        self.ventana = ctk.CTk()
        self.ventana.title("Área de Habitaciones")
        self.ventana.geometry("1400x750")
        self.ventana.configure(fg_color=COLOR_FONDO)

        try:
            self.ventana.state("zoomed")
        except:
            self.ventana.attributes("-zoomed", True)

        self.frame_scroll = ctk.CTkScrollableFrame(self.ventana)
        self.frame_scroll.pack(fill="both", expand=True, padx=20, pady=20)

        titulo = ctk.CTkLabel(self.frame_scroll, text="SIMULACIÓN DE HABITACIONES", text_color=COLOR_TEXTO, font=("Arial", 28, "bold"))
        titulo.pack(pady=20)

        self.frame_datos = ctk.CTkFrame(self.frame_scroll, border_width=2, border_color=COLOR_CONTORNO)
        self.frame_datos.pack(fill="x", padx=20, pady=20)

        ancho_entry = 250
        alto_entry = 55

        ctk.CTkLabel(self.frame_datos, text="Cantidad de habitaciones:", text_color=COLOR_TEXTO, font=("Arial", 16)).grid(row=0, column=0, padx=20, pady=(20, 5))

        self.entry_habitaciones = ctk.CTkEntry(self.frame_datos, width=ancho_entry, height=alto_entry)
        self.entry_habitaciones.grid(row=1, column=0, padx=20, pady=(0, 20))

        ctk.CTkLabel(self.frame_datos, text="Costo de mantenimiento:", text_color=COLOR_TEXTO, font=("Arial", 16)).grid(row=0, column=1, padx=20, pady=(20, 5))

        self.entry_mantenimiento = ctk.CTkEntry(self.frame_datos, width=ancho_entry, height=alto_entry)
        self.entry_mantenimiento.grid(row=1, column=1, padx=20, pady=(0, 20))

        ctk.CTkLabel(self.frame_datos, text="Costo de limpieza:", text_color=COLOR_TEXTO, font=("Arial", 16)).grid(row=0, column=2, padx=20, pady=(20, 5))

        self.entry_limpieza = ctk.CTkEntry(self.frame_datos, width=ancho_entry, height=alto_entry)
        self.entry_limpieza.grid(row=1, column=2, padx=20, pady=(0, 20))

        ctk.CTkLabel(self.frame_datos, text="Personal disponible:", text_color=COLOR_TEXTO, font=("Arial", 16)).grid(row=0, column=3, padx=20, pady=(20, 5))

        self.entry_personal = ctk.CTkEntry(self.frame_datos, width=ancho_entry, height=alto_entry)
        self.entry_personal.grid(row=1, column=3, padx=20, pady=(0, 20))

        self.frame_probabilidades = ctk.CTkFrame(self.frame_scroll, border_width=2, border_color=COLOR_CONTORNO)
        self.frame_probabilidades.pack(fill="x", padx=20, pady=20)

        titulo_prob = ctk.CTkLabel(self.frame_probabilidades, text="TABLAS DE PROBABILIDAD", text_color=COLOR_TEXTO, font=("Arial", 22, "bold"))
        titulo_prob.pack(pady=20)

        contenedor_tablas = ctk.CTkFrame(self.frame_probabilidades, fg_color="transparent")
        contenedor_tablas.pack(pady=20, padx=20)

        frame_tabla1 = ctk.CTkFrame(contenedor_tablas)
        frame_tabla1.grid(row=0, column=0, padx=15, pady=15)

        ctk.CTkLabel(frame_tabla1, text="Llegadas por día", text_color=COLOR_TEXTO, font=("Arial", 16, "bold")).pack(pady=10)

        tabla_llegadas = [
            ["Llegadas", "Prob", "Acum", "Rango"],
            [0, 0.25, 0.25, "0.00 - 0.25"],
            [1, 0.25, 0.50, "0.2501 - 0.5"],
            [2, 0.25, 0.75, "0.5001 - 0.75"],
            [3, 0.25, 1.00, "0.7501 - 1.0"]
        ]

        self.tabla_llegadas = CTkTable(frame_tabla1, values=tabla_llegadas)
        self.tabla_llegadas.pack(padx=10, pady=10)

        frame_tabla2 = ctk.CTkFrame(contenedor_tablas)
        frame_tabla2.grid(row=1, column=0, padx=15, pady=15)

        ctk.CTkLabel(frame_tabla2, text="Tipo de habitación", text_color=COLOR_TEXTO, font=("Arial", 16, "bold")).pack(pady=10)

        tabla_tipo = [
            ["Tipo", "Prob", "Acum", "Rango"],
            ["Individual", 0.40, 0.40, "0.00 - 0.4"],
            ["Doble", 0.40, 0.80, "0.4001 - 0.8"],
            ["Suite", 0.20, 1.00, "0.8001 - 1.0"]
        ]

        self.tabla_tipo = CTkTable(frame_tabla2, values=tabla_tipo)
        self.tabla_tipo.pack(padx=10, pady=10)

        frame_tabla3 = ctk.CTkFrame(contenedor_tablas)
        frame_tabla3.grid(row=2, column=0, padx=15, pady=15)

        ctk.CTkLabel(frame_tabla3, text="Duración de estancia", text_color=COLOR_TEXTO, font=("Arial", 16, "bold")).pack(pady=10)

        tabla_estancia = [
            ["Noches", "Prob", "Acum", "Rango"],
            [1, 0.25, 0.25, "0.00 - 0.25"],
            [2, 0.35, 0.60, "0.2501 - 0.6"],
            [3, 0.25, 0.85, "0.6001 - 0.85"],
            [4, 0.15, 1.00, "0.8501 - 1.0"]
        ]

        self.tabla_estancia = CTkTable(frame_tabla3, values=tabla_estancia)
        self.tabla_estancia.pack(padx=10, pady=10)

        self.frame_kpis = ctk.CTkFrame(self.frame_scroll, border_width=2, border_color=COLOR_CONTORNO)
        self.frame_kpis.pack(fill="x", padx=20, pady=20)

        self.lbl_ingresos = ctk.CTkLabel(self.frame_kpis, text="Ingresos Totales: $0", text_color="#00FF99", font=("Arial", 18, "bold"))
        self.lbl_ingresos.grid(row=0, column=0, padx=40, pady=30)

        self.lbl_costos = ctk.CTkLabel(self.frame_kpis, text="Costos Totales: $0", text_color="#FF6666", font=("Arial", 18, "bold"))
        self.lbl_costos.grid(row=0, column=1, padx=40, pady=30)

        self.lbl_ganancias = ctk.CTkLabel(self.frame_kpis, text="Ganancia Neta: $0", text_color="#FFD700", font=("Arial", 18, "bold"))
        self.lbl_ganancias.grid(row=0, column=2, padx=40, pady=30)

        self.frame_botones = ctk.CTkFrame(self.frame_scroll, border_width=2, border_color=COLOR_CONTORNO)
        self.frame_botones.pack(fill="x", padx=20, pady=20)

        ancho_boton = 250
        alto_boton = 80

        self.btn_cargar = ctk.CTkButton(self.frame_botones, text="Cargar Datos", width=ancho_boton, height=alto_boton, fg_color="#FFBF42", text_color="#000000")
        self.btn_cargar.grid(row=0, column=0, padx=20, pady=30)

        self.btn_limpiar = ctk.CTkButton(self.frame_botones, text="Limpiar", width=ancho_boton, height=alto_boton, fg_color="#FFBF42", text_color="#000000")
        self.btn_limpiar.grid(row=0, column=1, padx=20, pady=30)

        self.btn_bajo = ctk.CTkButton(self.frame_botones, text="Valores Bajos", width=ancho_boton, height=alto_boton, fg_color="#FFBF42", text_color="#000000")
        self.btn_bajo.grid(row=0, column=2, padx=20, pady=30)

        self.btn_medio = ctk.CTkButton(self.frame_botones, text="Valores Medios", width=ancho_boton, height=alto_boton, fg_color="#FFBF42", text_color="#000000")
        self.btn_medio.grid(row=0, column=3, padx=20, pady=30)

        self.btn_alto = ctk.CTkButton(self.frame_botones, text="Valores Altos", width=ancho_boton, height=alto_boton, fg_color="#FFBF42", text_color="#000000")
        self.btn_alto.grid(row=0, column=4, padx=20, pady=30)

        self.frame_resultados = ctk.CTkFrame(self.frame_scroll, border_width=2, border_color=COLOR_CONTORNO)
        self.frame_resultados.pack(fill="both", expand=True, padx=20, pady=20)

        titulo_resultados = ctk.CTkLabel(self.frame_resultados, text="RESULTADOS DE LA SIMULACIÓN", text_color=COLOR_TEXTO, font=("Arial", 20, "bold"))
        titulo_resultados.pack(pady=20)

        tabla_resultados = [
            ["Día", "Llegadas", "Habitaciones", "Ingresos", "Costos", "Ganancia"],
            ["", "", "", "", "", ""],
            ["", "", "", "", "", ""],
            ["", "", "", "", "", ""],
            ["", "", "", "", "", ""]
        ]

        self.tabla_simulacion = CTkTable(self.frame_resultados, values=tabla_resultados)
        self.tabla_simulacion.pack(padx=20, pady=20)

        self.ventana.mainloop()

Habitaciones()