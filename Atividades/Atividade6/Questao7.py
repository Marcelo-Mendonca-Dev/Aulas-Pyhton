# Questão 7: Controle de Orçamento.

# Define a verba inicial da viagem com float pros centavos.
orcamento = 500.00

# O laço roda enquanto ainda tiver dinheiro sobrando no bolso.
while orcamento > 0:
    # Mostra quanto ainda tem disponivel pra gastar.
    print("Saldo atual: R$", orcamento)

    # Pede o valor do gasto da vez
    gasto = float(input("Digite o valor do gasto: R$ "))

    # Desconta a grana gasta do total.
    orcamento = orcamento - gasto

# Se saiu do while eh pq o saldo zerou ou ficou negativo.
print("Atenção: Você ficou sem saldo ou estourou seu orçamento!")
print("Saldo final: R$", orcamento)