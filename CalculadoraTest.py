from unittest import TestCase

from Calculadora import Calculadora

class CalculadoraTest(TestCase):
    def test_getEstadisticas(self):
        self.assertEquals(Calculadora().getEstadisticas(""), 0, "Cero numero de elementos")
