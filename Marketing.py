import customtkinter as ctk
from CTkTable import CTkTable
import random

COLOR_FONDO = "#5D4037"
COLOR_TEXTO = "#FFFFFF"
COLOR_EXTRA = "#8C8680"
COLOR_BOTON = "#3E2723"
COLOR_CONTORNO = "#4281FF"

class Marketing:

    def __init__(self):

        self.ventana = ctk.CTk()
        self.ventana.title("Área de Marketing")
        self.ventana.geometry("1400x750")
        self.ventana.configure(fg_color=COLOR_FONDO)

        try:
            self.ventana.state("zoomed")
        except:
            self.ventana.attributes("-zoomed", True)

        self.frame_scroll = ctk.CTkScrollableFrame(self.ventana)
        self.frame_scroll.pack(fill="both", expand=True, padx=20, pady=20)

        titulo = ctk.CTkLabel(self.frame_scroll, text="SIMULACIÓN DE MARKETING", text_color=COLOR_TEXTO, font=("Arial", 28, "bold"))
        titulo.pack(pady=20)

        self.frame_datos = ctk.CTkFrame(self.frame_scroll, border_width=2, border_color=COLOR_CONTORNO)
        self.frame_datos.pack(fill="x", padx=20, pady=20)

        ancho_entry = 250
        alto_entry = 55

        ctk.CTkLabel(self.frame_datos, text="Presupuesto mensual:", text_color=COLOR_TEXTO, font=("Arial", 16)).grid(row=0, column=0, padx=20, pady=(20, 5))

        self.entry_presupuesto = ctk.CTkEntry(self.frame_datos, width=ancho_entry, height=alto_entry)
        self.entry_presupuesto.grid(row=1, column=0, padx=20, pady=(0, 20))

        ctk.CTkLabel(self.frame_datos, text="Cantidad de campañas:", text_color=COLOR_TEXTO, font=("Arial", 16)).grid(row=0, column=1, padx=20, pady=(20, 5))

        self.entry_campanas = ctk.CTkEntry(self.frame_datos, width=ancho_entry, height=alto_entry)
        self.entry_campanas.grid(row=1, column=1, padx=20, pady=(0, 20))

        ctk.CTkLabel(self.frame_datos, text="Costo por anuncio:", text_color=COLOR_TEXTO, font=("Arial", 16)).grid(row=0, column=2, padx=20, pady=(20, 5))

        self.entry_anuncio = ctk.CTkEntry(self.frame_datos, width=ancho_entry, height=alto_entry)
        self.entry_anuncio.grid(row=1, column=2, padx=20, pady=(0, 20))

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

        ctk.CTkLabel(frame_tabla1, text="Generación de Leads", text_color=COLOR_TEXTO, font=("Arial", 16, "bold")).pack(pady=10)

        tabla_leads = [
            ["Leads", "Prob", "Acum", "Rango"],
            [0, 0.10, 0.10, "0.00 - 0.1"],
            [5, 0.20, 0.30, "0.1001 - 0.3"],
            [10, 0.30, 0.60, "0.3001 - 0.6"],
            [15, 0.25, 0.85, "0.6001 - 0.85"],
            [20, 0.15, 1.00, "0.8501 - 1.00"]
        ]

        self.tabla_leads = CTkTable(frame_tabla1, values=tabla_leads)
        self.tabla_leads.pack(padx=10, pady=10)

        frame_tabla2 = ctk.CTkFrame(contenedor_tablas)
        frame_tabla2.grid(row=1, column=0, padx=15, pady=15)

        ctk.CTkLabel(frame_tabla2, text="Conversión de Reservas", text_color=COLOR_TEXTO, font=("Arial", 16, "bold")).pack(pady=10)

        tabla_conversion = [
            ["Reservas", "Prob", "Acum", "Rango"],
            [1, 0.20, 0.20, "0.00 - 0.2"],
            [2, 0.30, 0.50, "0.2001 - 0.5"],
            [3, 0.25, 0.75, "0.5001 - 0.75"],
            [4, 0.15, 0.90, "0.7501 - 0.9"],
            [5, 0.10, 1.00, "0.9001 - 1.0"]
        ]

        self.tabla_conversion = CTkTable(frame_tabla2, values=tabla_conversion)
        self.tabla_conversion.pack(padx=10, pady=10)

        frame_tabla3 = ctk.CTkFrame(contenedor_tablas)
        frame_tabla3.grid(row=2, column=0, padx=15, pady=15)

        ctk.CTkLabel(frame_tabla3, text="Impacto de Campaña", text_color=COLOR_TEXTO, font=("Arial", 16, "bold")).pack(pady=10)

        tabla_impacto = [
            ["Impacto", "Prob", "Acum", "Rango"],
            ["Bajo", 0.30, 0.30, "0.00 - 0.3"],
            ["Medio", 0.50, 0.80, "0.3001 - 0.8"],
            ["Alto", 0.20, 1.00, "0.8001 - 1.0"]
        ]

        self.tabla_impacto = CTkTable(frame_tabla3, values=tabla_impacto)
        self.tabla_impacto.pack(padx=10, pady=10)

        self.frame_kpis = ctk.CTkFrame(self.frame_scroll, border_width=2, border_color=COLOR_CONTORNO)
        self.frame_kpis.pack(fill="x", padx=20, pady=20)

        self.lbl_leads = ctk.CTkLabel(self.frame_kpis, text="Leads Totales: 0", text_color="#00FF99", font=("Arial", 18, "bold"))
        self.lbl_leads.grid(row=0, column=0, padx=40, pady=30)

        self.lbl_reservas = ctk.CTkLabel(self.frame_kpis, text="Reservas Totales: 0", text_color="#FFD700", font=("Arial", 18, "bold"))
        self.lbl_reservas.grid(row=0, column=1, padx=40, pady=30)

        self.lbl_roi = ctk.CTkLabel(self.frame_kpis, text="ROI Total: $0", text_color="#FF6666", font=("Arial", 18, "bold"))
        self.lbl_roi.grid(row=0, column=2, padx=40, pady=30)

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
            ["Día", "Leads", "Reservas", "Ingresos", "Costos", "ROI"],
            ["", "", "", "", "", ""],
            ["", "", "", "", "", ""],
            ["", "", "", "", "", ""],
            ["", "", "", "", "", ""]
        ]

        self.tabla_resultados = CTkTable(self.frame_resultados, values=tabla_resultados)
        self.tabla_resultados.pack(padx=20, pady=20)

        self.ventana.mainloop()

Marketing()