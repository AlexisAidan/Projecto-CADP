from datetime import datetime

def crear_nuevo_empleado(cursor, conexion):
   nombre = input("Ingrese nombre del empleado: ")
   apellido = input("Ingrese apellido del empleado: ")
   correo = str(nombre[0] + apellido + "@mi_empresa.mx")
   contraseña = input("Ingrese la contraseña del correo electronico: ")
   fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
   
   empleado = {
      "ID": None,
      "NOMBRE_EMPLEADO": nombre,
      "APELLIDO_EMPLEADO": apellido,
      "CORREO_EMPLEADO": correo,
      "CONTRASEÑA_CORREO": contraseña,
      "TIEMPO_EMPLEADO": fecha_actual
    }

   #cursor.execute("INSERT INTO EMPLEADO VALUES (NULL,?,?,?,?,?)", empleado)
   cursor.execute("INSERT INTO EMPLEADO VALUES (:ID, :NOMBRE_EMPLEADO, :APELLIDO_EMPLEADO, :CORREO_EMPLEADO, :CONTRASEÑA_CORREO, :TIEMPO_EMPLEADO)", empleado)

   cursor.execute("Select ID FROM EMPLEADO WHERE CORREO_EMPLEADO = ?", (correo,))

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