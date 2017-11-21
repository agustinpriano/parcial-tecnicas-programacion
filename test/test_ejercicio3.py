import unittest
import ejercicio3

class TestDiccionarioEquipos(unittest.TestCase):
    def test_diccionarioEquipos(self):
        self.assertEqual(ejercicio3.diccionarioEquipos([("a", 1, "b", 0), ("a", 1, "c", 2), ("c", 3, "b", 0)]),{'b': [], 'a': [2], 'c': [2, 2]})
        self.assertEqual(ejercicio3.diccionarioEquipos([]),{})
        self.assertEqual(ejercicio3.diccionarioEquipos([("a", 1, "b", 0)]), {'a': [2], 'b': []})

class TestListaEquipos(unittest.TestCase):
    def test_listaEquipos(self):
        self.assertEqual(ejercicio3.listaEquipos({}), [])
        self.assertEqual(ejercicio3.listaEquipos({'a': [2, 1], 'b': [1]}), [['a', [2, 1]], ['b', [1]]])



