import random

def menu():
    print("=" * 8 + " JUEGO - BOTNET " + "=" * 8)
    print("1. Comenzar")
    print("2. Salir")
    print("=" * 32)

def solicitar_opcion():
    while True:
        try:
            return int(input("Seleccione una opcion: "))
        except ValueError:
            print("Error. Eliga un numero valido.\n")

def solicitar_opciones():
    while True:
        try:
            opcion = int(input("Tu respuesta: "))
            if opcion in [1, 2, 3]:
                return opcion
            print("Error. Ingrese un numero entre las opciones.")
        except ValueError:
            print("Error. Ingrese un numero valido.")

def juego():
    # vida del admin
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
        print(f"\n>>> INICIANDO COMBATE CONTRA NODO {nodo}... <<<")
        print("NIVEL DE AMENAZA:", nivel_amenaza)
        turno = 1
        nodo_neutralizado = False
        # loop interno, turnos
        while turno <= 10 and not nodo_neutralizado and seguridad > 0:
            print(f"\n=== TURNO {turno}/10 - NODO {nodo}/3 ===")
            numero_defensa = random.randint(1, 3)
            print("BOT ATACA. ADIVINA EL NUMERO (1, 2 o 3)")
            # loop para pedir la defensa
            respuesta_defensa = solicitar_opciones()
            defensa = respuesta_defensa == numero_defensa
            if defensa:
                print("\n>>> DEFENSA EXITOSA <<<")
                print("NO SUFRES DAÑO")
            else:
                daño = random.randint(10, 20)
                seguridad -= daño
                print(f"\n>>> DEFENSA FALLIDA (Era {numero_defensa}) <<<")
                print(f"HAS SUFRIDO {daño} DE DAÑO")
            # jugador se quedo sin vida
            if seguridad <= 0:
                seguridad = 0 # no pasa a negativo
                print("\n>>> LA SEGURIDAD LLEGO A 0 <<<")
                print("HAS PERDIDO")
                print("=" * 32, "\n\n")
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
                    case 1: # ataque debil
                        nivel_amenaza -= 10
                        if nivel_amenaza < 0:
                            nivel_amenaza = 0 # no pasa a negativo
                        print("\n>>> ATAQUE DEBIL EJECUTADO <<<")
                        print(f"Amenaza baja a {nivel_amenaza}")
                        turno_gastado = True
                    case 2: # ataque fuerte
                        numero_ataque = random.randint(1, 10)
                        print("\n=== Adivina el numero (1-10): ===")
                        print("1. Mayor a 5")
                        print("2. Menor a 5")
                        print("3. Igual a 5")
                        print("=" * 32)
                        opcion = solicitar_opciones()
                        if (opcion == 1 and numero_ataque > 5) or (opcion == 2 and numero_ataque < 5):
                            nivel_amenaza -= 20 # doble del ataque debil
                            if nivel_amenaza < 0:
                                nivel_amenaza = 0 # no pasa a negativo
                            print(f"\n>>> ¡ACERTASTE (Era {numero_ataque})! <<<")
                            print(f"Amenaza baja a {nivel_amenaza}")
                        elif opcion == 3 and numero_ataque == 5:
                            nivel_amenaza -= 30 # triple del ataque debil
                            if nivel_amenaza < 0:
                                nivel_amenaza = 0 # no pasa a negativo
                            print("\n>>> ¡CRÍTICO! <<<")
                            print(f"Amenaza baja a {nivel_amenaza}")
                        else:
                            print(f"\n>>> FALLASTE (Era {numero_ataque}) <<<")
                            print(f"No se ejerce daño")
                        turno_gastado = True
                    case 3: # analizar estado, no gasta turno
                        print(f"\n=== ESTADO ===")
                        print("Turno Actual:", turno)
                        print("Nivel de Seguridad Actual:", seguridad)
                        print("Nivel de Amenaza Actual:", nivel_amenaza)
                        print("=" * 32)
                    case _:
                        print("Error. Opción inválida.")
            if nivel_amenaza <= 0:
                nodo_neutralizado = True
                print(f"\n>>> NODO {nodo} NEUTRALIZADO <<<")
                nodos_restantes = 3 - nodo
                if nodos_restantes > 0:
                    print(f"NODOS RESTANTES: {nodos_restantes}")
                break
            turno += 1
        # termino del turno analizar estado de la partida
        if nodo_neutralizado:
            if nodos_restantes > 0:
                print("\nAVANZANDO AL SIGUIENTE NODO...")
        else:
            print("\n>>> FIN DE LOS TURNOS <<<")
            if nodo == 3:
                print("EVALUANDO MECANISMO DE EMERGENCIA...")
                if nivel_amenaza <= 50:
                    print("\nNIVEL DE AMENAZA MENOR A 50")
                    print("ACTIVANDO PROTOCOLO (30% de éxito)...")
                    probabilidad = random.randint(1, 10)
                    if probabilidad <= 3:
                        nivel_amenaza = 0
                        print("\n>>> EXITOSO <<<")
                        print("AMENAZA HA BAJADO A 0")
                        print("HAS GANADO")
                        print("=" * 32, "\n\n")
                        return
                    else:
                        print("\n>>> FALLIDO <<<")
                        print("HAS PERDIDO")
                        print("=" * 32, "\n\n")
                        return
                else:
                    print("\n>>> NO SE HA ACTIVADO EL MECANISMO DE EMERGENCIA <<<")
                    print("NIVEL DE AMENAZA MAYOR A 50")
                    print("HAS PERDIDO")
                    print("=" * 32, "\n\n")
                    return
            print("NO SE NEUTRALIZO EL NODO")
            print("HAS PERDIDO")
            print("=" * 32, "\n\n")
            return
    # termina el loop externo, verificar si aun tienes vida
    if seguridad > 0:
        print("\n=== VICTORIA TOTAL ===")
        print("HAS NEUTRALIZADO A TODOS LOS NODOS")
        print(f"SEGURIDAD FINAL: {seguridad}")
        print("=" * 32, "\n\n")

# loop principal
while True:
    menu() # mostrar menu
    opcion = solicitar_opcion()
    match opcion:
        case 1:
            juego()
        case 2:
            print("\nSaliendo...")
            break # apagar el programa
        case _:
            print("\nOpcion invalida. Intentalo de nuevo.")