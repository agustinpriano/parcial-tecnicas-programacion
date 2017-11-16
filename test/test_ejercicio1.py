import unittest
import ejercicio1

class TestGeneroListaDeCaracteres(unittest.TestCase):
    def test_generoListaDeCaracteres(self):
        self.assertEqual(ejercicio1.generoListaDeCaracteres("hola"),['h','o','l','a'])
        self.assertEqual(ejercicio1.generoListaDeCaracteres(""),[])
        self.assertEqual(ejercicio1.generoListaDeCaracteres("   "),[' ',' ',' '])

class TestComprueboValidezDePalabra(unittest.TestCase):
    def test_comprueboValidezDePalabra(self):
        self.assertEqual(ejercicio1.comprueboValidezDePalabra(['a'],"a"),True)
        self.assertEqual(ejercicio1.comprueboValidezDePalabra(['a','b','c'], "abc"), True)
        self.assertEqual(ejercicio1.comprueboValidezDePalabra([' '], " "), False)
        self.assertEqual(ejercicio1.comprueboValidezDePalabra([' ',' '], "  "), False)

class TestGeneroListasDePalabrasRotadas(unittest.TestCase):
    def test_generoListasDePalabrasRotadas(self):
        self.assertEqual(ejercicio1.generoListasDePalabrasRotadas(['a','b','c'],"abc"),["abc","bca","cab"])
        self.assertEqual(ejercicio1.generoListasDePalabrasRotadas(['b', 'c', 'a'], "abc"), ["bca", "cab", "abc"])
        self.assertEqual(ejercicio1.generoListasDePalabrasRotadas([''], ""), [""])
        self.assertEqual(ejercicio1.generoListasDePalabrasRotadas([' '], " "), [" "])

class TestRotarPalabra(unittest.TestCase):
    def test_rotarPalabra(self):
        self.assertEqual(ejercicio1.rotarPalabra(""),[])
        self.assertEqual(ejercicio1.rotarPalabra("a"), ['a'])
        self.assertEqual(ejercicio1.rotarPalabra("ab"), ['ab','ba'])
        self.assertEqual(ejercicio1.rotarPalabra("paz"), ['paz','azp','zpa'])
        self.assertEqual(ejercicio1.rotarPalabra("so l"),['so l','o ls',' lso','lso '])