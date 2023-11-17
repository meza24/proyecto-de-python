import datetime
from time import sleep #Libreria para realizar cuenta regresiva

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
        # Se inicializa el diccionario de productos con la lista de productos como base de datos.
        self.productos = {
    123: ["Leche", 2000],
    1234: ["Pan", 2100],
    12345: ["Huevo", 2500],
    123456: ["Arroz", 3100],
    234: ["Azúcar", 1800],
    345: ["Frijoles", 2200],
    456: ["Aceite", 3200],
    567: ["Pasta", 2400],
    678: ["Harina", 2000],
    789: ["Café", 3500],
    890: ["Carne de res", 6000],
    901: ["Pollo", 4500],
    912: ["Pescado", 5500],
    102: ["Plátanos", 1800],
    213: ["Papas", 2300],
    324: ["Cebolla", 2000],
    435: ["Tomate", 2500],
    546: ["Zanahorias", 2100],
    657: ["Mantequilla", 2800],
    768: ["Queso", 3500],
    879: ["Yogur", 2200],
    980: ["Jabón", 2300],
    111: ["Detergente", 2700],
    222: ["Papel higiénico", 3000]
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
            print("El producto no existe en la base de datos.")
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
        print('---------------------------')
        print("Carrito de compras:")
        # Se recorre el diccionario de carrito y se imprime el nombre del producto, el precio unitario y la cantidad.
        for producto, valores in self.carrito.items():
            # Se extrae el precio y la cantidad de la lista de valores. 
            precio = valores[0]
            cantidad = valores[1]
            # Se imprime el nombre del producto, el precio unitario y la cantidad.
            print(f"Producto: {producto}, Precio unitario: {precio}, Cantidad: {cantidad}")
            # Se utiliza la funcion sleep para realizar una cuenta regresiva de 1 segundo entre cada producto.
            sleep(1)

    '''
    Metodo para calcular el total de la compra. Se recorre el diccionario de carrito y se calcula el total de la compra
    sumando el precio unitario por la cantidad de cada producto.
    '''    
    def calcular_total(self):
        total = sum(valores[0] * valores[1] for valores in self.carrito.values())
        print('---------------------------')
        print(f"Total a pagar: {total} colones.")
        print('---------------------------')

'''
Inicio del programa principal donde se crea un objeto de la clase Factura y se llama a los metodos de la clase
'''
# Programa principal
mi_factura = Factura()
fecha = datetime.datetime.now()
print("Fecha: ", fecha)
print("Bienvenido a Supermercado MezaFresh")

# Se inicia un bucle para solicitar código de barras y cantidad hasta que se introduzca '0' para terminar (este es el menu). 
while True:
    # Se utiliza un bloque try-except para manejar errores al ingresar el código de barras y la cantidad.
    try:
        # Se solicita el código de barras y la cantidad.
        codigo = input("Ingrese el código de barras del producto o '0' para terminar: ")
        
        # Si se ingresa '0', se rompe el bucle y termina la entrada de productos.
        if codigo == '0':
            break
        
        # Se convierte el código de barras a entero.
        codigo = int(codigo)
        # Se solicita la cantidad de productos.
        cantidad = int(input("Ingrese la cantidad: "))
        
        # Llamada a la función para agregar el producto al carrito de la factura. 
        mi_factura.agregar_al_carrito(codigo, cantidad)

    # Manejo de errores al ingresar el código de barras y la cantidad.     
    except ValueError:
        print("El código de barras y la cantidad deben ser enteros.")
        # Si hay un error al ingresar el código o cantidad, se solicita nuevamente el código.
        # Esto permite al usuario corregir su entrada.
        continue

'''
Instanciamos el objeto mi_factura de la clase Factura y llamamos a los metodos mostrar_carrito y calcular_total para
mostrar el carrito de compras y el total de la compra respectivamente.
'''
mi_factura.mostrar_carrito()
mi_factura.calcular_total()
print("Gracias por su compra.")