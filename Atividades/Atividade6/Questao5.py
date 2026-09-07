# Questão 5: Tabuada Simples.

# Pede pro usuario o numero que ele quer ver a tabuada.
numero = int(input("Digite um número inteiro para ver a tabuada: "))

# Variavel de incremento/contador comecando em 1
contador = 1

# O laco vai rodar de 1 ate 10.
while contador <= 10:
    # Faz a conta da multiplicacao.
    resultado = numero * contador

    # Mostra a linha da tabuada formatada (ex: 5 x 1 = 5).
    print(numero, "x", contador, "=", resultado)

    # Incrementa +1 no contador pra ir pro proximo numero da tabuada.
    contador = contador + 1