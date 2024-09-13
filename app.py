
import time
import bcrypt
from datetime import datetime, timedelta

#dados dos usuários
usuarios = {"master": bcrypt.hashpw("senha_master".encode('utf-8'), bcrypt.gensalt())}
clientes = []

#função para criptografar senha
def criptografar_senha(senha):
    return bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt())

#função para verificar senha
def verificar_senha(hash_senha, senha):
    return bcrypt.checkpw(senha.encode('utf-8'), hash_senha)

#função lambda criada para cálculo do preço
calcular_preco = lambda horas, minutos: (horas * 10) + (minutos // 15) * 3

#closure empregada dentro de uma função de alta ordem
def criar_cliente_fun():
    def registrar_cliente(nome, placa, tipo):
        hora_entrada = datetime.now()
        clientes.append({
            "nome": nome,
            "placa": placa,
            "hora_entrada": hora_entrada,
            "tipo": tipo
        })
    return registrar_cliente

registrar_cliente = criar_cliente_fun()

#tela de login
def login():
    print("Bem-vindo ao Estacionamento SHEI")
    while True:
        usuario = input("Usuário: ")
        senha = input("Senha: ")
        if usuario in usuarios and verificar_senha(usuarios[usuario], senha):
            print("Login bem-sucedido!\n")
            return True
        else:
            print("Usuário ou senha incorretos.\n")

#cadastrar cliente
def cadastrar_cliente():
    nome = input("Nome do cliente: ")
    placa = input("Placa do veículo: ")
    tipo = input("Tipo (diarista ou mensalista): ").strip().lower()
    registrar_cliente(nome, placa, tipo)
    print("Cliente cadastrado com sucesso!\n")

#list comprehension usada para listar clientes
def listar_clientes():
    agora = datetime.now()
    clientes_ativos = [cliente for cliente in clientes if cliente['tipo'] == 'diarista']
    clientes_mensalistas = [cliente for cliente in clientes if cliente['tipo'] == 'mensalista']
    
    print("\nClientes Ativos (Diaristas):")
    for cliente in clientes_ativos:
        horas = (agora - cliente["hora_entrada"]).seconds // 3600
        minutos = ((agora - cliente["hora_entrada"]).seconds % 3600) // 60
        valor = calcular_preco(horas, minutos)
        print(f"Nome: {cliente['nome']}, Placa: {cliente['placa']}, Tempo: {horas}h {minutos}m, Valor: R${valor:.2f}")
    
    print("\nClientes Mensalistas:")
    for cliente in clientes_mensalistas:
        print(f"Nome: {cliente['nome']}, Placa: {cliente['placa']}, Mensalista")
    print()

#menu principal
def menu():
    login()
    while True:
        print("1. Cadastrar Cliente")
        print("2. Listar Clientes")
        print("3. Sair")
        escolha = input("Escolha uma opção: ").strip()
        
        if escolha == "1":
            cadastrar_cliente()
        elif escolha == "2":
            listar_clientes()
        elif escolha == "3":
            print("Saindo do sistema...\n")
            break
        else:
            print("Opção inválida!\n")

#iniciar aplicação
if __name__ == "__main__":
    menu()


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
        #criar senha e hash
        senha = "senha_segura"
        hash_senha = criptografar_senha(senha)
        
        #teste de verificação de senha correta
        self.assertTrue(verificar_senha(hash_senha, senha))
        
        #teste de verificação de senha incorreta
        self.assertFalse(verificar_senha(hash_senha, "senha_errada"))

if __name__ == "__main__":
    #roda testes se o script for executado diretamente
    unittest.main(argv=['first-arg-is-ignored'], exit=False)