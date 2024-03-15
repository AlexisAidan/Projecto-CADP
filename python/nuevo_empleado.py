from datetime import datetime

def crear_nuevo_empleado(cursor, conexion):
   nombre = input("Ingrese nombre del empleado: ")
   apellido = input("Ingrese apellido del empleado: ")
   contraseña = input("Ingrese la contraseña del correo electronico: ")
   fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
   empleado = [nombre, apellido, nombre[0] + apellido + "@mi_empresa.mx", contraseña, fecha_actual]
   cursor.execute("INSERT INTO EMPLEADO VALUES (NULL,?,?,?,?,?)", empleado)

   cursor.execute("Select ID FROM EMPLEADO WHERE NOMBRE_EMPLEADO = ? AND APELLIDO_EMPLEADO = ?", (nombre, apellido))

   consulta = cursor.fetchone()

   print(f"El ID del empleado es: {consulta[0]}")

   conexion.commit()
"""
⠀⠀⠀⠀⠀⠀⠀   ⣀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣀
⠀⠀⠀⠀⠀ ⢀⢄⣾⣿⣿⣿⣿⣿⣿⢿⣿⣟⣿⣿⣿⣿⣿⣿⣷⡢⣀⠀⠀⠀⠀ ⠀⠀
     ⣠⢾⠽⠟⢛⣉⣉⣉⡙⠻⢿⣿⣿⣿⡿⠛⢋⣉⣉⣙⠛⠿⠿⣳⣄⠀⠀ ⠀
   ⢠⢫⣀⠀⣴⣿⣿⣿⣿⡿⣷⡄⠁⣀⠈⣠⣾⣿⣿⣿⢿⣿⣦⠀⣀⡯⡆⠀ ⠀
   ⡨⡯⣾⠐⣟⣏⠀⠴⠈⣿⣿⣿⢀⣿⡀⣿⣿⣧⡏⠀⠖⢸⣿⠀⢟⣞⡕⠀ ⠀
   ⢪⢽⡎⢂⢻⡿⣦⣴⣾⣿⣿⠇⣼⣿⣇⠹⣿⣿⣷⣶⣶⣾⠏⣰⢸⣪⢪⠀ ⠀
   ⠨⡓⠇⣺⢦⣉⠛⠻⠛⢋⣡⠾⠛⠛⠛⠷⣌⠛⠛⠟⠙⣠⣴⣟⠀⢞⡜⠀ ⠀⠀⠀
      ⢁⣾⣿⣿⣺⣿⣿⣿⣿⢄⠀⠀⠀⢀⣿⣿⣿⣿⣿⣽⣿⡟⣀⠀⠀⠀ ⠀
   ⢠⣠⣵⣷⣮⣟⣳⣝⢿⣛⣛⡍⣥⠀⣤⢡⣹⣛⡿⣏⣾⣛⣵⣾⣷⣬⡠⠀ 
   ⣼⣾⢿⣿⢿⣿⣿⣿⣿⣿⣶⣶⣶⣶⣶⣶⣶⣴⣾⣿⣿⣿⣿⣿⣿⢷⣿⣯⣷ 
   ⣿⣾⡿⡿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⢿⣽⢾
"""