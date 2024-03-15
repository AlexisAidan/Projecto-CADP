import sqlite3
from menu import mostrar_menu
from nuevo_empleado import crear_nuevo_empleado
from modificar_empleado import *
from consultar_empleado import consultar
from eliminar_empleado import eliminar_empleado

Conexion = sqlite3.connect("Base de datos empleados")
Cursor = Conexion.cursor()
Cursor.execute('''
                CREATE TABLE IF NOT EXISTS EMPLEADO (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                NOMBRE_EMPLEADO VARCHAR(20),
                APELLIDO_EMPLEADO VARCHAR(20),
                CORREO_EMPLEADO VARCHAR(30) UNIQUE,
                CONTRASEÑA_CORREO VARCHAR(20),
                TIEMPO_EMPLEADO DATETIME DEFAULT CURRENT_TIMESTAMP)
                ''')

Conexion_Desempleados = sqlite3.connect("Base de datos desempleados")
Cursor_Desempleados = Conexion_Desempleados.cursor()
Cursor_Desempleados.execute('''
                CREATE TABLE IF NOT EXISTS EMPLEADO_ELIMINADO (
                ID INTEGER UNIQUE,
                NOMBRE_EMPLEADO VARCHAR(20),
                APELLIDO_EMPLEADO VARCHAR(20),
                CORREO_EMPLEADO VARCHAR(30) UNIQUE,
                TIEMPO_EMPLEADO DATETIME DEFAULT CURRENT_TIMESTAMP)
                ''')

while True:
    Opcion = mostrar_menu()
    Indice = 0

    if Opcion == 1:
        crear_nuevo_empleado(Cursor, Conexion)
        continue
    elif Opcion == 2:
        mostrar_menu_modificar_empleado()
        modificar_empleado(Cursor, Conexion)
        continue
    elif Opcion == 3:
        eliminar_empleado(Cursor, Cursor_Desempleados, Conexion ,Conexion_Desempleados)
        continue
    elif Opcion == 4:
        consultar(Cursor, Cursor_Desempleados)
        continue
    else:
        break

Conexion.close()
Conexion_Desempleados.close()