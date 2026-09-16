import random

def menu():
    print("=" * 8 + " JUEGO  BOT NET " + "=" * 8)
    print("1. Comenzar")
    print("2. Salir")
    print("=" * 32)

def solicitar_opcion():
    while True:
        try:
            return int(input("Seleccione una opcion: "))
        except:
            print("Error. Eliga un numero valido.\n")

def solicitar_rango_de_opciones(rango: list):
    while True:
        try:
            opcion = int(input("Tu respuesta: "))
            if opcion in rango:
                return opcion
            else:
                print("Error. Ingrese un numero entre las opciones.")
        except:
            print("Error. Ingrese un numero valido.")

def juego():
    # vida
    seguridad = 100
    # loop externo, nodos (3)
    for nodo in range(1, 4):
        # nivel de amenaza segun el nodo actual
        match nodo:
            case 1:
                nivel_amenaza = random.randint(100, 300)
            case 2:
                nivel_amenaza = random.randint(200, 400)
            case _:
                nivel_amenaza = random.randint(300, 500)
        # inicio de combate
        print(f"\n=== INICIANDO COMBATE CONTRA NODO {nodo} ===")
        print("NIVEL DE AMENAZA:", nivel_amenaza)
        turno = 1
        nodo_neutralizado = False
        # loop interno, turnos
        while turno <= 10 and not nodo_neutralizado and seguridad > 0:
            print(f"\n=== TURNO {turno}/10 - NODO {nodo}/3 ===")
            numero_defensa = random.randint(1, 3)
            print("BOT ATACA. ADIVINA EL NUMERO (1, 2 o 3)")
            # loop para pedir la defensa
            defensa = solicitar_rango_de_opciones([1, 2, 3])
            if defensa == numero_defensa:
                print("\n>>> DEFENSA EXITOSA <<<")
            else:
                daño = random.randint(10, 20)
                seguridad -= daño
                print(f"\n>>> DEFENSA FALLIDA (Era {numero_defensa}) <<<")
            # jugador se quedo sin vida
            if seguridad <= 0:
                print("\nHAS PERDIDO. LA SEGURIDAD LLEGO A 0.")
                return
            turno_gastado = False
            while not turno_gastado and not nodo_neutralizado and seguridad > 0:
                print("\n=== MENU DE ACCIONES ===")
                print("1. Ataque Debil")
                print("2. Ataque Fuerte")
                print("3. Analizar Estado")
                print("=" * 32)
                accion = solicitar_opcion()
                match accion:
                    case 1:
                        nivel_amenaza -= 10
                        print(f"\n>>> ATAQUE DEBIL EJECUTADO. Amenaza baja a {nivel_amenaza}. <<<")
                        turno_gastado = True
                    case 2:
                        numero_ataque = random.randint(1, 10)
                        print("\n=== Adivina el numero (1-10): ===")
                        print("1. Mayor a 5")
                        print("2. Menor a 5")
                        print("3. Igual a 5")
                        print("=" * 32)
                        opcion = solicitar_rango_de_opciones([1, 2, 3])
                        if (opcion == 1 and numero_ataque > 5) or (opcion == 2 and numero_ataque < 5):
                            nivel_amenaza -= 20
                            print(f"\n>>> ¡ACERTASTE (Era {numero_ataque})! Amenaza baja a {nivel_amenaza}. <<<")
                        elif opcion == 3 and numero_ataque == 5:
                            nivel_amenaza -= 30
                            print(f"\n>>> ¡CRÍTICO! Amenaza baja a {nivel_amenaza}. <<<")
                        else:
                            print(f"\n>>> FALLASTE (Era {numero_ataque}). No hay daño. <<<")
                        turno_gastado = True
                    case 3:
                        # analizar estado no gasta turno
                        print(f"\n=== ESTADO ===")
                        print("Turno:", turno)
                        print("Seguridad:", seguridad)
                        print("Amenaza:", nivel_amenaza)
                        print("=" * 32)
                    case _:
                        print("Error. Opción inválida.")
            if nivel_amenaza <= 0:
                nodo_neutralizado = True
                print(f"\n=== NODO {nodo} NEUTRALIZADO ===")
                break
            turno += 1
        # termino del turno analizar estado de la partida
        if nodo_neutralizado:
            if nodo == 3:
                print("=== HAS GANADO ===")
            else:
                print("AVANZANDO AL SIGUIENTE NODO...")
        else:
            if nodo == 3:
                print("=== FIN DE LOS TURNOS ===")
                print("EVALUANDO MECANISMO DE EMERGENCIA...")
                if nivel_amenaza <= 50:
                    print("\nACTIVANDO PROTOCOLO...")
                    probabilidad = random.randint(1, 10)
                    if probabilidad <= 3:
                        print("=== EXITOSO ===")
                        print("HAS GANADO")
                        return
                    else:
                        print("=== FALLADO ===")
                        print("HAS PERDIDO")
                        return
                else:
                    print("=== NO SE ACTIVA EL MECANISMO DE EMERGENCIA ===")
                    print("HAS PERDIDO")
                    return
            else:
                print("=== FIN DE LOS TURNOS ===")
                print("HAS PERDIDO")
                return
    # termina el loop externo, verificar si aun tienes vida
    if seguridad > 0:
        print("=== VICTORIA TOTAL ===")

# loop principal
while True:
    menu() # mostrar menu
    opcion = solicitar_opcion()
    match opcion:
        case 1:
            juego()
        case 2:
            print("\nSaliendo...")
            break # terminar el loop
        case _:
            print("\nOpcion invalida. Intentalo de nuevo.")