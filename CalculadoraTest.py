from unittest import TestCase

import  Calculadora

class CalculadoraTest(TestCase):
    def test_getEstadisticas(self):
        self.assertEquals(Calculadora().getEstadisticas(""), 0, "cadena vacia")
