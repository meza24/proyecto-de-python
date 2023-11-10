# Librerias
import datetime

# Aquí obtenemos la fecha y hora actual del día
def obtener_fecha_hora_actual():
    fecha_hora_actual = datetime.datetime.now()
    return fecha_hora_actual

'''
    Esta clase servirá para trabajar con todos los métodos que ocupará 
    un sistema de facturas de una tienda de Super Mercado
'''
class Factura():
    '''
    Crearemos un método constructor que tenga como atributos de una factura, como fecha
    y nombre del supermercado. El título se predefinirá como "MEZAFRESH" si no se proporciona.
    '''
    def __init__(self, fecha, titulo="MEZAFRESH"):
        self.titulo = titulo
        self.fecha = fecha

# Aquí vamos a instanciar nuestros objetos
if __name__ == '__main__':
    fecha = obtener_fecha_hora_actual()
    factura1 = Factura(fecha)  # Aquí creamos el primer objeto con el título predefinido
    print(f'Supermercado:{factura1.titulo}\nFecha: {factura1.fecha}')
