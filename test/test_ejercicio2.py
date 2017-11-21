import unittest
import ejercicio2

class TestContarColumnasPorFila(unittest.TestCase):
    def test_contarColumnasPorFila(self):
        self.assertEqual(ejercicio2.contarColumnasPorFila([]),0)
        self.assertEqual(ejercicio2.contarColumnasPorFila(["b.bb.","bb"]), 0)
        self.assertEqual(ejercicio2.contarColumnasPorFila(["", ""]), 1)
        self.assertEqual(ejercicio2.contarColumnasPorFila([" ", ""]), 0)
        self.assertEqual(ejercicio2.contarColumnasPorFila(["bbb", "..."]), 1)

class TestDevolverBarcosNoHundidos(unittest.TestCase):
    def test_devolverBarcosNoHundidos(self):
        self.assertEqual(ejercicio2.devolverBarcosNoHundidos(["b.b.","....","..bb","b.b"],[(1,1),(3,4),(1,3),(4,5)]),[])
        self.assertEqual(ejercicio2.devolverBarcosNoHundidos(["b.b..","b...b",".....","....b"], [(1, 1), (3, 4), (1, 3), (4, 5)]), [(2,1),(2,5)])
        self.assertEqual(ejercicio2.devolverBarcosNoHundidos(["b..","...","..b"],[]),[(1, 1), (3, 3)])
        self.assertEqual(ejercicio2.devolverBarcosNoHundidos([], [(1,1),(3,4),(1,3),(4,5)]), [])

