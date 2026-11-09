#ACTIVIDAD2: Simulación de Batalla
#Una nave en el espacio necesita interactuar y defenderse en combate. Vamos a dotar de comportamiento a la clase NaveEspacial. 
#requerimientos:
#1. Utiliza la clase NaveEspacial del ejercicio anterior.
#2. Agrega un método recibir_disparo(dano) que reste la cantidad de daño al nivel_escudo. ▪ Si el escudo baja de 0, debe ajustarse a 0 e imprimir un mensaje indicando que la nave ha sido destruida. ▪ De lo contrario, debe imprimir el escudo restante. 
#3. Agrega un método recargar_escudo(cantidad) que aumente el escudo.
#4. Crea un objeto nave y simula una secuencia donde reciba un par de disparos y luego intente recargar escudos.

class NaveEspacial:
    def __init__(self, nombre: str, piloto: str, nivel_escudo: int):
        self.nombre = nombre
        self.piloto = piloto
        self.nivel_escudo = nivel_escudo

    #metodo recibir_disparo que resta el daño al nivel de escudo
    def recibir_disparo(self, daño: int):
        self.nivel_escudo -= daño
        if self.nivel_escudo <= 0:
            self.nivel_escudo = 0
            print(f"{self.nombre} ha sido destruida.")
        else:
            print(f"{self.nombre} recibió un disparo. Escudo restante: {self.nivel_escudo}")

    #metodo recargar_escudo que aumenta el escudo
    def recargar_escudo(self, cantidad: int):
        self.nivel_escudo += cantidad
        print(f"{self.nombre} ha recargado su escudo. Nivel actual: {self.nivel_escudo}")

# simulación de la secuencia de disparos y recarga
nave =NaveEspacial("Estrella de la Muerte", "Satanas", 100)
nave.recibir_disparo(40)
nave.recibir_disparo(70)
nave.recargar_escudo(50)
print(f"Escudo final de {nave.nombre}: {nave.nivel_escudo}")
