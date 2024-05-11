import sqlite3
from menu import mostrar_menu
from nuevo_empleado import crear_nuevo_empleado
from modificar_empleado import *
from consultar_empleado import consultar
from eliminar_empleado import eliminar_empleado
from concurrent.futures import ThreadPoolExecutor

def inicializar_base_de_datos_empleados():
    try:
        global Conexion
        global Cursor
        Conexion = sqlite3.connect("Base de datos empleados", check_same_thread=False)
        Cursor = Conexion.cursor()
        Cursor.execute('''
                        CREATE TABLE EMPLEADO (
                        ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        NOMBRE_EMPLEADO VARCHAR(20),
                        APELLIDO_EMPLEADO VARCHAR(20),
                        CORREO_EMPLEADO VARCHAR(30) UNIQUE,
                        CONTRASEÑA_CORREO VARCHAR(20),
                        TIEMPO_EMPLEADO DATETIME DEFAULT CURRENT_TIMESTAMP)
                        ''')
    except sqlite3.OperationalError: 
        Conexion = sqlite3.connect("Base de datos empleados")
        Cursor = Conexion.cursor()

def inicializar_base_de_datos_desempleados():
    try: 
        global Conexion_Desempleados
        global Cursor_Desempleados
        Conexion_Desempleados = sqlite3.connect("Base de datos desempleados", check_same_thread=False)
        Cursor_Desempleados = Conexion_Desempleados.cursor()
        Cursor_Desempleados.execute('''
                        CREATE TABLE EMPLEADO_ELIMINADO (
                        ID INTEGER UNIQUE,
                        NOMBRE_EMPLEADO VARCHAR(20),
                        APELLIDO_EMPLEADO VARCHAR(20),
                        CORREO_EMPLEADO VARCHAR(30) UNIQUE,
                        TIEMPO_EMPLEADO DATETIME DEFAULT CURRENT_TIMESTAMP)
                        ''')
    except sqlite3.OperationalError: 
        Conexion_Desempleados = sqlite3.connect("Base de datos desempleados")
        Cursor_Desempleados = Conexion_Desempleados.cursor()

def main():
    while True:
        Opcion = mostrar_menu()

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
        elif Opcion == 0:
            break
        else:
            print("Esa opción no es valida")

    Conexion.close()
    Conexion_Desempleados.close()

executor = ThreadPoolExecutor(max_workers=1)
executor.submit (inicializar_base_de_datos_empleados)
executor.submit(inicializar_base_de_datos_desempleados)
executor.submit(main)