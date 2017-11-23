import unittest
import ejercicio3

class TestDiccionarioEquipos(unittest.TestCase):
    def test_diccionarioEquipos(self):
        self.assertEqual(ejercicio3.diccionarioEquipos([("a", 1, "b", 0), ("a", 1, "c", 2), ("c", 3, "b", 0)]),{'b': [], 'a': [2], 'c': [2, 2]})
        self.assertEqual(ejercicio3.diccionarioEquipos([]),{})
        self.assertEqual(ejercicio3.diccionarioEquipos([("a", 1, "b", 0)]), {'a': [2], 'b': []})

class TestListaEquipos(unittest.TestCase):
    def test_listaEquipos(self):
        lista=ejercicio3.listaEquipos({'a': [2, 1], 'b': [1], 'c': [2,2,2]})
        for x in lista:
            self.assertIn(x,[['a', [2, 1]], ['b', [1]], ['c', [2, 2, 2]]])
        self.assertEqual(ejercicio3.listaEquipos({}), [])

class TestListaEquiposConPuntosSumados(unittest.TestCase):
    def test_testListaEquiposConPuntosSumados(self):
        self.assertEqual(ejercicio3.listaEquiposConPuntosSumados([['a', [2, 1]], ['c', [2, 2, 2]], ['b', [1]]]), [['a', 3], ['c', 6], ['b', 1]])
        self.assertEqual(ejercicio3.listaEquiposConPuntosSumados([]),[])
        self.assertEqual(ejercicio3.listaEquiposConPuntosSumados([ ['a', [2, 1]], ['c', [2, 2, 2]], ['b', [1]], ['d', [2, 1]] ]),[['a', 3], ['c', 6], ['b', 1], ['d', 3]])

class TestOrdenarPorCantidadDePuntos(unittest.TestCase):
    def test_ordenarPorCantidadDePuntos(self):
        self.assertEqual(ejercicio3.ordenarPorCantidadDePuntos([['b', [1]], ['a', [3]], ['c', [6]]]), [['b', [1]], ['a', [3]], ['c', [6]]])
        self.assertEqual(ejercicio3.ordenarPorCantidadDePuntos([['a', [6]], ['b', [3]], ['c', [1]]]), [['c', [1]], ['b', [3]], ['a', [6]]])
        self.assertEqual(ejercicio3.ordenarPorCantidadDePuntos([['a', [3]], ['b', [1]], ['c', [6]]]),[['b', [1]], ['a', [3]], ['c', [6]]])

class TestDevolverListaConEquiposEmpatados(unittest.TestCase):
    def test_devolverListaConEquiposEmpatados(self):
        self.assertEqual(ejercicio3.devolverListaConEquiposEmpatados([['c', [1]], ['b', [3]], ['a', [6]]]),['a'])
        self.assertEqual(ejercicio3.devolverListaConEquiposEmpatados([['c', [1]], ['b', [6]], ['a', [6]]]), ['a','b'])
        self.assertEqual(ejercicio3.devolverListaConEquiposEmpatados([['c', [3]], ['b', [3]], ['a', [3]]]), ['a','b','c'])
        self.assertEqual(ejercicio3.devolverListaConEquiposEmpatados([['c', [1]]]), ['c'])

class TestOrdenarPorOrdenAlfabetico(unittest.TestCase):
    def test_ordenarPorOrdenAlfabetico(self):
        self.assertEqual(ejercicio3.ordenarPorOrdenAlfabetico(['c','d','a']),['a','c','d'])
        self.assertEqual(ejercicio3.ordenarPorOrdenAlfabetico(['Boca', 'Almagro', 'River']), ['Almagro', 'Boca', 'River'])
        self.assertEqual(ejercicio3.ordenarPorOrdenAlfabetico(['c', 'f', 'a','z']), ['a','c','f','z'])

class TestGanadorDeLiga(unittest.TestCase):
    def test_ganadorDeLiga(self):
        self.assertEqual(ejercicio3.ganadorDeLiga([("a", 1, "b", 0)]),'a')
        self.assertEqual(ejercicio3.ganadorDeLiga([("a", 1, "b", 0), ("a", 1, "c", 2), ("c", 3, "b", 0)]),"c")
        self.assertEqual(ejercicio3.ganadorDeLiga([("a", 1, "b", 0), ("a", 1, "c", 2), ("c", 3, "b", 0)]), "c")
        self.assertEqual(ejercicio3.ganadorDeLiga([("Boca", 1, "Belgrano", 1), ("Boca", 1, "Almagro", 1), ("Almagro", 1, "Belgrano", 1)]), "Almagro")
        self.assertEqual(ejercicio3.ganadorDeLiga([("a", 1, "b", -2), ("a", 1, "c", 1), ("c", 1, "b", 1), ("d", 1, "a", 9)]), "a")
