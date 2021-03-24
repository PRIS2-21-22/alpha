import operaciones


def menu():
    print("¿Con qué número quieres operar?\n--------------------\n1.Triangular\n2.Trapezoidal")
    numero_operar = input()
    elegir_numero_operar(numero_operar)

def menu_operaciones():
    print("¿Qué quieres hacer?\n--------------------\n1.Suma\n2.Resta\n3.Opuesto\n4.Multiplicación\n5.División")
    opcion_elegida = input()
    elegir_opcion(opcion_elegida)

def elegir_numero_operar(opcion):
    print("Eligiendo tipo de número...")

    if(operaciones.check_value(opcion)==False):
        menu()
        return
    if(opcion=="1"):
        menu_operaciones()
        operaciones.realizar_operaciones(3)
        return
    if(opcion=="2"):
        menu_operaciones()
        operaciones.realizar_operaciones(4)
        return

    print("\n\nxxxxxxxxxxxxxxxxx\nOpción inválida\nxxxxxxxxxxxxxxxxx\n\n")
    menu()
    

def elegir_opcion(opcion):
    if(operaciones.check_value(opcion)==False):
        menu_operaciones()
        return

    if(opcion=="1"):
        operaciones.suma()
        return
    if(opcion=="2"):
        operaciones.resta()
        return
    if(opcion=="3"):
        operaciones.opuesto()
        return
    if(opcion=="4"):
        operaciones.multiplicacion()
        return
    if(opcion=="5"):
        operacionLogica.division()
        return

    print("\n\nxxxxxxxxxxxxxxxxx\nOpción inválida\nxxxxxxxxxxxxxxxxx\n\n")
    menu_operaciones()

