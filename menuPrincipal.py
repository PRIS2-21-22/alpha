import operacionLogica
import variable

def menu():
    print("¿Qué quieres hacer?\n--------------------\n1.Variable\n2.Operaciones lógicas\n3.Realizar operación lógica")
    opcionElegida = input()
    elegirOpcion(opcionElegida)

def elegirOpcion(opcion):
    print("Eligiendo opción...")
    if(opcion=="1"):
        variable.mainVariable()
        return
    if(opcion=="2"):
        operacionLogica.mainOperacionLogica()
        return
    if(opcion=="3"):
        operacionLogica.realizarOperacionLogica()
        return
    print("\n\nxxxxxxxxxxxxxxxxx\nOpción inválida\nxxxxxxxxxxxxxxxxx\n\n")
    menu()

