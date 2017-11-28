import unittest
import ejercicio2

class TestEjercicio2(unittest.TestCase):

    posicionesDeDisparosDePrueba = [(1, 1), (3, 4), (1, 3), (4, 5)]

    def test_devolverBarcosHundidosRecibeListaVaciaYPosicionesDePruebaDeberiaDevolverListaVacia(self):
        self.assertEqual(ejercicio2.devolverBarcosNoHundidos([],self.posicionesDeDisparosDePrueba),[])

    def test_devolverBarcosHundidosRecibeListaDeCadenaNulaYPosicionesDePruebaDeberiaDevolverListaVacia(self):
        self.assertEqual(ejercicio2.devolverBarcosNoHundidos([""],self.posicionesDeDisparosDePrueba),[])

    def test_devolverBarcosHundidosRecibeListaDeCadenaConEspaciosYPosicionesDePruebaDeberiaDevolverListaVacia(self):
        self.assertEqual(ejercicio2.devolverBarcosNoHundidos(["      "],self.posicionesDeDisparosDePrueba),[])

    def test_devolverBarcosHundidosRecibeListaDeCadenaInvalidaYPosicionesDePruebaDeberiaDevolverListaVacia(self):
        self.assertEqual(ejercicio2.devolverBarcosNoHundidos(["soy NO valido"],self.posicionesDeDisparosDePrueba),[])

    def test_devolverBarcosHundidosRecibeListaDeCadenasInvalidasYPosicionesDePruebaDeberiaDevolverListaVacia(self):
        self.assertEqual(ejercicio2.devolverBarcosNoHundidos(["yo","tambien","soy","invalido"],self.posicionesDeDisparosDePrueba),[])

    def test_devolverBarcosHundidosRecibeListaDeCadenasConNumeroDistintoDeElementosPorCadenaDeberiaYPosicionesDePruebaDevolverListaVacia(self):
        self.assertEqual(ejercicio2.devolverBarcosNoHundidos(["b.b.","....","..bb","b.b"],self.posicionesDeDisparosDePrueba),[])

    def test_devolverBarcosHundidosRecibeListaDeCadenasValidaYPosicionesDePruebaDeberiaDevolverListaConPosicionesDeBarcosSupervivientes(self):
        self.assertEqual(ejercicio2.devolverBarcosNoHundidos(["b.b..","b...b",".....","....b"],self.posicionesDeDisparosDePrueba),[(2,1),(2,5)])

    def test_devolverBarcosHundidosRecibeListaDeCadenasValidaYListaDePosicionesVaciaDeberiaDevolverListaConPosicionesDeBarcosSupervivientes(self):
        self.assertEqual(ejercicio2.devolverBarcosNoHundidos(["b..","...","..b"],[]), [(1,1),(3,3)])