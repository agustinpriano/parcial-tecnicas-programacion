import unittest
import ejercicio1

class TestEjercicio1(unittest.TestCase):

    def test_rotarPalabraRecibePalabraVaciaDeberiaDevolverListaVacia(self):
        self.assertEqual(ejercicio1.rotarPalabra(""),[])

    def test_rotarPalabraRecibeCadenaDeEspaciosDeberiaDevolverListaVacia(self):
        self.assertEqual(ejercicio1.rotarPalabra("     "),[])

    def test_rotarPalabraRecibeLetraUnicaDeberiaDevolverListaConLaLetraComoUnicoElemento(self):
        self.assertEqual(ejercicio1.rotarPalabra("a"),['a'])

    def test_rotarPalabraRecibePalabraDeDosCaracteresDeberiaDevolverListaConLasDosRotacionesPosibles(self):
        self.assertEqual(ejercicio1.rotarPalabra("ab"),['ab','ba'])

    def test_rotarPalabraRecibePalabraDeTresCaracteresDeberiaDevolverListaConLasTresRotacionesPosibles(self):
        self.assertEqual(ejercicio1.rotarPalabra("paz"),['paz','azp','zpa'])

    def test_rotarPalabraRecibePalabraDeCuatroCaracteresConUnEspacioDeberiaDevolverListaConLasCuatroRotaciones(self):
        self.assertEqual(ejercicio1.rotarPalabra("so l"),['so l','o ls',' lso','lso '])

    def test_rotarPalabraRecibePalabraDeCincoCaracteresDeberiaDevolverListaConLasCincoRotacionesPosibles(self):
        self.assertEqual(ejercicio1.rotarPalabra("rotar"),['rotar','otarr','tarro','arrot','rrota'])