# Funciones de Catálogo de AutoPartesUsuario:
#1
def listaAutoParte(dicAutoPartes):
    print(dicAutoPartes)
    return listaAutoParte

#2 Buscar autoparte nombre/descripción:
def buscarAutopartePorNombre(dicAutoPartes, nombreAutoParte):
    # Convertimos el nombre ingresado a minúsculas para búsqueda sin distinción de mayúsculas
    nombreAutoParte = nombreAutoParte.lower()
    
    # Banderas para identificar si se encuentra o no la autoparte
    encontrada = False

    # Recorremos todas las autopartes en el diccionario
    for autoparte in dicAutoPartes.values():
        # Convertimos la descripción a minúsculas para comparar
        if autoparte["Descripcion"].lower() == nombreAutoParte:
            print(f"Autoparte encontrada: {autoparte['Descripcion']}")
            print(f"Marca: {autoparte['Marca']}")
            print(f"Stock: {autoparte['Stock']}")
            print(f"Precio: ${autoparte['Precio']:.2f}")
            encontrada = True
            break
    
    # Si no se encuentra, mostramos un mensaje
    if not encontrada:
        print("La autoparte no existe o no está en el almacén del local.")
    return 

#3 BuscarAutoParte por Id:
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
    return dicAutoPartes

#4 BuscarAutoParte por Marca:
def buscarAutoParteMarca(dicAutoPartes, nombreDeMarca):
    autoPartesEncontradas = []
    # Convertimos el nombre de marca ingresado a minúsculas para búsqueda sin distinción de mayúsculas
    nombreDeMarca = nombreDeMarca.lower()
    encontradoMarca = False
    for id, detalles in dicAutoPartes.items():
        # Convertimos la descripción a minúsculas para comparar
        if detalles["Marca"].lower() == nombreDeMarca:
            autoPartesEncontradas.append(detalles)
    #Verificar si existen las autopartes
    if autoPartesEncontradas:
        #Mostrar las autopartes existentes
        print(f"Autopartes encontradas para la marca '{nombreDeMarca.capitalize()}':")
        for autoparte in autoPartesEncontradas:
            print(autoparte)
    else:
        # Mostrar un mensaje de error si no se encuentra la marca
        print(f"No se encontraron autopartes para la marca '{marcaBuscada.capitalize()}'.")
#5 Agregar Autoparte (Admin):
# Divide el int en "." para pasarse por float.
def esFlotante(precio):
    partes = precio.split('.')
    return len(partes) == 2 and partes[0].isdigit() and partes[1].isdigit()

# Función para agregar una autoparte
def agregarAutoParte(dicAutoPartes, esFlotante):
    # Solicitar identificación
    identificacion = input("Agregue el número de identificación (solo números): ")
    while not identificacion.isdigit():
        identificacion = input("Agregue un valor válido (solo números): ")
    identificacion = int(identificacion)  # Convertir a entero después de validarlo

    # Solicitar marca de auto
    marcaAuto = input("Agregue el nombre de la marca de la autoparte: ")
    while not marcaAuto.isalpha():
        marcaAuto = input("Agregue un valor válido en letras: ")

    # Solicitar descripción de autoparte (permite letras y números con espacios)
    descripcionAutoParte = input("Agregue la descripción/nombre de la autoparte: ")
    while not descripcionAutoParte.replace(" ", "").isalnum():
        descripcionAutoParte = input("Agregue un valor válido (solo letras y números): ")

    # Solicitar stock disponible
    stockdisponible = input("Agregue la cantidad de stock disponible (solo números): ")
    while not stockdisponible.isdigit():
        stockdisponible = input("Agregue un valor válido (solo números): ")
    stockdisponible = int(stockdisponible)  # Convertir a entero después de validarlo

    # Solicitar precio
    precio = input("Agregue el valor de precio del producto (formato decimal, ej. 299.99): ")
    while not esFlotante(precio):
        precio = input("Agregue un valor válido (número flotante, ej. 299.99): ")
    precio = float(precio)  # Convertir a float después de validarlo

    # Crear nuevo producto
    nuevaAutoParte = {
        "Id": str(identificacion),  # Convertir ID a string para mantener consistencia
        "Marca": marcaAuto,
        "Descripcion": descripcionAutoParte,
        "Stock": stockdisponible,
        "Precio": precio
    }

    # Agregar el nuevo producto al diccionario
    dicAutoPartes[identificacion] = nuevaAutoParte
    return dicAutoPartes
#Funcion para borrar AutoParte
def borrarAutoParte(dicAutoPartes):
    identificacion = input("Ingrese el número de identificación de la autoparte a eliminar: ")

    # Verificar que la identificación sea un número válido
    while not identificacion.isdigit():
        identificacion = input("Ingrese un valor válido (número entero): ")

    identificacion = int(identificacion)  # Convertir a entero

    # Comprobar si la identificación está en el diccionario
    if identificacion in dicAutoPartes:
        # Crear un nuevo diccionario sin la autoparte especificada
        dicAutoPartes = {key: value for key, value in dicAutoPartes.items() if key != identificacion}
        print(f"Autoparte con ID {identificacion} ha sido eliminada.")
    else:
        print(f"No se encontró ninguna autoparte con ID {identificacion}.")

    return dicAutoPartes
#Funcion de modificar Stock de autopartes:
def modificarStock(dicAutoPartes):
    identificacion = input("Ingrese el número de identificación de la autoparte a modificar el stock: ")

    # Verificar que la identificación sea un número válido
    while not identificacion.isdigit():
        identificacion = input("Ingrese un valor válido (número entero): ")

    identificacion = int(identificacion)  # Convertir a entero

    # Comprobar si la identificación está en el diccionario
    if identificacion in dicAutoPartes:
        nuevoStock = input("Ingrese el nuevo stock: ")

        # Validar que el nuevo stock sea un número entero
        while not nuevoStock.isdigit():
            nuevoStock = input("Ingrese un valor válido para el stock (número entero): ")

        # Actualizar el stock de la autoparte
        dicAutoPartes[identificacion]['Stock'] = int(nuevoStock)
        print(f"El stock de la autoparte con ID {identificacion} ha sido modificado a {nuevoStock}.")
    else:
        print(f"No se encontró ninguna autoparte con ID {identificacion}.")

    return dicAutoPartes

# MenuPrincipalUsuario:
def menuPrincipalUsuario(dicAutoPartes, opciones):
   while True:
        print("---------------------------")
        print("MENÚ DEL SISTEMA COMO USUARIO")
        print("---------------------------")
        print("[1] Catálogo de Autopartes (Imprimir Lista de Auto partes, Buscar Autoparte por nombre, Buscar Autoparte por ID, Buscar Autoparte por Marca)")
        print("[2] Opción 2")
        print("[3] Opción 3")
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
#MenuPrincipalAdmin:
def menuPrincipalAdmin(dicAutoPartes,opcionesAdmin):
    while True:
        print("---------------------------")
        print("MENÚ DEL SISTEMA COMO ADMINISTRADOR")
        print("---------------------------")
        print("[1] Catálogo de Autopartes (Imprimir Lista de Auto partes, Buscar Autoparte por: nombre,ID,Marca,Agregar autoparte, borrar autoparte, modificar Stock)")
        print("[2] Opción 2")
        print("[3] Opción 3")
        print("[4] Opción 4")
        print("---------------------------")
        print("[0] Salir del programa")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            submenuCatalogoAutoPartesAdmin(dicAutoPartes)
        elif opcion == "2":
            print("Opcion 2")
        elif opcion == "3":
            # Lógica para listar autopartes
            print("Opcion 3")
        elif opcion == "4":
            # Buscar AutoParte por Marca
            print("Buscando Autoparte/s por su nombre de marca: ")
            nombreDeMarca = input("Ingrese la marca que desea buscar")
            buscarAutoParteMarca(dicAutoPartes, nombreDeMarca)
        elif opcion == "5":
            # Agregar AutoParte
            dicAutoPartes = agregarAutoParte(dicAutoPartes, esFlotante)
            print(dicAutoPartes)
        elif opcion == "6":
            borrarAutoParte(dicAutoPartes)
            print(dicAutoPartes)
            
            
        elif opcion == "0":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Inténtelo de nuevo.")
    
#SubmenuCatalogoAutoPartesUsuario:
def submenuCatalogoAutoPartesUsuario(dicAutoPartes):
    while True:
        print("---------------------------")
        print("SUBMENÚ - Catálogo de Autopartes - USUARIO")
        print("---------------------------")
        print("[1] Lista")
        print("[2] Buscar Autoparte por nombre (Descripción)")
        print("[3] Buscar Autoparte por ID")
        print("[4] Buscar Autoparte por Marca")
        print("---------------------------")
        print("[0] Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("A continuación, se imprimira la lista de autoPartes: ")
            listaAutoParte(dicAutoPartes)
        elif opcion == "2":
            print("Buscar Autoparte por nombre (Descripción")
            nombreAutoParte = input("Ingrese el nombre o descripción de la autoparte que desea buscar: ")
            buscarAutopartePorNombre(dicAutoPartes, nombreAutoParte)
        elif opcion == "3":
            # Lógica para listar autopartes
            print("Buscar Autoparte por ID...")
            idAutoParte = int(input("Ingrese el ID que desea buscar: "))
            buscarAutoParte(dicAutoPartes, idAutoParte)
        elif opcion == "4":
            # Buscar AutoParte por Marca
            print("Buscando Autoparte/s por su nombre de marca: ")
            nombreDeMarca = input("Ingrese la marca que desea buscar")
            buscarAutoParteMarca(dicAutoPartes, nombreDeMarca)
        elif opcion == "0":
            # Vuelve al menú principal
            break
        else:
            print("Opción inválida. Inténtelo de nuevo.")
        
        input("Presione ENTER para volver al submenú.")
#SubmenuCatalogoAutoPartesUsuario
def submenuCatalogoAutoPartesAdmin(dicAutoPartes):
    while True:
        print("---------------------------")
        print("SUBMENÚ - Catálogo de Autopartes - Admin")
        print("---------------------------")
        print("[1] Lista")
        print("[2] Buscar Autoparte por nombre (Descripción)")
        print("[3] Buscar Autoparte por ID")
        print("[4] Buscar Autoparte por Marca")
        print("[5] Agregar Autoparte")
        print("[6] Borrar Autoparte")
        print("[7] Modificar Stock de Autoparte")
        
        print("---------------------------")
        print("[0] Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("A continuación, se imprimira la lista de autoPartes")
            listaAutoParte(dicAutoPartes)
        elif opcion == "2":
            #Logica para buscar autoparte por nombre
            print("Buscar Autoparte por nombre (Descripción")
            nombreAutoParte = input("Ingrese el nombre o descripción de la autoparte que desea buscar: ")
            buscarAutopartePorNombre(dicAutoPartes, nombreAutoParte)
        elif opcion == "3":
            # Lógica para buscar autopartes por ID
            print("Buscar Autoparte por ID...")
            idAutoParte = int(input("Ingrese el ID que desea buscar"))
            buscarAutoParte(dicAutoPartes, idAutoParte)
        elif opcion == "4":
            # Buscar AutoParte por Marca
            print("Buscando Autoparte/s por su nombre de marca: ")
            nombreDeMarca = input("Ingrese la marca que desea buscar")
            buscarAutoParteMarca(dicAutoPartes, nombreDeMarca)
        elif opcion == "5":
            # Logica para agregar autoparte
            dicAutoPartes = agregarAutoParte(dicAutoPartes, esFlotante)
            print("Diccionario actualizado de autopartes:")
            for id_auto, detalles in dicAutoPartes.items():
                print(f"ID: {id_auto}, Detalles: {detalles}")
            print("Autoparte agregada correctamente")
        elif opcion == "6":
            # Logica para borrar autoparte
            dicAutoPartes = borrarAutoParte(dicAutoPartes)
            print("Auto parte borrada exitosamente")            
        elif opcion == "7":
            #Logica para modificar el stock de autoparte
            modificarStock(dicAutoPartes)
            print("Stock modificado correctamente")
            
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
    opcionesAdmin = 4
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
                menuPrincipalAdmin(dicAutoPartes,opcionesAdmin)
                break
            else:
                contador -= 1
                print(f"Contraseña incorrecta. Te quedan {contador} intentos")
                if contador == 0:
                    print("No ingresó ninguna contraseña válida, el programa se cerrará.")
                    exit()
main()

