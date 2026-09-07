#Questão 1: A Divisão da Conta (Calculadora)

# Pede o valor da conta e usa float pq quase sempre tem centavos (tipo 50.50)
valor_total = float(input("Digite o valor da conta:"))

# Pega o total da galera na mesa, aqui tem que ser int pq nao existe meia pessoa kkk
quantidade_pessoas = int(input("Digite a quantidade de pessoas: "))

# Faz a conta basica dividindo o valor pelo numero de amigos
valor_divido = valor_total / quantidade_pessoas

# Mostra na tela o total da conta e quanto cada um vai ter que desembolsar
# noinspection LanguageDetectionInspection
print("O valor total foi de R$", valor_total, "e cada pessoa deve pagar R$", valor_divido)