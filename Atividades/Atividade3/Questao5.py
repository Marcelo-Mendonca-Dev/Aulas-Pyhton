# Questão 5: O Sistema de Desconto (Lógica OR)

# Pede o valor gasto na compra (usando float pros centavos)
valor_compra = float(input("Digite o valor total da compra: R$ "))

# Pergunta se o cliente eh VIP (1 pra sim e 0 pra nao, por isso usa int)
eh_vip = int(input("Voce possui cartao VIP? (Digite 1 para Sim ou 0 para Nao): "))

# Regra da loja: basta bater uma das condicoes pra levar o frete na faixa
# Se a compra passar de 200 OU se digitou 1 no VIP, ja da True direto
frete_gratis = valor_compra > 200.00 or eh_vip == 1

# Mostra na tela se o cliente conseguiu o frete gratis ou se vai ter que pagar
print("Tem direito a frete gratis?", frete_gratis)