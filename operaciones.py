variable1 = []
variable2 = []

def realizar_operaciones(numero):
    asignar_variables(numero)

def suma():
    print("Realizando suma...")

def resta():
    print("Realizando resta...")

def opuesto():
    print("Realizando opuesto...")

def multiplicacion():
    print("Realizando multiplicación...")

def division():
    print("Realizando división...")

def asignar_variables(numero):
    print("Asignando variables...")
    
    for x in range(len(variable1), numero):
        print("Ingresando en el primer borroso el valor número: ", x+1)
        entrada = input()
        if(check_value(entrada)==False):
            print("Valor incorrecto")
            asignar_variables(numero)
            return
        variable1.append(entrada)
    for y in range(len(variable2), numero):
        print("Ingresando en el segundo borroso el valor número: ", y+1)
        entrada = input()
        if(check_value(variable2[y])==False):
            print("Valor incorrecto")
            asignar_variables(numero)
            return
        variable2.append(entrada)


def check_value(es_un_numero):
    try:
        int(es_un_numero)
        return True
    except ValueError:
        try:
            float(es_un_numero)
            return True
        except ValueError:
            return False
    return True
