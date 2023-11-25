# Sistema de Facturación con Lectura de Códigos de Barras

Este programa implementa un sistema básico de facturación que permite la lectura de códigos de barras desde imágenes. Utiliza la librería `pyzbar` para decodificar los códigos de barras.

## Instalación de Librerías

Antes de ejecutar el programa, asegúrate de tener las siguientes librerías instaladas en tu entorno de Python:

- **pyzbar**: Para instalar, utiliza el comando `pip install pyzbar` en Windows o `pip3 install pyzbar` en Linux.
- **datetime**: Para instalar, utiliza el comando `pip install datetime` en Windows o `pip3 install datetime` en Linux.
- **time**: No es necesario instalarlo, ya que es parte de la biblioteca estándar de Python.

## Uso del Programa

1. **Ejecución del Script**:
    - Ejecuta el script `inventario.py`.
2. **Opciones del Programa**:
    - **'imagen'**: Permite escanear códigos de barras desde una imagen.
    - **'manual'**: Permite introducir manualmente el código de barras.
    - **'0'**: Termina el programa.
3. **Instrucciones de Uso**:
    - Sigue las indicaciones para escanear o introducir manualmente códigos de barras y las cantidades correspondientes.
4. **Resultados**:
    - El programa mostrará el carrito de compras con los productos agregados y el total a pagar.

## Funcionalidades Principales

- **Clase Factura**: Contiene métodos para:
    - Agregar productos al inventario.
    - Agregar productos al carrito desde imágenes o manualmente.
    - Mostrar el contenido del carrito de compras.
    - Calcular el total a pagar.
- **Agregar desde Imagen**: Permite la lectura de códigos de barras desde una imagen.
- **Agregar Manualmente**: Permite la introducción manual de códigos de barras y detalles del producto.

## Ejemplo de Uso

```bash
python inventario.py
