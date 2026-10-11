from clases.pokemon import Pokemon, LOG_EVENTOS

def menu():
    mis_pokemons=[]

    while True:
        print("\n ==== Menú Principal ====")
        print("1.- Capturar nuevos pokemons")
        print("2.- Entrenarlos")
        print("3.- Ver información de los pokemons")
        print("4.- Calcular cuantos pokemons existen")
        print("5.- Liberar un pokemon")
        print("6.- Simular una batalla pokemon")
        print("7.- Ver resigtro de eventos globales")
        print("8.- Salir")

        opcion = input("Selecciona una opcion (1-8): ").strip()

        if opcion == "1":
            print("\n --- Capturar Pokemon ---")
            nombre = input("Nombre del Pokemon: ").strip()
            tipo = input("Tipo (Ej. Fuego, Agua, Planta): ").strip()
            
            try:
                nivel_input = input("Nivel inicial (Enter para 1): ").strip()
                nivel = int(nivel_input) if nivel_input else 1
                
                ataque_input = input("Ataque base (Enter para 10): ").strip()
                ataque = int(ataque_input) if ataque_input else 10
                
                defensa_input = input("Defensa base (Enter para 5): ").strip()
                defensa = int(defensa_input) if defensa_input else 5
                
                salud_input = input("Salud base (Enter para 50): ").strip()
                salud = int(salud_input) if salud_input else 50
                
                nuevo_poke = Pokemon(nombre, tipo, nivel, ataque, defensa, salud)
                mis_pokemons.append(nuevo_poke)
                print(f"¡Has capturado exitosamente a {nombre}!")
            except ValueError:
                print("Error: Los valores numéricos deben ser enteros válidos.")

        elif opcion == "2":
            if not mis_pokemons:
                print("No tienes Pokemon para entrenar.")
                continue
                
            print("\nTus Pokemon disponibles:")
            for i, p in enumerate(mis_pokemons):
                print(f"{i + 1}. {p.nombre} (Nivel {p.nivel})")
                
            try:
                idx = int(input("Selecciona el número del Pokemon a entrenar: ")) - 1
                if 0 <= idx < len(mis_pokemons):
                    poke_seleccionado = mis_pokemons[idx]
                    print("\nOpciones de entrenamiento:")
                    print("1. Entrenamiento general (mejora todo)")
                    print("2. Entrenamiento personalizado (ej. ataque defensa)")
                    sub_op = input("Elige opción de entrenamiento (1 o 2): ").strip()
                    
                    if sub_op == "2":
                        stats_input = input("Ingresa las estadísticas a mejorar separadas por espacio (ej. ataque defensa salud): ").strip()
                        if stats_input:
                            stats_args = stats_input.split()
                            poke_seleccionado.entrenar(*stats_args)
                        else:
                            print("No ingresaste estadísticas, se hará entrenamiento general.")
                            poke_seleccionado.entrenar()
                    else:
                        poke_seleccionado.entrenar()
                else:
                    print("Número fuera de rango.")
            except ValueError:
                print("Entrada inválida.")

        elif opcion == "3":
            if not mis_pokemons:
                print("No hay Pokemon registrados.")
            else:
                for p in mis_pokemons:
                    p.mostrar_info()

        elif opcion == "4":
            total = Pokemon.total_pokemones()
            print(f"\nTotal de Pokemon creados actualmente en el sistema: {total}")

        elif opcion == "5":
            if not mis_pokemons:
                print("No hay Pokemon para liberar.")
                continue
                
            print("\nTus Pokemon:")
            for i, p in enumerate(mis_pokemons):
                print(f"{i + 1}. {p.nombre}")
                
            try:
                idx = int(input("Selecciona el número del Pokemon a liberar: ")) - 1
                if 0 <= idx < len(mis_pokemons):
                    poke_a_liberar = mis_pokemons.pop(idx)
                    del poke_a_liberar  
                else:
                    print("Número fuera de rango.")
            except ValueError:
                print("Entrada inválida.")

        elif opcion == "6":
            if len(mis_pokemons) < 2:
                print("Necesitas al menos 2 Pokemon para simular una batalla.")
                continue
                
            print("\nSelecciona el Pokemon :")
            for i, p in enumerate(mis_pokemons):
                print(f"{i + 1}. {p.nombre}")
            try:
                idx_atacante = int(input("Número del atacante: ")) - 1
                
                print("\nSelecciona el Pokemon RIVAL:")
                for i, p in enumerate(mis_pokemons):
                    if i != idx_atacante:
                        print(f"{i + 1}. {p.nombre}")
                idx_rival = int(input("Número del defensor: ")) - 1
                
                if 0 <= idx_atacante < len(mis_pokemons) and 0 <= idx_rival < len(mis_pokemons):
                    if idx_atacante == idx_rival:
                        print("Un Pokemon no puede atacarse a sí mismo.")
                    else:
                        atacante = mis_pokemons[idx_atacante]
                        defensor = mis_pokemons[idx_rival]
                        atacante.atacar(defensor)
                else:
                    print("Selección inválida.")
            except ValueError:
                print("Entrada inválida.")

        elif opcion == "7":
            print("\n--- Registro Global de Eventos ---")
            if not LOG_EVENTOS:
                print("No hay eventos registrados aún.")
            else:
                for evento in LOG_EVENTOS:
                    print(f"- {evento}")

        elif opcion == "8":
            print("\n¡Saliendo del simulador Pokemon. ¡Adiós!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()