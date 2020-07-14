import unittest
from switch import switch_name

class TestSwitch(unittest.TestCase): # A classe criada vai herdar todas as funçoes da classe TestCase localizadas no modulo unittest
    def test_basic(self): # Qualquer função criada com o prefixo test vai se tornar em testes que podem ser executados pelo framework de teste
        testcase = "Lovelace, Ada"
        expected = "Ada Lovelace"
        self.assertEqual(switch_name(testcase),expected)

    def test_empty(self):
        testcase = ""
        expected = ""
        self.assertEqual(switch_name(testcase),expected)

    def test_duble_name(self):
        testcase = "Hopper, Grace M."
        expected = "Grace M. Hopper"
        self.assertEqual(switch_name(testcase),expected)

    def test_one_name(self):
        testcase = "Hopper"
        expected = "Hopper"
        self.assertEqual(switch_name(testcase),expected)

unittest.main()