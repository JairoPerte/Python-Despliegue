import operaciones

# Función para mostrar el menú
def mostrar_menu():
   opcion=0
   while(opcion<1 or opcion>8):
      print("1- sumar, 2- restar, 3- multiplicar, 4-dividir, 5- salir, 6- factorial(recursivo) y 8- fibonacci(recursivo)")
      opcion = int(input("¿Qué opción elige? "))
   opciones(opcion)

# Función para mostrar la opcción
def opciones(opcion):
   if(opcion!=5):
      num1 = input("¿Cuál es el primer número? ")
      if(opcion!=6 and opcion!=8):
         num2 = input("¿Cuál es el segundo número? ")
   match opcion:
      case 1:
         solucion=operaciones.sumar(num1,num2)
      case 2:
         solucion=operaciones.restar(num1,num2)
      case 3:
         solucion=operaciones.multiplicar(num1,num2)
      case 4:
         if(num2 != "0"):
            solucion=operaciones.dividir(num1,num2)
      case 6:
         solucion=operaciones.factorial(num1)
         solucion=operaciones.factorial_iterativo(num1)
      case 8:
         solucion=operaciones.fibonacci();

   if(opcion != 5):
      try:
         if(solucion != False):
            print(f"La solución es {solucion}")
         else:
            if(opcion is 6):
               print("El número no es positivo o entero")
            else:
               print("Alguno de los números no son enteros o floats")
      except NameError:
            print("El divisor no puede ser 0")
      mostrar_menu()
