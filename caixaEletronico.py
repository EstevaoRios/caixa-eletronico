from os import system, name  # Funções usadas para limpar a tela do terminal

def limpaTela():
    """
    Função responsável por limpar o terminal. 
    Para isso, a função precisa saber o Sistema Operacional (SO) que o código está sendo executado.
    A definição do nome do SO é feito com auxílio do módulo 'os'. Supõem-se que o código
    será executado em Windows ou Linux. Se estiver usando outro SO, leia a documentação do 
    módulo 'os' para fazer as modificações necessárias. 
    
    """
    if name == 'nt':  # Windows
        system('cls')
    else:  # Linux ou outro SO
        system('clear')

def telaAbertura(): # Função que exibe a tela de abertura do programa
    print("Seja bem-vindo ao caixa eletrônico!")
    input("Pressione uma tecla para continuar...")


def leValor(funcaoConversao, msgInput="", msgErro="ERRO: Valor inválido"): 
    """
    Função para ler e validar um valor de entrada, tentando convertê-lo para o tipo especificado.
    Retorna o valor convertido se for bem-sucedido, ou chama recursivamente a si mesma em caso de erro.
    """
    try:  # Tenta fazer a conversão do valor digitado
        return funcaoConversao(input(msgInput))
    except ValueError:  # Captura o erro específico de conversão (ex: texto para int)
        print(msgErro)
        # Chama a função recursivamente para pedir um novo valor até que seja válido
        return leValor(funcaoConversao, msgInput, msgErro)
    
def deposito(saldo_atual, nota100_atual, nota50_atual, nota20_atual): 
    """
    Função que realiza o depósito de notas no caixa eletrônico.
    Aceita apenas notas de R$100, R$50 ou R$20.
    Retorna o novo saldo e a contagem atualizada das notas.
    """
    print("--- Área de Depósito ---")
    valorDeposito = leValor(int, "Digite o valor que deseja depositar (Notas de R$100, R$50, R$20): R$")

    if valorDeposito <= 0:
        print("ERRO: Deposite um valor acima de 0 reais!")
        return saldo_atual, nota100_atual, nota50_atual, nota20_atual # Retorna o estado atual sem alterações
    
    # Verifica se o valor corresponde a uma das notas válidas
    if valorDeposito == 100:
        nota100_atual += 1
    elif valorDeposito == 50:
        nota50_atual += 1
    elif valorDeposito == 20:
        nota20_atual += 1
    else:
        print("ERRO: Nota inválida! Favor depositar notas de R$100, R$50 ou R$20.")
        return saldo_atual, nota100_atual, nota50_atual, nota20_atual # Retorna o estado atual sem alterações

    saldo_atual += valorDeposito
    print(f"Valor depositado: R${valorDeposito:.2f}")
    print(f"Novo saldo: R${saldo_atual:.2f}")
    
    return saldo_atual, nota100_atual, nota50_atual, nota20_atual # Retorna os valores atualizados

def saque(saldo_atual, nota100_atual, nota50_atual, nota20_atual): 
    """
    Função que realiza o saque de valores do caixa eletrônico.
    Verifica se há saldo suficiente e notas disponíveis antes de efetuar o saque.
    Retorna o novo saldo e a contagem atualizada das notas.
    """
    print("--- Área de Saque ---")
    valorSaque = leValor(int, "Digite o valor que deseja sacar: R$")

    if valorSaque <= 0:
        print("ERRO: Saque um valor acima de 0 reais!")
        return saldo_atual, nota100_atual, nota50_atual, nota20_atual 

    if valorSaque > saldo_atual:
        print("ERRO: Não foi possível realizar o saque. Saldo insuficiente!")
        return saldo_atual, nota100_atual, nota50_atual, nota20_atual
    
    # Validações adicionais para saques com base nas notas disponíveis
    if valorSaque % 10 != 0: # Caixa só trabalha com notas de 20, 50, 100 (multiplos de 10)
        print("ERRO: Valor de saque inválido. O caixa só opera com notas de R$20, R$50 e R$100.")
        return saldo_atual, nota100_atual, nota50_atual, nota20_atual

    # Lógica de distribuição das notas
    temp_saque = valorSaque
    notas_sacadas_100 = 0
    notas_sacadas_50 = 0
    notas_sacadas_20 = 0

    # Tenta usar notas de 100 primeiro
    while temp_saque >= 100 and nota100_atual > 0:
        notas_sacadas_100 += 1
        nota100_atual -= 1
        temp_saque -= 100
    
    # Tenta usar notas de 50
    while temp_saque >= 50 and nota50_atual > 0:
        notas_sacadas_50 += 1
        nota50_atual -= 1
        temp_saque -= 50
    
    # Tenta usar notas de 20
    while temp_saque >= 20 and nota20_atual > 0:
        notas_sacadas_20 += 1
        nota20_atual -= 1
        temp_saque -= 20
    
    # Se depois de tentar distribuir as notas, ainda sobrar dinheiro em temp_saque
    # significa que o caixa não tem as combinações de notas para o valor solicitado.
    if temp_saque > 0:
        print("ERRO: Não foi possível sacar o valor. O caixa não possui as combinações de notas para este valor.")
        # Reverte as notas que foram "retiradas" temporariamente para a verificação
        nota100_atual += notas_sacadas_100
        nota50_atual += notas_sacadas_50
        nota20_atual += notas_sacadas_20
        return saldo_atual, nota100_atual, nota50_atual, nota20_atual
    
    # Se chegou aqui, o saque é possível e as notas foram distribuídas
    saldo_atual -= valorSaque
    print(f"Valor sacado: R${valorSaque:.2f}")
    print(f"Notas entregues: R$100 - {notas_sacadas_100}, R$50 - {notas_sacadas_50}, R$20 - {notas_sacadas_20}")
    print(f"Novo saldo: R${saldo_atual:.2f}")
    
    return saldo_atual, nota100_atual, nota50_atual, nota20_atual 

def caixaEletronico(): # Função principal que exibe o menu e gerencia as operações
    """
    Função principal que gerencia o menu do caixa eletrônico e as operações.
    Usa um loop 'while' para manter o menu ativo até que o usuário decida sair.
    """
    saldo = 0
    nota100 = 0
    nota50 = 0
    nota20 = 0

    while True: # Loop infinito que só é quebrado quando o usuário escolhe sair
        limpaTela()
        print("--- Caixa Eletrônico ---")
        print("1 - Depósito")
        print("2 - Saque")
        print("3 - Saldo")
        print("4 - Estoque de notas")
        print("5 - Sair")
        print("------------------------")
        
        opcao = leValor(int, "Digite uma opção: ", "ERRO: A opção deve ser um número inteiro.")

        if opcao == 1: # Abre o menu de depósito
            saldo, nota100, nota50, nota20 = deposito(saldo, nota100, nota50, nota20)
        elif opcao == 2: # Abre o menu de saque
            saldo, nota100, nota50, nota20 = saque(saldo, nota100, nota50, nota20)
        elif opcao == 3: # Exibe o saldo atual do usuário
            print(f"Saldo atual: R${saldo:.2f}")
        elif opcao == 4: # Exibe o estoque de notas disponíveis no caixa eletrônico
            print("--- Estoque de Notas ---")
            print(f"Notas de R$100: {nota100}")
            print(f"Notas de R$50: {nota50}")
            print(f"Notas de R$20: {nota20}")
        elif opcao == 5:
            print("Finalizando sessão. Obrigado por usar o caixa eletrônico!")
            break # Sai do loop while, encerrando o programa
        else:
            print("ERRO: Opção inválida! Por favor, escolha uma opção entre 1 e 5.")
        
        input("\nPressione Enter para retornar ao menu principal...")

def main(): # Função principal que inicializa o programa
    limpaTela()
    telaAbertura()
    caixaEletronico() # Chama a função que gerencia o caixa eletrônico

main()