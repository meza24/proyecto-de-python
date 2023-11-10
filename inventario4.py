'''
Axel Alberto Meza Mejias C04845
'''

'''En esta actualizacion, hemos creado tres funciones: imprimir_fecha_hora(), agregar_productos(),
y imprimir_carrito(). La función main() coordina el flujo del programa. Esto hace que el código sea más organizado y 
más fácil de entender.
'''
import datetime
from time import sleep

#Esta es la funcion que se encargara de imprimir la fecha y hora actual
def imprimir_fecha_hora():
    fecha_hora_actual = datetime.datetime.now()
    print(fecha_hora_actual)

#Esta funcion se encarga de agregar los productos y los precios hasta que el usuario digite 'listo'
def agregar_productos():
    productos = {}
    ingreso_producto = ''

    while ingreso_producto.lower() != 'listo':
        if ingreso_producto:
            precio = float(input('Ingrese el precio del producto: '))
            productos[ingreso_producto] = precio
            print(productos)
        print('------------------------------------------------------------------')
        ingreso_producto = input('Ingrese un nuevo producto o escriba listo para terminar: ')
    
    return productos


#Esta funcion se encargara de imprimir los productos y los precios.
def imprimir_carrito(productos):
    print('------------------------------------------------------------------')
    print('Los productos agregados al carrito de compras son: ')
    total = sum(productos.values())
    
    for producto, precio in productos.items():
        print(f'{producto}-------------${precio}')
        sleep(1)
    
    print('-------------')
    print(f'Total -------------${total}')
    print('Gracias por su compra.')

#Esta funcion se encargara de llamar todas las funciones necesarias para desplegar la info final en pantalla
def main():
    print('MezaFresh: Tu Supermercado al Alcance'.upper())
    imprimir_fecha_hora()
    productos = agregar_productos()
    imprimir_carrito(productos)

if __name__ == "__main__":
    main()
