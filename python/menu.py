def mostrar_menu():
    print("\n╔══════════════════════════╗")
    print("║         Menú             ║")
    print("╠══════════════════════════╣")
    print("║ 1. Dar de alta empleado  ║")
    print("║ 2. Modificar empleado    ║")
    print("║ 3. Eliminar empleado     ║")
    print("║ 4. Consultar empleado    ║")
    print("║ 0. Salir                 ║")
    print("╚══════════════════════════╝")

    Opcion = input()
    if Opcion.isdigit():
        return int(Opcion) 
    else: 
        return 0