import datetime

'''
Vamos a crear una padre Factira que tendra como atributos el codigo  de barras, el nombre y el precio del producto 
'''
class Factura:
    '''
    Constructor de la clase Factura que recibe como parametros el codigo de barras, el nombre y el precio del producto
    '''
    def __init__(self, codigo, nombre, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio

    '''
    Creamos el metodo __str__ para poder imprimir los atributos de la clase Factura
    '''
    def __str__(self):
        return "Codigo: " + str(self.codigo) + " Nombre: " + self.nombre + " Precio: " + str(self.precio)
    
    '''
    Crearemos un metodo para almacenar los datos de los produtos en un diccionario de productos
    '''
    def almacenar(self):
        self.productos = {123: ["Leche", 20.50], 1234: ["Pan", 35.00], 12345: ["Huevo", 25.00], 123456: ["Jamon", 50.00]}
        self.productos[self.codigo] = [self.nombre, self.precio]
        return self.productos

    '''
    Creamos un metodo carrito para poder almacenar los productos que el usuario va a comprar con nombre y precio.
    Si el producto no esta en el diccionario de productos, se pide el codigo de barras, el nombre y el precio del producto
    y se agregan al diccionario de productos
    '''
    def carrito(self):
        self.carrito = {}
        self.codigo = int(input("Ingrese el codigo de barras del producto: "))
        if self.codigo in self.productos:
            self.carrito[self.productos[self.codigo][0]] = self.productos[self.codigo][1]
        else:
            self.nombre = input("Ingrese el nombre del producto: ")
            self.precio = float(input("Ingrese el precio del producto: "))
            self.productos[self.codigo] = [self.nombre, self.precio]
            self.carrito[self.nombre] = self.precio
        return self.carrito

    '''
    Creamos un metodo para poder calcular el total de la compra
    '''
    def total(self):
        self.total = 0
        for i in self.carrito.values():
            self.total += i
        return self.total

    
#Inicio del programa
#Agregamos la fecha y hora de la compra
fecha = datetime.datetime.now()
print("Fecha: ", fecha)
print("Bienvenido a Supermercado MezaFresh")

'''
Pedimos al usuario el codigo de barras y buscamos el producto en el diccionario de productos. De estar en el diccionario
se agrega al carrito de compras, de lo contario se pide el nombre y el precio del producto y se agrega al diccionario de
productos y al carrito de compras
'''
codigo = (input("Ingrese el codigo de barras del producto: "))
nombre = ""
precio = 0
productos = Factura.almacenar(Factura(0, "", 0))
carrito = []
total = 0

while codigo != '0':
    if codigo in productos:
        carrito[productos[codigo][0]] = productos[codigo][1]
    else:
        nombre = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        productos[codigo] = [nombre, precio]
        carrito[nombre] = precio
    codigo = str(input("Ingrese el codigo de barras del producto o ingrese 0 para terminar: "))

#Imprimimos el carrito de compras
print("Carrito: ", carrito)
#imprimimos el total de la compra
print("Total: ", sum(carrito.values()))
