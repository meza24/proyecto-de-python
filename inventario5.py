class Factura:
    '''
    Esta clase servirá para trabajar con todos los métodos que se utilizarán
    en un sistema de facturas de un supermercado.
    '''
    tiene_id = True
    tiene_nombre = True
    tiene_precio = True

# Aquí vamos a instanciar nuestros objetos
if __name__ == '__main__':
    
    factura1 = Factura()  # Aquí creamos el primer objeto

    # Verificamos si la clase factura1 tiene nombre, id y precio 
    print(factura1.tiene_nombre)
    print(factura1.tiene_precio)
    print(factura1.tiene_id)
