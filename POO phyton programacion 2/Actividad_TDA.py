# TDA NAVE_ESPACIAL
#REQUERIMIENTOS:

class NaveEspacial:
    def __init__(self, nombre: str, piloto: str, nivel_escudo: int):
        self.nombre = nombre
        self.piloto = piloto
        self.nivel_escudo = nivel_escudo

    def mostrar_caracteristicas(self):
        print(f"Nave: {self.nombre}, Piloto: {self.piloto}, Nivel de Escudo: {self.nivel_escudo}")

# Instanciando las naves
halcon_milenario = NaveEspacial("Halcón Milenario", "Han Solo", 100)
x_wing = NaveEspacial("X-Wing", "Luke Skywalker", 50 )

# Imprimiendo las características iniciales de ambas naves
halcon_milenario.mostrar_caracteristicas()
x_wing.mostrar_caracteristicas()
