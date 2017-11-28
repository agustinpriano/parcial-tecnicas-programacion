import unittest
import ejercicio3

class TestEjercicio3(unittest.TestCase):

    def test_GanadorDeLigaRecibeListaVaciaDeberiaDevolverCadenaVacia(self):
        self.assertEqual(ejercicio3.ganadorDeLiga([]),"")

    def test_GanadorDeLigaRecibeListaDeTuplasConResultadoDeUnPartidoDondeGanoElEquipoADeberiaDevolverCadenaConElNombreDelEquipo(self):
        self.assertEqual(ejercicio3.ganadorDeLiga([("a", 1, "b", 0)]),"a")

    def test_GanadorDeLigaRecibeListaDeTuplasConResultadoDePartidosDondeSumoMasPuntosElEquipoCDeberiaDevolverCadenaConElNombreDelEquipo(self):
        self.assertEqual(ejercicio3.ganadorDeLiga([("a", 1, "b", 0), ("a", 1, "c", 2), ("c", 3, "b", 0)]),"c")

    def test_GanadorDeLigaRecibeListaDeTuplasConResultadoDePartidosDondeSumaronMasPuntosBocaYAlmagroDeberiaDevolverCadenaConElNombreDelPrimerEquipoOrdenadoAlfabeticamente(self):
        self.assertEqual(ejercicio3.ganadorDeLiga([("Boca", 1, "Belgrano", 1), ("Boca", 1, "Almagro", 1), ("Almagro", 1, "Belgrano", 1)]),"Almagro")

    def test_GanadorDeLigaRecibeListaDeTuplasConResultadoDePartidosDondeSumoMasPuntosElEquipoADeberiaDevolverCadenaConElNombreDelEquipo(self):
        self.assertEqual(ejercicio3.ganadorDeLiga([("a", 1, "b", -2), ("a", 1, "c", 1), ("c", 1, "b", 1), ("d", 1, "a", 9)]),"a")