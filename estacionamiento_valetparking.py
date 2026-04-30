import threading
import io
import sys
import random
import pandas as pd
import customtkinter as ctk

# =============================================================================
#   SECCIÓN 1 — TABLAS DE DATOS HISTÓRICOS
# =============================================================================

datos_tabla_1 = {
    "tiempo":    [  1,      2,      3,      4,     5,     6,     7,     8,     9,    10   ],
    "prob":      [  0.03,   0.05,   0.12,   0.20,  0.05,  0.05,  0.20,  0.10,  0.15,  0.05 ],
    "prob_acum": [  0.03,   0.08,   0.20,   0.40,  0.45,  0.50,  0.70,  0.80,  0.95,  1.00 ],
    "rango_inf": [  0.0000, 0.0301, 0.0801, 0.201, 0.401, 0.451, 0.501, 0.701, 0.801, 0.951],
    "rango_sup": [  0.03,   0.08,   0.20,   0.40,  0.45,  0.50,  0.70,  0.80,  0.95,  1.00 ],
}
TABLA_1_RECEPCION = pd.DataFrame(datos_tabla_1)

datos_tabla_2 = {
    "tiempo":    [  1,     2,     3,     4,     5,     6,     7,      8,      9,      10    ],
    "prob":      [  0.10,  0.20,  0.10,  0.20,  0.10,  0.05,  0.05,   0.05,   0.10,   0.05  ],
    "prob_acum": [  0.10,  0.30,  0.40,  0.60,  0.70,  0.75,  0.80,   0.85,   0.95,   1.00  ],
    "rango_inf": [  0.000, 0.101, 0.301, 0.401, 0.601, 0.701, 0.7501, 0.801,  0.8501, 0.9501],
    "rango_sup": [  0.10,  0.30,  0.40,  0.60,  0.70,  0.75,  0.80,   0.85,   0.95,   1.00  ],
}
TABLA_2_MANIOBRA = pd.DataFrame(datos_tabla_2)

datos_tabla_3 = {
    "tiempo":    [  1,     2,      3,     4,      5,      6,     7,      8,     9,      10    ],
    "prob":      [  0.05,  0.05,   0.03,  0.05,   0.02,   0.25,  0.15,   0.30,  0.05,   0.05  ],
    "prob_acum": [  0.05,  0.10,   0.13,  0.18,   0.20,   0.45,  0.60,   0.90,  0.95,   1.00  ],
    "rango_inf": [  0.000, 0.0501, 0.101, 0.1301, 0.1801, 0.201, 0.4501, 0.601, 0.901,  0.9501],
    "rango_sup": [  0.05,  0.10,   0.13,  0.18,   0.20,   0.45,  0.60,   0.90,  0.95,   1.00  ],
}
TABLA_3_PERMANENCIA = pd.DataFrame(datos_tabla_3)

datos_tabla_4 = {
    "tiempo":    [  2,     3,      4,     5    ],
    "prob":      [  0.15,  0.15,   0.30,  0.40 ],
    "prob_acum": [  0.15,  0.30,   0.60,  1.00 ],
    "rango_inf": [  0.000, 0.1501, 0.301, 0.601],
    "rango_sup": [  0.15,  0.30,   0.60,  1.00 ],
}
TABLA_4_SOLICITUD = pd.DataFrame(datos_tabla_4)

datos_tabla_5 = {
    "tiempo":    [  2,     3,     4,     5,      6     ],
    "prob":      [  0.20,  0.20,  0.50,  0.02,   0.08  ],
    "prob_acum": [  0.20,  0.40,  0.90,  0.92,   1.00  ],
    "rango_inf": [  0.000, 0.201, 0.401, 0.901,  0.9201],
    "rango_sup": [  0.20,  0.40,  0.90,  0.92,   1.00  ],
}
TABLA_5_DEVOLUCION = pd.DataFrame(datos_tabla_5)

datos_tabla_6 = {
    "turno":     ["Madrugada",  "Manana",    "Medio dia", "Tarde pico", "Noche",    "Noche Tardia"],
    "horario":   ["00-06h",     "06-10h",    "10-14h",    "14-18h",     "18-22h",   "22-00h"      ],
    "veh_hora":  ["1-2",        "4-6",       "6-9",       "10-14",      "8-11",     "3-5"         ],
    "prob":      [ 0.001,        0.001,       0.100,       0.300,        0.300,      0.300         ],
    "prob_acum": [ 0.001,        0.002,       0.102,       0.402,        0.702,      1.000         ],
    "rango_inf": [ 0.00000,      0.00101,     0.00201,     0.10201,      0.301,      0.601         ],
    "rango_sup": [ 0.001,        0.002,       0.102,       0.402,        0.702,      1.000         ],
}
TABLA_6_LLEGADAS = pd.DataFrame(datos_tabla_6)

datos_tabla_7 = {
    "cajones":   [ 10,    11,     12,     13,    14,     15,    16,    17,     18,    19,     20,     21    ],
    "prob":      [ 0.01,  0.01,   0.01,   0.01,  0.01,   0.15,  0.25,  0.05,   0.30,  0.09,   0.01,   0.10  ],
    "prob_acum": [ 0.01,  0.02,   0.03,   0.04,  0.05,   0.20,  0.45,  0.50,   0.80,  0.89,   0.90,   1.00  ],
    "rango_inf": [ 0.000, 0.0101, 0.0201, 0.030, 0.0401, 0.050, 0.201, 0.4501, 0.501, 0.801,  0.8901, 0.901 ],
    "rango_sup": [ 0.01,  0.02,   0.03,   0.04,  0.05,   0.20,  0.45,  0.50,   0.80,  0.89,   0.90,   1.00  ],
}
TABLA_7_MANTENIMIENTO = pd.DataFrame(datos_tabla_7)


# =============================================================================
#   SECCIÓN 2 — TARIFAS DEL SERVICIO
# =============================================================================

TARIFA_VALET         = 80
COSTO_CHOFER_POR_MIN = 0.5
PENALIZACION_NEGADO  = 50


# =============================================================================
#   SECCIÓN 3 — FUNCIONES AUXILIARES
# =============================================================================

def generar_na():
    na = random.random()
    return na


def consultar_tabla(na, tabla_df):
    numero_de_filas = len(tabla_df)
    indice_fila = 0

    while indice_fila < numero_de_filas:
        limite_inferior = tabla_df.loc[indice_fila, "rango_inf"]
        limite_superior = tabla_df.loc[indice_fila, "rango_sup"]

        if na >= limite_inferior and na <= limite_superior:
            columna_resultado = tabla_df.columns[0]
            resultado = tabla_df.loc[indice_fila, columna_resultado]
            return resultado

        indice_fila += 1

    columna_resultado = tabla_df.columns[0]
    ultima_fila       = numero_de_filas - 1
    resultado         = tabla_df.loc[ultima_fila, columna_resultado]
    return resultado


# =============================================================================
#   SECCIÓN 4 — CLASE PRINCIPAL DE SIMULACIÓN
# =============================================================================

class Estacionamiento_Valet_Parking():

    CAPACIDAD_FIJA = 50

    def __init__(self, num_choferes=3):
        self.capacidad_total = Estacionamiento_Valet_Parking.CAPACIDAD_FIJA
        self.num_choferes    = num_choferes
        self.registros       = []

    def mostrar_tablas(self):
        pd.set_option("display.float_format", "{:.4f}".format)
        pd.set_option("display.max_columns", 20)
        pd.set_option("display.width", 120)

        print("\n" + "=" * 70)
        print("  TABLAS DE DATOS HISTORICOS")
        print("=" * 70)

        print("\n--- TABLA 1: Tiempo de Recepcion (min) ---")
        print(TABLA_1_RECEPCION.to_string(index=False))

        print("\n--- TABLA 2: Tiempo de Maniobra (min) ---")
        print(TABLA_2_MANIOBRA.to_string(index=False))

        print("\n--- TABLA 3: Permanencia del Vehiculo (h) ---")
        print(TABLA_3_PERMANENCIA.to_string(index=False))

        print("\n--- TABLA 4: Solicitud de Devolucion (min) ---")
        print(TABLA_4_SOLICITUD.to_string(index=False))

        print("\n--- TABLA 5: Recuperacion y Devolucion (min) ---")
        print(TABLA_5_DEVOLUCION.to_string(index=False))

        print("\n--- TABLA 6: Tasa de Llegadas por Turno ---")
        print(TABLA_6_LLEGADAS.to_string(index=False))

        print("\n--- TABLA 7: Cajones en Mantenimiento ---")
        print(TABLA_7_MANTENIMIENTO.to_string(index=False))

    def metodo_estacionamiento(self, num_vehiculos=20):
        self.registros = []

        na_mantenimiento         = generar_na()
        cajones_en_mantenimiento = consultar_tabla(na_mantenimiento, TABLA_7_MANTENIMIENTO)
        cajones_disponibles      = self.capacidad_total - cajones_en_mantenimiento
        cajones_ocupados         = 0

        relojes_choferes = []
        numero_chofer    = 0
        while numero_chofer < self.num_choferes:
            relojes_choferes.append(0)
            numero_chofer += 1

        tiempo_turno_actual = 0
        ingresos_totales    = 0.0
        costos_totales      = 0.0
        penalizaciones      = 0.0
        total_espera_cola   = 0.0

        print("\n" + "=" * 65)
        print("  PARAMETROS DEL DIA")
        print("=" * 65)
        print(f"  Capacidad total de cajones : {self.capacidad_total}")
        print(f"  Choferes disponibles       : {self.num_choferes}")
        print(f"  NA mantenimiento           : {na_mantenimiento:.10f}")
        print(f"  Cajones en mantenimiento   : {cajones_en_mantenimiento}")
        print(f"  Cajones disponibles        : {cajones_disponibles}")
        print(f"  Tarifa valet ($MXN)        : ${TARIFA_VALET}")
        print(f"  Costo chofer ($/min)       : ${COSTO_CHOFER_POR_MIN}")
        print(f"  Penalizacion negado ($)    : ${PENALIZACION_NEGADO}")

        vehiculo_numero = 1

        while vehiculo_numero <= num_vehiculos:

            registro = {}
            registro["vehiculo"] = vehiculo_numero

            if cajones_ocupados >= cajones_disponibles:
                registro["atendido"]     = False
                registro["cajon_dispon"] = "No"
                registro["chofer_asig"]  = "---"
                registro["t_espera"]     = 0
                registro["ganancia"]     = -PENALIZACION_NEGADO

                penalizaciones += PENALIZACION_NEGADO
                costos_totales += PENALIZACION_NEGADO

                self.registros.append(registro)
                vehiculo_numero += 1
                continue

            indice_chofer_libre = 0
            tiempo_libre_minimo = relojes_choferes[0]

            indice_busqueda = 1
            while indice_busqueda < self.num_choferes:
                if relojes_choferes[indice_busqueda] < tiempo_libre_minimo:
                    tiempo_libre_minimo = relojes_choferes[indice_busqueda]
                    indice_chofer_libre = indice_busqueda
                indice_busqueda += 1

            if tiempo_libre_minimo > tiempo_turno_actual:
                t_espera_cola = tiempo_libre_minimo - tiempo_turno_actual
            else:
                t_espera_cola = 0

            total_espera_cola += t_espera_cola

            registro["atendido"]     = True
            registro["cajon_dispon"] = "Si"
            registro["chofer_asig"]  = indice_chofer_libre + 1
            registro["t_espera"]     = t_espera_cola

            na_recepcion = generar_na()
            t_recepcion  = consultar_tabla(na_recepcion, TABLA_1_RECEPCION)
            registro["na_recepcion"] = round(na_recepcion, 10)
            registro["t_recepcion"]  = t_recepcion

            na_maniobra = generar_na()
            t_maniobra  = consultar_tabla(na_maniobra, TABLA_2_MANIOBRA)
            registro["na_maniobra"] = round(na_maniobra, 10)
            registro["t_maniobra"]  = t_maniobra

            na_permanencia = generar_na()
            t_permanencia  = consultar_tabla(na_permanencia, TABLA_3_PERMANENCIA)
            registro["na_permanencia"] = round(na_permanencia, 10)
            registro["t_permanencia"]  = t_permanencia

            na_solicitud = generar_na()
            t_solicitud  = consultar_tabla(na_solicitud, TABLA_4_SOLICITUD)
            registro["na_solicitud"] = round(na_solicitud, 10)
            registro["t_solicitud"]  = t_solicitud

            na_devolucion = generar_na()
            t_devolucion  = consultar_tabla(na_devolucion, TABLA_5_DEVOLUCION)
            registro["na_devolucion"] = round(na_devolucion, 10)
            registro["t_devolucion"]  = t_devolucion

            cajones_ocupados += 1

            t_chofer_activo = t_recepcion + t_maniobra + t_solicitud + t_devolucion

            ingreso  = TARIFA_VALET
            costo    = t_chofer_activo * COSTO_CHOFER_POR_MIN
            ganancia = ingreso - costo

            ingresos_totales += ingreso
            costos_totales   += costo

            registro["t_chofer"]  = t_chofer_activo
            registro["ingreso"]   = ingreso
            registro["costo"]     = round(costo, 2)
            registro["ganancia"]  = round(ganancia, 2)

            tiempo_inicio_atencion                = max(tiempo_turno_actual, tiempo_libre_minimo)
            tiempo_nuevo_libre                    = tiempo_inicio_atencion + t_chofer_activo
            relojes_choferes[indice_chofer_libre] = tiempo_nuevo_libre

            tiempo_turno_actual = tiempo_inicio_atencion

            self.registros.append(registro)
            vehiculo_numero += 1

        costo_total_modelo  = round(costos_totales, 2)
        ganancias_obtenidas = round(ingresos_totales - costos_totales, 2)

        self.ingresos_totales  = round(ingresos_totales, 2)
        self.costos_totales    = costo_total_modelo
        self.penalizaciones    = round(penalizaciones, 2)
        self.ganancias_netas   = ganancias_obtenidas
        self.total_espera_cola = round(total_espera_cola, 2)
        self.relojes_choferes  = relojes_choferes

        return costo_total_modelo, ganancias_obtenidas


# =============================================================================
#   SECCIÓN 5 — PALETA DE COLORES
# =============================================================================

COLOR_BG_DARK      = "#1A1D2E"
COLOR_BG_CARD      = "#232740"
COLOR_BG_INPUT     = "#2E3354"
COLOR_ACCENT_BLUE  = "#4A90D9"
COLOR_ACCENT_TEAL  = "#3BBFA4"
COLOR_ACCENT_AMBER = "#F5A623"
COLOR_ACCENT_RED   = "#E05A5A"
COLOR_TEXT_PRIMARY = "#E8EAF6"
COLOR_TEXT_MUTED   = "#8B90B0"
COLOR_BORDER       = "#3A3F68"


# =============================================================================
#   SECCIÓN 6 — APLICACIÓN PRINCIPAL
# =============================================================================

class AppValetParking(ctk.CTk):

    def __init__(self):
        super().__init__()

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.title("Simulación Monte Carlo — Valet Parking")
        self.geometry("1200x820")
        self.minsize(1000, 700)
        self.configure(fg_color=COLOR_BG_DARK)

        self.hotel = None
        self._construir_ui()
        # Simular automáticamente al abrir
        self.after(300, self._iniciar_simulacion)

    # -------------------------------------------------------------------------
    # CONSTRUCCIÓN DE LA INTERFAZ
    # -------------------------------------------------------------------------

    def _construir_ui(self):

        frame_header = ctk.CTkFrame(self, fg_color=COLOR_BG_CARD, corner_radius=0, height=64)
        frame_header.pack(fill="x", side="top")
        frame_header.pack_propagate(False)

        ctk.CTkLabel(
            frame_header,
            text="  🚗  Simulación Monte Carlo — Valet Parking",
            font=ctk.CTkFont(size=20, weight="bold"),
            text_color=COLOR_TEXT_PRIMARY,
        ).pack(side="left", padx=24, pady=16)

        ctk.CTkLabel(
            frame_header,
            text="50 cajones disponibles",
            font=ctk.CTkFont(size=13),
            text_color=COLOR_ACCENT_TEAL,
        ).pack(side="right", padx=24)

        frame_body = ctk.CTkFrame(self, fg_color="transparent")
        frame_body.pack(fill="both", expand=True, padx=16, pady=12)

        frame_body.columnconfigure(0, weight=0, minsize=280)
        frame_body.columnconfigure(1, weight=1)
        frame_body.rowconfigure(0, weight=1)

        self.panel_izq = ctk.CTkFrame(
            frame_body, fg_color=COLOR_BG_CARD,
            corner_radius=12, border_width=1, border_color=COLOR_BORDER,
        )
        self.panel_izq.grid(row=0, column=0, sticky="nsew", padx=(0, 10))

        self._construir_panel_parametros(self.panel_izq)

        self.panel_der = ctk.CTkFrame(
            frame_body, fg_color=COLOR_BG_CARD,
            corner_radius=12, border_width=1, border_color=COLOR_BORDER,
        )
        self.panel_der.grid(row=0, column=1, sticky="nsew")

        self._construir_panel_resultados(self.panel_der)

    # ── Panel de parámetros ───────────────────────────────────────────────────

    def _construir_panel_parametros(self, parent):

        ctk.CTkLabel(
            parent,
            text="Parámetros del turno",
            font=ctk.CTkFont(size=15, weight="bold"),
            text_color=COLOR_ACCENT_BLUE,
        ).pack(anchor="w", padx=20, pady=(18, 4))

        ctk.CTkFrame(parent, fg_color=COLOR_BORDER, height=1).pack(fill="x", padx=20, pady=(0, 14))

        self._label_campo(parent, "Choferes disponibles")
        self.entry_choferes = self._entry_campo(parent, valor_defecto="3")

        self._label_campo(parent, "Vehículos a simular")
        self.entry_vehiculos = self._entry_campo(parent, valor_defecto="20")

        ctk.CTkFrame(parent, fg_color=COLOR_BORDER, height=1).pack(fill="x", padx=20, pady=(18, 10))

        ctk.CTkLabel(
            parent,
            text="Tarifas del servicio",
            font=ctk.CTkFont(size=13, weight="bold"),
            text_color=COLOR_TEXT_MUTED,
        ).pack(anchor="w", padx=20, pady=(0, 8))

        self._info_fila(parent, "Tarifa valet",         f"${TARIFA_VALET} MXN",         COLOR_ACCENT_TEAL)
        self._info_fila(parent, "Costo chofer / min",   f"${COSTO_CHOFER_POR_MIN} MXN", COLOR_ACCENT_AMBER)
        self._info_fila(parent, "Penalización negado",  f"${PENALIZACION_NEGADO} MXN",  COLOR_ACCENT_RED)

        ctk.CTkFrame(parent, fg_color=COLOR_BORDER, height=1).pack(fill="x", padx=20, pady=(18, 10))

        ctk.CTkLabel(
            parent,
            text="Ver tabla histórica",
            font=ctk.CTkFont(size=13, weight="bold"),
            text_color=COLOR_TEXT_MUTED,
        ).pack(anchor="w", padx=20, pady=(0, 8))

        tablas_disponibles = [
            ("Tabla 1 – Recepción",     TABLA_1_RECEPCION),
            ("Tabla 2 – Maniobra",      TABLA_2_MANIOBRA),
            ("Tabla 3 – Permanencia",   TABLA_3_PERMANENCIA),
            ("Tabla 4 – Solicitud",     TABLA_4_SOLICITUD),
            ("Tabla 5 – Devolución",    TABLA_5_DEVOLUCION),
            ("Tabla 6 – Llegadas",      TABLA_6_LLEGADAS),
            ("Tabla 7 – Mantenimiento", TABLA_7_MANTENIMIENTO),
        ]

        for nombre, df in tablas_disponibles:
            btn = ctk.CTkButton(
                parent,
                text=nombre,
                font=ctk.CTkFont(size=12),
                fg_color=COLOR_BG_INPUT,
                hover_color=COLOR_BORDER,
                text_color=COLOR_TEXT_PRIMARY,
                border_color=COLOR_BORDER,
                border_width=1,
                height=28,
                corner_radius=6,
                command=lambda n=nombre, d=df: self._mostrar_tabla_historica(n, d),
            )
            btn.pack(fill="x", padx=20, pady=2)

        ctk.CTkFrame(parent, fg_color=COLOR_BORDER, height=1).pack(fill="x", padx=20, pady=(12, 10))

        self.btn_consola = ctk.CTkButton(
            parent,
            text="🖥  SIMULAR EN CONSOLA",
            font=ctk.CTkFont(size=13, weight="bold"),
            fg_color=COLOR_BG_INPUT,
            hover_color=COLOR_BORDER,
            text_color=COLOR_ACCENT_AMBER,
            border_color=COLOR_ACCENT_AMBER,
            border_width=1,
            height=38,
            corner_radius=10,
            command=self._iniciar_simulacion_consola,
        )
        self.btn_consola.pack(fill="x", padx=20, pady=(0, 6))

        self.btn_simular = ctk.CTkButton(
            parent,
            text="▶  EJECUTAR SIMULACIÓN",
            font=ctk.CTkFont(size=14, weight="bold"),
            fg_color=COLOR_ACCENT_BLUE,
            hover_color="#3A7AC9",
            text_color="white",
            height=44,
            corner_radius=10,
            command=self._iniciar_simulacion,
        )
        self.btn_simular.pack(fill="x", padx=20, pady=(0, 20))

    # ── Panel de resultados ───────────────────────────────────────────────────

    def _construir_panel_resultados(self, parent):

        self.tabview = ctk.CTkTabview(
            parent,
            fg_color=COLOR_BG_CARD,
            segmented_button_fg_color=COLOR_BG_INPUT,
            segmented_button_selected_color=COLOR_ACCENT_BLUE,
            segmented_button_selected_hover_color="#3A7AC9",
            segmented_button_unselected_color=COLOR_BG_INPUT,
            segmented_button_unselected_hover_color=COLOR_BORDER,
            text_color=COLOR_TEXT_PRIMARY,
            border_width=0,
        )
        self.tabview.pack(fill="both", expand=True, padx=4, pady=4)

        self.tabview.add("Resumen")
        self.tabview.add("Tabla de simulación")
        self.tabview.add("Estado de choferes")
        self.tabview.add("Log completo")

        self._construir_tab_resumen(self.tabview.tab("Resumen"))
        self._construir_tab_tabla(self.tabview.tab("Tabla de simulación"))
        self._construir_tab_choferes(self.tabview.tab("Estado de choferes"))
        self._construir_tab_log(self.tabview.tab("Log completo"))

    # ── Pestaña: Resumen ──────────────────────────────────────────────────────

    def _construir_tab_resumen(self, parent):

        parent.configure(fg_color="transparent")

        frame_kpis = ctk.CTkFrame(parent, fg_color="transparent")
        frame_kpis.pack(fill="x", padx=12, pady=(12, 8))

        for i in range(4):
            frame_kpis.columnconfigure(i, weight=1)

        self.kpi_atendidos  = self._kpi_card(frame_kpis, "Vehículos atendidos",  "—", COLOR_ACCENT_TEAL,  0)
        self.kpi_negados    = self._kpi_card(frame_kpis, "Negados (sin cajón)",  "—", COLOR_ACCENT_RED,   1)
        self.kpi_ganancias  = self._kpi_card(frame_kpis, "Ganancias obtenidas",  "—", COLOR_ACCENT_TEAL,  2)
        self.kpi_costos     = self._kpi_card(frame_kpis, "Costo total modelo",   "—", COLOR_ACCENT_AMBER, 3)

        frame_kpis2 = ctk.CTkFrame(parent, fg_color="transparent")
        frame_kpis2.pack(fill="x", padx=12, pady=(0, 12))

        for i in range(4):
            frame_kpis2.columnconfigure(i, weight=1)

        self.kpi_espera      = self._kpi_card(frame_kpis2, "Espera total cola",  "—", COLOR_ACCENT_BLUE, 0)
        self.kpi_prom_espera = self._kpi_card(frame_kpis2, "Espera promedio",     "—", COLOR_ACCENT_BLUE, 1)
        self.kpi_prom_chofer = self._kpi_card(frame_kpis2, "T. chofer promedio",  "—", COLOR_TEXT_MUTED,  2)
        self.kpi_cajones     = self._kpi_card(frame_kpis2, "Cajones disponibles", "—", COLOR_TEXT_MUTED,  3)

        frame_detalle = ctk.CTkFrame(parent, fg_color=COLOR_BG_INPUT, corner_radius=10)
        frame_detalle.pack(fill="both", expand=True, padx=12, pady=(0, 12))

        ctk.CTkLabel(
            frame_detalle,
            text="Detalle completo del turno",
            font=ctk.CTkFont(size=13, weight="bold"),
            text_color=COLOR_TEXT_MUTED,
        ).pack(anchor="w", padx=16, pady=(12, 6))

        self.text_resumen = ctk.CTkTextbox(
            frame_detalle,
            fg_color="transparent",
            text_color=COLOR_TEXT_PRIMARY,
            font=ctk.CTkFont(family="Courier", size=12),
            wrap="none",
            activate_scrollbars=True,
        )
        self.text_resumen.pack(fill="both", expand=True, padx=12, pady=(0, 12))
        self.text_resumen.insert("end", "Ejecuta la simulación para ver los resultados.")
        self.text_resumen.configure(state="disabled")

    # ── Pestaña: Tabla de simulación ─────────────────────────────────────────

    def _construir_tab_tabla(self, parent):

        parent.configure(fg_color="transparent")

        frame_toolbar = ctk.CTkFrame(parent, fg_color="transparent")
        frame_toolbar.pack(fill="x", padx=12, pady=(8, 4))

        ctk.CTkLabel(
            frame_toolbar,
            text="Registros por vehículo",
            font=ctk.CTkFont(size=13, weight="bold"),
            text_color=COLOR_TEXT_MUTED,
        ).pack(side="left")

        self.lbl_conteo_filas = ctk.CTkLabel(
            frame_toolbar,
            text="",
            font=ctk.CTkFont(size=12),
            text_color=COLOR_ACCENT_TEAL,
        )
        self.lbl_conteo_filas.pack(side="right")

        frame_tabla_outer = ctk.CTkFrame(parent, fg_color=COLOR_BG_INPUT, corner_radius=10)
        frame_tabla_outer.pack(fill="both", expand=True, padx=12, pady=(0, 12))

        self.text_tabla = ctk.CTkTextbox(
            frame_tabla_outer,
            fg_color="transparent",
            text_color=COLOR_TEXT_PRIMARY,
            font=ctk.CTkFont(family="Courier", size=11),
            wrap="none",
            activate_scrollbars=True,
        )
        self.text_tabla.pack(fill="both", expand=True, padx=8, pady=8)
        self.text_tabla.insert("end", "Ejecuta la simulación para ver la tabla de vehículos.")
        self.text_tabla.configure(state="disabled")

    # ── Pestaña: Estado de choferes ───────────────────────────────────────────

    def _construir_tab_choferes(self, parent):

        parent.configure(fg_color="transparent")

        ctk.CTkLabel(
            parent,
            text="Estado final de los choferes al terminar el turno",
            font=ctk.CTkFont(size=13, weight="bold"),
            text_color=COLOR_TEXT_MUTED,
        ).pack(anchor="w", padx=16, pady=(12, 8))

        self.frame_choferes_scroll = ctk.CTkScrollableFrame(
            parent,
            fg_color="transparent",
            scrollbar_button_color=COLOR_BORDER,
        )
        self.frame_choferes_scroll.pack(fill="both", expand=True, padx=12, pady=(0, 12))

        self.lbl_choferes_placeholder = ctk.CTkLabel(
            self.frame_choferes_scroll,
            text="Ejecuta la simulación para ver el estado de los choferes.",
            text_color=COLOR_TEXT_MUTED,
            font=ctk.CTkFont(size=13),
        )
        self.lbl_choferes_placeholder.pack(pady=40)

    # ── Pestaña: Log completo ─────────────────────────────────────────────────

    def _construir_tab_log(self, parent):

        parent.configure(fg_color="transparent")

        frame_log = ctk.CTkFrame(parent, fg_color=COLOR_BG_INPUT, corner_radius=10)
        frame_log.pack(fill="both", expand=True, padx=12, pady=12)

        ctk.CTkLabel(
            frame_log,
            text="Salida completa de la simulación (stdout)",
            font=ctk.CTkFont(size=12),
            text_color=COLOR_TEXT_MUTED,
        ).pack(anchor="w", padx=12, pady=(8, 4))

        self.text_log = ctk.CTkTextbox(
            frame_log,
            fg_color="transparent",
            text_color=COLOR_TEXT_PRIMARY,
            font=ctk.CTkFont(family="Courier", size=11),
            wrap="none",
            activate_scrollbars=True,
        )
        self.text_log.pack(fill="both", expand=True, padx=8, pady=(0, 8))
        self.text_log.insert("end", "El log completo aparecerá aquí después de simular.")
        self.text_log.configure(state="disabled")

    # =========================================================================
    #   WIDGETS REUTILIZABLES
    # =========================================================================

    def _label_campo(self, parent, texto):
        ctk.CTkLabel(
            parent,
            text=texto,
            font=ctk.CTkFont(size=12),
            text_color=COLOR_TEXT_MUTED,
        ).pack(anchor="w", padx=20, pady=(8, 2))

    def _entry_campo(self, parent, valor_defecto=""):
        entry = ctk.CTkEntry(
            parent,
            fg_color=COLOR_BG_INPUT,
            border_color=COLOR_BORDER,
            text_color=COLOR_TEXT_PRIMARY,
            placeholder_text_color=COLOR_TEXT_MUTED,
            font=ctk.CTkFont(size=14, weight="bold"),
            height=36,
            corner_radius=8,
        )
        entry.insert(0, valor_defecto)
        entry.pack(fill="x", padx=20, pady=(0, 4))
        return entry

    def _info_fila(self, parent, etiqueta, valor, color_valor):
        frame = ctk.CTkFrame(parent, fg_color="transparent")
        frame.pack(fill="x", padx=20, pady=2)

        ctk.CTkLabel(
            frame,
            text=etiqueta,
            font=ctk.CTkFont(size=12),
            text_color=COLOR_TEXT_MUTED,
        ).pack(side="left")

        ctk.CTkLabel(
            frame,
            text=valor,
            font=ctk.CTkFont(size=12, weight="bold"),
            text_color=color_valor,
        ).pack(side="right")

    def _kpi_card(self, parent, titulo, valor_inicial, color, columna):
        frame = ctk.CTkFrame(
            parent,
            fg_color=COLOR_BG_INPUT,
            corner_radius=10,
            border_width=1,
            border_color=COLOR_BORDER,
        )
        frame.grid(row=0, column=columna, sticky="ew", padx=4, pady=0)

        ctk.CTkLabel(
            frame,
            text=titulo,
            font=ctk.CTkFont(size=11),
            text_color=COLOR_TEXT_MUTED,
        ).pack(anchor="w", padx=12, pady=(10, 2))

        lbl_valor = ctk.CTkLabel(
            frame,
            text=valor_inicial,
            font=ctk.CTkFont(size=22, weight="bold"),
            text_color=color,
        )
        lbl_valor.pack(anchor="w", padx=12, pady=(0, 10))

        return lbl_valor

    # =========================================================================
    #   VENTANA MODAL — TABLA HISTÓRICA
    # =========================================================================

    def _mostrar_tabla_historica(self, nombre, df):

        ventana = ctk.CTkToplevel(self)
        ventana.title(nombre)
        ventana.geometry("680x420")
        ventana.configure(fg_color=COLOR_BG_DARK)
        ventana.lift()
        ventana.focus_force()
        ventana.grab_set()

        ctk.CTkLabel(
            ventana,
            text=nombre,
            font=ctk.CTkFont(size=15, weight="bold"),
            text_color=COLOR_ACCENT_BLUE,
        ).pack(anchor="w", padx=20, pady=(16, 4))

        ctk.CTkFrame(ventana, fg_color=COLOR_BORDER, height=1).pack(fill="x", padx=20, pady=(0, 10))

        frame_tabla = ctk.CTkFrame(ventana, fg_color=COLOR_BG_INPUT, corner_radius=10)
        frame_tabla.pack(fill="both", expand=True, padx=20, pady=(0, 20))

        texto = ctk.CTkTextbox(
            frame_tabla,
            fg_color="transparent",
            text_color=COLOR_TEXT_PRIMARY,
            font=ctk.CTkFont(family="Courier", size=12),
            wrap="none",
        )
        texto.pack(fill="both", expand=True, padx=10, pady=10)

        contenido = df.to_string(index=False)
        texto.insert("end", contenido)
        texto.configure(state="disabled")

    # =========================================================================
    #   LÓGICA DE SIMULACIÓN (hilo secundario para no congelar la UI)
    # =========================================================================

    def _iniciar_simulacion(self):

        try:
            num_choferes  = int(self.entry_choferes.get())
            num_vehiculos = int(self.entry_vehiculos.get())
        except ValueError:
            self._mostrar_error("Ingresa números enteros válidos en ambos campos.")
            return

        if num_choferes < 1 or num_vehiculos < 1:
            self._mostrar_error("Los valores deben ser mayores a 0.")
            return

        self.btn_simular.configure(state="disabled", text="⏳  Simulando...")

        hilo = threading.Thread(
            target=self._ejecutar_simulacion,
            args=(num_choferes, num_vehiculos),
            daemon=True,
        )
        hilo.start()

    def _ejecutar_simulacion(self, num_choferes, num_vehiculos):

        buffer_stdout   = io.StringIO()
        stdout_original = sys.stdout
        sys.stdout      = buffer_stdout

        try:
            hotel = Estacionamiento_Valet_Parking(num_choferes=num_choferes)
            costo_total_modelo, ganancias_obtenidas = hotel.metodo_estacionamiento(
                num_vehiculos=num_vehiculos
            )
            self.hotel = hotel
        finally:
            sys.stdout = stdout_original

        log_completo = buffer_stdout.getvalue()

        self.after(0, lambda: self._actualizar_ui(
            hotel, costo_total_modelo, ganancias_obtenidas, log_completo, num_vehiculos
        ))

    def _actualizar_ui(self, hotel, costo_total_modelo, ganancias_obtenidas, log_completo, num_vehiculos):

        ingresos        = hotel.ingresos_totales
        penalizaciones  = hotel.penalizaciones
        espera_cola     = hotel.total_espera_cola
        relojes_finales = hotel.relojes_choferes
        registros       = hotel.registros

        total_atendidos = 0
        total_negados   = 0
        for r in registros:
            if r["atendido"]:
                total_atendidos += 1
            else:
                total_negados   += 1

        suma_recep = suma_maniob = suma_perm = suma_chofer = suma_espera = 0.0
        for r in registros:
            if r["atendido"]:
                suma_recep   += r["t_recepcion"]
                suma_maniob  += r["t_maniobra"]
                suma_perm    += r["t_permanencia"]
                suma_chofer  += r["t_chofer"]
                suma_espera  += r["t_espera"]

        if total_atendidos > 0:
            prom_recep   = round(suma_recep   / total_atendidos, 2)
            prom_maniob  = round(suma_maniob  / total_atendidos, 2)
            prom_perm    = round(suma_perm    / total_atendidos, 2)
            prom_chofer  = round(suma_chofer  / total_atendidos, 2)
            prom_espera  = round(suma_espera  / total_atendidos, 2)
        else:
            prom_recep = prom_maniob = prom_perm = prom_chofer = prom_espera = 0

        self.kpi_atendidos.configure(text=str(total_atendidos))
        self.kpi_negados.configure(text=str(total_negados))
        self.kpi_ganancias.configure(text=f"${ganancias_obtenidas:.2f}")
        self.kpi_costos.configure(text=f"${costo_total_modelo:.2f}")
        self.kpi_espera.configure(text=f"{espera_cola:.1f} min")
        self.kpi_prom_espera.configure(text=f"{prom_espera:.2f} min")
        self.kpi_prom_chofer.configure(text=f"{prom_chofer:.2f} min")
        self.kpi_cajones.configure(text=str(hotel.capacidad_total))

        lineas_resumen = [
            f"{'─'*52}",
            f"  RESUMEN DEL TURNO",
            f"{'─'*52}",
            f"  {'Cajones del estacionamiento':<34} {hotel.capacidad_total}",
            f"  {'Choferes en turno':<34} {hotel.num_choferes}",
            f"  {'Vehículos atendidos':<34} {total_atendidos}",
            f"  {'Vehículos negados (sin cajón)':<34} {total_negados}",
            f"  {'Espera total en cola (min)':<34} {espera_cola:.2f}",
            f"  {'Espera promedio por vehículo (min)':<34} {prom_espera:.2f}",
            f"{'─'*52}",
            f"  {'Ingresos totales ($MXN)':<34} ${ingresos:.2f}",
            f"  {'Costo total del modelo ($MXN)':<34} ${costo_total_modelo:.2f}",
            f"  {'Penalizaciones ($MXN)':<34} ${penalizaciones:.2f}",
            f"  {'Ganancias obtenidas ($MXN)':<34} ${ganancias_obtenidas:.2f}",
            f"{'─'*52}",
            f"  {'Promedio T.Recepción (min)':<34} {prom_recep}",
            f"  {'Promedio T.Maniobra (min)':<34} {prom_maniob}",
            f"  {'Promedio T.Permanencia (h)':<34} {prom_perm}",
            f"  {'Promedio T.Chofer activo (min)':<34} {prom_chofer}",
            f"{'─'*52}",
        ]

        self.text_resumen.configure(state="normal")
        self.text_resumen.delete("1.0", "end")
        self.text_resumen.insert("end", "\n".join(lineas_resumen))
        self.text_resumen.configure(state="disabled")

        self._renderizar_tabla_vehiculos(registros, total_atendidos + total_negados)
        self._renderizar_estado_choferes(relojes_finales, registros)

        self.text_log.configure(state="normal")
        self.text_log.delete("1.0", "end")
        self.text_log.insert("end", log_completo)
        self.text_log.configure(state="disabled")

        self.btn_simular.configure(state="normal", text="▶  EJECUTAR SIMULACIÓN")
        self.tabview.set("Resumen")

    # ── Renderizado de tabla de vehículos ─────────────────────────────────────

    def _renderizar_tabla_vehiculos(self, registros, total):

        self.lbl_conteo_filas.configure(text=f"{total} vehículos")

        encabezado = (
            f"{'Veh':>4}  {'Cajón':>5}  {'Chofer':>6}  {'Espera':>6}"
            f"  {'T.Recep':>7}  {'T.Maniob':>8}  {'T.Perm':>6}"
            f"  {'T.Solic':>7}  {'T.Devol':>7}  {'T.Chofer':>8}"
            f"  {'Ingreso':>8}  {'Costo':>7}  {'Ganancia':>9}"
        )
        separador = "─" * len(encabezado)

        lineas = [encabezado, separador]

        for r in registros:
            if r["atendido"]:
                linea = (
                    f"{r['vehiculo']:>4}  {'Sí':>5}  {r['chofer_asig']:>6}  {r['t_espera']:>6.0f}"
                    f"  {r['t_recepcion']:>7}  {r['t_maniobra']:>8}  {r['t_permanencia']:>6}"
                    f"  {r['t_solicitud']:>7}  {r['t_devolucion']:>7}  {r['t_chofer']:>8}"
                    f"  ${r['ingreso']:>7}  ${r['costo']:>6.2f}  ${r['ganancia']:>8.2f}"
                )
            else:
                linea = (
                    f"{r['vehiculo']:>4}  {'No':>5}  {'---':>6}  {'---':>6}"
                    f"  {'SERVICIO NEGADO — sin cajón disponible':<60}"
                    f"  ${-PENALIZACION_NEGADO:>8.2f}"
                )
            lineas.append(linea)

        self.text_tabla.configure(state="normal")
        self.text_tabla.delete("1.0", "end")
        self.text_tabla.insert("end", "\n".join(lineas))
        self.text_tabla.configure(state="disabled")

    # ── Renderizado de tarjetas de choferes ───────────────────────────────────

    def _renderizar_estado_choferes(self, relojes_finales, registros):

        for widget in self.frame_choferes_scroll.winfo_children():
            widget.destroy()

        num_choferes = len(relojes_finales)

        for idx in range(num_choferes):

            minuto_libre = relojes_finales[idx]
            num_chofer   = idx + 1

            vehiculos_del_chofer = []
            for r in registros:
                if r["atendido"] and r["chofer_asig"] == num_chofer:
                    vehiculos_del_chofer.append(r["vehiculo"])

            total_atendidos_chofer = len(vehiculos_del_chofer)

            if total_atendidos_chofer == 0:
                color_borde = COLOR_TEXT_MUTED
            elif minuto_libre > 150:
                color_borde = COLOR_ACCENT_AMBER
            else:
                color_borde = COLOR_ACCENT_TEAL

            card = ctk.CTkFrame(
                self.frame_choferes_scroll,
                fg_color=COLOR_BG_INPUT,
                corner_radius=12,
                border_width=2,
                border_color=color_borde,
            )
            card.pack(fill="x", padx=8, pady=6)

            frame_card_header = ctk.CTkFrame(card, fg_color="transparent")
            frame_card_header.pack(fill="x", padx=16, pady=(12, 6))

            ctk.CTkLabel(
                frame_card_header,
                text=f"Chofer  {num_chofer}",
                font=ctk.CTkFont(size=16, weight="bold"),
                text_color=color_borde,
            ).pack(side="left")

            ctk.CTkLabel(
                frame_card_header,
                text=f"libre al minuto  {minuto_libre}",
                font=ctk.CTkFont(size=13),
                text_color=COLOR_TEXT_MUTED,
            ).pack(side="right")

            frame_stats = ctk.CTkFrame(card, fg_color="transparent")
            frame_stats.pack(fill="x", padx=16, pady=(0, 12))
            frame_stats.columnconfigure(0, weight=1)
            frame_stats.columnconfigure(1, weight=1)
            frame_stats.columnconfigure(2, weight=1)

            self._stat_chofer(frame_stats, "Vehículos atendidos",
                              str(total_atendidos_chofer), COLOR_ACCENT_TEAL, 0)

            minutos_activo = 0
            for r in registros:
                if r["atendido"] and r["chofer_asig"] == num_chofer:
                    minutos_activo += r["t_chofer"]

            self._stat_chofer(frame_stats, "Minutos activo",
                              str(minutos_activo), COLOR_ACCENT_AMBER, 1)

            lista_vehs = ", ".join(str(v) for v in vehiculos_del_chofer) if vehiculos_del_chofer else "—"
            self._stat_chofer(frame_stats, "Vehículos (IDs)",
                              lista_vehs, COLOR_TEXT_MUTED, 2)

    def _stat_chofer(self, parent, titulo, valor, color, columna):
        frame = ctk.CTkFrame(parent, fg_color=COLOR_BG_CARD, corner_radius=8)
        frame.grid(row=0, column=columna, sticky="ew", padx=4, pady=4)

        ctk.CTkLabel(
            frame,
            text=titulo,
            font=ctk.CTkFont(size=11),
            text_color=COLOR_TEXT_MUTED,
        ).pack(anchor="w", padx=10, pady=(8, 2))

        ctk.CTkLabel(
            frame,
            text=valor,
            font=ctk.CTkFont(size=13, weight="bold"),
            text_color=color,
            wraplength=160,
        ).pack(anchor="w", padx=10, pady=(0, 8))

    # =========================================================================
    #   SIMULACIÓN MODO CONSOLA (replica exacta del __main__ original)
    # =========================================================================

    def _iniciar_simulacion_consola(self):

        try:
            num_choferes  = int(self.entry_choferes.get())
            num_vehiculos = int(self.entry_vehiculos.get())
        except ValueError:
            self._mostrar_error("Ingresa números enteros válidos en ambos campos.")
            return

        if num_choferes < 1 or num_vehiculos < 1:
            self._mostrar_error("Los valores deben ser mayores a 0.")
            return

        self.btn_consola.configure(state="disabled", text="⏳  Ejecutando...")
        self.btn_simular.configure(state="disabled")

        hilo = threading.Thread(
            target=self._ejecutar_simulacion_consola,
            args=(num_choferes, num_vehiculos),
            daemon=True,
        )
        hilo.start()

    def _ejecutar_simulacion_consola(self, num_choferes, num_vehiculos):

        buffer      = io.StringIO()
        stdout_orig = sys.stdout
        sys.stdout  = buffer

        try:
            hotel = Estacionamiento_Valet_Parking(num_choferes=num_choferes)

            print(f"  Estacionamiento iniciado con capacidad fija de {hotel.capacidad_total} cajones.")
            print(f"  Choferes en turno: {hotel.num_choferes}")

            hotel.mostrar_tablas()

            costo_total_modelo, ganancias_obtenidas = hotel.metodo_estacionamiento(
                num_vehiculos=num_vehiculos
            )

            ingresos        = hotel.ingresos_totales
            penalizaciones  = hotel.penalizaciones
            espera_cola     = hotel.total_espera_cola
            relojes_finales = hotel.relojes_choferes

            filas_atendidos = []
            filas_negados   = []

            for registro in hotel.registros:
                if registro["atendido"]:
                    fila = {
                        "Vehiculo":      registro["vehiculo"],
                        "Cajon":         registro["cajon_dispon"],
                        "Chofer":        registro["chofer_asig"],
                        "Espera(min)":   registro["t_espera"],
                        "NA Recep":      registro["na_recepcion"],
                        "T.Recep(min)":  registro["t_recepcion"],
                        "NA Maniob":     registro["na_maniobra"],
                        "T.Maniob(min)": registro["t_maniobra"],
                        "NA Perm":       registro["na_permanencia"],
                        "T.Perm(h)":     registro["t_permanencia"],
                        "NA Solic":      registro["na_solicitud"],
                        "T.Solic(min)":  registro["t_solicitud"],
                        "NA Devol":      registro["na_devolucion"],
                        "T.Devol(min)":  registro["t_devolucion"],
                        "T.Chofer(min)": registro["t_chofer"],
                        "Ingreso($)":    registro["ingreso"],
                        "Costo($)":      registro["costo"],
                        "Ganancia($)":   registro["ganancia"],
                    }
                    filas_atendidos.append(fila)
                else:
                    fila = {
                        "Vehiculo":      registro["vehiculo"],
                        "Cajon":         registro["cajon_dispon"],
                        "Chofer":        "---",
                        "Espera(min)":   "---",
                        "NA Recep":      "---",
                        "T.Recep(min)":  "---",
                        "NA Maniob":     "---",
                        "T.Maniob(min)": "---",
                        "NA Perm":       "---",
                        "T.Perm(h)":     "---",
                        "NA Solic":      "---",
                        "T.Solic(min)":  "---",
                        "NA Devol":      "---",
                        "T.Devol(min)":  "---",
                        "T.Chofer(min)": "---",
                        "Ingreso($)":    0,
                        "Costo($)":      PENALIZACION_NEGADO,
                        "Ganancia($)":   -PENALIZACION_NEGADO,
                    }
                    filas_negados.append(fila)

            todas = sorted(filas_atendidos + filas_negados, key=lambda x: x["Vehiculo"])
            df_simulacion = pd.DataFrame(todas)

            print("\n" + "=" * 80)
            print("  TABLA DE SIMULACION – MONTE CARLO VALET PARKING")
            print("=" * 80)
            pd.set_option("display.max_columns", 20)
            pd.set_option("display.width", 200)
            pd.set_option("display.float_format", "{:.4f}".format)
            print(df_simulacion.to_string(index=False))

            total_atendidos = total_negados = 0
            suma_recep = suma_maniob = suma_perm = suma_chofer = suma_espera = 0.0
            for r in hotel.registros:
                if r["atendido"]:
                    total_atendidos += 1
                    suma_recep   += r["t_recepcion"]
                    suma_maniob  += r["t_maniobra"]
                    suma_perm    += r["t_permanencia"]
                    suma_chofer  += r["t_chofer"]
                    suma_espera  += r["t_espera"]
                else:
                    total_negados += 1

            if total_atendidos > 0:
                prom_recep  = round(suma_recep  / total_atendidos, 2)
                prom_maniob = round(suma_maniob / total_atendidos, 2)
                prom_perm   = round(suma_perm   / total_atendidos, 2)
                prom_chofer = round(suma_chofer / total_atendidos, 2)
                prom_espera = round(suma_espera / total_atendidos, 2)
            else:
                prom_recep = prom_maniob = prom_perm = prom_chofer = prom_espera = 0

            estado_txt = "  ".join(
                f"Chofer {i+1}: libre al min {rel}" for i, rel in enumerate(relojes_finales)
            )

            df_resumen = pd.DataFrame({
                "Concepto": [
                    "Cajones del estacionamiento",
                    "Choferes en turno",
                    "Vehiculos atendidos",
                    "Vehiculos en cola de espera",
                    "Vehiculos negados (sin cajon)",
                    "Espera total en cola (min)",
                    "Espera promedio por vehiculo (min)",
                    "Ingresos totales ($MXN)",
                    "Costo total del modelo ($MXN)",
                    "Penalizaciones incluidas ($MXN)",
                    "Ganancias obtenidas ($MXN)",
                    "Promedio T.Recepcion (min)",
                    "Promedio T.Maniobra (min)",
                    "Promedio T.Permanencia (h)",
                    "Promedio T.Chofer activo (min)",
                    "Estado final choferes",
                ],
                "Valor": [
                    hotel.capacidad_total,
                    hotel.num_choferes,
                    total_atendidos,
                    int(espera_cola > 0),
                    total_negados,
                    round(espera_cola, 2),
                    prom_espera,
                    round(ingresos, 2),
                    costo_total_modelo,
                    round(penalizaciones, 2),
                    ganancias_obtenidas,
                    prom_recep,
                    prom_maniob,
                    prom_perm,
                    prom_chofer,
                    estado_txt,
                ],
            })

            print("\n" + "=" * 55)
            print("  RESUMEN DE LA SIMULACION")
            print("=" * 55)
            print(df_resumen.to_string(index=False))
            print("=" * 55)

            print("\n" + "=" * 55)
            print("  VARIABLES DE RETORNO DEL MODELO")
            print("=" * 55)
            print(f"  costo_total_modelo  = ${costo_total_modelo:.2f} MXN")
            print(f"  ganancias_obtenidas = ${ganancias_obtenidas:.2f} MXN")
            print("=" * 55)
            print("  (Estas son las dos variables que retorna el metodo")
            print("   metodo_estacionamiento() al ser importado)")
            print("=" * 55)

        finally:
            sys.stdout = stdout_orig

        output = buffer.getvalue()
        self.after(0, lambda: self._mostrar_ventana_consola(output))

    def _mostrar_ventana_consola(self, output):

        self.btn_consola.configure(state="normal", text="🖥  SIMULAR EN CONSOLA")
        self.btn_simular.configure(state="normal")

        ventana = ctk.CTkToplevel(self)
        ventana.title("Output de consola — Simulación completa")
        ventana.geometry("1100x700")
        ventana.configure(fg_color=COLOR_BG_DARK)
        ventana.lift()
        ventana.focus_force()
        ventana.grab_set()

        ctk.CTkLabel(
            ventana,
            text="🖥  Salida completa — modo consola",
            font=ctk.CTkFont(size=15, weight="bold"),
            text_color=COLOR_ACCENT_AMBER,
        ).pack(anchor="w", padx=20, pady=(16, 4))

        ctk.CTkFrame(ventana, fg_color=COLOR_BORDER, height=1).pack(fill="x", padx=20, pady=(0, 8))

        frame_out = ctk.CTkFrame(ventana, fg_color=COLOR_BG_INPUT, corner_radius=10)
        frame_out.pack(fill="both", expand=True, padx=20, pady=(0, 12))

        texto = ctk.CTkTextbox(
            frame_out,
            fg_color="transparent",
            text_color=COLOR_TEXT_PRIMARY,
            font=ctk.CTkFont(family="Courier", size=11),
            wrap="none",
            activate_scrollbars=True,
        )
        texto.pack(fill="both", expand=True, padx=10, pady=10)
        texto.insert("end", output)
        texto.configure(state="disabled")

        ctk.CTkButton(
            ventana,
            text="Cerrar",
            fg_color=COLOR_BG_INPUT,
            hover_color=COLOR_BORDER,
            text_color=COLOR_TEXT_PRIMARY,
            border_color=COLOR_BORDER,
            border_width=1,
            height=36,
            corner_radius=8,
            command=ventana.destroy,
        ).pack(pady=(0, 16))

    # =========================================================================
    #   UTILIDADES
    # =========================================================================

    def _mostrar_error(self, mensaje):
        ventana = ctk.CTkToplevel(self)
        ventana.title("Error de entrada")
        ventana.geometry("380x160")
        ventana.configure(fg_color=COLOR_BG_DARK)
        ventana.grab_set()

        ctk.CTkLabel(
            ventana,
            text="⚠  Error de entrada",
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color=COLOR_ACCENT_RED,
        ).pack(pady=(24, 8))

        ctk.CTkLabel(
            ventana,
            text=mensaje,
            font=ctk.CTkFont(size=13),
            text_color=COLOR_TEXT_PRIMARY,
        ).pack()

        ctk.CTkButton(
            ventana,
            text="Cerrar",
            fg_color=COLOR_ACCENT_RED,
            hover_color="#B04040",
            command=ventana.destroy,
        ).pack(pady=20)


# =============================================================================
#   PUNTO DE ENTRADA
# =============================================================================

if __name__ == "__main__":
    app = AppValetParking()
    app.mainloop()