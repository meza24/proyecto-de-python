'''
Axel Alberto Meza Mejias C04845
'''

'''Esta actualizacion se agregan diccionarios en lugar de listas para agregar productos y precios.
Ademas, se pasa de diccionario a tupla para iterar sobre cada clave y valor e imprimir en pantalla
Tambien se agrega el totatl del los productos utilizando la funcion de obtener valores de un diccionario
'''
print('MezaFresh: Tu Supermercado al Alcance'.upper())
#Librerias
import datetime #Libreria para importar fecha
from time import sleep #Libreria para realizar cuenta regresiva

#Aqui se imprime la fecha y hora actual del dia
fecha_hora_actual = datetime.datetime.now()
print(fecha_hora_actual)

productos = {}

#Tenemos que agregar un nuevo valor precio
ingreso_producto = ''
precio = 0

while ingreso_producto.lower() != 'listo':

    if ingreso_producto:
        precio = float(input('Ingrese el presio del producto: ')) #Agregamos una nueva captura de datos para los precios de los productos
        productos[ingreso_producto ] = precio
        print(productos)

    print('------------------------------------------------------------------')
    ingreso_producto = input('Ingrese un nuevo producto o escriba listo para terminar: ')


print('------------------------------------------------------------------')
print('Los productos agregados al carrito de compras son: ')
total = sum(productos.values())

for producto, precio in productos.items(): #Aqui convertimos la lista 'productos' en tupla para poder iterar sobre ella por clave y valor
    print(f'{producto}-------------${precio}')
    sleep(1)
