'''
Axel Alberto Meza Mejias C04845
'''

#Esta actualizacion contiene la cuenta regresiva de la lista

print('MezaFresh: Tu Supermercado al Alcance'.upper())
#Librerias
import datetime #Libreria para importar fecha
from time import sleep #Libreria para realizar cuenta regresiva

#Aqui impromimos la fecha y hora actual del dia
fecha_hora_actual = datetime.datetime.now()
print(fecha_hora_actual)

productos = []

ingreso_producto = ''

while ingreso_producto.lower() != 'listo':

    if ingreso_producto:
        productos.append(ingreso_producto)
        print(productos)

    print('------------------------------------------------------------------')
    ingreso_producto = input('Ingrese un nuevo producto o escriba listo para terminar: ')


print('------------------------------------------------------------------')
print('Los productos agregados al carrito de compras son: ')
for producto in productos:
    print(producto)
    sleep(1)
print('Gracias por su compra.')