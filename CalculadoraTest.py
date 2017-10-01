from unittest import TestCase

from Calculadora import Calculadora

class CalculadoraTest(TestCase):
    def test_getEstadisticas(self):
        self.assertEquals(Calculadora().getEstadisticas("")[0], 0, "Cero numero de elementos")

    def test_getEstadisticasUnNumero(self):
        self.assertEquals(Calculadora().getEstadisticas("2")[0], 1, "Un elemento")

    def test_getEstadisticasDosNumeros(self):
        self.assertEquals(Calculadora().getEstadisticas("2,3")[0], 2, "Dos elementos")

    def test_getEstadisticasVariosNumeros(self):
        self.assertEquals(Calculadora().getEstadisticas("2,3,5,1")[0], 4, "Varios elementos")

    def test_getEstadisticasMinimo(self):
        self.assertEquals(Calculadora().getEstadisticas("")[1], 0, "Cero numero de elementos")

    def test_getEstadisticasMinimoUnNumero(self):
        self.assertEquals(Calculadora().getEstadisticas("2")[1], 2, "Un elemento")

    def test_getEstadisticasMinimoDosNumeros(self):
        self.assertEquals(Calculadora().getEstadisticas("2,3")[1], 2, "Dos elementos")