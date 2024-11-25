# Función para mostrar el menú
def mostrar_menu():
   opcion=0
   while(opcion<1 or opcion>5):
      print("1- sumar, 2- restar, 3- multiplicar, 4-dividir y 5- salir")
      opcion = int(input("¿Qué opción elige? "))
   return opcion

# Función para mostrar la opcción
def opcion(opcion):
   num1=0
   num2=0
   while((num1<1 or num1>4) or (num2<1 or num2>4)):
    num1 = int(input("¿Cuál es el primer número 1? "))
    num2 = int(input("¿Cuál es el primer número 2? "))
   match opcion:
      case 1:
         solucion=operaciones.sumar(num1,num2)
      case 2:
         solucion=operaciones.restar(num1,num2)
      case 3:
         solucion=operaciones.multiplicar(num1,num2)
      case 4:
         solucion=operaciones.dividir(num1,num2)
   if(opcion!=5):
      print(f"La solución es {solucion}")
      mostrar_menu()
