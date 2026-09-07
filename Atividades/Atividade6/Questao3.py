# Questão 3: Somador de Números.

# Começa o total acumulado zerado.
soma = 0

# Pede o primeiro numero pro usuário.
numero = int(input("Digite um número inteiro (ou 0 para sair): "))

# O laco continua rodando enquanto o numero digitado nao for zero.
while numero != 0:
    # Soma o numero atual ao total guardado..
    soma = soma + numero
    # Pede o proximo numero pro laco nao travar no mesmo valor.
    numero = int(input("Digite outro número inteiro (ou 0 para sair): "))

# Mostra o resultado final da soma depois que saiu do while.
print("A soma de todos os números digitados foi:", soma)