import customtkinter as ctk


class BodegaHotel():
    def __init__(self):
        self.ventana = ctk.CTk()
        self.ventana.title("Bodega Central - Alimentos y Bebidas")
        self.ventana.geometry("1400x800")
        
        self.color_fondo = "#5D4037"
        self.color_hover = "#3E2723"
        self.color_texto = "#FFFFFF"
        self.color_Extra = "#8C8680"
        
        self.container = ctk.CTkFrame(self.ventana)
        self.container.pack(fill="both", expand=True)
        
        self.crear_bodega()
        
        self.ventana.mainloop()
    
    def crear_bodega(self):
        # Titulo
        self.titulo = ctk.CTkLabel(self.container, text="BODEGA CENTRAL DE ALIMENTOS Y BEBIDAS", font=("Arial", 28, "bold"), text_color=self.color_texto)
        self.titulo.pack(pady=20)
        
        # Frame principal dividido en 3 columnas
        self.frame_izquierdo = ctk.CTkFrame(self.container, fg_color=self.color_fondo)
        self.frame_izquierdo.pack(side="left", fill="both", expand=True, padx=10, pady=10)
        
        self.frame_centro = ctk.CTkFrame(self.container, fg_color=self.color_fondo)
        self.frame_centro.pack(side="left", fill="both", expand=True, padx=10, pady=10)
        
        self.frame_derecho = ctk.CTkFrame(self.container, fg_color=self.color_fondo)
        self.frame_derecho.pack(side="left", fill="both", expand=True, padx=10, pady=10)
        
        # Llegadas de mercancias
        self.label_llegadas = ctk.CTkLabel(self.frame_izquierdo, text="LLEGADAS DE MERCANCIAS", font=("Arial", 18, "bold"), text_color=self.color_texto)
        self.label_llegadas.pack(pady=10)
        
        self.caja_proveedor = ctk.CTkEntry(self.frame_izquierdo, placeholder_text="Nombre del proveedor", width=300, height=50, fg_color=self.color_hover, text_color=self.color_texto)
        self.caja_proveedor.pack(pady=5)
        
        self.caja_tiempo_descarga = ctk.CTkEntry(self.frame_izquierdo, placeholder_text="Tiempo de descarga (minutos)", width=300, height=50, fg_color=self.color_hover, text_color=self.color_texto)
        self.caja_tiempo_descarga.pack(pady=5)
        
        self.boton_verificar_calidad = ctk.CTkButton(self.frame_izquierdo, text="Verificar calidad", width=250, height=50, fg_color=self.color_fondo, hover_color=self.color_hover, text_color=self.color_texto)
        self.boton_verificar_calidad.pack(pady=10)
        
        self.text_area_llegadas = ctk.CTkTextbox(self.frame_izquierdo, width=350, height=200, fg_color=self.color_hover, text_color=self.color_texto)
        self.text_area_llegadas.pack(pady=10)
        

        # Almacenamiento por secciones
        self.label_almacen = ctk.CTkLabel(self.frame_centro, text="ALMACENAMIENTO POR SECCIONES", font=("Arial", 18, "bold"), text_color=self.color_texto)
        self.label_almacen.pack(pady=10)
        
        self.boton_area_seca = ctk.CTkButton(self.frame_centro, text="Área Seca", width=200, height=50, fg_color=self.color_Extra, hover_color=self.color_hover, text_color=self.color_texto)
        self.boton_area_seca.pack(pady=5)
        
        self.boton_refrigeracion = ctk.CTkButton(self.frame_centro, text="Refrigeración", width=200, height=50, fg_color=self.color_Extra, hover_color=self.color_hover, text_color=self.color_texto)
        self.boton_refrigeracion.pack(pady=5)
        
        self.boton_congelacion = ctk.CTkButton(self.frame_centro, text="Congelación", width=200, height=50, fg_color=self.color_Extra, hover_color=self.color_hover, text_color=self.color_texto)
        self.boton_congelacion.pack(pady=5)
        
        self.text_area_almacen = ctk.CTkTextbox(self.frame_centro, width=350, height=200, fg_color=self.color_hover, text_color=self.color_texto)
        self.text_area_almacen.pack(pady=10)
        
        # Demanda y pedidos
        self.label_demanda = ctk.CTkLabel(self.frame_derecho, text="DEMANDA DE PRODUCTOS", font=("Arial", 18, "bold"), text_color=self.color_texto)
        self.label_demanda.pack(pady=10)
        
        self.caja_producto = ctk.CTkEntry(self.frame_derecho, placeholder_text="Producto solicitado", width=300, height=50, fg_color=self.color_hover, text_color=self.color_texto)
        self.caja_producto.pack(pady=5)
        
        self.caja_cantidad = ctk.CTkEntry(self.frame_derecho, placeholder_text="Cantidad", width=300, height=50, fg_color=self.color_hover, text_color=self.color_texto)
        self.caja_cantidad.pack(pady=5)
        
        self.boton_pedido = ctk.CTkButton(self.frame_derecho, text="Enviar pedido a bodega", width=250, height=50, fg_color=self.color_fondo, hover_color=self.color_hover, text_color=self.color_texto)
        self.boton_pedido.pack(pady=10)
        
        self.text_area_pedidos = ctk.CTkTextbox(self.frame_derecho, width=350, height=200, fg_color=self.color_hover, text_color=self.color_texto)
        self.text_area_pedidos.pack(pady=10)

        self.frame_inferior = ctk.CTkFrame(self.container, fg_color=self.color_fondo)
        self.frame_inferior.pack(side="bottom", fill="x", padx=10, pady=10)
        
        self.label_inventario = ctk.CTkLabel(self.frame_inferior, text="SISTEMA DE INVENTARIO", font=("Arial", 18, "bold"), text_color=self.color_texto)
        self.label_inventario.pack(pady=5)
        
        self.caja_stock = ctk.CTkEntry(self.frame_inferior, placeholder_text="Stock actual", width=200, height=40, fg_color=self.color_hover, text_color=self.color_texto)
        self.caja_stock.pack(side="left", padx=10, pady=5)
        
        self.caja_punto_reorden = ctk.CTkEntry(self.frame_inferior, placeholder_text="Punto de reorden", width=200, height=40, fg_color=self.color_hover, text_color=self.color_texto)
        self.caja_punto_reorden.pack(side="left", padx=10, pady=5)
        
        self.boton_alerta = ctk.CTkButton(self.frame_inferior, text="Activar alerta proveedor", width=200, height=40, fg_color=self.color_fondo, hover_color=self.color_hover, text_color=self.color_texto)
        self.boton_alerta.pack(side="left", padx=10, pady=5)
        
        self.text_area_inventario = ctk.CTkTextbox(self.frame_inferior, width=500, height=80, fg_color=self.color_hover, text_color=self.color_texto)
        self.text_area_inventario.pack(side="left", padx=10, pady=5)
        
        self.boton_volver = ctk.CTkButton(self.container, text="← Volver", width=100, height=40, fg_color=self.color_fondo, hover_color=self.color_hover, text_color=self.color_texto, corner_radius=25)
        self.boton_volver.pack(side="bottom", anchor="sw", padx=10, pady=10)


if __name__ == "__main__":
    app = BodegaHotel()