# Funciones de Catálogo de AutoPartes:
#1
def listaAutoParte(dicAutoPartes):
    print(dicAutoPartes)
    return listaAutoParte
#2
def buscarAutoParte(dicAutoPartes, idAutoParte):
    if idAutoParte in dicAutoPartes:
        autoparte = dicAutoPartes[idAutoParte]
        print(f"Autoparte con id: {dicAutoPartes[idAutoParte]}")
        print(f"Autoparte encontrada: {autoparte['Descripcion']}")
        print(f"Marca: {autoparte['Marca']}")
        print(f"Stock: {autoparte['Stock']}")
        print(f"Precio: ${autoparte['Precio']:.2f}")
    else:
        print("La autoparte no existe o no está en el almacén del local.")

# Funciones:
def menuPrincipalUsuario(dicAutoPartes, opciones):
   while True:
        print("---------------------------")
        print("MENÚ DEL SISTEMA")
        print("---------------------------")
        print("[1] Catálogo de Autopartes (Agregar, Modificar, Listar, Eliminar, Modificar Stock)")
        print("[2] Opción 2")
        print("[3] Opción 3")
        print("[4] Opción 4")
        print("---------------------------")
        print("[0] Salir del programa")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            submenuCatalogoAutoPartesUsuario(dicAutoPartes)
        elif opcion == "0":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Inténtelo de nuevo.")

def submenuCatalogoAutoPartesUsuario(dicAutoPartes):
    while True:
        print("---------------------------")
        print("SUBMENÚ - Catálogo de Autopartes")
        print("---------------------------")
        print("[1] Lista")
        print("[2] Buscar Autoparte por nombre (Descripción)")
        print("[3] Buscar Autoparte por ID")
        print("[4] Buscar Autoparte por Marca")
        print("[5] Modificar Stock")
        print("---------------------------")
        print("[0] Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("A continuación, se imprimira la lista de autoPartes")
            listaAutoParte(dicAutoPartes)
        elif opcion == "2":
            # Lógica para modificar autoparte
            print("Buscar Autoparte por nombre (Descripción")
        elif opcion == "3":
            # Lógica para listar autopartes
            print("Buscar Autoparte por ID...")
            idAutoParte = int(input("Ingrese el ID que desea buscar"))
            buscarAutoParte(dicAutoPartes, idAutoParte)
        elif opcion == "4":
            # Lógica para eliminar autoparte
            print("Eliminar Autoparte...")
        elif opcion == "5":
            # Lógica para modificar stock
            print("Modificar Stock...")
        elif opcion == "0":
            # Vuelve al menú principal
            break
        else:
            print("Opción inválida. Inténtelo de nuevo.")
        
        input("Presione ENTER para volver al submenú.")


def main():
    # Diccionarios:
    dicAutoPartes = {100: {"Id": "100", "Marca": "Toyota", "Descripcion": "Filtro de aire", "Stock": 150, "Precio": 300.50}, 
                 101: {"Id": "101", "Marca": "Ford", "Descripcion": "Bujía de encendido", "Stock": 250, "Precio": 120.75}, 
                 102: {"Id": "102", "Marca": "Chevrolet", "Descripcion": "Pastillas de freno", "Stock": 200, "Precio": 450.00}, 
                 103: {"Id": "103", "Marca": "Honda", "Descripcion": "Aceite de motor", "Stock": 500, "Precio": 60.30}, 
                 104: {"Id": "104", "Marca": "Volkswagen", "Descripcion": "Filtro de combustible", "Stock": 300, "Precio": 80.99}, 
                 105: {"Id": "105", "Marca": "Nissan", "Descripcion": "Amortiguador", "Stock": 120, "Precio": 1200.99}, 
                 106: {"Id": "106", "Marca": "BMW", "Descripcion": "Batería", "Stock": 75, "Precio": 950.75}, 
                 107: {"Id": "107", "Marca": "Audi", "Descripcion": "Llanta", "Stock": 80, "Precio": 850.60}, 
                 108: {"Id": "108", "Marca": "Mercedes-Benz", "Descripcion": "Espejo retrovisor", "Stock": 45, "Precio": 300.40}, 
                 109: {"Id": "109", "Marca": "Hyundai", "Descripcion": "Radiador", "Stock": 130, "Precio": 1100.20}, 
                 110: {"Id": "110", "Marca": "Kia", "Descripcion": "Faro delantero", "Stock": 90, "Precio": 450.00}}
    
    
    # Variables:
    contrasenias = [1234, 1111, 1414]
    contador = 3
    opciones = 4

    print("Entrando al programa...")
    userOrAdmin = input("Ingrese un valor para ingresar al sistema: U = Usuario, A = Admin, o 0 para salir: ")
    
    while userOrAdmin not in ["U", "A", "0"]:
        print("Error, ingrese un valor válido: U = Usuario, A = Admin, o 0 para salir del programa")
        userOrAdmin = input("Ingrese un valor para ingresar al sistema: U = Usuario, A = Admin, o 0 para salir: ")
    
    if userOrAdmin == "U":
        print("Bienvenido: Usuario")
        menuPrincipalUsuario(dicAutoPartes, opciones)
        return
    
    elif userOrAdmin == "A":
        print("Introduzca la contraseña")
        while contador > 0:
            contrasenia = int(input("Ingrese la contraseña: "))
            if contrasenia in contrasenias:
                print("Bienvenido admin")
                menuPrincipalUsuario(opciones, dicAutoPartes)
                break
            else:
                contador -= 1
                print(f"Contraseña incorrecta. Te quedan {contador} intentos")
                if contador == 0:
                    print("No ingresó ninguna contraseña válida, el programa se cerrará.")
                    exit()
main()
