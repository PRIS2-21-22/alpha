from menuPrincipal import elegirOpcion


import menuPrincipal

def main_variable():
    print("Cargando menú de variables...")
    print("¿Qué quieres hacer?\n--------------------\n1.Crear variable\n2.Asignar valor a variable\n3.Eliminar variable\n4.Volver atrás")
    opcionElegida = input()
    elegir_opcion(opcionElegida)

def elegir_opcion(opcion):
    print("Eligiendo opción...")
    if(opcion=="1"):
        crear_variable()
        return
    if(opcion=="2"):
        asignar_valor_variable()
        return
    if(opcion=="3"):
        eliminar_variable()
        return
    print("\n\nxxxxxxxxxxxxxxxxx\nOpción inválida\nxxxxxxxxxxxxxxxxx\n\n")
    main_variable()

def crear_variable():
    print("Ingrese el nombre de la variable")

def asignar_valor_variable():
    print("Seleccione la variable a la que le quiere asignar el valor")

def eliminar_variable():
    print("Indique el número de la variable a eliminar")