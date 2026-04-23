import customtkinter as ctk
from PIL import Image, ImageOps
import os


class main:
    def __init__(self):
        self.principal = ctk.CTk() 
        self.principal.title("HOTEL")
        
        try: self.principal.state("zoomed")
        except: self.principal.attributes("-zoomed", True)

        self.menu = ctk.CTkFrame(self.principal, width=400, corner_radius=0)
        self.menu.pack(side="left", fill="y")

        self.recepcion = ctk.CTkButton(self.menu, text="Recepcion")
        self.recepcion.pack(padx=10, pady=10)

        self.estacionamiento = ctk.CTkButton(self.menu, text="Estacionamiento")
        self.estacionamiento.pack(padx=10, pady=10)

        self.restaurante = ctk.CTkButton(self.menu, text="Restaurante", command=lambda: self.llamaCosina())
        self.restaurante.pack(padx=10, pady=10)

        self.Artencionmedica = ctk.CTkButton(self.menu, text="Atencion medica")
        self.Artencionmedica.pack(padx=10, pady=10)

        self.Lavanderia = ctk.CTkButton(self.menu, text="Lavanderia")
        self.Lavanderia.pack(padx=10, pady=10)

        self.bar = ctk.CTkButton(self.menu, text="Bar")
        self.bar.pack(padx=10, pady=10)

        self.mantenimiento = ctk.CTkButton(self.menu, text="Mantenimiento")
        self.mantenimiento.pack(padx=10, pady=10)

        self.ResercasOnline = ctk.CTkButton(self.menu, text="Reservas online")
        self.ResercasOnline.pack(padx=10, pady=10)

        self.marketing = ctk.CTkButton(self.menu, text="marketing")
        self.marketing.pack(padx=10, pady=10)

        self.Bodega = ctk.CTkButton(self.menu, text="Bodega central")
        self.Bodega.pack(padx=10, pady=10)


        self.contenido = ctk.CTkFrame(self.principal, fg_color="transparent")
        self.contenido.pack(fill="both", expand=True)

        base_path = os.path.dirname(os.path.abspath(__file__))

        # 2. Join it with the subfolder and image name
        ruta_absoluta = os.path.join(base_path, "images", "just-b-cozumel-hotel-boutique.jpg")

        print(f"Buscando en: {ruta_absoluta}")

        try:
            self.img_original_raw = Image.open(ruta_absoluta)
        except FileNotFoundError:
            print("Error: No se encontró la imagen. Verifica que la carpeta 'images' esté junto a main.py")

        self.img_fondo_tk = ctk.CTkImage(
            light_image=self.img_original_raw,
            dark_image=self.img_original_raw,
            size=(800, 600)      
        )
        self.lbl_fondo = ctk.CTkLabel(self.contenido, image=self.img_fondo_tk, text="")
        self.lbl_fondo.place(x=0, y=0, relwidth=1, relheight=1)

        self.entrada_datos = ctk.CTkEntry(
            self.contenido,
            placeholder_text="Escribe algo aquí...",
            width=300,
            height=40
        )
        self.entrada_datos.place(relx=0.5, rely=0.4, anchor="center")

        self.boton = ctk.CTkButton(
            self.contenido,
            text="Aceptar",
            command=lambda: print(self.entrada_datos.get())
        )
        self.boton.place(relx=0.5, rely=0.55, anchor="center")
        
        self.lbl_fondo.lower()
        self.contenido.bind("<Configure>", self.redimensionar_fondo)


        self.principal.mainloop()

    def redimensionar_fondo(self, event):
        ancho = event.width
        alto  = event.height
        if ancho > 0 and alto > 0:
            self.img_fondo_tk.configure(size=(ancho, alto))
            self.lbl_fondo.configure(image=self.img_fondo_tk)



        self.principal.mainloop()

    def llamaCosina(self):
        from restaurante import cocina
        obj = cocina()

if __name__ == "__main__":
    obj = main()