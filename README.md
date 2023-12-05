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

Pasos para la ejecución desde la terminal:
Para correr el código desde la terminal se deben seguir los siguientes pasos:

1. Abrir la terminal: Command Prompt en Windows (símbolo de sistema o PowerShell), Terminal en macOS o Linux.
2. Navegar hasta el directorio donde se encuentra tu archivo Python: usando el comando cd (change directory). Por ejemplo, si tu archivo está en el escritorio y estás en el directorio de inicio, podrías escribir cd Escritorio en Windows.
3. Ejecutar el archivo de Python: utiliza el comando python seguido del nombre de tu archivo. Por ejemplo, para un archivo llamado mi_script.py, escribe python mi_script.py y presiona Enter. Si estás utilizando Python 3, es posible que necesites escribir python3 en lugar de python. También puedes escribir directamente la versión de Python más el directorio, por ejemplo, python3 /home/usuario1/Descargas/inventario12.py.

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
