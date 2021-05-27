from operacoes.multiplicacao import Multiplicacao
from operacoes.soma import Soma
from operacoes.divisao import Divisao
from operacoes.subtracao import Subtracao
import unittest

n1 = 10
n2 = 5


class TestCase(unittest.TestCase):

    def test_instancia(self):
        soma = Soma(n1, n2)
        self.assertIsInstance(soma, Soma)

    def test_soma(self):
        soma = Soma(n1, n2)
        self.assertEqual(soma.result, 15)

    def test_subtracao(self):
        subtracao = Subtracao(n1, n2)
        self.assertEqual(subtracao.result, 5)

    def test_divisao(self):
        divisao = Divisao(n1, n2)
        self.assertEqual(divisao.result, 2)

    def test_multiplicacao(self):
        multiplicacao = Multiplicacao(n1, n2)
        self.assertEqual(multiplicacao.result, 50)


if __name__ == '__main__':
    unittest.main()