# ACTIVIDAD 3: Sistema de Acceso a la Baticueva
# Para proteger los secretos de Batman, el sistema informático de la Baticueva
# necesita almacenar datos confidenciales que nadie más pueda alterar directamente.

class BatcuevaSystem:
    def __init__(self, password="Gotham2025", nivel_alerta="Verde"):
        self.__mando_central_pass = password
        self.__nivel_alerta = nivel_alerta

    def obtener_alerta(self):
        """Devuelve el nivel de alerta actual."""
        return self.__nivel_alerta

    def cambiar_alerta(self, nueva_alerta, clave_ingresada):
        """Cambia la alerta solo si la clave es correcta."""
        if clave_ingresada != self.__mando_central_pass:
            print("Acceso denegado: clave incorrecta.")
            return False

        alertas_validas = {"Verde", "Amarillo", "Rojo"}
        if nueva_alerta not in alertas_validas:
            print(f"Alerta no válida: '{nueva_alerta}'.")
            return False

        self.__nivel_alerta = nueva_alerta
        print(f"Alerta cambiada correctamente a: {self.__nivel_alerta}")
        return True


# Prueba del funcionamiento
baticueva = BatcuevaSystem()
print(f"Alerta inicial: {baticueva.obtener_alerta()}")

print("\nIntento 1: clave correcta")
baticueva.cambiar_alerta("Amarillo", "Gotham2025")
print(f"Alerta actual: {baticueva.obtener_alerta()}")

print("\nIntento 2: clave incorrecta")
baticueva.cambiar_alerta("Rojo", "clave_incorrecta")
print(f"Alerta actual: {baticueva.obtener_alerta()}")
