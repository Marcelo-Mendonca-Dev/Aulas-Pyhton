# Questão 2: A Fábrica de Caixas (Operador de Módulo)

# Pede quantas maças foram colhidas, usa int pq a contagem é sempre número inteiro.
total_macas = int(input("Digite a quantidade total de maças colhidas"))

# Aqui usa o % (resto da divisão) pra ver quantas sobram depois de fechar as caixas de 12.
sobra = total_macas % 12

# Joga na tela só as maças que sobraram e ficaram de fora.
print("A quantidade de maças que sobrarão fora das caixas é:", sobra)