import operacionLogica
import variable

def menu():
    print("¿Qué quieres hacer?\n--------------------\n1.Variable\n2.Operaciones lógicas\n3.Realizar operación lógica")
    opcion_elegida = input()
    elegir_opcion(opcion_elegida)

def elegir_opcion(opcion):
    print("Eligiendo opción...")
    if(opcion=="1"):
        variable.main_variable()
        return
    if(opcion=="2"):
        operacionLogica.main_operacion_logica()
        return
    if(opcion=="3"):
        operacionLogica.realizar_operacion_logica()
        return
    print("\n\nxxxxxxxxxxxxxxxxx\nOpción inválida\nxxxxxxxxxxxxxxxxx\n\n")
    menu()

