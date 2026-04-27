import customtkinter as ctk

COLOR_FONDO = "#5D4037"
COLOR_TEXTO = "#FFFFFF"
COLOR_EXTRA = "#8C8680"
COLOR_BOTON = "#3E2723"

class Marketing:
    def __init__(self):
        self.ventana = ctk.CTk()
        self.ventana.title("Área de Marketing")
        self.ventana.geometry("1200x600")
        self.ventana.configure(fg_color=COLOR_FONDO)

        titulo = ctk.CTkLabel(self.ventana, text="Simulación de Marketing", text_color=COLOR_TEXTO, font=("Arial", 20, "bold"))
        titulo.pack(pady=10)

        frame_inputs = ctk.CTkFrame(self.ventana, fg_color=COLOR_EXTRA)
        frame_inputs.pack(pady=10, padx=20, fill="x")

        ctk.CTkLabel(frame_inputs, text="Días:", text_color=COLOR_TEXTO).grid(row=0, column=0, padx=10, pady=10)

        self.entry_dias = ctk.CTkEntry(frame_inputs)
        self.entry_dias.grid(row=0, column=1)

        self.boton = ctk.CTkButton(frame_inputs, text="Simular", fg_color=COLOR_BOTON)
        self.boton.grid(row=0, column=2, padx=10)

        frame_kpis = ctk.CTkFrame(self.ventana, fg_color=COLOR_EXTRA)
        frame_kpis.pack(pady=10, padx=20, fill="x")

        self.lbl_leads = ctk.CTkLabel(frame_kpis, text="Leads: 0", text_color=COLOR_TEXTO)
        self.lbl_leads.grid(row=0, column=0, padx=20)

        self.lbl_reservas = ctk.CTkLabel(frame_kpis, text="Reservas: 0", text_color=COLOR_TEXTO)
        self.lbl_reservas.grid(row=0, column=1, padx=20)

        self.lbl_roi = ctk.CTkLabel(frame_kpis, text="ROI: 0", text_color=COLOR_TEXTO)
        self.lbl_roi.grid(row=0, column=2, padx=20)

        frame_tabla = ctk.CTkFrame(self.ventana, fg_color=COLOR_EXTRA)
        frame_tabla.pack(pady=10, padx=20, fill="both", expand=True)

        self.tabla = ctk.CTkTextbox(frame_tabla)
        self.tabla.pack(fill="both", expand=True)

        self.ventana.mainloop()
    
Marketing()