# Questão 6: Jogo da Adivinhação com Tentativas

# Define o número secreto fixo no código.
numero_secreto = 14

# Começa o contador de tentativas zerado.
tentativas = 0

# Variável de controle começando com um valor diferente do segredo só pra entrar no laço.
palpite = 0

# O laço roda enquanto o palpite digitado for diferente do número secreto.
while palpite != numero_secreto:
    # Pede o palpite pro usuário
    palpite = int(input("Adivinhe o número secreto: "))

    # Soma +1 tentativa a cada chute dado.
    tentativas = tentativas + 1

# Quando acertar e sair do while, mostra a mensagem de vitória com o total de chutes.
print("Parabéns! Você acertou o número secreto em", tentativas, "tentativas!")