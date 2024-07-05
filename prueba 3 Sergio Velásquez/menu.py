import os
import globales
import ventas



def menu():
    while True:
        print("1. Asignar montos aleatorios.")
        print("2. Ver estadísticas.")
        print("3. Salir del programa.")

        opcion = globales.seleccionar_opcion(3)

        if opcion == 1:
            os.system("cls")
            print("1. Asignar montos aleatorios.")
            ventas.valores_aleatorios()
            print("Valores asignados de manera aleatoria a todos los productos e iva incluido. Listo!")


        elif opcion == 2:
            os.system("cls")
            print("2. Ver estadísticas.")
            print("A continuacion lás estadisticas de: \nProducto con valor más alto. \nProducto con valor del IVA más bajo. \nPromedio del valor de los productos. \nMedia geométrica del valor de los productos.")
            ventas.ver_estadisticas()
            

        elif opcion == 3:
            print("3. Salir del programa.")
            return

        input()

if __name__ == "__main__":
    menu()