import threading
import random
import pandas as pd
import customtkinter as ctk
from pathlib import Path




class Agarrar_aleatorios:
    #agarrar los aleatorios del archivo y si no, uso aletorios random

    def __init__(self):
        self._numeros: list[float] = []
        self._indice:  int        = 0
        self._cargar()

    def _cargar(self):
        ruta = Path(__file__).resolve().parent / "Aleatorios.txt"
        try:
            with open(ruta, "r") as f:
                self._numeros = [
                    float(linea.strip())
                    for linea in f
                    if linea.strip()        # ignorar líneas vacías
                ]
            print(f"[Aleatorios] {len(self._numeros)} números cargados.")
        except FileNotFoundError:
            print("[Aleatorios] Archivo no encontrado, usando random.random().")

    def siguiente(self) -> float:
        """Devuelve el próximo número; si se agotaron usa random como respaldo."""
        if self._indice < len(self._numeros):
            na = self._numeros[self._indice]
            self._indice += 1
            return na
        # respaldo
        return random.random()

    def reiniciar(self):
        """Vuelve al inicio del archivo para una nueva corrida."""
        self._indice = 0

    def reiniciar(self):
        """Vuelve al inicio del archivo para una nueva corrida."""
        self._indice = 0


#cargar archivo
_aleatorios = Agarrar_aleatorios()


def generar_probabilidades_aleatorias(n):
    valores=[]
    for i in range(n):
        valores.append(random.random())
    suma=sum(valores)
    probabilidades=[]
    for valor in valores:
        probabilidades.append(round(valor / suma, 4))
        #hacer q sea 1 de a huevo
    diferencia = round(1.0 - sum(probabilidades),4)
    probabilidades[-1] = round(probabilidades[-1] + diferencia, 4) #uktima
    return probabilidades


def construir_tabla_aleatoria(tiempos):
    n=len(tiempos)
    #probabilidaedes
    valores=[]
    for i in range(n):
        valores.append(random.random())
    suma=sum(valores)
    probabilidades=[]

    for valor in valores:
        probabilidades.append(round(valor / suma, 4))
    diferencia=round(1.0 - sum(probabilidades),4)
    probabilidades[-1]= round(probabilidades[-1] + diferencia , 4)

    #probabilidad acumulada
    prob_acum=[]
    acum=0.0

    for p in probabilidades:
        acum=round(acum + p , 4)
        prob_acum.append(acum)
    prob_acum[-1]=1.0

    rango_inf = []
    rango_inf.append(0.0)
    for pa in prob_acum[:-1]:
        rango_inf.append(round(pa + 0.0001, 4))

    rango_sup = []
    for pa in prob_acum:
        rango_sup.append(pa)    


    return {
        "TIEMPO": tiempos,
        "PROB": probabilidades,
        "PROB ACUM": prob_acum,
        "RANGO INF": rango_inf,
        "RANGO SUP": rango_sup,
    }


def construir_tabla_llegadas_aleatoria():
    turnos   = ["Madrugada", "Mañana", "Medio día", "Tarde pico", "Noche", "Noche tardía"]
    horarios = ["00-06h", "06-10h", "10-14h", "14-18h", "18-22h", "22-00h"]
    veh_hora = ["1-2", "4-6", "6-9", "10-14", "8-11", "3-5"]
    n= len(turnos)
    probabilidades= generar_probabilidades_aleatorias(n)
    prob_acum = []
    acum      = 0.0
    for p in probabilidades:
        acum = round(acum + p, 4)
        prob_acum.append(acum)
    prob_acum[-1] = 1.0
    rango_inf = [0.0] + [round(pa + 0.0001, 4) for pa in prob_acum[:-1]]
    return {
        "turno":     turnos,
        "horario":   horarios,
        "veh_hora":  veh_hora,
        "prob":      probabilidades,
        "prob_acum": prob_acum,
        "rango_inf": rango_inf,
        "rango_sup": prob_acum.copy(),
    }


def generar_todas_las_tablas():
    return {
        "TABLA_1_RECEPCION":     pd.DataFrame(construir_tabla_aleatoria([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])),
        "TABLA_2_MANIOBRA":      pd.DataFrame(construir_tabla_aleatoria([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])),
        "TABLA_3_PERMANENCIA":   pd.DataFrame(construir_tabla_aleatoria([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])),
        "TABLA_4_SOLICITUD":     pd.DataFrame(construir_tabla_aleatoria([2, 3, 4, 5])),
        "TABLA_5_DEVOLUCION":    pd.DataFrame(construir_tabla_aleatoria([2, 3, 4, 5, 6])),
        "TABLA_6_LLEGADAS":      pd.DataFrame(construir_tabla_llegadas_aleatoria()),
        "TABLA_7_MANTENIMIENTO": pd.DataFrame(construir_tabla_aleatoria([10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21])),
    }


# =============================================================================
#   SECCIÓN 2 — PARÁMETROS ECONÓMICOS
# =============================================================================

TARIFA_VALET         = 80
COSTO_CHOFER_POR_MIN = 20
PENALIZACION_NEGADO  = 50


# =============================================================================
#   SECCIÓN 3 — FUNCIONES AUXILIARES
# =============================================================================

def generar_na():
    na = _aleatorios.siguiente()
    print(f"NA usado: {na}")
    return na


def consultar_tabla(na, tabla_df):
    for i in range(len(tabla_df)):
        if tabla_df.loc[i, "rango_inf"] <= na <= tabla_df.loc[i, "rango_sup"]:
            return tabla_df.loc[i, tabla_df.columns[0]]
    return tabla_df.loc[len(tabla_df) - 1, tabla_df.columns[0]]


def recalcular_rangos(df: pd.DataFrame) -> pd.DataFrame:
    df    = df.copy()
    acum  = 0.0
    pa    = []
    for p in df["prob"]:
        acum = round(acum + p, 4)
        pa.append(acum)
    pa[-1] = 1.0
    df["prob_acum"] = pa
    df["rango_inf"] = [0.0] + [round(x + 0.0001, 4) for x in pa[:-1]]
    df["rango_sup"] = pa
    return df


def consultar_turno_t6(na, t6_df):
    #NUERO ALEATORIO PARA SABER EN Q TURBNO LLEGA
    for i in range(len(t6_df)):
        if t6_df.loc[i, "rango_inf"] <= na <= t6_df.loc[i, "rango_sup"]:
            return t6_df.loc[i, "turno"], t6_df.loc[i, "horario"]
    return t6_df.loc[len(t6_df) - 1, "turno"], t6_df.loc[len(t6_df) - 1, "horario"]


# =============================================================================
#   SECCIÓN 4 — MODELO DE SIMULACIÓN
# =============================================================================

class Estacionamiento_Valet_Parking:

    CAPACIDAD_FIJA = 50

    def __init__(self, num_choferes=3):
        self.capacidad_total = self.CAPACIDAD_FIJA
        self.num_choferes    = num_choferes
        self.registros       = []
        self.tablas          = None

    def metodo_estacionamiento(self, num_vehiculos=20):
        """
        Simula N vehículos. Para cada uno se sortea un NA en T6 para
        determinar a qué turno pertenece. Luego pasa por T1-T5 y T7 normal.
        """
        self.registros = []
        if self.tablas is None:
            self.tablas = generar_todas_las_tablas()

        T1 = self.tablas["TABLA_1_RECEPCION"]
        T2 = self.tablas["TABLA_2_MANIOBRA"]
        T3 = self.tablas["TABLA_3_PERMANENCIA"]
        T4 = self.tablas["TABLA_4_SOLICITUD"]
        T5 = self.tablas["TABLA_5_DEVOLUCION"]
        T6 = self.tablas["TABLA_6_LLEGADAS"].reset_index(drop=True)
        T7 = self.tablas["TABLA_7_MANTENIMIENTO"]

        alea_mant           = generar_na()
        cajones_mant        = consultar_tabla(alea_mant, T7)
        cajones_disponibles = self.capacidad_total - cajones_mant
        cajones_ocupados    = 0
        relojes_choferes    = [0] * self.num_choferes

        tiempo_turno_actual = 0
        ingresos_totales    = 0.0
        costos_totales      = 0.0
        penalizaciones      = 0.0
        total_espera_cola   = 0.0

        for num_vh in range(1, num_vehiculos + 1):
            # ── Sortear turno con T6 ──────────────────────────────────
            na_t6  = generar_na()
            turno, horario = consultar_turno_t6(na_t6, T6)

            registro = {
                "vehiculo": num_vh,
                "na_t6":    round(na_t6, 10),
                "turno":    turno,
                "horario":  horario,
            }

            if cajones_ocupados >= cajones_disponibles:
                registro.update({
                    "atendido": False, "cajon_dispon": "No",
                    "chofer_asig": "---", "t_espera": 0,
                    "ganancia": -PENALIZACION_NEGADO,
                })
                penalizaciones += PENALIZACION_NEGADO
                costos_totales += PENALIZACION_NEGADO
                self.registros.append(registro)
                continue

            idx_libre         = relojes_choferes.index(min(relojes_choferes))
            t_libre           = relojes_choferes[idx_libre]
            t_espera_cola     = max(0, t_libre - tiempo_turno_actual)
            total_espera_cola += t_espera_cola

            registro.update({
                "atendido": True, "cajon_dispon": "Sí",
                "chofer_asig": idx_libre + 1, "t_espera": t_espera_cola,
            })

            na_rec = generar_na(); t_rec = consultar_tabla(na_rec, T1)
            na_man = generar_na(); t_man = consultar_tabla(na_man, T2)
            na_per = generar_na(); t_per = consultar_tabla(na_per, T3)
            na_sol = generar_na(); t_sol = consultar_tabla(na_sol, T4)
            na_dev = generar_na(); t_dev = consultar_tabla(na_dev, T5)

            registro.update({
                "na_recepcion":   round(na_rec, 10), "t_recepcion":   t_rec,
                "na_maniobra":    round(na_man, 10), "t_maniobra":    t_man,
                "na_permanencia": round(na_per, 10), "t_permanencia": t_per,
                "na_solicitud":   round(na_sol, 10), "t_solicitud":   t_sol,
                "na_devolucion":  round(na_dev, 10), "t_devolucion":  t_dev,
            })

            cajones_ocupados += 1
            t_chofer  = t_rec + t_man + t_sol + t_dev
            ingreso   = TARIFA_VALET
            costo     = round(t_chofer * COSTO_CHOFER_POR_MIN, 2)
            ganancia  = round(ingreso - costo, 2)

            ingresos_totales += ingreso
            costos_totales   += costo

            registro.update({
                "t_chofer": t_chofer, "ingreso": ingreso,
                "costo": costo,       "ganancia": ganancia,
            })

            t_inicio = max(tiempo_turno_actual, t_libre)
            relojes_choferes[idx_libre] = t_inicio + t_chofer
            tiempo_turno_actual = t_inicio
            self.registros.append(registro)

        self.ingresos_totales    = round(ingresos_totales, 2)
        self.costos_totales      = round(costos_totales, 2)
        self.penalizaciones      = round(penalizaciones, 2)
        self.ganancias_netas     = round(ingresos_totales - costos_totales, 2)
        self.total_espera_cola   = round(total_espera_cola, 2)
        self.relojes_choferes    = relojes_choferes
        self.cajones_disponibles = cajones_disponibles

        return self.costos_totales, self.ganancias_netas


# =============================================================================
#   SECCIÓN 5 — PALETA DE COLORES
# =============================================================================

COLOR_BG_DARK      = "#5D4037"
COLOR_BG_CARD      = "#4E342E"
COLOR_BG_INPUT     = "#3E2723"
COLOR_ACCENT_BLUE  = "#FFFFFF"
COLOR_ACCENT_TEAL  = "#D7CCC8"
COLOR_ACCENT_AMBER = "#8C8680"
COLOR_ACCENT_RED   = "#FFCCBC"
COLOR_TEXT_PRIMARY = "#FFFFFF"
COLOR_TEXT_MUTED   = "#8C8680"
COLOR_BORDER       = "#6D4C41"
COLOR_OK_GREEN     = "#A5D6A7"
COLOR_WARN_RED     = "#FFAB91"

TABS_TABLAS = [
    ("T1", "TABLA_1_RECEPCION",     "T1 – Recepción (min)"),
    ("T2", "TABLA_2_MANIOBRA",      "T2 – Maniobra (min)"),
    ("T3", "TABLA_3_PERMANENCIA",   "T3 – Permanencia (h)"),
    ("T4", "TABLA_4_SOLICITUD",     "T4 – Solicitud (min)"),
    ("T5", "TABLA_5_DEVOLUCION",    "T5 – Devolución (min)"),
    ("T6", "TABLA_6_LLEGADAS",      "T6 – Llegadas"),
    ("T7", "TABLA_7_MANTENIMIENTO", "T7 – Mantenimiento"),
]

COL_PRIMARIA = {
    "TABLA_1_RECEPCION":     "tiempo",
    "TABLA_2_MANIOBRA":      "tiempo",
    "TABLA_3_PERMANENCIA":   "tiempo",
    "TABLA_4_SOLICITUD":     "tiempo",
    "TABLA_5_DEVOLUCION":    "tiempo",
    "TABLA_6_LLEGADAS":      "turno",
    "TABLA_7_MANTENIMIENTO": "tiempo",
}


# =============================================================================
#   SECCIÓN 6 — WIDGET TablaVisor
# =============================================================================

class TablaVisor(ctk.CTkFrame):

    def __init__(self, parent, **kwargs):
        super().__init__(parent, fg_color="transparent", **kwargs)
        self._tablas_data  = None
        self._tab_activa   = "T1"
        self._botones_tab  = {}
        self._edit_mode    = False
        self._filas_edit   = []
        self._construir()

    def _construir(self):
        frame_tabs = ctk.CTkFrame(self, fg_color=COLOR_BG_INPUT, corner_radius=8)
        frame_tabs.pack(fill="x", pady=(0, 6))

        for i, (label, _key, _titulo) in enumerate(TABS_TABLAS):
            btn = ctk.CTkButton(
                frame_tabs, text=label, width=36, height=26,
                font=ctk.CTkFont(size=10, weight="bold"),
                corner_radius=6, fg_color=COLOR_BG_INPUT,
                hover_color=COLOR_BORDER, text_color=COLOR_TEXT_MUTED,
                border_width=0,
                command=lambda l=label: self._seleccionar_tab(l),
            )
            btn.grid(row=0, column=i, padx=2, pady=3, sticky="ew")
            frame_tabs.columnconfigure(i, weight=1)
            self._botones_tab[label] = btn

        self._frame_body = ctk.CTkFrame(
            self, fg_color=COLOR_BG_INPUT,
            corner_radius=8, border_width=1, border_color=COLOR_BORDER,
        )
        self._frame_body.pack(fill="both", expand=True)

        frame_enc = ctk.CTkFrame(self._frame_body, fg_color="transparent")
        frame_enc.pack(fill="x", padx=10, pady=(8, 2))

        self.lbl_titulo = ctk.CTkLabel(
            frame_enc, text="",
            font=ctk.CTkFont(size=11, weight="bold"),
            text_color=COLOR_ACCENT_BLUE,
        )
        self.lbl_titulo.pack(side="left")

        self.lbl_suma = ctk.CTkLabel(
            frame_enc, text="",
            font=ctk.CTkFont(size=10),
            text_color=COLOR_ACCENT_AMBER,
        )
        self.lbl_suma.pack(side="left", padx=(8, 0))

        self._frame_btns = ctk.CTkFrame(frame_enc, fg_color="transparent")
        self._frame_btns.pack(side="right")

        self.btn_editar = ctk.CTkButton(
            self._frame_btns, text="✏  Editar", width=80, height=24,
            font=ctk.CTkFont(size=10, weight="bold"),
            fg_color=COLOR_BG_DARK, hover_color=COLOR_BORDER,
            text_color=COLOR_TEXT_PRIMARY, corner_radius=6,
            command=self._activar_edicion,
        )
        self.btn_editar.pack(side="left", padx=2)

        self.btn_add = ctk.CTkButton(
            self._frame_btns, text="+ Fila", width=68, height=24,
            font=ctk.CTkFont(size=10, weight="bold"),
            fg_color="#1B5E20", hover_color="#2E7D32",
            text_color=COLOR_OK_GREEN, corner_radius=6,
            command=self._agregar_fila,
        )

        self.btn_guardar = ctk.CTkButton(
            self._frame_btns, text="✔  Guardar", width=86, height=24,
            font=ctk.CTkFont(size=10, weight="bold"),
            fg_color="#0D47A1", hover_color="#1565C0",
            text_color="#90CAF9", corner_radius=6,
            command=self._guardar_edicion,
        )

        self.btn_cancelar = ctk.CTkButton(
            self._frame_btns, text="✕  Cancelar", width=88, height=24,
            font=ctk.CTkFont(size=10, weight="bold"),
            fg_color=COLOR_BG_INPUT, hover_color=COLOR_BORDER,
            text_color=COLOR_TEXT_MUTED, corner_radius=6,
            command=self._cancelar_edicion,
        )

        self._contenedor = ctk.CTkFrame(self._frame_body, fg_color="transparent")
        self._contenedor.pack(fill="both", expand=True, padx=8, pady=(0, 8))

        self._text_vista = ctk.CTkTextbox(
            self._contenedor,
            fg_color="transparent", text_color=COLOR_TEXT_PRIMARY,
            font=ctk.CTkFont(family="Courier", size=14),
            wrap="none", activate_scrollbars=True,
        )
        self._text_vista.pack(fill="both", expand=True)
        self._text_vista.insert("end", "Ejecuta la simulación\npara ver las tablas.")
        self._text_vista.configure(state="disabled")

        self._scroll_edit = ctk.CTkScrollableFrame(
            self._contenedor, fg_color="transparent",
            scrollbar_button_color=COLOR_BORDER,
        )

        self._resaltar_tab("T1")

    def actualizar_tablas(self, tablas_dict: dict):
        self._tablas_data = tablas_dict
        if self._edit_mode:
            self._cancelar_edicion()
        else:
            self._renderizar_tab(self._tab_activa)

    def _seleccionar_tab(self, label):
        if self._edit_mode:
            self._cancelar_edicion()
        self._tab_activa = label
        self._resaltar_tab(label)
        self._renderizar_tab(label)

    def _resaltar_tab(self, activa):
        for label, btn in self._botones_tab.items():
            if label == activa:
                btn.configure(fg_color=COLOR_BG_DARK, text_color=COLOR_TEXT_PRIMARY)
            else:
                btn.configure(fg_color=COLOR_BG_INPUT, text_color=COLOR_TEXT_MUTED)

    def _renderizar_tab(self, label):
        entrada = next((e for e in TABS_TABLAS if e[0] == label), None)
        if not entrada:
            return
        _l, key, titulo = entrada

        self.lbl_titulo.configure(text=titulo)
        self._text_vista.configure(state="normal")
        self._text_vista.delete("1.0", "end")

        if self._tablas_data is None:
            self._text_vista.insert("end", "Ejecuta la simulación\npara ver las tablas.")
            self.lbl_suma.configure(text="sin datos", text_color=COLOR_TEXT_MUTED)
        else:
            df   = self._tablas_data[key]
            suma = round(df["prob"].sum(), 4)
            self._text_vista.insert("end", df.to_string(index=False))
            color = COLOR_OK_GREEN if abs(suma - 1.0) < 0.0002 else COLOR_WARN_RED
            self.lbl_suma.configure(text=f"Σ prob = {suma}  ✓", text_color=color)

        self._text_vista.configure(state="disabled")

    def _activar_edicion(self):
        if self._tablas_data is None:
            return
        self._edit_mode = True
        self.btn_editar.pack_forget()
        self.btn_add.pack(side="left", padx=2)
        self.btn_guardar.pack(side="left", padx=2)
        self.btn_cancelar.pack(side="left", padx=2)
        self._text_vista.pack_forget()
        self._scroll_edit.pack(fill="both", expand=True)
        self._construir_grid_edicion()

    def _construir_grid_edicion(self):
        for w in self._scroll_edit.winfo_children():
            w.destroy()
        self._filas_edit = []

        entrada = next((e for e in TABS_TABLAS if e[0] == self._tab_activa), None)
        if not entrada:
            return
        _l, key, _titulo = entrada
        df = self._tablas_data[key].copy().reset_index(drop=True)

        col_prim    = COL_PRIMARIA[key]
        es_llegadas = (key == "TABLA_6_LLEGADAS")

        headers    = [col_prim, "prob", "prob_acum", "rango_inf", "rango_sup", ""]
        if es_llegadas:
            headers = ["turno", "horario", "veh_hora", "prob", "prob_acum", "rango_inf", "rango_sup", ""]
        col_widths = self._col_widths(es_llegadas)

        sf = self._scroll_edit
        for c, (h, w) in enumerate(zip(headers, col_widths)):
            ctk.CTkLabel(
                sf, text=h,
                font=ctk.CTkFont(size=10, weight="bold"),
                text_color=COLOR_TEXT_MUTED,
                width=w, anchor="w",
            ).grid(row=0, column=c, padx=(4, 2), pady=(2, 4), sticky="w")

        ctk.CTkFrame(sf, fg_color=COLOR_BORDER, height=1).grid(
            row=1, column=0, columnspan=len(headers), sticky="ew", padx=4)

        for i, row in df.iterrows():
            self._insertar_fila_grid(sf, i + 2, row, es_llegadas, col_prim, col_widths)

        self._df_edit_key  = key
        self._es_llegadas  = es_llegadas
        self._col_prim     = col_prim

    def _col_widths(self, es_llegadas):
        if es_llegadas:
            return [90, 70, 60, 70, 80, 80, 80, 30]
        return [60, 70, 80, 80, 80, 30]

    def _insertar_fila_grid(self, sf, row_idx, row_data, es_llegadas, col_prim, col_widths):
        fila = {"row": row_idx}

        def make_entry(col, value, width, read_only=False, callback=None):
            e = ctk.CTkEntry(
                sf,
                fg_color=COLOR_BG_DARK if read_only else COLOR_BG_INPUT,
                border_color=COLOR_BORDER,
                text_color=COLOR_TEXT_MUTED if read_only else COLOR_TEXT_PRIMARY,
                font=ctk.CTkFont(size=11),
                height=26, width=width, corner_radius=4,
            )
            e.insert(0, str(value))
            if read_only:
                e.configure(state="disabled")
            e.grid(row=row_idx, column=col, padx=(4, 2), pady=2, sticky="w")
            if callback:
                e.bind("<KeyRelease>", callback)
            return e

        if es_llegadas:
            fila["e_turno"]   = make_entry(0, row_data.get("turno", ""), col_widths[0])
            fila["e_horario"] = make_entry(1, row_data.get("horario", ""), col_widths[1])
            fila["e_veh"]     = make_entry(2, row_data.get("veh_hora", ""), col_widths[2])
            fila["e_prob"]    = make_entry(3, f"{row_data['prob']:.4f}", col_widths[3],
                                           callback=lambda e: self._on_prob_change())
            fila["e_acum"]    = make_entry(4, f"{row_data['prob_acum']:.4f}", col_widths[4], read_only=True)
            fila["e_ri"]      = make_entry(5, f"{row_data['rango_inf']:.4f}", col_widths[5], read_only=True)
            fila["e_rs"]      = make_entry(6, f"{row_data['rango_sup']:.4f}", col_widths[6], read_only=True)
            del_col = 7
        else:
            fila["e_prim"] = make_entry(0, row_data[col_prim], col_widths[0])
            fila["e_prob"] = make_entry(1, f"{row_data['prob']:.4f}", col_widths[1],
                                        callback=lambda e: self._on_prob_change())
            fila["e_acum"] = make_entry(2, f"{row_data['prob_acum']:.4f}", col_widths[2], read_only=True)
            fila["e_ri"]   = make_entry(3, f"{row_data['rango_inf']:.4f}", col_widths[3], read_only=True)
            fila["e_rs"]   = make_entry(4, f"{row_data['rango_sup']:.4f}", col_widths[4], read_only=True)
            del_col = 5

        btn_del = ctk.CTkButton(
            sf, text="✕", width=26, height=26,
            fg_color=COLOR_BG_INPUT, hover_color="#5D1010",
            text_color=COLOR_ACCENT_RED, corner_radius=4,
            font=ctk.CTkFont(size=11, weight="bold"),
            command=lambda fi=fila: self._eliminar_fila(fi),
        )
        btn_del.grid(row=row_idx, column=del_col, padx=(4, 2), pady=2)
        fila["btn_del"] = btn_del
        self._filas_edit.append(fila)

    def _agregar_fila(self):
        if not self._edit_mode:
            return
        sf       = self._scroll_edit
        col_w    = self._col_widths(self._es_llegadas)
        row_idx  = max((f["row"] for f in self._filas_edit), default=1) + 1

        if not self._es_llegadas:
            try:
                ultimo_val = int(self._filas_edit[-1]["e_prim"].get())
                nuevo_val  = ultimo_val + 1
            except (ValueError, IndexError):
                nuevo_val = 1
        else:
            nuevo_val = "Nuevo"

        dummy = {
            self._col_prim: nuevo_val,
            "prob": 0.0, "prob_acum": 0.0, "rango_inf": 0.0, "rango_sup": 0.0,
            "horario": "HH-HHh", "veh_hora": "0-0",
        }
        self._insertar_fila_grid(sf, row_idx, dummy, self._es_llegadas, self._col_prim, col_w)
        self._on_prob_change()

    def _eliminar_fila(self, fila):
        if len(self._filas_edit) <= 2:
            return
        for key, widget in fila.items():
            if key == "row":
                continue
            try:
                widget.destroy()
            except Exception:
                pass
        self._filas_edit.remove(fila)
        self._on_prob_change()

    def _on_prob_change(self):
        probabilidades = []
        for f in self._filas_edit:
            try:
                p = round(float(f["e_prob"].get()), 4)
            except ValueError:
                p = 0.0
            probabilidades.append(p)

        suma  = round(sum(probabilidades), 4)
        color = COLOR_OK_GREEN if abs(suma - 1.0) < 0.0002 else COLOR_WARN_RED
        self.lbl_suma.configure(
            text=f"Σ prob = {suma:.4f}{'  ✓' if abs(suma-1.0)<0.0002 else '  ✗'}",
            text_color=color,
        )

        acum = 0.0
        for i, (f, p) in enumerate(zip(self._filas_edit, probabilidades)):
            acum = round(acum + p, 4)
            pa   = 1.0 if i == len(probabilidades) - 1 else acum
            ri   = 0.0 if i == 0 else round(sum(probabilidades[:i]), 4) + 0.0001
            rs   = pa
            for key, val in [("e_acum", pa), ("e_ri", ri), ("e_rs", rs)]:
                w = f.get(key)
                if w:
                    w.configure(state="normal")
                    w.delete(0, "end")
                    w.insert(0, f"{val:.4f}")
                    w.configure(state="disabled")

    def _guardar_edicion(self):
        probabilidades = []
        for f in self._filas_edit:
            try:
                p = round(float(f["e_prob"].get()), 4)
            except ValueError:
                p = 0.0
            probabilidades.append(p)

        suma = round(sum(probabilidades), 4)
        if abs(suma - 1.0) > 0.0002:
            self._mostrar_alerta(
                f"La suma de probabilidades es {suma:.4f}.\n"
                "Debe ser exactamente 1.0000 para poder guardar."
            )
            return

        key         = self._df_edit_key
        col_prim    = self._col_prim
        es_llegadas = self._es_llegadas

        filas_data = []
        for f, p in zip(self._filas_edit, probabilidades):
            if es_llegadas:
                row = {
                    "turno":    f["e_turno"].get(),
                    "horario":  f["e_horario"].get(),
                    "veh_hora": f["e_veh"].get(),
                    "prob":     p,
                }
            else:
                try:
                    val = int(f["e_prim"].get())
                except ValueError:
                    val = f["e_prim"].get()
                row = {col_prim: val, "prob": p}
            filas_data.append(row)

        df_nuevo = pd.DataFrame(filas_data)
        df_nuevo = recalcular_rangos(df_nuevo)
        self._tablas_data[key] = df_nuevo

        self._finalizar_edicion()
        self._renderizar_tab(self._tab_activa)

    def _cancelar_edicion(self):
        self._finalizar_edicion()
        self._renderizar_tab(self._tab_activa)

    def _finalizar_edicion(self):
        self._edit_mode  = False
        self._filas_edit = []
        self.btn_add.pack_forget()
        self.btn_guardar.pack_forget()
        self.btn_cancelar.pack_forget()
        self.btn_editar.pack(side="left", padx=2)
        self._scroll_edit.pack_forget()
        self._text_vista.pack(fill="both", expand=True)
        for w in self._scroll_edit.winfo_children():
            w.destroy()

    def _mostrar_alerta(self, mensaje):
        v = ctk.CTkToplevel(self)
        v.title("Atención")
        v.geometry("360x160")
        v.configure(fg_color=COLOR_BG_DARK)
        v.grab_set()
        ctk.CTkLabel(v, text="⚠  Validación",
                     font=ctk.CTkFont(size=13, weight="bold"),
                     text_color=COLOR_ACCENT_RED).pack(pady=(18, 6))
        ctk.CTkLabel(v, text=mensaje,
                     font=ctk.CTkFont(size=12),
                     text_color=COLOR_TEXT_PRIMARY,
                     wraplength=320).pack(padx=16)
        ctk.CTkButton(v, text="Entendido",
                      fg_color=COLOR_BG_INPUT, hover_color=COLOR_BORDER,
                      command=v.destroy).pack(pady=14)



class Interfaz_EVP(ctk.CTk):

    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        self.title("Simulación Monte Carlo — Valet Parking")
        self.geometry("1280x820")
        self.minsize(1050, 680)
        self.configure(fg_color=COLOR_BG_DARK)
        self.hotel = None
        self._construir_ui()
        self.after(300, self._iniciar_simulacion)

    def _construir_ui(self):
        frame_header = ctk.CTkFrame(self, fg_color=COLOR_BG_CARD, corner_radius=0, height=52)
        frame_header.pack(fill="x", side="top")
        frame_header.pack_propagate(False)
        ctk.CTkLabel(
            frame_header,
            text="  ESTACIONAMIENTO Y VALET PARKING",
            font=ctk.CTkFont(size=17, weight="bold"),
            text_color=COLOR_TEXT_PRIMARY,
        ).pack(side="right", padx=20, pady=14)

        frame_body = ctk.CTkFrame(self, fg_color="transparent")
        frame_body.pack(fill="both", expand=True, padx=14, pady=10)
        frame_body.columnconfigure(0, weight=0, minsize=280)
        frame_body.columnconfigure(1, weight=1)
        frame_body.rowconfigure(0, weight=1)

        panel_izq = ctk.CTkFrame(
            frame_body, fg_color=COLOR_BG_CARD,
            corner_radius=12, border_width=1, border_color=COLOR_BORDER,
        )
        panel_izq.grid(row=0, column=0, sticky="nsew", padx=(0, 10))
        self._construir_panel_izq(panel_izq)

        panel_der = ctk.CTkFrame(
            frame_body, fg_color=COLOR_BG_CARD,
            corner_radius=12, border_width=1, border_color=COLOR_BORDER,
        )
        panel_der.grid(row=0, column=1, sticky="nsew")
        self._construir_panel_der(panel_der)

    def _construir_panel_izq(self, parent):
        frame_top = ctk.CTkFrame(parent, fg_color="transparent")
        frame_top.pack(fill="x", padx=16, pady=(16, 0))

        ctk.CTkLabel(
            frame_top, text="Parámetros",
            font=ctk.CTkFont(size=13, weight="bold"),
            text_color=COLOR_ACCENT_BLUE,
        ).pack(anchor="w", pady=(0, 8))

        frame_entradas = ctk.CTkFrame(frame_top, fg_color="transparent")
        frame_entradas.pack(fill="x")
        frame_entradas.columnconfigure(0, weight=1)
        frame_entradas.columnconfigure(1, weight=1)

        ctk.CTkLabel(frame_entradas, text="Choferes",
                     font=ctk.CTkFont(size=11), text_color=COLOR_TEXT_MUTED,
                     ).grid(row=0, column=0, sticky="w", padx=(0, 6), pady=(0, 2))
        ctk.CTkLabel(frame_entradas, text="Vehículos",
                     font=ctk.CTkFont(size=11), text_color=COLOR_TEXT_MUTED,
                     ).grid(row=0, column=1, sticky="w", padx=(6, 0), pady=(0, 2))

        self.entry_choferes = ctk.CTkEntry(
            frame_entradas,
            fg_color=COLOR_BG_INPUT, border_color=COLOR_BORDER,
            text_color=COLOR_TEXT_PRIMARY,
            font=ctk.CTkFont(size=14, weight="bold"),
            height=34, corner_radius=8,
        )
        self.entry_choferes.insert(0, "3")
        self.entry_choferes.grid(row=1, column=0, sticky="ew", padx=(0, 6))

        self.entry_vehiculos = ctk.CTkEntry(
            frame_entradas,
            fg_color=COLOR_BG_INPUT, border_color=COLOR_BORDER,
            text_color=COLOR_TEXT_PRIMARY,
            font=ctk.CTkFont(size=14, weight="bold"),
            height=34, corner_radius=8,
        )
        self.entry_vehiculos.insert(0, "20")
        self.entry_vehiculos.grid(row=1, column=1, sticky="ew", padx=(6, 0))

        # Nota explicativa de T6
        ctk.CTkLabel(
            frame_top,
            text="ℹ  El turno de cada vehículo\nse sortea con T6 – Llegadas.",
            font=ctk.CTkFont(size=10),
            text_color=COLOR_TEXT_MUTED,
            justify="left",
        ).pack(anchor="w", pady=(6, 0))

        frame_tarifas = ctk.CTkFrame(parent, fg_color="transparent")
        frame_tarifas.pack(fill="x", padx=16, pady=(16, 0))
        ctk.CTkLabel(
            frame_tarifas, text="Tarifas",
            font=ctk.CTkFont(size=13, weight="bold"),
            text_color=COLOR_ACCENT_BLUE,
        ).pack(anchor="w", pady=(0, 6))
        self._fila_tarifa(frame_tarifas, "Tarifa valet",        f"${TARIFA_VALET} MXN",         COLOR_ACCENT_TEAL)
        self._fila_tarifa(frame_tarifas, "Costo chofer/min",    f"${COSTO_CHOFER_POR_MIN} MXN", COLOR_ACCENT_AMBER)
        self._fila_tarifa(frame_tarifas, "Penalización negado", f"${PENALIZACION_NEGADO} MXN",  COLOR_ACCENT_RED)

        ctk.CTkFrame(parent, fg_color="transparent").pack(fill="both", expand=True)
        ctk.CTkFrame(parent, fg_color=COLOR_BORDER, height=1).pack(fill="x", padx=16, pady=(0, 10))

        frame_btns = ctk.CTkFrame(parent, fg_color="transparent")
        frame_btns.pack(fill="x", padx=16, pady=(0, 16))

        self.btn_simular = ctk.CTkButton(
            frame_btns,
            text="▶  EMPEZAR SIMULACIÓN",
            font=ctk.CTkFont(size=13, weight="bold"),
            fg_color=COLOR_BG_INPUT, hover_color=COLOR_BG_DARK,
            text_color=COLOR_TEXT_PRIMARY, height=40, corner_radius=8,
            command=self._iniciar_simulacion,
        )
        self.btn_simular.pack(fill="x")

    def _construir_panel_der(self, parent):
        self.tabview = ctk.CTkTabview(
            parent,
            fg_color=COLOR_BG_CARD,
            segmented_button_fg_color=COLOR_BG_INPUT,
            segmented_button_selected_color=COLOR_BG_DARK,
            segmented_button_selected_hover_color=COLOR_BORDER,
            segmented_button_unselected_color=COLOR_BG_INPUT,
            segmented_button_unselected_hover_color=COLOR_BORDER,
            text_color=COLOR_TEXT_PRIMARY,
            border_width=0,
        )
        self.tabview.pack(fill="both", expand=True, padx=4, pady=4)

        self.tabview.add("Tablas")
        self.tabview.add("Tabla de simulación")
        self.tabview.add("Resumen")

        self._construir_tab_tablas(self.tabview.tab("Tablas"))
        self._construir_tab_tabla(self.tabview.tab("Tabla de simulación"))
        self._construir_tab_resumen(self.tabview.tab("Resumen"))

    def _construir_tab_tablas(self, parent):
        parent.configure(fg_color="transparent")
        self.tabla_visor = TablaVisor(parent)
        self.tabla_visor.pack(fill="both", expand=True, padx=12, pady=12)

    def _construir_tab_tabla(self, parent):
        parent.configure(fg_color="transparent")

        frame_toolbar = ctk.CTkFrame(parent, fg_color="transparent")
        frame_toolbar.pack(fill="x", padx=12, pady=(8, 4))
        ctk.CTkLabel(
            frame_toolbar, text="Registros por vehículo",
            font=ctk.CTkFont(size=13, weight="bold"), text_color=COLOR_TEXT_MUTED,
        ).pack(side="left")
        self.lbl_conteo_filas = ctk.CTkLabel(
            frame_toolbar, text="",
            font=ctk.CTkFont(size=12), text_color=COLOR_ACCENT_TEAL,
        )
        self.lbl_conteo_filas.pack(side="right")

        frame_outer = ctk.CTkFrame(parent, fg_color=COLOR_BG_INPUT, corner_radius=10)
        frame_outer.pack(fill="both", expand=True, padx=12, pady=(0, 12))
        self.text_tabla = ctk.CTkTextbox(
            frame_outer, fg_color="transparent", text_color=COLOR_TEXT_PRIMARY,
            font=ctk.CTkFont(family="Courier", size=14),
            wrap="none", activate_scrollbars=True,
        )
        self.text_tabla.pack(fill="both", expand=True, padx=8, pady=8)
        self.text_tabla.insert("end", "Ejecuta la simulación para ver la tabla.")
        self.text_tabla.configure(state="disabled")

    def _construir_tab_resumen(self, parent):
        parent.configure(fg_color="transparent")
        frame = ctk.CTkFrame(parent, fg_color=COLOR_BG_INPUT, corner_radius=10)
        frame.pack(fill="both", expand=True, padx=12, pady=12)
        ctk.CTkLabel(
            frame, text="Resultados del turno",
            font=ctk.CTkFont(size=13, weight="bold"),
            text_color=COLOR_TEXT_MUTED,
        ).pack(anchor="w", padx=14, pady=(12, 4))
        self.text_resumen = ctk.CTkTextbox(
            frame, fg_color="transparent", text_color=COLOR_TEXT_PRIMARY,
            font=ctk.CTkFont(family="Courier", size=13),
            wrap="none", activate_scrollbars=True,
        )
        self.text_resumen.pack(fill="both", expand=True, padx=12, pady=(0, 12))
        self.text_resumen.insert("end", "Ejecuta la simulación para ver los resultados.")
        self.text_resumen.configure(state="disabled")

    def _fila_tarifa(self, parent, etiqueta, valor, color):
        f = ctk.CTkFrame(parent, fg_color="transparent")
        f.pack(fill="x", pady=1)
        ctk.CTkLabel(f, text=etiqueta, font=ctk.CTkFont(size=11),
                     text_color=COLOR_TEXT_MUTED).pack(side="left")
        ctk.CTkLabel(f, text=valor, font=ctk.CTkFont(size=11, weight="bold"),
                     text_color=color).pack(side="right")

    # ------------------------------------------------------------------
    # Simulación
    # ------------------------------------------------------------------
    def _iniciar_simulacion(self):
        try:
            nc = int(self.entry_choferes.get())
            nv = int(self.entry_vehiculos.get())
        except ValueError:
            self._mostrar_error("Ingresa números enteros válidos.")
            return
        if nc < 1 or nv < 1:
            self._mostrar_error("Los valores deben ser mayores a 0.")
            return

        self.btn_simular.configure(state="disabled", text="⏳  Simulando...")
        threading.Thread(
            target=self._ejecutar_simulacion, args=(nc, nv), daemon=True
        ).start()

    def _ejecutar_simulacion(self, nc, nv):
        try:
            _aleatorios.reiniciar()
            hotel = Estacionamiento_Valet_Parking(num_choferes=nc)
            if self.tabla_visor._tablas_data is not None:
                hotel.tablas = {k: v.copy() for k, v in self.tabla_visor._tablas_data.items()}
            else:
                hotel.tablas = generar_todas_las_tablas()
            costo, ganancia = hotel.metodo_estacionamiento(num_vehiculos=nv)
            self.hotel = hotel
        except Exception as e:
            self.after(0, lambda: self._mostrar_error(str(e)))
            self.after(0, lambda: self.btn_simular.configure(
                state="normal", text="▶  EMPEZAR SIMULACIÓN"))
            return
        self.after(0, lambda: self._actualizar_ui(hotel, costo, ganancia))

    def _actualizar_ui(self, hotel, costo, ganancia):
        self.tabla_visor.actualizar_tablas(hotel.tablas)

        registros = hotel.registros
        atendidos = sum(1 for r in registros if r["atendido"])
        negados   = sum(1 for r in registros if not r["atendido"])

        s = {"rec": 0, "man": 0, "per": 0, "cho": 0, "esp": 0}
        for r in registros:
            if r["atendido"]:
                s["rec"] += r["t_recepcion"];   s["man"] += r["t_maniobra"]
                s["per"] += r["t_permanencia"]; s["cho"] += r["t_chofer"]
                s["esp"] += r["t_espera"]

        n = atendidos if atendidos > 0 else 1
        p = {k: round(v / n, 2) for k, v in s.items()}

        W = 46
        lineas = [
            f"{'─' * W}", "  RESUMEN DEL TURNO", f"{'─' * W}",
            f"  {'Cajones disponibles':<30} {hotel.cajones_disponibles}",
            f"  {'Choferes en turno':<30} {hotel.num_choferes}",
            f"  {'Vehículos atendidos':<30} {atendidos}",
            f"  {'Vehículos negados':<30} {negados}",
            f"{'─' * W}",
            f"  {'Espera total cola (min)':<30} {hotel.total_espera_cola:.2f}",
            f"  {'Espera promedio (min)':<30} {p['esp']:.2f}",
            f"{'─' * W}",
            f"  {'Ingresos totales ($MXN)':<30} ${hotel.ingresos_totales:.2f}",
            f"  {'Costo total ($MXN)':<30} ${costo:.2f}",
            f"  {'Penalizaciones ($MXN)':<30} ${hotel.penalizaciones:.2f}",
            f"  {'Ganancias ($MXN)':<30} ${ganancia:.2f}",
            f"{'─' * W}",
            f"  {'Tiempo promedio Recepción (min)':<30} {p['rec']}",
            f"  {'Tiempo promedio Maniobra (min)':<30} {p['man']}",
            f"  {'Tiempo promedio Permanencia (h)':<30} {p['per']}",
            f"  {'Tiempo promedio Chofer activo':<30} {p['cho']}",
            f"{'─' * W}",
            "  Estado de choferes:",
        ]
        for i, t in enumerate(hotel.relojes_choferes):
            lineas.append(f"    Chofer {i+1}  : libre al min {t}")
        lineas.append(f"{'─' * W}")

        self.text_resumen.configure(state="normal")
        self.text_resumen.delete("1.0", "end")
        self.text_resumen.insert("end", "\n".join(lineas))
        self.text_resumen.configure(state="disabled")

        self._renderizar_tabla_vehiculos(registros, atendidos + negados)
        self.btn_simular.configure(state="normal", text="▶  EMPEZAR SIMULACIÓN")
        self.tabview.set("Tabla de simulación")

    def _renderizar_tabla_vehiculos(self, registros, total):
        self.lbl_conteo_filas.configure(text=f"{total} vehículos")

        COL_FIJAS = f"{'Veh':>4}  {'Turno':<12}  {'NA-T6':>8}  {'Cajón':>5}  {'Chofer':>6}  {'Espera':>6}"
        enc_var = (
            f"  {'NA-Recep':>8}  {'TRec':>4}"
            f"  {'NA-Maniob':>9}  {'TMan':>4}"
            f"  {'NA-Perm':>8}  {'TPer':>4}"
            f"  {'NA-Solic':>8}  {'TSol':>4}"
            f"  {'NA-Devol':>8}  {'TDev':>4}"
            f"  {'T.Chofer':>8}  {'Ingreso':>7}  {'Costo':>6}  {'Ganancia':>8}"
        )
        enc    = COL_FIJAS + enc_var
        lineas = [enc, "─" * len(enc)]

        for r in registros:
            turno_corto = r.get("turno", "")[:12]
            na_t6_str   = f"{r.get('na_t6', 0):.6f}"
            fijas = f"{r['vehiculo']:>4}  {turno_corto:<12}  {na_t6_str:>8}  {'Sí' if r['atendido'] else 'No':>5}  "
            if r["atendido"]:
                fijas += f"{r['chofer_asig']:>6}  {r['t_espera']:>6.0f}"
                var = (
                    f"  {r['na_recepcion']:>8.6f}  {r['t_recepcion']:>4}"
                    f"  {r['na_maniobra']:>9.6f}  {r['t_maniobra']:>4}"
                    f"  {r['na_permanencia']:>8.6f}  {r['t_permanencia']:>4}"
                    f"  {r['na_solicitud']:>8.6f}  {r['t_solicitud']:>4}"
                    f"  {r['na_devolucion']:>8.6f}  {r['t_devolucion']:>4}"
                    f"  {r['t_chofer']:>8}  ${r['ingreso']:>6}"
                    f"  ${r['costo']:>5.2f}  ${r['ganancia']:>8.2f}"
                )
                lineas.append(fijas + var)
            else:
                fijas += f"{'---':>6}  {'---':>6}"
                negado_txt = "  SERVICIO NEGADO — sin cajón disponible"
                lineas.append(
                    fijas + negado_txt.ljust(len(enc_var) - 2)
                    + f"  ${-PENALIZACION_NEGADO:>8.2f}"
                )

        self.text_tabla.configure(state="normal")
        self.text_tabla.delete("1.0", "end")
        self.text_tabla.insert("end", "\n".join(lineas))
        self.text_tabla.configure(state="disabled")

    def _mostrar_error(self, mensaje):
        v = ctk.CTkToplevel(self)
        v.title("Error"); v.geometry("360x150")
        v.configure(fg_color=COLOR_BG_DARK); v.grab_set()
        ctk.CTkLabel(v, text="⚠  Error",
                     font=ctk.CTkFont(size=14, weight="bold"),
                     text_color=COLOR_ACCENT_RED).pack(pady=(20, 6))
        ctk.CTkLabel(v, text=mensaje, font=ctk.CTkFont(size=13),
                     text_color=COLOR_TEXT_PRIMARY, wraplength=320).pack()
        ctk.CTkButton(v, text="Cerrar", fg_color=COLOR_BG_INPUT,
                      hover_color=COLOR_BORDER, command=v.destroy).pack(pady=16)


if __name__ == "__main__":
    app = Interfaz_EVP()
    app.mainloop()