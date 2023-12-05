import tkinter as tk
'Para la interfaz gráfica'
from tkinter import filedialog
'Para abrir el explorador de archivos'
import cv2
'Para leer la imagen'
from pyzbar.pyzbar import decode
'Para decodificar el código de barras'
from datetime import datetime
'Para mostrar la fecha y hora actual'

'Clase Factura que contiene los productos, el carrito y los métodos para agregar productos y agregar al carrito'
class Factura:

    ''''
    Constructor de la clase Factura que inicializa los productos y el carrito con los productos que se encuentran en la 
    base de datos y un diccionario vacío respectivamente.
    '''
    def __init__(self):
        self.productos = {
            12345: ["Leche", 1200],
            423123: ["Arroz", 3000],
            312314: ["Atún", 1500],
            234623: ["Avena", 2500],
            823423: ["Cereal", 3100],
            523423: ["Frijoles", 1800],
            723432: ["Galletas Soda", 2100],
            623423: ["Jugo de naranja", 1700],
            111111: ["Palomitas", 2200],
            934522: ["Queque", 4000],
        }
        self.carrito = {}

    '''
    Método que agrega un producto a la base de datos. Recibe como parámetros el código, el nombre y el precio del producto.
    Si el código ya existe en la base de datos, retorna un mensaje de error. Si el código no existe, agrega el producto a la base de datos.
    '''
    def agregar_producto(self, codigo, nombre, precio):
        if codigo in self.productos:
            return "El producto ya existe en la base de datos."
        else:
            self.productos[codigo] = [nombre, precio]
            return "Producto agregado con éxito a la base de datos."

    '''
    Método que agrega un producto al carrito. Recibe como parámetros el código del producto y la cantidad que se desea agregar.
    Si el código existe en la base de datos, agrega el producto al carrito. Si el código no existe, retorna un mensaje de error.
    '''
    def agregar_al_carrito(self, codigo, cantidad):
        if codigo in self.productos:
            nombre, precio = self.productos[codigo]
            if nombre in self.carrito:
                self.carrito[nombre][1] += cantidad
            else:
                self.carrito[nombre] = [precio, cantidad]
            return "Producto agregado al carrito."
        else:
            return "El producto no existe en la base de datos."

    def restar_al_carrito(self, codigo, cantidad):
        if codigo in self.productos:
            nombre, precio = self.productos[codigo]
            if nombre in self.carrito:
                nueva_cantidad = self.carrito[nombre][1] - cantidad
                if nueva_cantidad < 0:
                    return "No se puede restar una cantidad mayor a la que hay en el carrito."
                else:
                    self.carrito[nombre][1] = nueva_cantidad
                return "Producto restado del carrito."
            else:
                return "El producto no está en el carrito."
        else:
            return "El producto no existe en la base de datos."
    '''
    Método que muestra el carrito de compras. Recorre el diccionario carrito y va concatenando los productos, precios y cantidades
    en una variable de tipo string. Retorna la variable. 
    '''
    def mostrar_carrito(self):
        carrito_texto = '---------------------------\nCarrito de compras:\n'
        for producto, valores in self.carrito.items():
            precio = valores[0]
            cantidad = valores[1]
            if cantidad > 0:  # Solo mostrar productos con cantidad mayor a cero
                carrito_texto += f"Producto: {producto}, Precio unitario: {precio}, Cantidad: {cantidad}\n"
        return carrito_texto

    '''
    Método que calcula el total a pagar. Recorre el diccionario carrito y va multiplicando los precios por las cantidades y los va sumando.
    Retorna el total a pagar. 
    '''
    def calcular_total(self):
        total = sum(valores[0] * valores[1] for valores in self.carrito.values())
        return f'---------------------------\nTotal a pagar: {total} colones.\n---------------------------'

    '''
    Método que agrega un producto al carrito a partir de una imagen. Recibe como parámetros la ruta de la imagen y la cantidad que se
    desea agregar. Si la imagen contiene un código de barras, lo decodifica y obtiene el código. Luego, agrega el producto 
    al carrito. Si la imagen no contiene un código de barras, retorna un mensaje de error. 
    '''
    def agregar_desde_imagen(self, ruta_imagen, cantidad):
        try:
            imagen = cv2.imread(ruta_imagen)
            decoded_objects = decode(imagen)
            
            if decoded_objects:
                codigo = int(decoded_objects[0].data.decode('utf-8'))
                return self.agregar_al_carrito(codigo, cantidad)
            else:
                return "No se encontró ningún código de barras en la imagen."
        except cv2.error as e:
            return f"Error en OpenCV: {e}"
        except Exception as e:
            return f"Error: {e}"

    def restar_desde_imagen(self, ruta_imagen, cantidad):
        try:
            imagen = cv2.imread(ruta_imagen)
            decoded_objects = decode(imagen)

            if decoded_objects:
                codigo = int(decoded_objects[0].data.decode('utf-8'))
                nombre, precio = self.productos[codigo]

                if nombre in self.carrito:
                    nueva_cantidad = self.carrito[nombre][1] - cantidad
                    if nueva_cantidad < 0:
                        return "No se puede restar una cantidad mayor a la que hay en el carrito."
                    else:
                        self.carrito[nombre][1] = nueva_cantidad
                    return "Producto restado del carrito."
                else:
                    return "El producto no está en el carrito."
            else:
                return "No se encontró ningún código de barras en la imagen."
        except cv2.error as e:
            return f"Error en OpenCV: {e}"
        except Exception as e:
            return f"Error: {e}"

#Clase InterfazFactura que contiene la interfaz gráfica y los métodos para agregar productos y agregar al carrito 
class InterfazFactura:
    
    '''
    Constructor de la clase InterfazFactura que inicializa la ventana de la interfaz gráfica con sus respectivos widgets.
    '''
    def __init__(self, root):

        self.root = root # Ventana principal de la interfaz gráfica
        self.root.title("Carrito de compras SuperStore") # Título de la ventana principal

        # Configuración de la ventana principal de la interfaz gráfica 
        root.configure(bg="#F5F5DC", padx=20, pady=10, relief=tk.RAISED, bd=10, cursor="hand2", highlightcolor="grey", highlightthickness=5)
        
        self.mi_factura = Factura() # Instancia de la clase Factura 

        self.root.geometry("500x600") # Tamaño de la ventana principal
        self.root.resizable(False, False) # La ventana principal no se puede redimensionar

        self.label = tk.Label(root, text="Carrito de compras SuperStore", font=('Arial', 20), fg="blue") # Label con el título de la ventana principal
        self.label.pack() 

        self.label_fecha = tk.Label(root, text="", font=("Arial", 10), fg="green") # Label con la fecha y hora actual
        self.label_fecha.pack()
        self.mostrar_fecha_actual() # Método que muestra la fecha y hora actual

        # Label y Entry para ingresar la cantidad del producto a agregar manualmente
        self.label_cantidad = tk.Label(root, text="Cantidad:", fg="red", font=('Arial', 10), bg="#F5F5DC")
        self.label_cantidad.pack()

        # Entry para ingresar la cantidad del producto a agregar manualmente
        self.entry_cantidad = tk.Entry(root)
        self.entry_cantidad.pack()



        # Botón que abre el explorador de archivos para seleccionar una imagen 
        self.button_imagen = tk.Button(root, text="Agregar desde Imagen", command=self.agregar_desde_imagen) 
        self.button_imagen.pack()

        # Botón que abre el explorador de archivos para seleccionar una imagen
        self.button_imagen = tk.Button(root, text="Restar desde Imagen", command=self.restar_desde_imagen)
        self.button_imagen.pack()

        # Entry para ingresar el código de barras del producto a agregar manualmente
        self.entry_codigo = tk.Entry(root)
        self.entry_codigo.pack()

        # Label y Entry para ingresar el código de barras y la cantidad del producto a agregar manualmente
        self.label_codigo = tk.Label(root, text="Código de barras:", fg="red", font=('Arial', 10), bg="#F5F5DC")
        self.label_codigo.pack()


        # Botón que agrega un producto al carrito a partir de un código de barras y una cantidad
        self.button_agregar_manualmente = tk.Button(root, text="Agregar Manualmente", command=self.agregar_manualmente)
        self.button_agregar_manualmente.pack()

        # Botón que restar un producto al carrito a partir de un código de barras y una cantidad
        self.button_restar_manualmente = tk.Button(root, text="Restar Manualmente", command=self.restar_manualmente)
        self.button_restar_manualmente.pack()

        # Text para mostrar el carrito de compras 
        self.carrito_text = tk.Text(root, height=10, width=50, bg="white", fg="black", font=('Arial', 10), wrap=tk.WORD, padx=10, pady=10, bd=5, selectbackground="grey")
        self.carrito_text.pack()

        # Botón que muestra el carrito de compras
        self.button_mostrar = tk.Button(root, text="Mostrar Carrito", command=self.mostrar_carrito)
        self.button_mostrar.pack()

        self.button_total = tk.Button(root, text="Calcular Total", command=self.calcular_total)
        self.button_total.pack()

        # Botón que cierra la ventana principal
        self.button_salir = tk.Button(root, text="Salir", command=root.quit)
        self.button_salir.pack()

    '''
    Método que abre el explorador de archivos para seleccionar una imagen. Si la imagen contiene un código de barras, lo decodifica
    y obtiene el código. Luego, agrega el producto al carrito. Si la imagen no contiene un código de barras, retorna un mensaje de error.
    '''
    def agregar_desde_imagen(self):
        ruta_imagen = filedialog.askopenfilename()
        cantidad = self.entry_cantidad.get()

        if cantidad:
            try:
                mensaje = self.mi_factura.agregar_desde_imagen(ruta_imagen, int(cantidad))
                self.mostrar_mensaje(mensaje)
            except ValueError:
                self.mostrar_mensaje("Ingrese una cantidad válida.")
        else:
            self.mostrar_mensaje("Ingrese una cantidad.")

    def restar_desde_imagen(self):
        ruta_imagen = filedialog.askopenfilename()
        cantidad = self.entry_cantidad.get()

        if cantidad:
            try:
                mensaje = self.mi_factura.restar_desde_imagen(ruta_imagen, int(cantidad))
                self.mostrar_mensaje(mensaje)
            except ValueError:
                self.mostrar_mensaje("Ingrese una cantidad válida.")
        else:
            self.mostrar_mensaje("Ingrese una cantidad.")

    '''
    Método que agrega un producto al carrito a partir de un código de barras y una cantidad. Si el código existe en la base de datos,
    agrega el producto al carrito. Si el código no existe, retorna un mensaje de error.
    '''
    def agregar_manualmente(self):
        codigo = self.entry_codigo.get()
        cantidad = self.entry_cantidad.get()

        if codigo and cantidad:
            try:
                codigo_int = int(codigo)
                cantidad_int = int(cantidad)
                mensaje = self.mi_factura.agregar_al_carrito(codigo_int, cantidad_int)
                self.mostrar_mensaje(mensaje)
            except ValueError:
                self.mostrar_mensaje("Ingrese un código de barras y cantidad válidos.")
        else:
            self.mostrar_mensaje("Ingrese un código de barras y cantidad.")

    def restar_manualmente(self):
        codigo = self.entry_codigo.get()
        cantidad = self.entry_cantidad.get()

        if codigo and cantidad:
            try:
                codigo_int = int(codigo)
                cantidad_int = int(cantidad)
                mensaje = self.mi_factura.restar_al_carrito(codigo_int, cantidad_int)
                self.mostrar_mensaje(mensaje)
            except ValueError:
                self.mostrar_mensaje("Ingrese un código de barras y cantidad válidos.")
        else:
            self.mostrar_mensaje("Ingrese un código de barras y cantidad.")
    '''
    Método que muestra el carrito de compras.
    '''
    def mostrar_carrito(self):
        carrito_info = self.mi_factura.mostrar_carrito()
        self.carrito_text.insert(tk.END, carrito_info)

    '''
    Método que calcula el total a pagar.
    '''
    def calcular_total(self):
        total_info = self.mi_factura.calcular_total()
        self.mostrar_mensaje(total_info)


    '''
    Método que muestra un mensaje en el Text. Recibe como parámetro el mensaje a mostrar.
    '''
    def mostrar_mensaje(self, mensaje):
        self.carrito_text.delete(1.0, tk.END)
        self.carrito_text.insert(tk.END, mensaje + '\n')

    '''
    Método que muestra la fecha y hora actual en el Label. 
    '''
    def mostrar_fecha_actual(self):
        # Obtener la fecha actual y darle un formato legible
        fecha_actual = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        # Mostrar la fecha en el Label
        self.label_fecha.config(text=f"Fecha y hora actual: {fecha_actual}")
        # Actualizar cada segundo (opcional)
        self.root.after(1000, self.mostrar_fecha_actual)  # Actualiza cada segundo

'''
Función main que crea la ventana principal de la interfaz gráfica.
'''
if __name__ == "__main__":
    root = tk.Tk()
    interfaz = InterfazFactura(root)
    root.mainloop()