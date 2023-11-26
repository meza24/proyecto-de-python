import tkinter as tk
from tkinter import filedialog
import cv2 
from pyzbar.pyzbar import decode 
from datetime import datetime

class Factura:
    def __init__(self):
        self.productos = {
            5901234123457: ["Leche", 2000],
            1234: ["Pan", 2100],
            12345: ["Huevo", 2500],
            222: ["Papel higiénico", 3000]
        }
        self.carrito = {}

    def agregar_producto(self, codigo, nombre, precio):
        if codigo in self.productos:
            return "El producto ya existe en la base de datos."
        else:
            self.productos[codigo] = [nombre, precio]
            return "Producto agregado con éxito a la base de datos."

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

    def mostrar_carrito(self):
        carrito_texto = '---------------------------\nCarrito de compras:\n'
        for producto, valores in self.carrito.items():
            precio = valores[0]
            cantidad = valores[1]
            carrito_texto += f"Producto: {producto}, Precio unitario: {precio}, Cantidad: {cantidad}\n"
        return carrito_texto

    def calcular_total(self):
        total = sum(valores[0] * valores[1] for valores in self.carrito.values())
        return f'---------------------------\nTotal a pagar: {total} colones.\n---------------------------'

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

class InterfazFactura:
    def __init__(self, root):

        
        self.root = root
        self.root.title("CodeSnake SuperStore")

        root.configure(bg="#F5F5DC", padx=10, pady=10, relief=tk.RAISED, bd=10, cursor="hand2", highlightcolor="grey", highlightthickness=5)
        
        self.mi_factura = Factura()

        self.root.geometry("500x520")
        self.root.resizable(False, False)

        self.label = tk.Label(root, text="CodeSnake SuperStore", font=('Arial', 20), fg="blue")
        self.label.pack()

        self.label_fecha = tk.Label(root, text="", font=("Arial", 10), fg="green")
        self.label_fecha.pack()
        self.mostrar_fecha_actual()


        self.button_imagen = tk.Button(root, text="Agregar desde Imagen", command=self.agregar_desde_imagen)
        self.button_imagen.pack()

        self.label_codigo = tk.Label(root, text="Código de barras:", fg="red", font=('Arial', 10), bg="#F5F5DC")
        self.label_codigo.pack()

        self.entry_codigo = tk.Entry(root)
        self.entry_codigo.pack()

        self.label_cantidad = tk.Label(root, text="Cantidad:", fg="red", font=('Arial', 10), bg="#F5F5DC")
        self.label_cantidad.pack()

        self.entry_cantidad = tk.Entry(root)
        self.entry_cantidad.pack()

        self.button_agregar_manualmente = tk.Button(root, text="Agregar Manualmente", command=self.agregar_manualmente)
        self.button_agregar_manualmente.pack()

        self.carrito_text = tk.Text(root, height=10, width=50, bg="white", fg="black", font=('Arial', 10), wrap=tk.WORD, padx=10, pady=10, bd=5, selectbackground="grey")
        self.carrito_text.pack()

        self.button_mostrar = tk.Button(root, text="Mostrar Carrito", command=self.mostrar_carrito)
        self.button_mostrar.pack()

        self.button_total = tk.Button(root, text="Calcular Total", command=self.calcular_total)
        self.button_total.pack()

        self.button_salir = tk.Button(root, text="Salir", command=root.quit)
        self.button_salir.pack()

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

    def mostrar_carrito(self):
        carrito_info = self.mi_factura.mostrar_carrito()
        self.carrito_text.insert(tk.END, carrito_info)

    def calcular_total(self):
        total_info = self.mi_factura.calcular_total()
        self.mostrar_mensaje(total_info)

    def mostrar_mensaje(self, mensaje):
        self.carrito_text.delete(1.0, tk.END)
        self.carrito_text.insert(tk.END, mensaje + '\n')

    def mostrar_fecha_actual(self):
        # Obtener la fecha actual y darle un formato legible
        fecha_actual = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        # Mostrar la fecha en el Label
        self.label_fecha.config(text=f"Fecha y hora actual: {fecha_actual}")
        # Actualizar cada segundo (opcional)
        self.root.after(1000, self.mostrar_fecha_actual)  # Actualiza cada segundo

if __name__ == "__main__":
    root = tk.Tk()
    interfaz = InterfazFactura(root)
    root.mainloop()