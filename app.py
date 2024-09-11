
import time
import bcrypt
from datetime import datetime, timedelta

# Dados dos usuários
usuarios = {"master": bcrypt.hashpw("senha_master".encode('utf-8'), bcrypt.gensalt())}
clientes = []

# Função para criptografar senha
def criptografar_senha(senha):
    return bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt())

# Função para verificar senha
def verificar_senha(hash_senha, senha):
    return bcrypt.checkpw(senha.encode('utf-8'), hash_senha)

# Função lambda para cálculo do preço
calcular_preco = lambda horas, minutos: (horas * 10) + (minutos // 15) * 3

# Função de alta ordem (closure)
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

# Tela de login
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

# Cadastrar cliente
def cadastrar_cliente():
    nome = input("Nome do cliente: ")
    placa = input("Placa do veículo: ")
    tipo = input("Tipo (diarista ou mensalista): ").strip().lower()
    registrar_cliente(nome, placa, tipo)
    print("Cliente cadastrado com sucesso!\n")

# Listar clientes
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

# Menu principal
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

# Iniciar aplicação
if __name__ == "__main__":
    menu()