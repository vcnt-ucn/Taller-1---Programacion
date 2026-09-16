import random

def menu():
    print("=" * 8 + " JUEGO BOT NET " + "=" * 9)
    print("1. Comenzar")
    print("2. Salir")
    print("=" * 32)

def solicitar_opcion():
    while True:
        try:
            return int(input("Seleccione una opcion: "))
        except:
            print("Error. Eliga un numero valido.\n")

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
        print("\nINICIANDO COMBATE CONTRA NODO", nodo)
        print("NIVEL DE AMENAZA:", nivel_amenaza)
        turno = 1
        nodo_neutralizado = False
        # loop interno, turnos
        while turno <= 10 and not nodo_neutralizado and seguridad > 0:
            print("=" * 32)
            print(f"TURNO {turno}/10 - NODO {nodo}/3")
            print("=" * 32)
            numero_defensa = random.randint(1, 3)
            print("BOT ATACA. ADIVINA EL NUMERO (1, 2 o 3)")
            # loop para pedir la defensa
            while True:
                try:
                    defensa = int(input("Tu respuesta: "))
                    if defensa in [1, 2, 3]:
                        break
                    else:
                        print("Error. Ingrese un numero entre las opciones.")
                except:
                    print("Error. Ingrese un numero valido.")
            if defensa == numero_defensa:
                print("\nDEFENSA EXITOSA")
            else:
                daño = random.randint(10, 20)
                seguridad -= daño
                print("\nDEFENSA FALLIDA")
            if seguridad <= 0:
                print("\nHAS PERDIDO")
                return
            turno_gastado = False
            while not turno_gastado and not nodo_neutralizado and seguridad > 0:
                print("1. Ataque Debil")
                print("2. Ataque Fuerte")
                print("3. Analizar Estado")
                print("=" * 32)
                accion = solicitar_opcion()
                match accion:
                    case 1:
                        nivel_amenaza -= 10
                        print(f"Ataque débil. Amenaza baja a {nivel_amenaza}")
                        turno_gastado = True
                    case 2:
                        numero_ataque = random.randint(1, 10)
                        print("\nAdivina (1-10): \n1. Mayor a 5\n2. Menor a 5\n3. Igual a 5")
                        opc_fuerte = solicitar_opcion()
                        if (opc_fuerte == 1 and numero_ataque > 5) or (opc_fuerte == 2 and numero_ataque < 5):
                            nivel_amenaza -= 20
                            print(f"¡Acertaste ({numero_ataque})! Amenaza baja a {nivel_amenaza}")
                        elif opc_fuerte == 3 and numero_ataque == 5:
                            nivel_amenaza -= 30
                            print(f"¡CRÍTICO (5)! Amenaza baja a {nivel_amenaza}")
                        else:
                            print(f"Fallaste (Era {numero_ataque}). No hay daño.")
                        turno_gastado = True
                    case 3:
                        # Analizar estado no cambia 'accion_completada', por lo que repite el menú
                        print(f"\n--- ESTADO: Turno {turno}, Seguridad {seguridad}, Amenaza {nivel_amenaza} ---")
                    case _:
                        print("Opción inválida.")
            if nivel_amenaza <= 0:
                nodo_neutralizado = True
                print(f"\nNODO {nodo} NEUTRALIZADO")
                break
            turno += 1
        # termino del turno analizar estado de la partida
        if nodo_neutralizado:
            if nodo == 3:
                print("HAS GANADO")
            else:
                print("AVANZANDO AL SIGUIENTE NODO")
        else:
            if nodo == 3:
                print("FIN DE LOS TURNOS")
                print("EVALUANDO MECANISMO DE EMERGENCIA")
                if nivel_amenaza <= 50:
                    print("ACTIVANDO PROTOCOLO")
                    probabilidad = random.randint(1, 10)
                    if probabilidad <= 3:
                        print("EXITOSO")
                        print("HAS GANADO")
                        return
                    else:
                        print("FALLADO")
                        print("HAS PERDIDO")
                        return
                else:
                    print("NO SE ACTIVA EL MECANISMO DE EMERGENCIA")
                    print("HAS PERDIDO")
                    return
            else:
                print("FIN DE LOS TURNOS")
                print("HAS PERDIDO")
                return
    # termina el loop externo, verificar si aun tienes vida
    if seguridad > 0:
        print("VICTORIA TOTAL")

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