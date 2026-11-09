#Actividad 5:
#  Ejército de Transformers Diferentes Autobots y Decepticons responden a la misma orden de combate de maneras completamente distintas según su tipo de transformación
# . Requerimientos:
#  • Crea una clase base Transformer con un método genérico transformarse().
# • Crea las clases hijas AutobotCoche, AutobotAvion y AutobotDinosaurio.
#  • Sobrescribe el método transformarse() en cada clase hija para que devuelvan mensajes acordes a su forma (ejemplo: "¡Se convierte en un deportivo a 300 km/h!", "¡Despliega las alas y vuela a velocidad supersónica!", "¡Se transforma en un T-Rex robótico!"). 
# • Crea una lista con al menos un objeto de cada tipo y haz un bucle para llamar al método transformarse() de cada objeto en la lista.

# Clase base
class Transformer:
    def __init__(self, nombre: str, bando: str):
        self.nombre = nombre
        self.bando = bando

    def transformarse(self):
        """Método genérico diseñado para ser sobrescrito por las clases hijas."""
        return f"{self.nombre} se prepara para la batalla."


# Clases hijas con sobrescritura de método (Polimorfismo)
class AutobotCoche(Transformer):
    def transformarse(self):
        return f"[{self.bando}] {self.nombre}: ¡Se convierte en un deportivo a 300 km/h y quema llanta!"

class AutobotAvion(Transformer):
    def transformarse(self):
        return f"  [{self.bando}] {self.nombre}: ¡Despliega las alas y vuela a velocidad supersónica!"

class AutobotDinosaurio(Transformer):
    def transformarse(self):
        return f" [{self.bando}] {self.nombre}: ¡Se transforma en un T-Rex robótico y lanza un rugido metálico!"


# Creación del ejército de Transformers
ejercito = [
    AutobotCoche("Bumblebee", "Autobot"),
    AutobotAvion("Starscream", "Decepticon"),
    AutobotDinosaurio("Grimlock", "Autobot"),
    AutobotCoche("Barricade", "Decepticon"),
    AutobotAvion("Jetfire", "Autobot")
]

# Orden de combate: Procesamiento polimórfico de la lista
print("¡ORDEN DE COMBATE EMITIDA! \n")

for transformer in ejercito:
    print(transformer.transformarse())