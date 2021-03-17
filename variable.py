from menuPrincipal import elegirOpcion


import menuPrincipal

def mainVariable():
    print("Cargando menú de variables...")
    print("¿Qué quieres hacer?\n--------------------\n1.Crear variable\n2.Asignar valor a variable\n3.Eliminar variable\n4.Volver atrás")
    opcionElegida = input()
    elegirOpcion(opcionElegida)

def elegirOpcion(opcion):
    print("Eligiendo opción...")
    if(opcion=="1"):
        crearVariable()
        return
    if(opcion=="2"):
        asignarValorAVariable()
        return
    if(opcion=="3"):
        eliminarVariable()
        return
    print("\n\nxxxxxxxxxxxxxxxxx\nOpción inválida\nxxxxxxxxxxxxxxxxx\n\n")
    mainVariable()

def crearVariable():
    print("Ingrese el nombre de la variable")

def asignarValorAVariable():
    print("Seleccione la variable a la que le quiere asignar el valor")

def eliminarVariable():
    print("Indique el número de la variable a eliminar")