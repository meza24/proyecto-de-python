
#Forked By Ec0dek

# Librerias
from datetime import datetime


#Definimos el nombre del mercado como constante
SUPER_NOMBRE = "MEZAFRESH"


#Creamos la clase para crear una factura
class Factura:
    def __init__(self, titulo, fecha, productos:dict) -> None:
        self.titulo = titulo
        self.fecha = fecha
        self.productos = productos
        
    def Create(self):
        product_list = ""
        for producto, cantidad in self.productos.items():
            product_list += f"{producto} x{cantidad["Cantidad"]}\n"
            
        return f"{self.titulo}\n{self.fecha}\n\n{product_list}"
        
        
# lista de productos con el formato del "inventario1.py"
productos = {"Manzana": {"Cantidad": 1}}

#inciamos la instancia
if __name__ == "__main__":
    date = datetime.today()
    factura = Factura(SUPER_NOMBRE, date, productos)
    print("---------------------------------------------------")
    print(factura.Create())
