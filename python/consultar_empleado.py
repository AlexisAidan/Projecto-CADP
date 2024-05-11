from tabulate import tabulate

def consultar(cursor, cursor_desempleados):
    id = input("¿Cuál es el ID del empleado que desea consultar? ")
    cursor.execute("SELECT * FROM EMPLEADO WHERE ID = ?", (id,))
    consulta = cursor.fetchone()
    if consulta:
        titulos = {"ID": consulta[0], "Nombre": consulta[1], "Apellido": consulta[2], "Correo": consulta[3], "Antigüedad": consulta[5], "Estatus": "Activo"}
        datos_persona = [titulos]
        print(tabulate(datos_persona, headers="keys", tablefmt="fancy_grid"))
    else:
        cursor_desempleados.execute("SELECT * FROM EMPLEADO_ELIMINADO WHERE ID = ?", (id,))
        consulta = cursor_desempleados.fetchone()
        if consulta:
            titulos = {"ID": consulta[0], "Nombre": consulta[1], "Apellido": consulta[2], "Correo": consulta[3], "tiempo trabajado": consulta[4], "estatus": "Inactivo"}
            datos_persona = [titulos]
            print(tabulate(datos_persona, headers="keys", tablefmt="fancy_grid"))
        else:
            print("Empleado no encontrado en ninguna tabla.")

"""
⠀⠀⠀⠀⠀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⡀⣯⡭⠀⢟⢿⣷⣄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢠⣼⠏⠴⠶⠈⠘⠻⣘⡆⠀⠀⠀⠀⠀⠀
⠀⠀⣠⣾⡟⠁⡀⠀⠀⠀⡼⠡⠛⡄⠀⠀⠀⠀⠀
⠀⠀⠙⠻⢴⠞⠁⠀⠊⠀⠀⠀⠈⠉⢄⠀⠀⠀⠀
⠀⠀⠀⠀⢀⠀⠀⠀⢃⠄⠂⠀⠀⢀⠞⢣⡀⠀⠀
⠀⠀⠀⠀⡌⠁⠀⠀⠀⢀⠀⠐⠈⠀⠀⡺⠙⡄⠀
⠀⠀⠀⠀⡿⡀⠀⠀⠀⠁⠀⠴⠁⠀⠚⠀⡸⣷⠀
⠀⠀⠀⠀⢹⠈⠀⠀⠀⠀⠔⠁⠀⢀⠄⠀⠁⢻⣧
⠀⠀⠀⠀⣸⠀⢠⣇⠀⢘⣬⠀⠀⣬⣠⣦⣼⣿⠏
⡠⠐⢂⡡⠾⢀⡾⠋⠉⠉⡇⠀⢸⣿⣿⣿⡿⠃⠀
⠉⢉⡠⢰⠃⠸⠓⠒⠂⠤⡇⠀⡿⠟⠛⠁⠀⠀⠀
⠘⢳⡞⣅⡰⠁⠀⠀⠀⢀⠇⠀⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠉⠉⠀⠀⠀⠀⢀⣌⢀⢀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠘⠊⠀⠀⠀⠀⠀⠀⠀
"""
