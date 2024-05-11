def eliminar_empleado(cursor, cursor_desempleado, conexion, conexion_desempleados):
    id = input("¿Cual es el ID del empleado que desea eliminar?")
    cursor.execute("SELECT ID, NOMBRE_EMPLEADO, APELLIDO_EMPLEADO, CORREO_EMPLEADO, TIEMPO_EMPLEADO FROM EMPLEADO WHERE ID = ?", (id,))
    empleado = cursor.fetchone()
    if empleado:
        cursor_desempleado.execute("INSERT INTO EMPLEADO_ELIMINADO (ID, NOMBRE_EMPLEADO, APELLIDO_EMPLEADO, CORREO_EMPLEADO, TIEMPO_EMPLEADO) VALUES (?, ?, ?, ?, ?)", empleado)
        cursor.execute("DELETE FROM EMPLEADO WHERE ID = ?", (id,))
        conexion_desempleados.commit()
        conexion.commit()
        print("El empleado ha sido eliminado y movido a la tabla EMPLEADO_ELIMINADO")
    else:
        print("No se encontró ningún empleado con ese ID.")

    