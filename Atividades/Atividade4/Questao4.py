# Questão 4: O Teste do Saldo Bancário

# Pede quanto o cliente tem na conta e quanto quer tirar (float pros centavos).
saldo_atual = float(input("Digite o saldo atual da conta: R$ "))
valor_saque = float(input("Digite o valor que deseja sacar: R$ "))

# Checar se o dinheiro na conta cobre o saque.
if valor_saque <= saldo_atual:
    # Desconta a grana do saldo.
    novo_saldo = saldo_atual - valor_saque
    print("Saque realizado com sucesso! Saldo atual: R$", novo_saldo)
else:
    # Se pediu mais do que tem, barra a operacao.
    print("Saldo insuficiente para realizar esta operação")