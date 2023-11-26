================================================================
                    CodeSnake SuperStore
================================================================

Este programa proporciona una interfaz gráfica para gestionar un carrito de compras en una tienda utilizando códigos de barras y la lectura de imágenes.

Repositorio:
El código fuente está disponible en: https://github.com/meza24/proyecto-de-python.git
Para clonar el repositorio:
$ git clone https://github.com/meza24/proyecto-de-python.git

Requisitos:
- Python 3.x
- Bibliotecas necesarias:
  - tkinter
  - OpenCV (cv2)
  - pyzbar

Instalación de las bibliotecas:
$ pip install opencv-python-headless pyzbar

Uso:
1. Ejecuta el programa utilizando Python con el archivo inventario10.py.
2. Acciones disponibles:
   - Agregar productos desde imágenes con códigos de barras.
   - Agregar productos manualmente ingresando códigos de barras y cantidades.
   - Mostrar el contenido del carrito de compras.
   - Calcular el total a pagar.
   - Visualizar la fecha y hora actual.

Ejemplos de Uso:

- Agregar desde Imagen:
  - Seleccionar una imagen con un código de barras válido.
  - Decodificará el código y agregará el producto al carrito.

- Agregar manualmente:
  - Ingresar el código de barras y la cantidad del producto.
  - Se añadirá al carrito si el código es válido.

- Mostrar Carrito:
  - Visualizará una lista detallada de productos en el carrito, con cantidades y precios.

- Calcular Total:
  - Devuelve el monto total a pagar por todos los productos en el carrito.

Funcionalidades Principales:

Factura:
- Administra la base de datos de productos y el carrito de compras.
- Métodos para agregar, visualizar y calcular el total de productos.
- Capacidad para agregar productos desde imágenes con códigos de barras.

InterfazFactura:
- Crea una interfaz gráfica con tkinter.
- Interactúa con la clase Factura de manera amigable.
- Permite agregar productos, visualizar el carrito y obtener el total a pagar.

Autor:
Desarrollado por Axel Meza Mejias, [Eveling y demás compañeros].