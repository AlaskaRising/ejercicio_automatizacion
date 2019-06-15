import unittest
from pares import Numeros

class test_saber_si_es_par(unittest.TestCase):

    def test_numero(self):
        self.assertEqual(0, Numeros.saber_si_es_par(self, 3))
        self.assertEqual(1, Numeros.saber_si_es_par(self, 8))

unittest.main(argv=['ignored', '-v'], exit=False)