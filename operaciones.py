# Función sumar
def sumar(num1,num2):
    num1=convertir(num1)
    num2=convertir(num2)
    if(num1 is False or num2 is False):
        return False
    return num1+num2

# Función restar
def restar(num1,num2):
    num1=convertir(num1)
    num2=convertir(num2)
    if(num1 is False or num2 is False):
        return False
    return num1-num2

# Función multiplicar
def multiplicar(num1,num2):
    num1=convertir(num1)
    num2=convertir(num2)
    if(num1 is False or num2 is False):
        return False
    resultado=0
    for i in range(0,num2):
        resultado+=num1
    return resultado

# Función dividir
def dividir(num1, num2):
    num1=convertir(num1)
    num2=convertir(num2)
    if(num1 is False or num2 is False):
        return False
    resto = num1
    contador = 0
    while resto >= num2:
        resto -= num2
        contador = contador +1
    return contador

# Convierte y si tiene una excepción pues significa que es false  
def convertir(num):
    try:
        num=int(num)
    except ValueError:
        try:
            num=float(num)
        except ValueError:
            return False
    return num