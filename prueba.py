import customtkinter as ctk
from CTkTable import CTkTable

def mostrar_detalle_dia(datos_celda):
    # datos_celda['row'] nos dice qué día presionó el usuario
    fila = datos_celda["row"]
    valor = datos_celda["value"]
    
    # Evitamos que se abra la ventana si presiona el encabezado (fila 0)
    if fila == 0:
        return

    # Crear la ventana emergente (Toplevel)
    ventana_detalle = ctk.CTkToplevel()
    ventana_detalle.title(f"Sub-eventos del Día {valor}")
    ventana_detalle.geometry("400x300")
    
    # Asegurar que la ventana aparezca al frente
    ventana_detalle.after(100, ventana_detalle.lift)

    # Aquí crearías otra CTkTable con los sub-eventos de ese día específico
    etiqueta = ctk.CTkLabel(ventana_detalle, text=f"Detalle detallado del día: {valor}")
    etiqueta.pack(pady=20)
    
    # Ejemplo de tabla de sub-eventos
    datos_sub = [["Hora", "Evento", "Encargado"], ["09:00", "Llegada", "Enfermero"], ["10:30", "Urgencia", "Doctor"]]
    tabla_sub = CTkTable(ventana_detalle, values=datos_sub, header_color="#3E2723")
    tabla_sub.pack(padx=20, pady=10)

# --- En tu clase principal ---
# Al crear la tabla original:
self.tabla = CTkTable(
    master=self.Frame_tabla_montecarlo,
    values=Titulos,
    command=mostrar_detalle_dia, # <--- AQUÍ ASIGNAS EL EVENTO
    header_color="#3E2723",
    text_color="white"
)
self.tabla.grid(row=0, column=0, sticky="ew")