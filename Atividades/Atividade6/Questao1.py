# Questão 1: Contagem Regressiva

# Começa o contador no 10 pro lançamento.
contador = 10

# O laco vai rodar enquanto o contador for maior ou igual a 1.
while contador >= 1:
    print(contador)
    # Diminui 1 a cada volta pra contagem descer (senao fica em loop infinito).
    contador = contador - 1

# Mensagem final quando sai do laco e chega no zero.
print("Foguete lançado!")