import operaciones

# Función para mostrar el menú
def mostrar_menu():
   opcion=0
<<<<<<< HEAD
   while(opcion<1 or opcion>8):
      print("1- sumar, 2- restar, 3- multiplicar, 4-dividir, 5- salir, 6- factorial(recursivo) y 8- fibonacci(recursivo)")
=======
   while(opcion<1 or opcion>7):
      print("1- sumar, 2- restar, 3- multiplicar, 4-dividir, 5- salir, 6- Factorial iterativo y 7- factorial(recursivo)")
>>>>>>> 2e390b1ed86496b5daf3f1dcab51ea0fd2663e0a
      opcion = int(input("¿Qué opción elige? "))
   opciones(opcion)

# Función para mostrar la opcción
def opciones(opcion):
   if(opcion!=5):
<<<<<<< HEAD
      num1 = input("¿Cuál es el primer número? ")
      if(opcion!=6 and opcion!=8):
         num2 = input("¿Cuál es el segundo número? ")
=======
      num1 = input("Dame un número ")
      if(opcion!=6 and opcion!=7):
         num2 = input("Dame otro número ")
>>>>>>> 2e390b1ed86496b5daf3f1dcab51ea0fd2663e0a
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
         solucion=operaciones.factorial_iterativo(num1)
<<<<<<< HEAD
      case 8:
         solucion=operaciones.fibonacci(num1)
=======
      case 7:
         solucion=operaciones.factorial(num1)
>>>>>>> 2e390b1ed86496b5daf3f1dcab51ea0fd2663e0a

   if(opcion != 5):
      try:
         if(solucion != False):
            print(f"La solución es {solucion}")
         else:
<<<<<<< HEAD
            if(opcion is 6 or opcion is 8):
=======
            if(opcion is 6 or opcion is 7):
>>>>>>> 2e390b1ed86496b5daf3f1dcab51ea0fd2663e0a
               print("El número no es positivo o entero")
            else:
               print("Alguno de los números no son enteros o floats")
      except NameError:
            print("El divisor no puede ser 0")
      mostrar_menu()
