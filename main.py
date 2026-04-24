import customtkinter as ctk
from PIL import Image, ImageOps
import os


class main:
    def __init__(self):
        self.principal = ctk.CTk() 
        self.principal.title("HOTEL")

        self.ingresos = 0
        self.egresos = 0
        self.total = 0
        
        try: self.principal.state("zoomed")
        except: self.principal.attributes("-zoomed", True)

        

        self.menu = ctk.CTkFrame(self.principal, width=400, corner_radius=0, fg_color="#D7CCC8")
        self.menu.pack(side="left", fill="y")

        w, h = 400, 60
        color_fondo = "#5D4037"
        color_hover = "#3E2723"
        color_texto = "#FFFFFF"
        # grisesito = #8C8680

        self.recepcion = ctk.CTkButton(self.menu, text="Recepcion", width=w, height=h, fg_color=color_fondo, hover_color=color_hover, text_color=color_texto)
        self.recepcion.pack(padx=10, pady=10)

        self.estacionamiento = ctk.CTkButton(self.menu, text="Estacionamiento", width=w, height=h, fg_color=color_fondo, hover_color=color_hover, text_color=color_texto)
        self.estacionamiento.pack(padx=10, pady=10)

        self.restaurante = ctk.CTkButton(self.menu, text="Restaurante", width=w, height=h, fg_color=color_fondo, hover_color=color_hover, text_color=color_texto, command=lambda: self.llamaCosina())
        self.restaurante.pack(padx=10, pady=10)

        self.Artencionmedica = ctk.CTkButton(self.menu, text="Atencion medica", width=w, height=h, fg_color=color_fondo, hover_color=color_hover, text_color=color_texto)
        self.Artencionmedica.pack(padx=10, pady=10)

        self.Lavanderia = ctk.CTkButton(self.menu, text="Lavanderia", width=w, height=h, fg_color=color_fondo, hover_color=color_hover, text_color=color_texto)
        self.Lavanderia.pack(padx=10, pady=10)

        self.bar = ctk.CTkButton(self.menu, text="Bar", width=w, height=h, fg_color=color_fondo, hover_color=color_hover, text_color=color_texto)
        self.bar.pack(padx=10, pady=10)

        self.mantenimiento = ctk.CTkButton(self.menu, text="Mantenimiento", width=w, height=h, fg_color=color_fondo, hover_color=color_hover, text_color=color_texto)
        self.mantenimiento.pack(padx=10, pady=10)

        self.ResercasOnline = ctk.CTkButton(self.menu, text="Reservas online", width=w, height=h, fg_color=color_fondo, hover_color=color_hover, text_color=color_texto)
        self.ResercasOnline.pack(padx=10, pady=10)

        self.marketing = ctk.CTkButton(self.menu, text="marketing", width=w, height=h, fg_color=color_fondo, hover_color=color_hover, text_color=color_texto)
        self.marketing.pack(padx=10, pady=10)

        self.Bodega = ctk.CTkButton(self.menu, text="Bodega central", width=w, height=h, fg_color=color_fondo, hover_color=color_hover, text_color=color_texto)
        self.Bodega.pack(padx=10, pady=10)


        self.contenido = ctk.CTkFrame(self.principal, fg_color="transparent")
        self.contenido.pack(fill="both", expand=True)

        # --- Imagen de fondo ---
        base_path = os.path.dirname(os.path.abspath(__file__))
        ruta_absoluta = os.path.join(base_path, "images", "just-b-cozumel-hotel-boutique.jpg")
        print(f"Buscando en: {ruta_absoluta}")

        try:
            self.img_original_raw = Image.open(ruta_absoluta)
        except FileNotFoundError:
            print("Error: No se encontró la imagen.")
            return

        self.img_fondo_tk = ctk.CTkImage(
            light_image=self.img_original_raw,
            dark_image=self.img_original_raw,
            size=(800, 600)
        )

        self.lbl_fondo = ctk.CTkLabel(self.contenido, image=self.img_fondo_tk, text="")
        self.lbl_fondo.place(x=0, y=0, relwidth=1, relheight=1)

        self.contenido.bind("<Configure>", self.redimensionar_fondo)

        # self.frame_widgets = ctk.CTkFrame(self.contenido, fg_color="transparent")
        # self.frame_widgets.place(relx=0.5, rely=0.5, anchor="center")  # centrado

        self.caja_ingresos = ctk.CTkTextbox(
            master=self.contenido,
            width=500,
            height=70,
            fg_color="#F5F5DC",        
            text_color="#228B22",    
            border_color="#228B22",    
            border_width=10,
            font=("Consolas", 20, "bold") 
        )
        self.caja_ingresos.grid(row=0, column=0, pady=20, padx=20)

        self.caja_ingresos.delete("0.0", "end") 
        self.caja_ingresos.insert("end", f"Ingresos: {self.ingresos}")\
        
        self.caja_Egresos = ctk.CTkTextbox(
            master=self.contenido,
            width=500,
            height=70,
            fg_color="#F5F5DC",        
            text_color="#B22222",    
            border_color="#B22222",    
            border_width=10,
            font=("Consolas", 20, "bold") 
        )
        self.caja_Egresos.grid(row=1, column=0, pady=20, padx=20)

        self.caja_Egresos.delete("0.0", "end") 
        self.caja_Egresos.insert("end", f"Egresos: {self.egresos}")

        self.caja_Totales = ctk.CTkTextbox(
            master=self.contenido,
            width=500,
            height=70,
            fg_color="#F5F5DC",        
            text_color="#DAA520",    
            border_color="#DAA520",    
            border_width=10,
            font=("Consolas", 20, "bold") 
        )
        self.caja_Totales.grid(row=2, column=0, pady=20, padx=20)

        self.caja_Totales.delete("0.0", "end") 
        self.caja_Totales.insert("end", f"Totales: {self.total}")

        self.label = ctk.CTkLabel(self.contenido, text="")
        self.label.grid(row=3, column=0, pady=20, padx=20)

        self.label = ctk.CTkLabel(self.contenido, text="")
        self.label.grid(row=4, column=0, pady=20, padx=20)

        self.Dias = ctk.CTkTextbox(
            master=self.contenido,
            width=500,
            height=70,
            fg_color="#F5F5DC",        
            text_color="#8C8680",    
            border_color="#8C8680",    
            border_width=10,
            font=("Consolas", 20, "bold") 
        )
        self.Dias.grid(row=5, column=0, pady=20, padx=20)

        self.Dias.delete("0.0", "end") 
        self.Dias.insert("end", f"A: 00 M: 00 D: 00")

        self.boton = ctk.CTkButton(
            self.contenido,
            text="Aceptar",
            fg_color="#5D4037",      
            hover_color="#3E2723",
            width=400,
            height=70,
            text_color="#FFFFFF",  
            border_color="#8C8680",
            border_width=2,
            font=("Consolas", 18, "bold")
        )
        self.boton.grid(row=6, column=0, pady=10)

        self.boton2 = ctk.CTkButton(
            self.contenido,
            text="Detalles",
            fg_color="#5D4037",      
            hover_color="#3E2723",
            width=400,
            height=70,
            text_color="#FFFFFF",  
            border_color="#8C8680",
            border_width=2,
            font=("Consolas", 18, "bold")
        )
        self.boton2.grid(row=7, column=0, pady=10)

    def redimensionar_fondo(self, event):
            ancho = event.width
            alto  = event.height
            if ancho > 0 and alto > 0:
                self.img_fondo_tk.configure(size=(ancho, alto))
                self.lbl_fondo.configure(image=self.img_fondo_tk)

    def llamaCosina(self):
        from restaurante import cocina
        obj = cocina()

if __name__ == "__main__":
    app = main()
    app.principal.mainloop() 