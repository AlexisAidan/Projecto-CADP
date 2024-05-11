import random
import string
from consultar_empleado import consultar

def mostrar_menu_modificar_empleado():
    print("\n╔══════════════════════════════════════════════════╗")
    print("║                 Menú de Opciones                  ║")
    print("╠═══════════════════════════════════════════════════╣")
    print("║ 1. Cambiar Nombre                                 ║")
    print("║ 2. Cambiar Apellido                               ║")
    print("║ 3. Cambiar Nombre y Apellido                      ║")
    print("║ 4. Cambiar Contraseña de Correo Electrónico       ║")
    print("║ 0. Salir                                          ║")
    print("╚═══════════════════════════════════════════════════╝")

def modificar_empleado(cursor, conexion):

    opcion_modificar_empleado = int(input("Seleccione una opción: "))
    
    if opcion_modificar_empleado < 0 or opcion_modificar_empleado > 4:
        print("Numero fuera del rango")
    
    while (1 <= opcion_modificar_empleado <= 4):
        id = int(input("¿Cual es el ID del empleado que desea modificar su informacion? "))
        if opcion_modificar_empleado == 1:
            nombre = input("Ingrese el nuevo nombre del empleado: ")
            
            datos = {"ID":id,
                    "NOMBRE_EMPLEADO": nombre}
            cursor.execute("UPDATE EMPLEADO SET NOMBRE_EMPLEADO = :NOMBRE_EMPLEADO WHERE ID = :ID", datos)
            conexion.commit()

        elif opcion_modificar_empleado == 2:
            apellido = input("Ingrese el nuevo apellido del empleado: ")

            datos = {"ID":id,
                    "APELLIDO_EMPLEADO": apellido}
            cursor.execute("UPDATE EMPLEADO SET APELLIDO_EMPLEADO = :APELLIDO_EMPLEADO WHERE ID = :ID", datos)
            conexion.commit()

        elif opcion_modificar_empleado == 3:
            nombre = input("Ingrese el nuevo nombre del empleado: ")
            apellido = input("Ingrese el nuevo apellido del empleado: ")

            datos = {"ID":id,
                "NOMBRE_EMPLEADO": nombre,
                "APELLIDO_EMPLEADO": apellido}
            cursor.execute("UPDATE EMPLEADO SET NOMBRE_EMPLEADO = :NOMBRE_EMPLEADO WHERE ID = :ID", datos)
            cursor.execute("UPDATE EMPLEADO SET APELLIDO_EMPLEADO = :APELLIDO_EMPLEADO WHERE ID = :ID", datos)
            conexion.commit()

        elif opcion_modificar_empleado == 4:
            contraseña = generar_contrasena_aleatoria(12)

            datos = {"ID": id,
                     "CONTRASEÑA_CORREO":contraseña}
            print(f"Su nueva contraseña es: {datos["CONTRASEÑA_CORREO"]} ")
            cursor.execute("UPDATE EMPLEADO SET CONTRASEÑA_CORREO = :CONTRASEÑA_CORREO WHERE ID = :ID", datos)
            conexion.commit()
        
        else: print("Error")

        break


def generar_contrasena_aleatoria(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = ''.join(random.choice(caracteres) for i in range(longitud))
    
    return contrasena

"""
⣿⣿⣿⣿⣿⣿⣿⡿⠟⠋⠉⢁⣀⣀⣀⡈⠉⠛⢿⡿⠿⢿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠏⢀⣴⣾⣿⣿⣿⣿⣿⡟⠃⢀⣀⣤⣤⣄⠉⢿⣿
⣿⣿⣿⣿⣿⡏⠀⣾⣿⣿⣿⣿⣿⣿⠏⠀⣴⣿⣿⣿⣯⣻⣧⠀⢻
⣿⣿⣿⣿⣿⠁⢸⣿⣿⣿⣿⣿⣿⣿⠀⠸⣿⣿⣿⣿⣿⣿⣿⡇⠈
⣿⣿⣿⣿⡏⠀⣼⣿⣿⣿⣿⣿⣿⣿⣧⠀⠹⢿⣿⣿⣿⡿⠟⠀⣼
⣿⣿⣿⡿⠇⠀⠛⠿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣀⡈⠉⠀⠀⣴⣿⣿
⣿⡿⠁⣀⢠⢤⣤⠀⠀⠉⢀⠀⠀⠈⠉⠻⢿⣿⣿⣿⡇⠀⣿⣿⣿
⡟⠀⣴⣽⣷⣷⠆⠀⣴⣾⣿⣔⡳⢦⡄⣄⣠⣿⣿⣿⡇⠀⣿⣿⣿
⠀⢰⣿⣿⣿⠇⠀⣼⣿⣿⣿⣿⣿⣷⣶⣿⣿⣿⣿⣿⣿⠀⢻⣿⣿
⠀⠸⣾⣿⣿⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⢸⣿⣿
⣧⠀⠻⢿⣿⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⢸⣿⣿
⣿⣷⣤⣀⣈⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⠟⠙⣿⣿⣿⡏⠀⣼⣿⣿
⣿⣿⣿⣿⣿⡇⠀⣄⠀⠙⠛⠿⠿⠛⠁⢀⣼⣿⣿⣿⡇⠀⣿⣿⣿
⣿⣿⣿⣿⣿⣷⡀⠘⠿⠶⠀⢀⣤⣤⡀⠙⢿⣿⣿⡿⠁⢰⣿⣿⣿
⢻⣿⣿⣿⣿⣿⣿⣦⣤⣤⣴⣿⣿⣿⣷⣄⣀⠈⠁⣀⣠⣿⣿⣿⣿
⣹⣿⣿⣿⡿⢋⣩⣬⣩⣿⠃⣿⣿⣿⣿⢸⣿⡿⢋⣡⣬⣩⣿⣿⣿
⡗⣿⣿⣿⣧⣈⣛⠛⠻⣿⠀⣿⣿⣿⡿⢸⣿⣧⣈⣛⠛⠻⣿⣿⣿
⣿⣿⣿⣿⠹⣿⣿⡿⠂⣿⣇⠸⣿⣿⠃⣼⣿⠻⣿⣿⡿⠀⣿⣿⣿
⣿⣿⣿⣿⣶⣤⣤⣴⣾⣿⣿⣶⣤⣤⣾⣿⣿⣶⣤⣤⣴⣾⣿⣿⣿
"""
