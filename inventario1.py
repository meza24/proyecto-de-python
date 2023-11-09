'''
Axel Alberto Meza Mejias C04845
'''
print('MezaFresh: Tu Supermercado al Alcance'.upper())
#Librerias
import datetime 

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
print(f'Los productos ingresados son los siguientes:\n{productos}.\nGracias por su compra.')

