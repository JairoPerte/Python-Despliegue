# Función sumar
def sumar(num1,num2):
    if (type(num1) is int or type(num1) is float) and (type(num2) is int or type(num2) is float):
        return num1+num2
    else:
        return False

# Función restar
def restar(num1,num2):
    if (type(num1) is int or type(num1) is float) and (type(num2) is int or type(num2) is float):
        return num1-num2
    else:
        return False

# Función multiplicar
def multiplicar(num1,num2):
    if (type(num1) is int or type(num1) is float) and (type(num2) is int or type(num2) is float):
        resultado=0
        for i in range(1,num2):
            resultado+=num1
        return resultado
    else:
        return False


def dividir(num1, num2):
    if ((type(num1) is int or type(num1) is float) and (type(num2) is int or type(num2) is float) and num2 != 0):
        resto = num1
        contador = 0
        while resto >= num2:
            resto -= num2
            contador = contador +1
        return contador
    else:
        return False


