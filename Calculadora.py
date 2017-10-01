
class Calculadora:
    def getEstadisticas(self, cadena):
        if cadena == "":
            return [0, 0, 0, 0]
        elif "," in cadena:
            numeros = cadena.split(",")
            return [len(numeros), int(min(numeros)), int(max(numeros))]
        else:
            return [1, int(cadena), int(cadena)]