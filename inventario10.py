'''
En este programa se utiliza la librería pyzbar para leer códigos de barras desde una imagen. 
Para instalar la librería pyzbar se utiliza el comando pip install pyzbar (en Windows) o pip3 install pyzbar (en Linux).
Para instalar la librería datetime se utiliza el comando pip install datetime (en Windows) o pip3 install datetime (en Linux).
Para instalar la librería time se utiliza el comando pip install time (en Windows) o pip3 install time (en Linux).
'''
import cv2 
from pyzbar.pyzbar import decode 
import datetime 
from time import sleep 


'''
Se crea la clase Factura con los atributos productos y carrito. El atributo productos es un diccionario que contiene
los productos en el inventario. El atributo carrito es un diccionario que contiene los productos en el carrito de compras.
'''
class Factura:
    '''
    El metodo __init__ es el constructor de la clase Factura. Se inicializan los atributos productos y carrito. El atributo
    productos es un diccionario que contiene los productos en el inventario. El atributo carrito es un diccionario que
    contiene los productos en el carrito de compras. 
    '''
    def __init__(self):
        self.productos = {
            5901234123457: ["Leche", 2000],
            1234: ["Pan", 2100],
            12345: ["Huevo", 2500],
            # ... (otros productos)
            222: ["Papel higiénico", 3000]
        }
        self.carrito = {}

    '''
    El metodo agregar_producto agrega un producto al diccionario de productos. El codigo de barras es la clave y una lista
    con el nombre y el precio del producto es el valor. Si el codigo de barras ya existe en el diccionario de productos
    se imprime un mensaje de error, de lo contrario se agrega el producto al diccionario de productos. 
    '''
    def agregar_producto(self, codigo, nombre, precio):
        if codigo in self.productos:
            print("El producto ya existe en la base de datos.")
        else:
            self.productos[codigo] = [nombre, precio]
            print("Producto agregado con éxito a la base de datos.")

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
    El metodo mostrar_carrito muestra los productos en el carrito de compras. Se recorre el diccionario de carrito y se
    imprime el nombre del producto, el precio unitario y la cantidad. 
    '''
    def mostrar_carrito(self):
        print('---------------------------')
        print("Carrito de compras:")
        for producto, valores in self.carrito.items():
            precio = valores[0]
            cantidad = valores[1]
            print(f"Producto: {producto}, Precio unitario: {precio}, Cantidad: {cantidad}")
            sleep(1)

    '''
    El metodo calcular_total calcula el total de la compra. Se recorre el diccionario de carrito y se calcula el total
    de la compra sumando el precio unitario por la cantidad de cada producto. 
    '''
    def calcular_total(self):
        total = sum(valores[0] * valores[1] for valores in self.carrito.values())
        print('---------------------------')
        print(f"Total a pagar: {total} colones.")
        print('---------------------------')

    '''
    El metodo agregar_desde_imagen agrega un producto al carrito de compras leyendo el codigo de barras desde una imagen. 
    '''
    def agregar_desde_imagen(self, ruta_imagen):

        '''Atajo para leer el codigo de barras desde una imagen. Se utiliza la funcion decode de la libreria pyzbar.
        La funcion decode recibe como parametro una imagen y retorna una lista de objetos decodificados. Cada objeto
        decodificado es una instancia de la clase Decoded. El atributo data de la clase Decoded contiene el codigo de
        barras como una cadena de texto.
        '''
        try:
            imagen = cv2.imread(ruta_imagen)
            decoded_objects = decode(imagen)
            
            if decoded_objects:
                codigo = decoded_objects[0].data.decode('utf-8')
                cantidad = int(input("Ingrese la cantidad: "))
                self.agregar_al_carrito(int(codigo), cantidad)
            else:
                print("No se encontró ningún código de barras en la imagen.")

        except Exception as e:
            print(f"Error: {e}")

    '''
    El metodo agregar_manualmente_al_carrito agrega un producto al carrito de compras introduciendo el codigo de barras
    manualmente. 
    '''
    def agregar_manualmente_al_carrito(self):
        while True:
            try:
                codigo = int(input("Ingrese el código de barras o '0' para terminar: "))

                if codigo == 0:
                    break

                if codigo in self.productos:
                    cantidad = int(input("Ingrese la cantidad: "))
                    self.agregar_al_carrito(codigo, cantidad)
                else:
                    print("El código de barras no existe en la base de datos.")
                    nombre = input("Ingrese el nombre del producto: ")
                    precio = float(input("Ingrese el precio del producto: "))
                    self.agregar_producto(codigo, nombre, precio)
                    cantidad = int(input("Ingrese la cantidad: "))
                    self.agregar_al_carrito(codigo, cantidad)

            except ValueError:
                print("Ingrese un código de barras válido.")

# Programa principal donde se crea un objeto de la clase Factura y se llama a los metodos de la clase 
mi_factura = Factura()
fecha = datetime.datetime.now()
print("Fecha: ", fecha)
print("Bienvenido a Supermercado MezaFresh")

'''
Se inicia un bucle para solicitar código de barras y cantidad hasta que se introduzca '0' para terminar (este es el menu).'''
while True:
    opcion = input("Ingrese 'imagen' para escanear desde una imagen, 'manual' para introducir manualmente el código o '0' para terminar: ")

    if opcion == '0':
        break

    if opcion == 'imagen':
        ruta_imagen = input("Ingrese la ruta de la imagen: ")
        mi_factura.agregar_desde_imagen(ruta_imagen)

    elif opcion == 'manual':
        mi_factura.agregar_manualmente_al_carrito()

    else:
        print("Opción no válida. Ingrese 'imagen', 'manual' o '0' para terminar.")

'''
Se llama a los metodos mostrar_carrito y calcular_total para mostrar los productos en el carrito de compras y el total
de la compra. 
'''
mi_factura.mostrar_carrito()
mi_factura.calcular_total()
print("Gracias por su compra.")