'''
Axel Alberto Meza Mejias C04845

Forked by Ec0dek
'''
print('MezaFresh: Tu Supermercado al Alcance'.upper())
#Librerias
from datetime import datetime

#Se imprime la fecha actual
date = datetime.today()
print(date)

products = {}
ready = False

# Funcion para añadir productos al diccionario products
def add_item(key):
    if key in list(products.keys()):
        products[key]["Cantidad"] += 1
    else:
        products[key] = {"Cantidad": 1}


# instancia
while not ready:
    producto = input('Ingrese un nuevo producto o escriba "listo" para terminar: ')
    print('------------------------------------------------------------------')
    
    if producto.lower() == "listo":
        ready = True
    else:
        add_item(producto.lower())
        print(products)

print('------------------------------------------------------------------')
print(f'Los productos ingresados son los siguientes:\n{products}.\nGracias por su compra.')
