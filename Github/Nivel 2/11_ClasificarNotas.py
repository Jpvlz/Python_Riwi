
listaNotas = []

def Imprimir ():
    print(f"\nTu nota es:\n")
    for i, nota in enumerate(listaNotas, start = 1):
        print(f"Nota {i}. {nota}")
    return

def CalcularPromedio ():
    suma = sum(listaNotas)
    if suma >= 0 and suma <= 49:
        promedio = "Reprobado"
        print(f"""Tus notas son {Imprimir ()}
Tu promedio es {suma} - {promedio}""")
    return

while True:
    nota = float(input("Ingresa una nota:\n"))
    listaNotas.append(nota)
    opcion = int(input("""\nDesea Ingresar otra nota?
Ingrese 1 para continuar
Ingrese 2 para salir
Ingrese 3 para imprimir las notas
Ingrese 4 para ver la calificacion\n"""))
    if opcion == 2:
        Imprimir()
        break

    if opcion == 3:
        Imprimir()


    if opcion == 4:
        CalcularPromedio()
