import datetime

'''
Vamos a crear una padre Factura que tendra como atributos el codigo  de barras, el nombre y el precio del producto.
'''
class Factura:

    '''
    Constructor de la clase Factura que contiene los diccionarios de productos y carrito de compras como atributos. Ade
    mas, contiene una lista de productos como base de datos. El diccionario de productos contiene el codigo de barras
    como clave y una lista con el nombre y el precio del producto como valor. El diccionario de carrito se inicializa 
    vacio y se va llenando con el nombre del producto como clave y una lista con el precio y la cantidad como valor.
    '''
    def __init__(self):
        self.productos = {
            123: ["Leche", 20.50],
            1234: ["Pan", 35.00],
            12345: ["Huevo", 25.00],
            123456: ["Jamon", 50.00]
        }
        self.carrito = {}

    '''
    Metodo para agregar un producto al diccionario de productos con el codigo de barras como clave y una lista con el
    nombre y el precio del producto como valor. 
    '''
    def agregar_producto(self, codigo, nombre, precio):
        if codigo in self.productos:
            print("El producto ya existe en la base de datos.")
        else:
            self.productos[codigo] = [nombre, precio]
            print("Producto agregado con éxito.")

    '''
    Metodo para agregar un producto al carrito de compras. Si el codigo de barras esta en el diccionario de productos
    se agrega el producto al carrito de compras, de lo contrario se pide el nombre y el precio del producto y se agrega
    al diccionario de productos y al carrito de compras.
    '''
    def agregar_al_carrito(self, codigo, cantidad):
        if codigo in self.productos:
            nombre, precio = self.productos[codigo]
            if nombre in self.carrito:
                self.carrito[nombre][1] += cantidad
            else:
                self.carrito[nombre] = [precio, cantidad]
            print("Producto agregado al carrito.")
        else:
            nombre = input("Ingrese el nombre del producto: ")
            precio = float(input("Ingrese el precio del producto: "))
            self.productos[codigo] = [nombre, precio]
            self.carrito[nombre] = [precio, cantidad]
            print("Producto agregado al carrito.")

    '''
    Metodo para mostrar los productos en el carrito de compras. Se recorre el diccionario de carrito y se imprime el
    nombre del producto, el precio unitario y la cantidad.
    '''
    def mostrar_carrito(self):
        print("Carrito de compras:")
        for producto, valores in self.carrito.items():
            precio = valores[0]
            cantidad = valores[1]
            print(f"Producto: {producto}, Precio unitario: {precio}, Cantidad: {cantidad}")

    '''
    Metodo para calcular el total de la compra. Se recorre el diccionario de carrito y se calcula el total de la compra
    sumando el precio unitario por la cantidad de cada producto.
    '''    
    def calcular_total(self):
        total = sum(valores[0] * valores[1] for valores in self.carrito.values())
        print(f"Total a pagar: {total}")

'''
Inicio del programa principal donde se crea un objeto de la clase Factura y se llama a los metodos de la clase
'''
# Programa principal
mi_factura = Factura()
fecha = datetime.datetime.now()
print("Fecha: ", fecha)
print("Bienvenido a Supermercado MezaFresh")

'''
Pedimos al usuario el codigo de barras y buscamos el producto en el diccionario de productos. De estar en el diccionario
se agrega al carrito de compras, de lo contario se pide el nombre y el precio del producto y se agrega al diccionario de
productos y al carrito de compras. El ciclo se repite hasta que el usuario ingrese '0'
'''
codigo = input("Ingrese el código de barras del producto o '0' para terminar: ")

'''
Aquí se llama al método agregar_al_carrito de la clase Factura para agregar los productos al carrito de compras y se
pide al usuario el código de barras del producto o '0' para terminar el ciclo. Si el producto ya existe en el carrito
se suma la cantidad, de lo contrario se agrega el producto al carrito de compras y se pide el nombre y el precio del
producto para agregarlo al diccionario de productos y al carrito de compras.
'''
while codigo != '0':
    cantidad = int(input("Ingrese la cantidad: "))
    mi_factura.agregar_al_carrito(int(codigo), cantidad)
    codigo = input("Ingrese el código de barras del producto o '0' para terminar: ")

'''
Instanciamos el objeto mi_factura de la clase Factura y llamamos a los metodos mostrar_carrito y calcular_total para
mostrar el carrito de compras y el total de la compra respectivamente.
'''
mi_factura.mostrar_carrito()
mi_factura.calcular_total()