import datetime

# Obtiene la fecha y hora actual del día
def obtener_fecha_hora_actual():
    fecha_hora_actual = datetime.datetime.now()
    return fecha_hora_actual

'''
    Esta clase servirá para trabajar con todos los métodos que usará 
    un sistema de facturación de una tienda de supermercado.
'''
class Factura:
    '''
    Constructor que define los atributos de una factura, como la fecha
    y el nombre del supermercado. El título se predefinirá como "MEZAFRESH" si no se proporciona.
    '''
    def __init__(self, fecha, titulo="MEZAFRESH"):
        self.titulo = titulo
        self.fecha = fecha

'''
    Clase para gestionar una base de datos de productos
    con su número de código de barras (UPC), nombre y precio.
'''
class Productos:
    def __init__(self):
        self.lista_productos = [{'upc': '123456789', 'nombre': 'Arroz', 'precio': 15.99}]
        self.carrito = []

    '''
    Esta función agrega productos a una lista de compras. 
    Solicita al usuario el código de barras del producto, 
    busca en la lista de productos de la base de datos.
    Si el producto no está registrado, solicita al usuario 
    el nombre y el precio para agregarlo a la lista de productos.
    '''
    def agregar_al_carrito(self, upc):
        for producto in self.lista_productos:
            if producto['upc'] == upc:
                print('Agregado al carrito.')
                self.carrito.append(producto)
                return

        print('Producto no encontrado en la base de datos.')
        nombre = input('Ingresa el nombre del producto: ')
        precio = float(input('Ingresa el precio del producto: '))
        nuevo_producto = {'upc': upc, 'nombre': nombre, 'precio': precio}
        self.lista_productos.append(nuevo_producto)
        self.carrito.append(nuevo_producto)
        print('Producto agregado a la base de datos y al carrito.')

if __name__ == '__main__':
    fecha = obtener_fecha_hora_actual()

    factura1 = Factura(fecha)
    print(f'Supermercado: {factura1.titulo}\nFecha: {factura1.fecha}')

    producto1 = Productos()
    while True:
        upc_usuario = input('Ingresa el UPC del producto a agregar al carrito o escribe "listo" para terminar la compra: ')
        
        if upc_usuario.lower() == 'listo':
            break
        
        producto1.agregar_al_carrito(upc_usuario)
    
    print('Carrito:', producto1.carrito)
