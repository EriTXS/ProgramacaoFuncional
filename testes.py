import unittest

class TestEstacionamentoSHEI(unittest.TestCase):

    def test_registrar_cliente(self):
        #reseta lista de clientes para o teste
        global clientes
        clientes = []
        
        #registra cliente
        registrar_cliente("Teste", "ABC1234", "diarista")
        
        #verifica se o cliente foi adicionado corretamente
        self.assertEqual(len(clientes), 1)
        self.assertEqual(clientes[0]["nome"], "Teste")
        self.assertEqual(clientes[0]["placa"], "ABC1234")
        self.assertEqual(clientes[0]["tipo"], "diarista")

    def test_verificar_senha(self):
        #cria senha e hash
        senha = "senha_segura"
        hash_senha = criptografar_senha(senha)
        
        #testa verificação de senha correta
        self.assertTrue(verificar_senha(hash_senha, senha))
        
        #testa verificação de senha incorreta
        self.assertFalse(verificar_senha(hash_senha, "senha_errada"))

if __name__ == "__main__":
    #roda testes se o script for executado diretamente
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
