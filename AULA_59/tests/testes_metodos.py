from AULA_59.metodos import Calc
import unittest

# Testando se o objeto é instância da classe Calc()

class TestCalc(unittest.TestCase):

    def test_soma(self):
        global objeto
        objeto = Calc(20,10)

        self.assertIsInstance(objeto, Calc)
        self.assertIs(objeto.get_n1(), 20, 'Não é Igual')
        self.assertNotEqual(objeto.soma(), objeto.get_resultado(), 'Erro')

    def test_subtracao(self):
        objeto.set_n1(20)
        self.assertIs(objeto.get_n1(), 20)

    def test_multiplicacao(self):



if __name__ == '__main__':
    unittest.main()

