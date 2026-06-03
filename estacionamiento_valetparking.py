import threading
import random
import pandas as pd
import customtkinter as ctk
from pathlib import Path



nums_no_usados= []
nums_usados= []

def _cargar_aleatorios():
    global nums_no_usados
    if nums_no_usados:
        return
    ruta = Path(__file__).resolve().parent / "GeneradorDeNumeroAleatorios" / "Aleatorios.txt"
    with open(ruta, "r") as f:
        for linea in f:
            nums_no_usados.append(float(linea.strip()))
    random.shuffle(nums_no_usados)

def reiniciar_aleatorios():
    global nums_no_usados, nums_usados
    _cargar_aleatorios()
    nums_no_usados = nums_no_usados + nums_usados
    nums_usados = []
    random.shuffle(nums_no_usados)

def generar_na() -> float:
    global nums_no_usados, nums_usados
    _cargar_aleatorios()
    if len(nums_no_usados) == 0:
        reiniciar_aleatorios()
    numero = nums_no_usados[0]
    nums_no_usados.remove(numero)
    nums_usados.append(numero)
    return numero


def generar_probabilidades_aleatorias(n):
    valores = []
    for _ in range(n):
        valores.append(random.random())
    suma = sum(valores)
    probabilidades = []
    for valor in valores:
        probabilidades.append(round(valor / suma, 4))
    diferencia = round(1.0 - sum(probabilidades), 4)
    probabilidades[-1] = round(probabilidades[-1] + diferencia, 4)
    return probabilidades


def construir_tabla_t1():
    tiempos = [1,2,3,4,5,6,7,8,9,10]
    n = len(tiempos)
    valores = []
    for _ in range(n):
        valores.append(random.random())
    suma = sum(valores)
    probabilidades = []
    for valor in valores:
        probabilidades.append(round(valor / suma, 4))
    diferencia = round(1.0 - sum(probabilidades), 4)
    probabilidades[-1] = round(probabilidades[-1] + diferencia, 4)
    prob_acum = []
    acum = 0.0
    for p in probabilidades:
        acum = round(acum + p, 4)
        prob_acum.append(acum)
    prob_acum[-1] = 1.0
    rango_inf = []
    for i in range(n):
        if i == 0:
            rango_inf.append(0.0)
        else:
            rango_inf.append(round(prob_acum[i-1] + 0.0001, 4))
    rango_sup = []
    for pa in prob_acum:
        rango_sup.append(pa)
    return {
        "tiempo": tiempos,
        "prob": probabilidades,
        "prob_acum": prob_acum,
        "rango_inf": rango_inf,
        "rango_sup": rango_sup,
    }

def construir_tabla_t2():
    tiempos =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    n = len(tiempos)
    valores = []
    for _ in range(n):
        valores.append(random.random())
    suma = sum(valores)
    probabilidades = []
    for valor in valores:
        probabilidades.append(round(valor / suma, 4))
    diferencia = round(1.0 - sum(probabilidades), 4)
    probabilidades[-1] = round(probabilidades[-1] + diferencia, 4)
    prob_acum = []
    acum = 0.0
    for p in probabilidades:
        acum = round(acum + p, 4)
        prob_acum.append(acum)
    prob_acum[-1] = 1.0
    rango_inf = []
    for i in range(n):
        if i == 0:
            rango_inf.append(0.0)
        else:
            rango_inf.append(round(prob_acum[i-1] + 0.0001, 4))
    rango_sup = []
    for pa in prob_acum:
        rango_sup.append(pa)
    return {
        "tiempo": tiempos,
        "prob": probabilidades,
        "prob_acum": prob_acum,
        "rango_inf": rango_inf,
        "rango_sup": rango_sup,
    }

def construir_tabla_t3():
    tiempos =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    n = len(tiempos)
    valores = []
    for _ in range(n):
        valores.append(random.random())
    suma = sum(valores)
    probabilidades = []
    for valor in valores:
        probabilidades.append(round(valor / suma, 4))
    diferencia = round(1.0 - sum(probabilidades), 4)
    probabilidades[-1] = round(probabilidades[-1] + diferencia, 4)
    prob_acum = []
    acum = 0.0
    for p in probabilidades:
        acum = round(acum + p, 4)
        prob_acum.append(acum)
    prob_acum[-1] = 1.0
    rango_inf = []
    for i in range(n):
        if i == 0:
            rango_inf.append(0.0)
        else:
            rango_inf.append(round(prob_acum[i-1] + 0.0001, 4))
    rango_sup = []
    for pa in prob_acum:
        rango_sup.append(pa)
    return {
        "tiempo": tiempos,
        "prob": probabilidades,
        "prob_acum": prob_acum,
        "rango_inf": rango_inf,
        "rango_sup": rango_sup,
    }

def construir_tabla_t4():
    tiempos =[2, 3, 4, 5]
    n = len(tiempos)
    valores = []
    for _ in range(n):
        valores.append(random.random())
    suma = sum(valores)
    probabilidades = []
    for valor in valores:
        probabilidades.append(round(valor / suma, 4))
    diferencia = round(1.0 - sum(probabilidades), 4)
    probabilidades[-1] = round(probabilidades[-1] + diferencia, 4)
    prob_acum = []
    acum = 0.0
    for p in probabilidades:
        acum = round(acum + p, 4)
        prob_acum.append(acum)
    prob_acum[-1] = 1.0
    rango_inf = []
    for i in range(n):
        if i == 0:
            rango_inf.append(0.0)
        else:
            rango_inf.append(round(prob_acum[i-1] + 0.0001, 4))
    rango_sup = []
    for pa in prob_acum:
        rango_sup.append(pa)
    return {
        "tiempo": tiempos,
        "prob": probabilidades,
        "prob_acum": prob_acum,
        "rango_inf": rango_inf,
        "rango_sup": rango_sup,
    }


def construir_tabla_t5():
    tiempos =[2, 3, 4, 5 ,6]
    n = len(tiempos)
    valores = []
    for _ in range(n):
        valores.append(random.random())
    suma = sum(valores)
    probabilidades = []
    for valor in valores:
        probabilidades.append(round(valor / suma, 4))
    diferencia = round(1.0 - sum(probabilidades), 4)
    probabilidades[-1] = round(probabilidades[-1] + diferencia, 4)
    prob_acum = []
    acum = 0.0
    for p in probabilidades:
        acum = round(acum + p, 4)
        prob_acum.append(acum)
    prob_acum[-1] = 1.0
    rango_inf = []
    for i in range(n):
        if i == 0:
            rango_inf.append(0.0)
        else:
            rango_inf.append(round(prob_acum[i-1] + 0.0001, 4))
    rango_sup = []
    for pa in prob_acum:
        rango_sup.append(pa)
    return {
        "tiempo": tiempos,
        "prob": probabilidades,
        "prob_acum": prob_acum,
        "rango_inf": rango_inf,
        "rango_sup": rango_sup,
    }


def construir_tabla_t6():
    turnos = ["Madrugada", "Mañana", "Medio día", "Tarde pico", "Noche", "Noche tardía"]
    horarios = ["00-06h", "06-10h", "10-14h", "14-18h", "18-22h", "22-00h"]
    veh_hora = ["1-2", "4-6", "6-9", "10-14", "8-11", "3-5"]
    n = len(turnos)
    probabilidades = generar_probabilidades_aleatorias(n)

    prob_acum = []
    acum = 0.0
    for p in probabilidades:
        acum = round(acum + p, 4)
        prob_acum.append(acum)
    prob_acum[-1] = 1.0

    rango_inf = []
    for i in range(n):
        if i == 0:
            rango_inf.append(0.0)
        else:
            rango_inf.append(round(prob_acum[i-1] + 0.0001, 4))

    rango_sup = []
    for pa in prob_acum:
        rango_sup.append(pa)

    return {
        "turno":     turnos,
        "horario":   horarios,
        "veh_hora":  veh_hora,
        "prob":      probabilidades,
        "prob_acum": prob_acum,
        "rango_inf": rango_inf,
        "rango_sup": prob_acum.copy(),
    }


def construir_tabla_t7():
    tiempos =[2, 3, 4, 5]
    n = len(tiempos)
    valores = []
    for _ in range(n):
        valores.append(random.random())
    suma = sum(valores)
    probabilidades = []
    for valor in valores:
        probabilidades.append(round(valor / suma, 4))
    diferencia = round(1.0 - sum(probabilidades), 4)
    probabilidades[-1] = round(probabilidades[-1] + diferencia, 4)
    prob_acum = []
    acum = 0.0
    for p in probabilidades:
        acum = round(acum + p, 4)
        prob_acum.append(acum)
    prob_acum[-1] = 1.0
    rango_inf = []
    for i in range(n):
        if i == 0:
            rango_inf.append(0.0)
        else:
            rango_inf.append(round(prob_acum[i-1] + 0.0001, 4))
    rango_sup = []
    for pa in prob_acum:
        rango_sup.append(pa)
    return {
        "tiempo": tiempos,
        "prob": probabilidades,
        "prob_acum": prob_acum,
        "rango_inf": rango_inf,
        "rango_sup": rango_sup,
    }


def construir_tabla_t8_daños():
    tipos  = ["Sin daño", "Rayón leve", "Abolladura", "Vidrio roto", "Daño mayor"]
    costos = [0, 500, 1500, 3000, 6000]
    probs  = [0.50, 0.25, 0.13, 0.08, 0.04]

    acum = 0.0
    prob_acum = []
    for p in probs:
        acum = round(acum + p, 4)
        prob_acum.append(acum)
    prob_acum[-1] = 1.0

    rango_inf = [0.0] + [round(pa + 0.0001, 4) for pa in prob_acum[:-1]]

    return {
        "tipo de daño": tipos,
        "costo de rep": costos,
        "prob":      probs,
        "prob_acum": prob_acum,
        "rango_inf": rango_inf,
        "rango_sup": prob_acum.copy(),
    }


def construir_tabla_t9_excede():
    estados = ["No", "Sí"]
    probs   = [0.65, 0.35]
    acum = 0.0
    prob_acum = []
    for p in probs:
        acum = round(acum + p, 4)
        prob_acum.append(acum)
    prob_acum[-1] = 1.0
    rango_inf = [0.0] + [round(pa + 0.0001, 4) for pa in prob_acum[:-1]]
    return {
        "excede":    estados,
        "prob":      probs,
        "prob_acum": prob_acum,
        "rango_inf": rango_inf,
        "rango_sup": prob_acum.copy(),
    }

def construir_tabla_t9h_horas():
    horas      = [1,   2,   3  ]
    costos_ext = [300, 600, 900]
    probs      = [0.50, 0.30, 0.20]
    acum = 0.0
    prob_acum = []
    for p in probs:
        acum = round(acum + p, 4)
        prob_acum.append(acum)
    prob_acum[-1] = 1.0
    rango_inf = [0.0] + [round(pa + 0.0001, 4) for pa in prob_acum[:-1]]
    return {
        "horas_extra": horas,
        "costo_extra": costos_ext,
        "prob":        probs,
        "prob_acum":   prob_acum,
        "rango_inf":   rango_inf,
        "rango_sup":   prob_acum.copy(),
    }


def construir_tabla_t10_falla():
    estados = ["Activo", "Falla"]
    probs   = [0.90, 0.10]
    acum = 0.0
    prob_acum = []
    for p in probs:
        acum = round(acum + p, 4)
        prob_acum.append(acum)
    prob_acum[-1] = 1.0
    rango_inf = [0.0] + [round(pa + 0.0001, 4) for pa in prob_acum[:-1]]
    return {
        "estado_chofer":    estados,
        "prob":      probs,
        "prob_acum": prob_acum,
        "rango_inf": rango_inf,
        "rango_sup": prob_acum.copy(),
    }


def construir_tabla_t11_cancela():
    estados = ["No", "Sí"]
    probs   = [0.75, 0.25]
    acum = 0.0
    prob_acum = []
    for p in probs:
        acum = round(acum + p, 4)
        prob_acum.append(acum)
    prob_acum[-1] = 1.0
    rango_inf = [0.0] + [round(pa + 0.0001, 4) for pa in prob_acum[:-1]]
    return {
        "cancela":   estados,
        "prob":      probs,
        "prob_acum": prob_acum,
        "rango_inf": rango_inf,
        "rango_sup": prob_acum.copy(),
    }


def construir_tabla_t12_sale_temprano():
    estados = ["No", "Sí"]
    probs   = [0.70, 0.30]
    acum = 0.0
    prob_acum = []
    for p in probs:
        acum = round(acum + p, 4)
        prob_acum.append(acum)
    prob_acum[-1] = 1.0
    rango_inf = [0.0] + [round(pa + 0.0001, 4) for pa in prob_acum[:-1]]
    return {
        "sale_temprano": estados,
        "prob":      probs,
        "prob_acum": prob_acum,
        "rango_inf": rango_inf,
        "rango_sup": prob_acum.copy(),
    }


def construir_tabla_t13_clima():
    climas          = ["Despejado",  "Nublado", "Lluvia leve", "Lluvia fuerte"]
    factores_daño   = [1.0,          1.2,       1.5,           2.0           ]
    factores_lleg   = [1.0,          0.9,       0.7,           0.5           ]
    probs           = [0.40,         0.30,      0.20,          0.10          ]
    acum = 0.0
    prob_acum = []
    for p in probs:
        acum = round(acum + p, 4)
        prob_acum.append(acum)
    prob_acum[-1] = 1.0
    rango_inf = [0.0] + [round(pa + 0.0001, 4) for pa in prob_acum[:-1]]
    return {
        "clima":           climas,
        "factor_daño":     factores_daño,
        "factor_llegadas": factores_lleg,
        "prob":            probs,
        "prob_acum":       prob_acum,
        "rango_inf":       rango_inf,
        "rango_sup":       prob_acum.copy(),
    }


def generar_todas_las_tablas():
    return {
        "T1":  pd.DataFrame(construir_tabla_t1()),
        "T2":  pd.DataFrame(construir_tabla_t2()),
        "T3":  pd.DataFrame(construir_tabla_t3()),
        "T4":  pd.DataFrame(construir_tabla_t4()),
        "T5":  pd.DataFrame(construir_tabla_t5()),
        "T6":  pd.DataFrame(construir_tabla_t6()),
        "T7":  pd.DataFrame(construir_tabla_t7()),
        "T8":  pd.DataFrame(construir_tabla_t8_daños()),
        "T9":  pd.DataFrame(construir_tabla_t9_excede()),
        "T9H": pd.DataFrame(construir_tabla_t9h_horas()),
        "T10": pd.DataFrame(construir_tabla_t10_falla()),
        "T11": pd.DataFrame(construir_tabla_t11_cancela()),
        "T12": pd.DataFrame(construir_tabla_t12_sale_temprano()),
        "T13": pd.DataFrame(construir_tabla_t13_clima()),
    }


TARIFA_VALET = 80
COSTO_CHOFER_POR_MIN = 20
PENALIZACION_NEGADO  = 50


def consultar_tabla(na, tabla_df):
    col0 = tabla_df.columns[0]

    def _normalizar(val):
        try:
            i = int(val)
            f = float(val)
            if i == f:
                return i
            else:
                return f
        except (ValueError, TypeError):
            return val

    for i in range(len(tabla_df)):
        if tabla_df.loc[i, "rango_inf"] <= na <= tabla_df.loc[i, "rango_sup"]:
            return _normalizar(tabla_df.loc[i, col0])
    return _normalizar(tabla_df.loc[len(tabla_df) - 1, col0])


def recalcular_rangos(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    col0 = df.columns[0]

    def _a_int(v):
        try:
            return int(v)
        except (ValueError, TypeError):
            return v

    try:
        convertidos = [_a_int(v) for v in df[col0]]
        if all(isinstance(v, int) for v in convertidos):
            df[col0] = convertidos
    except Exception:
        pass

    acum = 0.0
    pa = []
    for p in df["prob"]:
        acum = round(acum + p, 4)
        pa.append(acum)
    pa[-1] = 1.0
    df["prob_acum"] = pa
    df["rango_inf"] = [0.0] + [round(x + 0.0001, 4) for x in pa[:-1]]
    df["rango_sup"] = pa
    return df


def consultar_turno_t6(na, t6_df):
    for i in range(len(t6_df)):
        if t6_df.loc[i, "rango_inf"] <= na <= t6_df.loc[i, "rango_sup"]:
            return t6_df.loc[i, "turno"], t6_df.loc[i, "horario"]
    return t6_df.loc[len(t6_df) - 1, "turno"], t6_df.loc[len(t6_df) - 1, "horario"]


def consultar_t8_daño(na, t8_df, factor_daño=1.0):
    na_ajustada = min(na * factor_daño, 1.0)
    for i in range(len(t8_df)):
        if t8_df.loc[i, "rango_inf"] <= na_ajustada <= t8_df.loc[i, "rango_sup"]:
            return t8_df.loc[i, "tipo de daño"], int(t8_df.loc[i, "costo de rep"])
    return t8_df.loc[len(t8_df) - 1, "tipo de daño"], int(t8_df.loc[len(t8_df) - 1, "costo de rep"])


def consultar_clima_t13(na, t13_df):
    for i in range(len(t13_df)):
        if t13_df.loc[i, "rango_inf"] <= na <= t13_df.loc[i, "rango_sup"]:
            return (
                t13_df.loc[i, "clima"],
                float(t13_df.loc[i, "factor_daño"]),
                float(t13_df.loc[i, "factor_llegadas"]),
            )
    last = len(t13_df) - 1
    return (
        t13_df.loc[last, "clima"],
        float(t13_df.loc[last, "factor_daño"]),
        float(t13_df.loc[last, "factor_llegadas"]),
    )


# =============================================================================
#   CLASE PRINCIPAL DE SIMULACIÓN
# =============================================================================

class Estacionamiento_Valet_Parking:

    CAPACIDAD_FIJA = 50

    def __init__(self, num_choferes=3):
        self.capacidad_total = self.CAPACIDAD_FIJA
        self.num_choferes    = num_choferes
        self.registros       = []
        self.tablas          = None

    def simular_dias(self, num_dias: int, num_vehiculos: int) -> list:
        historial = []
        for d in range(1, num_dias + 1):
            self.metodo_estacionamiento(num_vehiculos)
            historial.append(self._snapshot_dia(d))
        return historial

    def _snapshot_dia(self, numero_dia: int) -> dict:
        registros = self.registros
        atendidos = sum(
            1 for r in registros
            if r.get("atendido") and r.get("cajon_dispon") not in ("No", "Cancel")
        )
        negados = sum(
            1 for r in registros
            if not r.get("atendido") and r.get("cajon_dispon") == "No"
        )
        return {
            "dia":                  numero_dia,
            "clima":                self.clima_turno,
            "factor_daño":          self.factor_daño,
            "factor_llegadas":      self.factor_llegadas,
            "cajones_disponibles":  self.cajones_disponibles,
            "choferes_activos":     len(self.choferes_activos),
            "vehiculos_efectivos":  self.num_vehiculos_efectivos,
            "atendidos":            atendidos,
            "negados":              negados,
            "cancelaciones":        self.cancelaciones,
            "salidas_tempranas":    self.salidas_tempranas,
            "ingresos":             self.ingresos_totales,
            "costos":               self.costos_totales,
            "ganancias":            self.ganancias_netas,
            "penalizaciones":       self.penalizaciones,
            "costos_daños":         self.costos_daños_total,
            "costos_extra":         self.costos_extra_total,
            "espera_total":         self.total_espera_cola,
            "registros":            list(self.registros),
        }

    def metodo_estacionamiento(self, num_vehiculos=20):
        self.registros = []
        if self.tablas is None:
            self.tablas = generar_todas_las_tablas()

        T1  = self.tablas["T1"]
        T2  = self.tablas["T2"]
        T3  = self.tablas["T3"]
        T4  = self.tablas["T4"]
        T5  = self.tablas["T5"]
        T6  = self.tablas["T6"].reset_index(drop=True)
        T7  = self.tablas["T7"]
        T8  = self.tablas["T8"]
        T9  = self.tablas["T9"]
        T9H = self.tablas["T9H"]
        T10 = self.tablas["T10"]
        T11 = self.tablas["T11"]
        T12 = self.tablas["T12"]
        T13 = self.tablas["T13"]

        na_clima = generar_na()
        clima_turno, factor_daño, factor_llegadas = consultar_clima_t13(na_clima, T13)

        alea_mant = generar_na()
        cajones_mant  = int(float(consultar_tabla(alea_mant, T7)))
        cajones_disponibles = self.capacidad_total - cajones_mant
        cajones_ocupados = 0

        choferes_activos = []
        na_fallas_choferes = []
        estados_choferes   = []
        for c in range(self.num_choferes):
            na_f   = generar_na()
            estado = consultar_tabla(na_f, T10)
            na_fallas_choferes.append(round(na_f, 10))
            estados_choferes.append(estado)
            if estado == "Activo":
                choferes_activos.append(c)

        if not choferes_activos:
            estados_choferes[0] = "Activo"
            choferes_activos    = [0]

        relojes_choferes = {idx: 0 for idx in choferes_activos}

        num_vehiculos_efectivos = max(1, round(num_vehiculos * factor_llegadas))

        tiempo_turno_actual = 0
        ingresos_totales  = 0.0
        costos_totales    = 0.0
        penalizaciones  = 0.0
        total_espera_cola = 0.0
        costos_daños_total = 0.0
        costos_extra_total = 0.0
        cancelaciones = 0
        salidas_tempranas = 0
        conteo_daños = {}

        for num_vh in range(1, num_vehiculos_efectivos + 1):

            na_t6 = generar_na()
            turno, horario = consultar_turno_t6(na_t6, T6)

            registro = {
                "vehiculo":  num_vh,
                "na_t6":     round(na_t6, 10),
                "turno":     turno,
                "horario":   horario,
                "clima":        clima_turno,
                "na_clima":     round(na_clima, 10),
                "fact_daño":    factor_daño,
                "fact_lleg":    factor_llegadas,
            }

            if cajones_ocupados >= cajones_disponibles:
                registro.update({
                    "atendido":     False,
                    "cajon_dispon": "No",
                    "chofer_asig":  "---",
                    "t_espera":     0,
                    "ganancia":     -PENALIZACION_NEGADO,
                    "na_t10_chofer": "---", "estado_chofer": "---",
                    "na_t11": "---",        "cancela":        "---",
                    "na_t9":  "---",        "excede":         "---",
                    "na_t9h": "---",        "horas_extra":    0,    "costo_extra": 0,
                    "na_t12": "---",        "sale_temprano":  "---",
                })
                penalizaciones += PENALIZACION_NEGADO
                costos_totales += PENALIZACION_NEGADO
                self.registros.append(registro)
                continue

            idx_libre = min(relojes_choferes, key=relojes_choferes.get)
            t_libre   = relojes_choferes[idx_libre]

            estado_chofer_asig = estados_choferes[idx_libre]
            na_t10_chofer_asig = na_fallas_choferes[idx_libre]

            t_espera_cola = max(0, t_libre - tiempo_turno_actual)
            total_espera_cola += t_espera_cola

            registro.update({
                "atendido":      True,
                "cajon_dispon":  "Sí",
                "chofer_asig":   idx_libre + 1,
                "t_espera":      t_espera_cola,
                "na_t10_chofer":  round(na_t10_chofer_asig, 10),
                "estado_chofer":  estado_chofer_asig,
            })

            if t_espera_cola > 0:
                na_t11   = generar_na()
                cancela  = consultar_tabla(na_t11, T11)
            else:
                na_t11  = 0.0
                cancela = "No"

            registro.update({
                "na_t11": round(na_t11, 10),
                "cancela": cancela,
            })

            if cancela == "Sí":
                cancelaciones += 1
                registro.update({
                    "atendido":      False,
                    "cajon_dispon":  "Cancel",
                    "ganancia":      0,
                    "na_recepcion": 0, "t_recepcion": 0,
                    "na_maniobra":  0, "t_maniobra":  0,
                    "na_permanencia": 0, "t_permanencia": 0,
                    "na_solicitud": 0, "t_solicitud": 0,
                    "na_devolucion": 0, "t_devolucion": 0,
                    "t_chofer": 0, "ingreso": 0, "costo": 0,
                    "na_daño": 0, "tipo_daño": "---", "costo_daño": 0,
                    "na_t9":  0, "excede": "---",
                    "na_t9h": 0, "horas_extra": 0, "costo_extra": 0,
                    "na_t12":  0, "sale_temprano": "---",
                })
                self.registros.append(registro)
                continue

            na_rec = generar_na(); t_rec = int(float(consultar_tabla(na_rec, T1)))
            na_man = generar_na(); t_man = int(float(consultar_tabla(na_man, T2)))
            na_per = generar_na(); t_per = int(float(consultar_tabla(na_per, T3)))
            na_sol = generar_na(); t_sol = int(float(consultar_tabla(na_sol, T4)))
            na_dev = generar_na(); t_dev = int(float(consultar_tabla(na_dev, T5)))

            registro.update({
                "na_recepcion":    round(na_rec, 10), "t_recepcion":    t_rec,
                "na_maniobra":     round(na_man, 10), "t_maniobra":     t_man,
                "na_permanencia":  round(na_per, 10), "t_permanencia":  t_per,
                "na_solicitud":    round(na_sol, 10), "t_solicitud":    t_sol,
                "na_devolucion":   round(na_dev, 10), "t_devolucion":   t_dev,
            })

            cajones_ocupados += 1
            t_chofer = t_rec + t_man + t_sol + t_dev
            ingreso  = TARIFA_VALET
            costo    = round(t_chofer * COSTO_CHOFER_POR_MIN, 2)

            na_daño = generar_na()
            tipo_daño, c_daño = consultar_t8_daño(na_daño, T8, factor_daño)
            costo = round(costo + c_daño, 2)
            costos_daños_total += c_daño
            conteo_daños[tipo_daño] = conteo_daños.get(tipo_daño, 0) + 1
            registro.update({
                "na_daño":   round(na_daño, 10),
                "tipo_daño": tipo_daño,
                "costo_daño": c_daño,
            })

            na_t9  = generar_na()
            excede = consultar_tabla(na_t9, T9)

            if excede == "Sí":
                na_t9h   = generar_na()
                horas_extra = int(float(consultar_tabla(na_t9h, T9H)))
                costo_extra  = 0
                for i in range(len(T9H)):
                    if int(T9H.loc[i, "horas_extra"]) == horas_extra:
                        costo_extra = int(T9H.loc[i, "costo_extra"])
                        break
                ingreso = round(ingreso + costo_extra, 2)
                costos_extra_total += costo_extra
            else:
                na_t9h = 0.0
                horas_extra = 0
                costo_extra = 0

            registro.update({
                "na_t9":     round(na_t9, 10),
                "excede":    excede,
                "na_t9h":    round(na_t9h, 10),
                "horas_extra": horas_extra,
                "costo_extra": costo_extra,
            })

            na_t12  = generar_na()
            sale_temprano  = consultar_tabla(na_t12, T12)

            if sale_temprano == "Sí":
                salidas_tempranas  += 1
                cajones_ocupados = max(0, cajones_ocupados - 1)

            registro.update({
                "na_t12":        round(na_t12, 10),
                "sale_temprano": sale_temprano,
            })

            ganancia = round(ingreso - costo, 2)
            ingresos_totales += ingreso
            costos_totales   += costo

            registro.update({
                "t_chofer": t_chofer,
                "ingreso":  ingreso,
                "costo":    costo,
                "ganancia": ganancia,
            })

            t_inicio = max(tiempo_turno_actual, t_libre)
            relojes_choferes[idx_libre] = t_inicio + t_chofer
            tiempo_turno_actual = t_inicio
            self.registros.append(registro)

        self.clima_turno  = clima_turno
        self.factor_daño   = factor_daño
        self.factor_llegadas = factor_llegadas
        self.na_clima       = round(na_clima, 10)
        self.na_fallas_choferes  = na_fallas_choferes
        self.estados_choferes    = estados_choferes
        self.choferes_activos = choferes_activos
        self.ingresos_totales = round(ingresos_totales, 2)
        self.costos_totales  = round(costos_totales, 2)
        self.penalizaciones  = round(penalizaciones, 2)
        self.ganancias_netas = round(ingresos_totales - costos_totales, 2)
        self.total_espera_cola  = round(total_espera_cola, 2)
        self.relojes_choferes_map = relojes_choferes
        self.cajones_disponibles = cajones_disponibles
        self.costos_daños_total = round(costos_daños_total, 2)
        self.costos_extra_total = round(costos_extra_total, 2)
        self.cancelaciones   = cancelaciones
        self.salidas_tempranas  = salidas_tempranas
        self.num_vehiculos_efectivos = num_vehiculos_efectivos
        self.conteo_daños = conteo_daños

        self.relojes_choferes = [relojes_choferes.get(i, 0) for i in range(self.num_choferes)]

        return self.costos_totales, self.ganancias_netas


# =============================================================================
#   PALETA DE COLORES
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
    ("T1",  "T1",  "T1 – Recepción (min)"),
    ("T2",  "T2",  "T2 – Maniobra (min)"),
    ("T3",  "T3",  "T3 – Permanencia (h)"),
    ("T4",  "T4",  "T4 – Solicitud (min)"),
    ("T5",  "T5",  "T5 – Devolución (min)"),
    ("T6",  "T6",  "T6 – Llegadas"),
    ("T7",  "T7",  "T7 – Mantenimiento"),
    ("T8",  "T8",  "T8 – Tipo de daño"),
    ("T9",  "T9",  "T9 – Tiempo extra"),
    ("T9H", "T9H", "T9H – Horas extra"),
    ("T10", "T10", "T10 – Falla chofer"),
    ("T11", "T11", "T11 – Cancelación"),
    ("T12", "T12", "T12 – Salida temprana"),
    ("T13", "T13", "T13 – Clima"),
]

COL_PRIMARIA = {
    "T1":  "tiempo",
    "T2":  "tiempo",
    "T3":  "tiempo",
    "T4":  "tiempo",
    "T5":  "tiempo",
    "T6":  "turno",
    "T7":  "tiempo",
    "T8":  "tipo de daño",
    "T9":  "excede",
    "T9H": "horas_extra",
    "T10": "estado_chofer",
    "T11": "cancela",
    "T12": "sale_temprano",
    "T13": "clima",
}

TABLA_ESPECIAL = {
    "T8":  ["tipo de daño", "costo de rep"],
    "T9H": ["horas_extra", "costo_extra"],
    "T13": ["clima", "factor_daño", "factor_llegadas"],
    "T6":  ["turno", "horario", "veh_hora"],
}


def _df_a_tabla(df: pd.DataFrame) -> str:
    cols = list(df.columns)
    anchos = []
    for col in cols:
        max_val = max(
            len(str(col).lower()),          #  minúsculas
            *[len(str(v)) for v in df[col]]
        )
        anchos.append(max_val + 2)

    sep = "+" + "+".join("-" * a for a in anchos) + "+"

    def fila(vals, es_encabezado=False):
        partes = []
        for v, a in zip(vals, anchos):
            s = str(v).lower() if es_encabezado else str(v)  
            partes.append(" " + s.ljust(a - 1))
        return "|" + "|".join(partes) + "|"

    lineas = [sep, fila(cols, es_encabezado=True), sep]  
    for _, row in df.iterrows():
        lineas.append(fila([row[c] for c in cols]))
    lineas.append(sep)
    return "\n".join(lineas)

def _registros_a_tabla(registros: list) -> str:
    columnas = [
        "veh", "na-t6", "turno",
        "na-t13", "clima", "fdaño", "flleg",
        "na-t10", "estch", "cajón", "chofer",
        "espera", "na-t11", "cancela",
        "na-rec", "trec",
        "na-man", "tman",
        "na-per", "tper",
        "na-sol", "tsol",
        "na-dev", "tdev",
        "t.ch",
        "na-t9", "excede", "na-t9h", "hext", "$extra",
        "na-t12", "stemp",
        "na-daño", "tipo daño", "$daño",
        "ingreso", "costo", "ganancia",
    ]

    def extraer_fila(r):
        cajon_val = r.get("cajon_dispon", "No")
        cancela_s = r.get("cancela", "---")

        na10_s = f"{r.get('na_t10_chofer', 0):.6f}" if r.get("na_t10_chofer", "---") != "---" else "---"
        na11_s = f"{r.get('na_t11', 0):.6f}"        if r.get("na_t11", "---") != "---"         else "---"

        base = [
            str(r["vehiculo"]),
            f"{r.get('na_t6', 0):.6f}",          # na-t6 ANTES que turno
            r.get("turno", "")[:12],
            f"{r.get('na_clima', 0):.6f}",        # na-t13 ANTES que clima
            r.get("clima", "---")[:13],
            f"{r.get('fact_daño', 1):.1f}",
            f"{r.get('fact_lleg', 1):.1f}",
            na10_s,                               # na-t10 ANTES que estch
            r.get("estado_chofer", "---")[:6],
            cajon_val,                            # cajón DESPUÉS de estch
            str(r.get("chofer_asig", "---")),
            f"{r.get('t_espera', 0):.0f}",
            na11_s,                               # na-t11 ANTES que cancela
            cancela_s,
        ]

        if cajon_val == "No":
            resto = ["---"] * 23 + [f"${-PENALIZACION_NEGADO:.2f}"]
        elif cancela_s == "Sí":
            resto = ["---"] * 23 + ["$0.00"]
        else:
            tr  = int(r.get("t_recepcion",   0))
            tm  = int(r.get("t_maniobra",    0))
            tp  = int(r.get("t_permanencia", 0))
            ts  = int(r.get("t_solicitud",   0))
            td  = int(r.get("t_devolucion",  0))
            tch = int(r.get("t_chofer",      0))
            resto = [
                f"{r.get('na_recepcion',   0):.6f}", str(tr),   # na ANTES que tiempo
                f"{r.get('na_maniobra',    0):.6f}", str(tm),
                f"{r.get('na_permanencia', 0):.6f}", str(tp),
                f"{r.get('na_solicitud',   0):.6f}", str(ts),
                f"{r.get('na_devolucion',  0):.6f}", str(td),
                str(tch),
                f"{r.get('na_t9',  0):.6f}", r.get("excede", "---"),   # na-t9 → excede
                f"{r.get('na_t9h', 0):.6f}",                            # na-t9h → hext
                str(r.get("horas_extra", 0)),
                f"${r.get('costo_extra', 0)}",
                f"{r.get('na_t12', 0):.6f}", r.get("sale_temprano", "---"),  # na-t12 → stemp
                f"{r.get('na_daño', 0):.6f}", r.get("tipo_daño", "---"), f"${r.get('costo_daño', 0)}",
                f"${r.get('ingreso', 0)}", f"${r.get('costo', 0):.2f}", f"${r.get('ganancia', 0):.2f}",
            ]

        return base + resto

    filas_data = [extraer_fila(r) for r in registros]

    anchos = []
    for i, col in enumerate(columnas):
        max_ancho = len(col)
        for fila in filas_data:
            if i < len(fila):
                max_ancho = max(max_ancho, len(fila[i]))
        anchos.append(max_ancho + 2)

    sep = "+" + "+".join("-" * a for a in anchos) + "+"

    def render_fila(vals):
        partes = []
        for v, a in zip(vals, anchos):
            partes.append(" " + str(v).ljust(a - 1))
        return "|" + "|".join(partes) + "|"

    lineas = [sep, render_fila(columnas), sep]
    for fila in filas_data:
        lineas.append(render_fila(fila))
    lineas.append(sep)

    return "\n".join(lineas)
    

    def extraer_fila(r):
        cajon_val = r.get("cajon_dispon", "No")
        cancela_s = r.get("cancela", "---")

        na10_s  = f"{r.get('na_t10_chofer', 0):.6f}" if r.get("na_t10_chofer", "---") != "---" else "---"
        na11_s  = f"{r.get('na_t11', 0):.6f}"        if r.get("na_t11", "---") != "---"         else "---"

        base = [
            str(r["vehiculo"]),
            r.get("turno", "")[:12],
            f"{r.get('na_t6', 0):.6f}",
            r.get("clima", "---")[:13],
            f"{r.get('na_clima', 0):.6f}",
            f"{r.get('fact_daño', 1):.1f}",
            f"{r.get('fact_lleg', 1):.1f}",
            cajon_val,
            str(r.get("chofer_asig", "---")),
            na10_s,
            r.get("estado_chofer", "---")[:6],
            f"{r.get('t_espera', 0):.0f}",
            na11_s,
            cancela_s,
        ]

        if cajon_val == "No":
            resto = ["---", "---", "---", "---", "---", "---", "---", "---",
                     "---", "---", "---", "---", "---", "---", "---", "---",
                     "---", "---", "---", "---", "---", "---", "---",
                     f"${-PENALIZACION_NEGADO:.2f}"]
        elif cancela_s == "Sí":
            resto = ["---", "---", "---", "---", "---", "---", "---", "---",
                     "---", "---", "---", "---", "---", "---", "---", "---",
                     "---", "---", "---", "---", "---", "---", "---",
                     "$0.00"]
        else:
            tr  = int(r.get("t_recepcion",   0))
            tm  = int(r.get("t_maniobra",    0))
            tp  = int(r.get("t_permanencia", 0))
            ts  = int(r.get("t_solicitud",   0))
            td  = int(r.get("t_devolucion",  0))
            tch = int(r.get("t_chofer",      0))
            resto = [
                f"{r.get('na_recepcion',  0):.6f}", str(tr),
                f"{r.get('na_maniobra',   0):.6f}", str(tm),
                f"{r.get('na_permanencia',0):.6f}", str(tp),
                f"{r.get('na_solicitud',  0):.6f}", str(ts),
                f"{r.get('na_devolucion', 0):.6f}", str(td),
                str(tch),
                f"{r.get('na_t9',  0):.6f}",
                r.get("excede", "---"),
                f"{r.get('na_t9h', 0):.6f}",
                str(r.get("horas_extra", 0)),
                f"${r.get('costo_extra', 0)}",
                f"{r.get('na_t12', 0):.6f}",
                r.get("sale_temprano", "---"),
                f"{r.get('na_daño', 0):.6f}",
                r.get("tipo_daño", "---"),
                f"${r.get('costo_daño', 0)}",
                f"${r.get('ingreso', 0)}",
                f"${r.get('costo', 0):.2f}",
                f"${r.get('ganancia', 0):.2f}",
            ]

        return base + resto

    filas_data = [extraer_fila(r) for r in registros]

    anchos = []
    for i, col in enumerate(columnas):
        max_ancho = len(col)
        for fila in filas_data:
            if i < len(fila):
                max_ancho = max(max_ancho, len(fila[i]))
        anchos.append(max_ancho + 2)

    sep = "+" + "+".join("-" * a for a in anchos) + "+"

    def render_fila(vals):
        partes = []
        for v, a in zip(vals, anchos):
            partes.append(" " + str(v).ljust(a - 1))
        return "|" + "|".join(partes) + "|"

    lineas = [sep, render_fila(columnas), sep]
    for fila in filas_data:
        lineas.append(render_fila(fila))
    lineas.append(sep)

    return "\n".join(lineas)


# =============================================================================
#   WIDGET TablaVisor
# =============================================================================

class TablaVisor(ctk.CTkFrame):

    def __init__(self, parent, **kwargs):
        super().__init__(parent, fg_color="transparent", **kwargs)
        self._tablas_data = None
        self._tab_activa  = "T1"
        self._botones_tab = {}
        self._edit_mode   = False
        self._filas_edit  = []
        self._construir()

    def _construir(self):
        frame_tabs = ctk.CTkFrame(self, fg_color=COLOR_BG_INPUT, corner_radius=8)
        frame_tabs.pack(fill="x", pady=(0, 6))

        for i, (label, _key, _titulo) in enumerate(TABS_TABLAS):
            btn = ctk.CTkButton(
                frame_tabs, text=label, width=34, height=26,
                font=ctk.CTkFont(size=9, weight="bold"),
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
            self._frame_btns, text="Editar tabla", width=80, height=24,
            font=ctk.CTkFont(size=10, weight="bold"),
            fg_color=COLOR_BG_DARK, hover_color=COLOR_BORDER,
            text_color=COLOR_TEXT_PRIMARY, corner_radius=6,
            command=self._activar_edicion,
        )
        self.btn_editar.pack(side="left", padx=2)

        self.btn_add = ctk.CTkButton(
            self._frame_btns, text="Agregar fila", width=68, height=24,
            font=ctk.CTkFont(size=10, weight="bold"),
            fg_color="#1B5E20", hover_color="#2E7D32",
            text_color=COLOR_OK_GREEN, corner_radius=6,
            command=self._agregar_fila,
        )

        self.btn_guardar = ctk.CTkButton(
            self._frame_btns, text="Guardar tabla", width=86, height=24,
            font=ctk.CTkFont(size=10, weight="bold"),
            fg_color="#0D47A1", hover_color="#1565C0",
            text_color="#90CAF9", corner_radius=6,
            command=self._guardar_edicion,
        )

        self.btn_cancelar = ctk.CTkButton(
            self._frame_btns, text="Cancelar", width=88, height=24,
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
            self._text_vista.insert("end", _df_a_tabla(df))
            color = COLOR_OK_GREEN if abs(suma - 1.0) < 0.0002 else COLOR_WARN_RED
            self.lbl_suma.configure(text=f"Sumas de la probabilidad = {suma}  ", text_color=color)

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
        es_llegadas = (key == "T6")
        es_daños    = (key == "T8")
        es_t9h      = (key == "T9H")
        es_t13      = (key == "T13")

        if es_daños:
            headers    = ["tipo de daño", "costo de rep", "prob", "prob_acum", "rango_inf", "rango_sup", ""]
            col_widths = [100, 80, 70, 80, 80, 80, 30]
        elif es_t9h:
            headers    = ["horas_extra", "costo_extra", "prob", "prob_acum", "rango_inf", "rango_sup", ""]
            col_widths = [90, 90, 70, 80, 80, 80, 30]
        elif es_t13:
            headers    = ["clima", "factor_daño", "factor_llegadas", "prob", "prob_acum", "rango_inf", "rango_sup", ""]
            col_widths = [100, 90, 90, 70, 80, 80, 80, 30]
        elif es_llegadas:
            headers    = ["turno", "horario", "veh_hora", "prob", "prob_acum", "rango_inf", "rango_sup", ""]
            col_widths = [90, 70, 60, 70, 80, 80, 80, 30]
        else:
            headers    = [col_prim, "prob", "prob_acum", "rango_inf", "rango_sup", ""]
            col_widths = [80, 70, 80, 80, 80, 30]

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
            self._insertar_fila_grid(
                sf, i + 2, row,
                es_llegadas, es_daños, es_t9h, es_t13,
                col_prim, col_widths,
            )

        self._df_edit_key  = key
        self._es_llegadas  = es_llegadas
        self._es_daños     = es_daños
        self._es_t9h       = es_t9h
        self._es_t13       = es_t13
        self._col_prim     = col_prim

    def _insertar_fila_grid(self, sf, row_idx, row_data,
                             es_llegadas, es_daños, es_t9h, es_t13,
                             col_prim, col_widths):
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

        if es_daños:
            fila["e_prim"]  = make_entry(0, row_data.get("tipo de daño", ""),  col_widths[0])
            fila["e_costo"] = make_entry(1, row_data.get("costo de rep", 0),   col_widths[1])
            fila["e_prob"]  = make_entry(2, f"{row_data['prob']:.4f}",         col_widths[2],
                                         callback=lambda e: self._on_prob_change())
            fila["e_acum"]  = make_entry(3, f"{row_data['prob_acum']:.4f}",    col_widths[3], read_only=True)
            fila["e_ri"]    = make_entry(4, f"{row_data['rango_inf']:.4f}",    col_widths[4], read_only=True)
            fila["e_rs"]    = make_entry(5, f"{row_data['rango_sup']:.4f}",    col_widths[5], read_only=True)
            del_col = 6

        elif es_t9h:
            fila["e_prim"]  = make_entry(0, row_data.get("horas_extra", 1),   col_widths[0])
            fila["e_costo"] = make_entry(1, row_data.get("costo_extra", 0),   col_widths[1])
            fila["e_prob"]  = make_entry(2, f"{row_data['prob']:.4f}",        col_widths[2],
                                         callback=lambda e: self._on_prob_change())
            fila["e_acum"]  = make_entry(3, f"{row_data['prob_acum']:.4f}",   col_widths[3], read_only=True)
            fila["e_ri"]    = make_entry(4, f"{row_data['rango_inf']:.4f}",   col_widths[4], read_only=True)
            fila["e_rs"]    = make_entry(5, f"{row_data['rango_sup']:.4f}",   col_widths[5], read_only=True)
            del_col = 6

        elif es_t13:
            fila["e_prim"]   = make_entry(0, row_data.get("clima", ""),              col_widths[0])
            fila["e_fdaño"]  = make_entry(1, row_data.get("factor_daño", 1.0),       col_widths[1])
            fila["e_flleg"]  = make_entry(2, row_data.get("factor_llegadas", 1.0),   col_widths[2])
            fila["e_prob"]   = make_entry(3, f"{row_data['prob']:.4f}",              col_widths[3],
                                          callback=lambda e: self._on_prob_change())
            fila["e_acum"]   = make_entry(4, f"{row_data['prob_acum']:.4f}",         col_widths[4], read_only=True)
            fila["e_ri"]     = make_entry(5, f"{row_data['rango_inf']:.4f}",         col_widths[5], read_only=True)
            fila["e_rs"]     = make_entry(6, f"{row_data['rango_sup']:.4f}",         col_widths[6], read_only=True)
            del_col = 7

        elif es_llegadas:
            fila["e_turno"]   = make_entry(0, row_data.get("turno", ""),    col_widths[0])
            fila["e_horario"] = make_entry(1, row_data.get("horario", ""),  col_widths[1])
            fila["e_veh"]     = make_entry(2, row_data.get("veh_hora", ""), col_widths[2])
            fila["e_prob"]    = make_entry(3, f"{row_data['prob']:.4f}",    col_widths[3],
                                           callback=lambda e: self._on_prob_change())
            fila["e_acum"]    = make_entry(4, f"{row_data['prob_acum']:.4f}", col_widths[4], read_only=True)
            fila["e_ri"]      = make_entry(5, f"{row_data['rango_inf']:.4f}", col_widths[5], read_only=True)
            fila["e_rs"]      = make_entry(6, f"{row_data['rango_sup']:.4f}", col_widths[6], read_only=True)
            del_col = 7

        else:
            fila["e_prim"] = make_entry(0, row_data[col_prim],              col_widths[0])
            fila["e_prob"] = make_entry(1, f"{row_data['prob']:.4f}",       col_widths[1],
                                        callback=lambda e: self._on_prob_change())
            fila["e_acum"] = make_entry(2, f"{row_data['prob_acum']:.4f}",  col_widths[2], read_only=True)
            fila["e_ri"]   = make_entry(3, f"{row_data['rango_inf']:.4f}",  col_widths[3], read_only=True)
            fila["e_rs"]   = make_entry(4, f"{row_data['rango_sup']:.4f}",  col_widths[4], read_only=True)
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
        sf      = self._scroll_edit
        row_idx = max((f["row"] for f in self._filas_edit), default=1) + 1

        es_daños    = getattr(self, "_es_daños",    False)
        es_t9h      = getattr(self, "_es_t9h",      False)
        es_t13      = getattr(self, "_es_t13",      False)
        es_llegadas = getattr(self, "_es_llegadas",  False)

        if es_daños:
            col_w = [100, 80, 70, 80, 80, 80, 30]
            dummy = {"tipo de daño": "Nuevo", "costo de rep": 0,
                     "prob": 0.0, "prob_acum": 0.0, "rango_inf": 0.0, "rango_sup": 0.0}
        elif es_t9h:
            col_w = [90, 90, 70, 80, 80, 80, 30]
            dummy = {"horas_extra": 1, "costo_extra": 0,
                     "prob": 0.0, "prob_acum": 0.0, "rango_inf": 0.0, "rango_sup": 0.0}
        elif es_t13:
            col_w = [100, 90, 90, 70, 80, 80, 80, 30]
            dummy = {"clima": "Nuevo", "factor_daño": 1.0, "factor_llegadas": 1.0,
                     "prob": 0.0, "prob_acum": 0.0, "rango_inf": 0.0, "rango_sup": 0.0}
        elif es_llegadas:
            col_w = [90, 70, 60, 70, 80, 80, 80, 30]
            dummy = {"turno": "Nuevo", "horario": "HH-HHh", "veh_hora": "0-0",
                     "prob": 0.0, "prob_acum": 0.0, "rango_inf": 0.0, "rango_sup": 0.0}
        else:
            col_w = [80, 70, 80, 80, 80, 30]
            try:
                ultimo_val = int(self._filas_edit[-1]["e_prim"].get())
                nuevo_val  = ultimo_val + 1
            except (ValueError, IndexError):
                nuevo_val = 1
            dummy = {self._col_prim: nuevo_val,
                     "prob": 0.0, "prob_acum": 0.0, "rango_inf": 0.0, "rango_sup": 0.0}

        row_s = pd.Series(dummy)
        self._insertar_fila_grid(
            sf, row_idx, row_s,
            es_llegadas, es_daños, es_t9h, es_t13,
            self._col_prim, col_w,
        )
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
            text=f"suma de probs = {suma:.4f}{'  ' if abs(suma-1.0)<0.0002 else '  '}",
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
                "Debe ser exactamente 1.0000 para que funcione."
            )
            return

        key         = self._df_edit_key
        col_prim    = self._col_prim
        es_llegadas = self._es_llegadas
        es_daños    = self._es_daños
        es_t9h      = self._es_t9h
        es_t13      = self._es_t13

        filas_data = []
        for f, p in zip(self._filas_edit, probabilidades):
            if es_daños:
                try:
                    costo = int(f["e_costo"].get())
                except ValueError:
                    costo = 0
                row = {"tipo de daño": f["e_prim"].get(), "costo de rep": costo, "prob": p}

            elif es_t9h:
                try:
                    horas = int(f["e_prim"].get())
                    costo = int(f["e_costo"].get())
                except ValueError:
                    horas, costo = 1, 0
                row = {"horas_extra": horas, "costo_extra": costo, "prob": p}

            elif es_t13:
                try:
                    fd = float(f["e_fdaño"].get())
                    fl = float(f["e_flleg"].get())
                except ValueError:
                    fd, fl = 1.0, 1.0
                row = {"clima": f["e_prim"].get(), "factor_daño": fd, "factor_llegadas": fl, "prob": p}

            elif es_llegadas:
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
        ctk.CTkLabel(v, text="errorr",
                     font=ctk.CTkFont(size=13, weight="bold"),
                     text_color=COLOR_ACCENT_RED).pack(pady=(18, 6))
        ctk.CTkLabel(v, text=mensaje,
                     font=ctk.CTkFont(size=12),
                     text_color=COLOR_TEXT_PRIMARY,
                     wraplength=320).pack(padx=16)
        ctk.CTkButton(v, text="Entendido",
                      fg_color=COLOR_BG_INPUT, hover_color=COLOR_BORDER,
                      command=v.destroy).pack(pady=14)


# =============================================================================
#   INTERFAZ PRINCIPAL
# =============================================================================

class Interfaz_EVP(ctk.CTk):

    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        self.title("Simulación Monte Carlo — Valet Parking")
        self.geometry("1280x820")
        self.minsize(1050, 680)
        self.configure(fg_color=COLOR_BG_DARK)
        self.hotel      = None
        self._historial = []
        self._dia_activo = 0
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
        frame_entradas.columnconfigure(2, weight=1)

        ctk.CTkLabel(frame_entradas, text="Choferes",
                     font=ctk.CTkFont(size=11), text_color=COLOR_TEXT_MUTED,
                     ).grid(row=0, column=0, sticky="w", padx=(0, 4), pady=(0, 2))
        ctk.CTkLabel(frame_entradas, text="Vehículos",
                     font=ctk.CTkFont(size=11), text_color=COLOR_TEXT_MUTED,
                     ).grid(row=0, column=1, sticky="w", padx=(4, 4), pady=(0, 2))
        ctk.CTkLabel(frame_entradas, text="Días",
                     font=ctk.CTkFont(size=11), text_color=COLOR_TEXT_MUTED,
                     ).grid(row=0, column=2, sticky="w", padx=(4, 0), pady=(0, 2))

        self.entry_choferes = ctk.CTkEntry(
            frame_entradas,
            fg_color=COLOR_BG_INPUT, border_color=COLOR_BORDER,
            text_color=COLOR_TEXT_PRIMARY,
            font=ctk.CTkFont(size=14, weight="bold"),
            height=34, corner_radius=8,
        )
        self.entry_choferes.insert(0, "3")
        self.entry_choferes.grid(row=1, column=0, sticky="ew", padx=(0, 4))

        self.entry_vehiculos = ctk.CTkEntry(
            frame_entradas,
            fg_color=COLOR_BG_INPUT, border_color=COLOR_BORDER,
            text_color=COLOR_TEXT_PRIMARY,
            font=ctk.CTkFont(size=14, weight="bold"),
            height=34, corner_radius=8,
        )
        self.entry_vehiculos.insert(0, "20")
        self.entry_vehiculos.grid(row=1, column=1, sticky="ew", padx=(4, 4))

        self.entry_dias = ctk.CTkEntry(
            frame_entradas,
            fg_color=COLOR_BG_INPUT, border_color=COLOR_BORDER,
            text_color=COLOR_TEXT_PRIMARY,
            font=ctk.CTkFont(size=14, weight="bold"),
            height=34, corner_radius=8,
        )
        self.entry_dias.insert(0, "7")
        self.entry_dias.grid(row=1, column=2, sticky="ew", padx=(4, 0))

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
            text="SIMULAR",
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

    # ── Tabla de simulación: ahora incluye selector de días integrado ─────────
    def _construir_tab_tabla(self, parent):
        parent.configure(fg_color="transparent")

        # ── Barra de días (scrollable horizontal) ────────────────────────────
        self._frame_selector_dias = ctk.CTkScrollableFrame(
            parent,
            fg_color=COLOR_BG_INPUT, corner_radius=8,
            height=48, orientation="horizontal",
            scrollbar_button_color=COLOR_BORDER,
        )
        self._frame_selector_dias.pack(fill="x", padx=12, pady=(8, 0))

        self._btn_dias = []

        # ── Franja de resumen del día seleccionado ───────────────────────────
        self._frame_dia_info = ctk.CTkFrame(
            parent, fg_color=COLOR_BG_INPUT, corner_radius=8,
        )
        self._frame_dia_info.pack(fill="x", padx=12, pady=(4, 0))

        self.lbl_dia_titulo = ctk.CTkLabel(
            self._frame_dia_info, text="",
            font=ctk.CTkFont(size=12, weight="bold"),
            text_color=COLOR_ACCENT_BLUE,
        )
        self.lbl_dia_titulo.pack(side="left", padx=12, pady=5)

        self.lbl_conteo_filas = ctk.CTkLabel(
            self._frame_dia_info, text="",
            font=ctk.CTkFont(size=11),
            text_color=COLOR_ACCENT_TEAL,
        )
        self.lbl_conteo_filas.pack(side="left", padx=(0, 8), pady=5)

        self.lbl_dia_resumen = ctk.CTkLabel(
            self._frame_dia_info, text="",
            font=ctk.CTkFont(size=11),
            text_color=COLOR_ACCENT_AMBER,
        )
        self.lbl_dia_resumen.pack(side="left", padx=(0, 12), pady=5)

        # ── Tabla de vehículos ───────────────────────────────────────────────
        frame_outer = ctk.CTkFrame(parent, fg_color=COLOR_BG_INPUT, corner_radius=10)
        frame_outer.pack(fill="both", expand=True, padx=12, pady=(4, 12))

        self.text_tabla = ctk.CTkTextbox(
            frame_outer, fg_color="transparent", text_color=COLOR_TEXT_PRIMARY,
            font=ctk.CTkFont(family="Courier", size=14),
            wrap="none", activate_scrollbars=True,
        )
        self.text_tabla.pack(fill="both", expand=True, padx=8, pady=8)
        self.text_tabla.insert("end", "Ejecuta la simulación para ver la tabla.")
        self.text_tabla.configure(state="disabled")

    def _reconstruir_botones_dias(self, num_dias: int):
        """Crea/recrea los botones de selección de día dentro de 'Tabla de simulación'."""
        for w in self._frame_selector_dias.winfo_children():
            w.destroy()
        self._btn_dias = []

        for d in range(num_dias):
            btn = ctk.CTkButton(
                self._frame_selector_dias,
                text=f"Día {d + 1}",
                width=60, height=30,
                font=ctk.CTkFont(size=10, weight="bold"),
                corner_radius=6,
                fg_color=COLOR_BG_DARK,
                hover_color=COLOR_BORDER,
                text_color=COLOR_TEXT_MUTED,
                command=lambda idx=d: self._seleccionar_dia(idx),
            )
            btn.pack(side="left", padx=3, pady=6)
            self._btn_dias.append(btn)

    def _seleccionar_dia(self, idx: int):
        """Resalta el botón activo y actualiza la tabla + franja de resumen."""
        self._dia_activo = idx

        for i, btn in enumerate(self._btn_dias):
            if i == idx:
                btn.configure(fg_color=COLOR_BG_INPUT, text_color=COLOR_TEXT_PRIMARY)
            else:
                btn.configure(fg_color=COLOR_BG_DARK, text_color=COLOR_TEXT_MUTED)

        if not self._historial:
            return

        snap = self._historial[idx]

        # Franja de resumen rápido
        self.lbl_dia_titulo.configure(
            text=f"Día {snap['dia']}  —  {snap['clima']}"
        )
        self.lbl_conteo_filas.configure(
            text=f"  {snap['vehiculos_efectivos']} vehículos"
        )
        self.lbl_dia_resumen.configure(
            text=(
                f"  Atend: {snap['atendidos']}  "
                f"Negad: {snap['negados']}  "
                f"Cancel: {snap['cancelaciones']}  │  "
                f"Ingresos: ${snap['ingresos']:.2f}  "
                f"Costos: ${snap['costos']:.2f}  "
                f"Ganancia: ${snap['ganancias']:.2f}"
            )
        )

        # Tabla de vehículos del día seleccionado
        contenido = _registros_a_tabla(snap["registros"])
        self.text_tabla.configure(state="normal")
        self.text_tabla.delete("1.0", "end")
        self.text_tabla.insert("end", contenido)
        self.text_tabla.configure(state="disabled")

    def _construir_tab_resumen(self, parent):
        parent.configure(fg_color="transparent")
        frame = ctk.CTkFrame(parent, fg_color=COLOR_BG_INPUT, corner_radius=10)
        frame.pack(fill="both", expand=True, padx=12, pady=12)
        ctk.CTkLabel(
            frame, text="Resultados",
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

    def _iniciar_simulacion(self):
        try:
            nc = int(self.entry_choferes.get())
            nv = int(self.entry_vehiculos.get())
            nd = int(self.entry_dias.get())
        except ValueError:
            self._mostrar_error("Ingresa números enteros válidos.")
            return
        if nc < 1 or nv < 1 or nd < 1:
            self._mostrar_error("Los valores deben ser mayores a 0.")
            return

        self.btn_simular.configure(state="disabled", text="⏳  Simulando...")
        threading.Thread(
            target=self._ejecutar_simulacion, args=(nc, nv, nd), daemon=True
        ).start()

    def _ejecutar_simulacion(self, nc, nv, nd):
        try:
            reiniciar_aleatorios()
            hotel = Estacionamiento_Valet_Parking(num_choferes=nc)
            if self.tabla_visor._tablas_data is not None:
                hotel.tablas = {k: v.copy() for k, v in self.tabla_visor._tablas_data.items()}
            else:
                hotel.tablas = generar_todas_las_tablas()

            historial = hotel.simular_dias(nd, nv)
            self.hotel = hotel
        except Exception as e:
            import traceback
            tb = traceback.format_exc()
            self.after(0, lambda msg=tb: self._mostrar_error(msg))
            self.after(0, lambda: self.btn_simular.configure(
                state="normal", text="SIMULAR"))
            return
        self.after(0, lambda: self._actualizar_ui(hotel, historial))

    def _actualizar_ui(self, hotel, historial):
        self._historial = historial
        self.tabla_visor.actualizar_tablas(hotel.tablas)

        # Reconstruir selector de días y mostrar día 1 automáticamente
        self._reconstruir_botones_dias(len(historial))
        self._seleccionar_dia(0)

        # Resumen global
        self._renderizar_resumen(hotel, historial)

        self.btn_simular.configure(state="normal", text="SIMULAR")
        self.tabview.set("Tabla de simulación")

    def _renderizar_resumen(self, hotel, historial):
        nd = len(historial)

        total_ingresos    = sum(s["ingresos"]    for s in historial)
        total_costos      = sum(s["costos"]      for s in historial)
        total_ganancias   = sum(s["ganancias"]   for s in historial)
        total_atendidos   = sum(s["atendidos"]   for s in historial)
        total_negados     = sum(s["negados"]     for s in historial)
        total_cancel      = sum(s["cancelaciones"] for s in historial)
        total_daños       = sum(s["costos_daños"] for s in historial)
        total_penal       = sum(s["penalizaciones"] for s in historial)
        total_espera      = sum(s["espera_total"] for s in historial)
        total_efect       = sum(s["vehiculos_efectivos"] for s in historial)

        mejor_dia  = max(historial, key=lambda s: s["ganancias"])
        peor_dia   = min(historial, key=lambda s: s["ganancias"])
        prom_gan   = round(total_ganancias / nd, 2)

        W = 52
        lineas = [
            f"{'─'*W}",
            f"  RESUMEN GLOBAL — {nd} DÍA(S)",
            f"{'─'*W}",
            f"  {'Vehículos efectivos (total)':<36} {total_efect}",
            f"  {'Vehículos atendidos (total)':<36} {total_atendidos}",
            f"  {'Vehículos negados (total)':<36} {total_negados}",
            f"  {'Cancelaciones (total)':<36} {total_cancel}",
            f"{'─'*W}",
            f"  {'Ingresos acumulados':<36} ${total_ingresos:.2f}",
            f"  {'Costos acumulados':<36} ${total_costos:.2f}",
            f"  {'Costo daños acumulado':<36} ${total_daños:.2f}",
            f"  {'Penalizaciones acumuladas':<36} ${total_penal:.2f}",
            f"  {'Ganancias netas acumuladas':<36} ${total_ganancias:.2f}",
            f"  {'Promedio diario de ganancias':<36} ${prom_gan:.2f}",
            f"{'─'*W}",
            f"  {'Mejor día (ganancias)':<36} Día {mejor_dia['dia']} (${mejor_dia['ganancias']:.2f})",
            f"  {'Peor día (ganancias)':<36} Día {peor_dia['dia']}  (${peor_dia['ganancias']:.2f})",
            f"  {'Espera total acumulada (min)':<36} {total_espera:.2f}",
            f"{'─'*W}",
            f"  DETALLE POR DÍA",
            f"{'─'*W}",
            f"  {'Día':<5} {'Clima':<14} {'Efect':>5} {'Atend':>5} {'Negad':>5} {'Canc':>5} {'Ingresos':>10} {'Costos':>10} {'Ganancia':>10}",
            f"  {'─'*4} {'─'*13} {'─'*5} {'─'*5} {'─'*5} {'─'*5} {'─'*10} {'─'*10} {'─'*10}",
        ]

        for s in historial:
            lineas.append(
                f"  {s['dia']:<5} {s['clima'][:13]:<14} "
                f"{s['vehiculos_efectivos']:>5} {s['atendidos']:>5} "
                f"{s['negados']:>5} {s['cancelaciones']:>5} "
                f"{s['ingresos']:>10.2f} {s['costos']:>10.2f} {s['ganancias']:>10.2f}"
            )

        lineas.append(f"{'─'*W}")

        self.text_resumen.configure(state="normal")
        self.text_resumen.delete("1.0", "end")
        self.text_resumen.insert("end", "\n".join(lineas))
        self.text_resumen.configure(state="disabled")

    def _mostrar_error(self, mensaje):
        v = ctk.CTkToplevel(self)
        v.title("Error"); v.geometry("600x400")
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