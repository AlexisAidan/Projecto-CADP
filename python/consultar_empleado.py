def consultar(cursor, cursor_desempleados):
    id = input("¿Cual es el ID del empleado que desea consultar?")
    cursor.execute("Select * FROM EMPLEADO WHERE ID = ?", id)
    consulta = cursor.fetchone()
    if consulta:
        print(f"{consulta[1]} {consulta[2]} {consulta[3]} {consulta[5]}")
    else:
        cursor_desempleados.execute("Select * FROM EMPLEADO_ELIMINADO WHERE ID = ?", id)
        consulta = cursor_desempleados.fetchone()
        if consulta:
            print(f"Empleado encontrado en la tabla desempleado: {consulta[1]} {consulta[2]} {consulta[3]} {consulta[4]}")
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