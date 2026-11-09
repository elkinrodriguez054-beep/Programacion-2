class Mago:
    def __init__(self, nombre, mana_base):
        self.nombre = nombre
        self.mana_base = mana_base

    def mostrar_estado(self):
        print(f"{self.nombre} tiene {self.mana_base} puntos de maná.")


class MagoFuego(Mago):
    def __init__(self, nombre, mana_base, temperatura_llama):
        super().__init__(nombre, mana_base)
        self.temperatura_llama = temperatura_llama

    def lanzar_bola_fuego(self):
        costo_mana = 20
        if self.mana_base >= costo_mana:
            self.mana_base -= costo_mana
            print(f"{self.nombre} lanza una bola de fuego a {self.temperatura_llama}°C. ¡Ataque ardiente!")
        else:
            print(f"{self.nombre} no tiene suficiente maná para lanzar una bola de fuego.")


class MagoHielo(Mago):
    def __init__(self, nombre, mana_base, grosor_escudo_hielo):
        super().__init__(nombre, mana_base)
        self.grosor_escudo_hielo = grosor_escudo_hielo

    def congelar_terreno(self):
        costo_mana = 15
        if self.mana_base >= costo_mana:
            self.mana_base -= costo_mana
            print(f"{self.nombre} congela el terreno con un escudo de hielo de {self.grosor_escudo_hielo} cm.")
        else:
            print(f"{self.nombre} no tiene suficiente maná para congelar el terreno.")


# Instancias de cada especialidad
mago_fuego = MagoFuego("Ignis", 100, 1200)
mago_hielo = MagoHielo("Eryx", 90, 25)

mago_fuego.lanzar_bola_fuego()
mago_hielo.congelar_terreno()

mago_fuego.mostrar_estado()
mago_hielo.mostrar_estado()

