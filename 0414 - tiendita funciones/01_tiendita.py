def menu():
    print("")
    print("-------------------------------------")
    print("1. Mostrar productos")
    print("2. Mostrar el carrito")
    print("3. Agregar al carrito")
    print("4. Borrar un producto del carrito")
    print("5. Cantidad a pagar")
    print("6. Salir")
    print("")
    opcion = int(input("Opción: "))
    print("")
    return opcion

def mostrar_productos(l_productos, l_precio):
    tamano = len(l_productos)
    # print("No.      Nombre       Precio")
    print("{:<5s}{:<15s}{:>8s}".format("No.", "Nombre", "Precio"))
    for i in range(tamano):
        print("{:<5d}{:<15s}{:>8.2f}".format(i + 1, l_productos[i], l_precio[i]))


def mostrar_carrito (l_productos,l_precio, c_cantidad, c_producto):
    tamano = len(c_producto)
    print("----  Carrito ----------")
    print("{:<5s}{:<15s}{:>8s}{:>10s}".format("No.", "Nombre", "Precio", "Cantidad"))
    # print("No.      Nombre         Precio         Cantidad")
    for i in range(tamano):
        # print(i+1,". ", lista_productos[ carrito_producto[i] ],"  ",lista_precio[ carrito_producto[i] ], "   ", carrito_cantidad[i])
        print("{:<5d}{:<15s}{:>8.2f}{:>10d}".format(i + 1, l_productos[c_producto[i]], l_precio[c_producto[i]], c_cantidad[i]))


def agregar_al_carrito():

    mostrar_productos(lista_productos, lista_precio)

    print("------------------------")
    num_producto = int(input("Ingresa el número del prodcto a agregar: "))
    cant_producto = int(input("Cuantos articulos quieres de este producto: "))
    carrito_producto.append(num_producto - 1)
    carrito_cantidad.append(cant_producto)


# Lista de los productos
lista_productos = ["papas", "refrescos", "tortillas", "jamon", "mazapan"]
# Lista de los precios
lista_precio =    [12,      10.5,         20,         40,  5,]
# Lista del carrito con los productos
carrito_producto = []
# Lista de la cantidad en cada producto
carrito_cantidad = []

# Opción del menu
opcion = 0

# Mientras la opción  no sea igual a 6 repetir el menu
# Mientras la opción sea diferente a 6 repetir el menu
while opcion != 6:

    opcion = menu()

    if opcion == 1:
        mostrar_productos(lista_productos, lista_precio)
    elif opcion == 2:
        mostrar_carrito(lista_productos, lista_precio, carrito_cantidad, carrito_producto)
    elif opcion == 3:
        agregar_al_carrito()
    elif opcion == 4:
        tamano = len(carrito_producto)
        print("----  Carrito ----------")
        print("No.     Nombre      Precio       Cantidad")
        for i in range(tamano):
            print(i+1,". ", lista_productos[ carrito_producto[i] ],"    ",lista_precio[ carrito_producto[i] ], "   ", carrito_cantidad[i])
        print("------------------------")
        # Leemos el numero del carrito a borrar
        num_producto = int(input("Ingresa el número del producto a borrar: "))
        # Sustituir por un 0 el valor del articulo a borrar
        carrito_producto[ num_producto-1 ] = -1
        carrito_cantidad[ num_producto-1 ] = -1
        # Removerlo de la lista del carrito
        carrito_producto.remove(-1)
        carrito_cantidad.remove(-1)

    elif opcion == 5:
        total = 0.0
        tamano = len(carrito_producto)
        for i in range(tamano):
            total = total + lista_precio[ carrito_producto[i] ] * carrito_cantidad[i]
        print("La cantidad total a pagar es: ", total)
        print("----------------------------------------")

    elif opcion == 6:
        print("Gracias por usar el programa")
    else:
        print("La opción no existe.")








