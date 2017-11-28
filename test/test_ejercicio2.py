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

    def test_devolverBarcosHundidosRecibeMapaInvalidoYPosicionesDePruebaDeberiaDevolverListaVacia(self):
        self.assertEqual(ejercicio2.devolverBarcosNoHundidos(["soy NO valido"],self.posicionesDeDisparosDePrueba),[])

    def test_devolverBarcosHundidosRecibeMapaInvalidoYPosicionesDePruebaDeberiaDevolverListaVacia(self):
        self.assertEqual(ejercicio2.devolverBarcosNoHundidos(["yo","tambien","soy","invalido"],self.posicionesDeDisparosDePrueba),[])

    def test_devolverBarcosHundidosRecibeMapaConCantidadDeElementosDistintosPorFilaYPosicionesDePruebaDeberiaDevolverListaVacia(self):
        self.assertEqual(ejercicio2.devolverBarcosNoHundidos(["b.b.","....","..bb","b.b"],self.posicionesDeDisparosDePrueba),[])

    def test_devolverBarcosHundidosRecibeMapaValidoYPosicionesDePruebaDeberiaDevolverListaConPosicionesDeBarcosSupervivientes(self):
        self.assertEqual(ejercicio2.devolverBarcosNoHundidos(["b.b..","b...b",".....","....b"],self.posicionesDeDisparosDePrueba),[(2,1),(2,5)])

    def test_devolverBarcosHundidosRecibeMapaValidoYListaDePosicionesVaciaDeberiaDevolverListaConPosicionesDeBarcosSupervivientes(self):
        self.assertEqual(ejercicio2.devolverBarcosNoHundidos(["b..","...","..b"],[]), [(1,1),(3,3)])