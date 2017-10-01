
class Calculadora:
    def getEstadisticas(self, cadena):
        if cadena == "":
            return [0, 0, 0, 0]
        elif "," in cadena:
            numeros = cadena.split(",")
            numerosInt = map(float, numeros)
            return [len(numeros), int(min(numeros)), int(max(numeros)), sum(numerosInt)/len(numerosInt)]
        else:
            return [1, int(cadena), int(cadena), int(cadena)]