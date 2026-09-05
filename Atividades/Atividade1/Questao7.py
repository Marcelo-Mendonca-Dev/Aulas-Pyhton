#Questao 7 - desconto da loja

#Pegando o valor da compra
total_compra = float(input("Digite o valor total da compra: R$ "))

#Calculando 15% de desconto e o valor final com desconto
valor_desconto = total_compra * 0.15
total_pagar = total_compra - valor_desconto

#Exibindo os tres resultados
print("Valor original: R$", round(total_compra, 2))
print("Valor economizado: R$", round(valor_desconto, 2))
print("Valor final a pagar: R$", round(total_pagar, 2))