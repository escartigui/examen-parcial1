empleados = {}
def menu():
    while True:
        print("MENU")
        print("1.Ingresar")
        print("2.Mostrar")
        print("3.Salir")
        op = int(input("Ingrese su opción"))
        if op == 1:
            cantidad = int(input("Ingrese la cantidad de empleados"))
            for i in range(cantidad):
             print(f"Empleado #{i+1}")
             Id = int(input("Ingrese la ID del empleado"))
             while True:
                 if Id in empleados:
                     print("Ya esta Ingresado")
                     break
                 else:
                    empleados[Id]={}
                    break
             empleados[Id]["nombre"] = input("Ingrese nombre")
             empleados[Id]["Departamento"] = input("Ingrese departamento al que trabaja")
             empleados[Id]["años"] = input("Cuantos años tiene de antigüedad")
             empleados[Id]['evalución'] = {}
             while True:
              puntualidad = int(input("Califique la puntualidad de 1 a 10: "))
              if puntualidad >= 11:
                 print("Debe calificar dentro del rango")
              elif puntualidad <=0:
                 print("Debe calificar dentro del rango")
              else:
                 break
             while True:
              trabajoenequipo = int(input("Califique el trabajo en equipo de 1 a 10"))
              if trabajoenequipo >= 11:
                  print("Debe calificar dentro del rango")
              elif trabajoenequipo <= 0:
                  print("Debe calificar dentro del rango")
              else:
                  break
             while True:
              productividad = int(input("Califique el productividad de 1 a 10"))
              if productividad >=11:
                  print("debe calificar dentro del rango")
              elif productividad <=0:
               print("debe calificar dentro del rango")
              else:
                  break
             observaciones =input("Deja tu comentario para mejorar")
             promedio = puntualidad + trabajoenequipo + productividad % 3
             print(f"el promedio es de {promedio}")
             empleados[Id]["Contacto"] = {}
             telefono = int(input("Ingrese telefono del empleado"))
             correo = input("Ingrese correo del empleado")

        if op == 2:
            print("lISTADO")
            for Id, datos in empleados.items():
             print(f"Nombre {empleados[Id]['nombre']}")



        if op == 3:
            buscado = input("Ingrese busqueda del empleado")
            for Id, buscado in empleados.items():
                print(f"Nombre {empleados[Id]['nombre']}")

menu()