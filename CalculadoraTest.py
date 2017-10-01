from unittest import TestCase

from Calculadora import Calculadora

class CalculadoraTest(TestCase):
    def test_getEstadisticas(self):
        self.assertEquals(Calculadora().getEstadisticas("")[0], 0, "Cero numero de elementos")

    def test_getEstadisticasUnNumero(self):
        self.assertEquals(Calculadora().getEstadisticas("2")[0], 1, "Un elemento")

    def test_getEstadisticasDosNumeros(self):
        self.assertEquals(Calculadora().getEstadisticas("2,3")[0], 2, "Dos elementos")