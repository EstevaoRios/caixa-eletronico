# Caixa Eletrônico em Python

Um simples programa de simulação de caixa eletrônico desenvolvido em Python, que permite realizar operações básicas como depósito, saque, consulta de saldo e visualização do estoque de notas. Este projeto foi criado com o objetivo de praticar conceitos de lógica de programação, funções, controle de fluxo e manipulação de entrada/saída em Python.

---

## Funcionalidades

O Caixa Eletrônico oferece as seguintes opções:

* **Depósito:** Permite depositar valores no caixa. Aceita apenas notas de R$100, R$50 e R$20. O estoque de notas é atualizado a cada depósito.
* **Saque:** Possibilita sacar dinheiro do caixa. O sistema verifica se há saldo suficiente e se o caixa possui as combinações de notas (R$100, R$50, R$20) para o valor solicitado. O estoque de notas é debitado após um saque bem-sucedido.
* **Saldo:** Exibe o saldo atual da conta.
* **Estoque de Notas:** Mostra a quantidade de notas de R$100, R$50 e R$20 disponíveis no caixa.
* **Sair:** Encerra a execução do programa.

---

## Estrutura do Código

O programa é dividido em funções para melhor organização e modularidade:

* `limpaTela()`: Limpa o terminal para uma interface mais limpa.
* `telaAbertura()`: Exibe a mensagem de boas-vindas inicial.
* `leValor()`: Função utilitária para ler entradas do usuário, garantindo que sejam do tipo correto e tratando erros de digitação.
* `deposito()`: Lida com a lógica de depósito de valores e atualização do estoque de notas.
* `saque()`: Gerencia a lógica de saque, incluindo verificação de saldo, distribuição de notas e atualização do estoque.
* `caixaEletronico()`: A função principal que exibe o menu e orquestra as chamadas das outras funções.
* `main()`: Ponto de entrada do programa.

---
