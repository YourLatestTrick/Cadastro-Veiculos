import os
from veiculo import Veiculo
from carro import Carro
from moto import Moto
from caminhao import Caminhao
#BD em memória
listaVeiculos = [
    Carro("Hyundai", 'HB20', 'ABC', 2023, 4),
    Moto('Yamaha', 'Lander', 'DEF', 2008, 250),
    Caminhao("Scania", 'Scania 113H', 'GHI', 1990, 2, 8, 5000)
]

def cadastrar():
    print('Qual o tipo de veículo: (1) Carro - (2) Moto - (3) Caminhão')
    tipo = input()
    print("Digite a marca:")
    marca = input()
    print("Digite o modelo:")
    modelo = input()
    print("Digite o placa:")
    placa = input()
    print("Digite o Ano:")
    ano = input()
    print()

    if tipo == '1':
        nPortas = input('Digite o número de portas:')
        veiculoAdd = Carro(marca, modelo, placa, ano, nPortas)

    elif tipo == '2':
        cilindradas = input('Digite as cilindradas: ')
        veiculoAdd = Moto(marca, modelo, placa, ano, cilindradas)
    
    elif tipo == '3':
        nPortas = input('Digite o número de portas: ')
        comprimento = input('Digite o comprimento: ')
        capacidade = input('Digite a capacidade: ')
        veiculoAdd = Caminhao(marca, modelo, placa, ano, nPortas, comprimento, capacidade)

    listaVeiculos.append(veiculoAdd)
    

def listar():
    os.system('cls')
    if len(listaVeiculos) == 0:
        print ("Não existem veículos cadastrados")
    else:
        for n, veiculo in enumerate(listaVeiculos):
            print(f"Veículo: {n + 1}")
            print(f" - {veiculo}")
            print()

def excluir():
    listar()
    print("Digite a placa que deseja excluir")
    placa = input()
    encontrou = False
    for veiculo in listaVeiculos:
        if veiculo.get_placa() == placa:
            listaVeiculos.remove(veiculo)
            encontrou = True
            break
    if encontrou:
        print("Veículo excluído")
    else:
        print("Veículo não encontrado")

os.system('cls')
while True:
    print("Escolha uma das opções:")
    print("1 - Cadastrar Veículo")
    print("2 - Listar Veículos")
    print("3 - Excluir Veículo")
    print("0 - SAIR\n")
    opcao = input()
    try:
        opcao = int(opcao)
    except:
        print("Opção Inválida")
    if opcao == 1:
        cadastrar()
    elif opcao == 2:
        listar()
    elif opcao == 3:
        excluir()
    elif opcao == 0:
        break
    else:
        print("Opção Inválida")