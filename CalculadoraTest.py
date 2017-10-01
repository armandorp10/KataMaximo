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
        self.assertEquals(Calculadora().getEstadisticas("3,2")[1], 2, "Dos elementos")

    def test_getEstadisticasMinimoVariosNumeros(self):
        self.assertEquals(Calculadora().getEstadisticas("2,3,5,1")[1], 1, "Varios elementos")

    def test_getEstadisticasMaximo(self):
        self.assertEquals(Calculadora().getEstadisticas("")[2], 0, "Cero numero de elementos")

    def test_getEstadisticasMaximoUnNumero(self):
        self.assertEquals(Calculadora().getEstadisticas("2")[2], 2, "Un elemento")

    def test_getEstadisticasMaximoDosNumeros(self):
        self.assertEquals(Calculadora().getEstadisticas("3,2")[2], 3, "Dos elementos")

    def test_getEstadisticasMaximoVariosNumeros(self):
        self.assertEquals(Calculadora().getEstadisticas("2,3,5,1")[2], 5, "Varios elementos")

    def test_getEstadisticasPromedio(self):
        self.assertEquals(Calculadora().getEstadisticas("")[3], 0, "Cero numero de elementos")

    def test_getEstadisticasPromedioUnNumero(self):
        self.assertEquals(Calculadora().getEstadisticas("2")[3], 2, "Un elemento")

    def test_getEstadisticasPromedioDosNumeros(self):
        self.assertEquals(Calculadora().getEstadisticas("3,2")[3], 2.5, "Dos elementos")

    def test_getEstadisticasPromedioVariosNumeros(self):
        self.assertEquals(Calculadora().getEstadisticas("2,3,5,1")[3], 2.75, "Varios elementos")