# Questão 3: A Catraca do Parque (Operadores de Comparação)

# Pede a altura com float pq tem ponto decimal (tipo 1.35)
altura = float(input("Qual a altura da criança em metros (ex: 1.35) "))

# Compara se a altura da crianca é 1.40 ou mais, se for da True senao False.
pode_entrar = altura >= 1.40

# Exibe na tela se a crianca foi liberada ou barrada no brinquedo.
print("Pode entrar na montanha-russa?", pode_entrar)
