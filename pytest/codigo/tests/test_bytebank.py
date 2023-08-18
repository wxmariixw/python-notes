
from bytebank import Funcionario

class TestClass:
    def test_quando_dade_recebe_13_03_2000_deve_retornar_o_valor_de_22(self):
        # given -  Contexto
        entrada = '13/03/2000'
        esperado = 22

        funcionario_teste = Funcionario('Teste', entrada, 1111)
        resultado = funcionario_teste.idade()

        assert resultado == esperado