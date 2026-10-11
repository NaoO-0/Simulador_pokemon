LOG_EVENTOS = []

class Pokemon:
    _total_pokemons = 0

    def __init__(self, nombre, tipo, nivel=1, ataque=10, defensa=5, salud=50):
        self.nombre = nombre
        self.tipo = tipo
        self.nivel = nivel
        self.ataque = ataque
        self.defensa = defensa
        self.salud = salud

        Pokemon._total_pokemons += 1

        print(f"¡Un nuevo {self.nombre} de tipo {self.tipo} ha aparecido!")

    def __del__(self):
        Pokemon._total_pokemons -= 1
        print(f"{self.nombre} ha sido liberado ✨")

    def mostrar_info(self):
        print(f"\n ---Informacion de {self.nombre}---")
        print(f"\n Tipo: {self.tipo}")
        print(f"\n Nivel: {self.nivel}")
        print(f"\n Ataque: {self.ataque}")
        print(f"\n Defensa: {self.defensa}")
        print(f"\n Salud: {self.salud}")

    def entrenar(self, *args):
        incremento = 5 * self.nivel
        
        if not args:
            self.ataque += incremento
            self.defensa += incremento
            self.salud += incremento * 2
            self.nivel += 1
            print(f"¡{self.nombre} ha entrenado duro de forma general! Sube al nivel {self.nivel}.")
        else:
            for stat in args:
                stat_lower = stat.lower()
                if stat_lower == "ataque":
                    self.ataque += incremento
                    print(f"-> ¡El ataque de {self.nombre} subió!")
                elif stat_lower == "defensa":
                    self.defensa += incremento
                    print(f"-> ¡La defensa de {self.nombre} subió!")
                elif stat_lower == "salud":
                    self.salud += incremento * 2
                    print(f"-> ¡La salud de {self.nombre} subió!")
                else:
                    print(f"-> Estadística '{stat}' desconocida.")
            self.nivel += 1
            print(f"¡El entrenamiento de {self.nombre} ha finalizado y ha subido al nivel {self.nivel}!")

    def atacar(self, objetivo):
        print(f"\n ¡{self.nombre} ataca a {objetivo.nombre}!")

        daño = max (1, self.ataque - objetivo.defensa)
        objetivo.salud -= daño
        if objetivo.salud < 0:
            objetivo.salud = 0

        print(f"¡{self.nombre} inflige {daño} puntos de daño a {objetivo.nombre}!")
        print(f"Salud actual de {objetivo.nombre} es {objetivo.salud}")

        global LOG_EVENTOS
        LOG_EVENTOS.append(f"{self.nombre} atacó a {objetivo.nombre} causando {daño} de daño")

    @classmethod
    def total_pokemones(cls):
        return cls._total_pokemons

