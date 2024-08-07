import openpyxl as pd
import pandas as pd

# Inicializar listas para almacenar productos
cantidad = []
producto = []
precio = []

# Cargar productos desde archivo de Excel
try:
    df = pd.read_excel('productos.xlsx')
    for index, row in df.iterrows():
        nombre = row['Nombre']
        cantidad_producto = row['Cantidad']
        precio_producto = row['Precio']
        
        # Agregar el producto al inventario
        cantidad.append(cantidad_producto)
        producto.append(nombre)
        precio.append(precio_producto)
    
    print("Productos agregados al inventario desde archivo de Excel:")
    print(cantidad)
    print(producto)
    print(precio)
except FileNotFoundError:
    print("No se encontró el archivo de Excel 'productos.xlsx'")

# Menú principal
while True:
    print("""
(1) Agregar productos 
(2) Buscar productos
(3) Modificar productos
(4) Ver productos
(5) Salir
""")

    respuesta = int(input("Ingrese su opción: "))
    if respuesta == 1:
        ac = int(input("Ingrese la cantidad de producto: "))
        an = input("Ingrese el nombre de su producto: ")
        apre = int(input("Ingrese el precio de su producto: "))

        cantidad.append(ac)
        producto.append(an)
        precio.append(apre)

    elif respuesta == 2:
        buscar = input("Ingrese el nombre del producto que desea buscar: ")
        if buscar in producto:
            posicion = producto.index(buscar)
            print("La cantidad del producto es: ", cantidad[posicion])
            print("El nombre del producto es: ", producto[posicion])
            print("El precio del producto es: ", precio[posicion])
        else:
            print("Producto no encontrado")

    elif respuesta == 3:
        # Código para modificar productos
        buscar = input("Ingrese el nombre del producto que desea buscar: ")
        if buscar in producto:
            posicion = producto.index(buscar)
        ac = int(input("Ingrese la cantidad de producto: "))
        an = input("Ingrese el nombre de su producto: ")
        apre = int(input("Ingrese el precio de su producto: "))
        cantidad[posicion] = ac
        producto[posicion] = an
        precio[posicion] = apre
        pass

    elif respuesta == 4:
        print("La cantidad es: ", cantidad)
        print("El nombre del producto es: ", producto)
        print("El precio es:", precio)
        # Código para ver productos
        pass

    else:
        print("Opción inválida")
