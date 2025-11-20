
inventario = []

def pedirNombre():
    return input("Ingrese el nombre del producto: \n")

def pedirPrecio(nombre):
    return(float(input(f"Ingrese el precio de {nombre}: \n")))

def pedirCantidad(nombre):
    return int(input(f"Ingresa la cantidad de {nombre} \n"))

def pedirBuscar():
    return input("Ingrese el producto que quiere buscsar: \n")

def pedirCambiar():
    return input("Ingresa el producto que quieres cambiarle el precio y cantida:\n")

def pedirNuevoPrecio():
    return float(input("Ingresa el nuevo precio: \n"))

def pedirNuevaCantida():
    return int(input("Ingresa la nueva cantida: \n"))



def agregar(nombre,precio,cantidad):
    if buscar(nombre) != True:
        print(f"{nombre} No esta en el inventario")
        inventario.append({"nombre": nombre,"precio":precio,"cantidad":cantidad})
        return inventario
    else:
        print(f"""{nombre} Si esta en el inventario\n
Ingresa un producto que no este \n""")


def mostar():
    if not inventario:
        print("El inventario esta vacio")

    else:
        print("Este es el inventario:")
        for i in inventario:
            print(f""" \n
    {i}""")
        return

def buscar(busqueda):
    for producto in inventario:
        if producto["nombre"] == busqueda:
            return True,producto
    return False, None

def actulizar(producto,nuevoPrecio,nuevoCantidad):

    for i in inventario:
        if i["nombre"] == producto:
            i["precio"] = nuevoPrecio
            i["cantidad"] = nuevoCantidad

def eliminar(nombre):
    for i in inventario:
        if i["nombre"] == nombre:
            inventario.remove(i)
            print(f"Producto {nombre} eliminado.")
            break











while True:
    print("""Menú principal
1. Agregar 
2. Mostrar 
3. Buscar 
4. Actualizar 
5. Eliminar 
6. Estadísticas 
7. Guardar CSV 
8.Cargar CSV 
9. Salir""")
    
    obcion = input("Ingrese el numero de la opcion que quieres hacer: \n")

    if obcion == "1":
        nombre = pedirNombre()
        precio = pedirPrecio(nombre)
        cantidad = pedirCantidad(nombre)
        agregar(nombre,precio,cantidad)
        mostar()

    elif obcion == "2":
        mostar()

    elif obcion == "3":
        busqueda = pedirBuscar()
        if buscar(busqueda) == True:
            print(f"El producto {busqueda} Si esta\n")

        else:
            print(f"El producto {busqueda} No esta\n")
        
    
    elif obcion == "4":
        if not inventario:
            print("El inventario esta vacio")
        
        else:
            cambiar = pedirCambiar()
            encontrado,producto = buscar(cambiar)
            if not encontrado:
                print(f"El producto {cambiar} No esta en el inventario")
            else:
                print(f"Producto encontrado:{cambiar}")
                nuevoPrecio = pedirNuevoPrecio()
                nuevaCantidad = pedirNuevaCantida
                actulizar(cambiar,nuevoPrecio,nuevaCantidad)


    # elif obcion == "5":
    #     eliminar()

    # elif obcion == "6":
    #     estadisticas()

    # elif obcion == "7":
    #     guardar()

    # elif obcion == "8":
    #     cargar()

    elif obcion == "9":
        break